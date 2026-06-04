#!/usr/bin/env python3
"""
Rate-limited USPTO Patent Public Search (PPUBS) harvester for RI Tech Atlas.

PPUBS enforces aggressive throttling (~"Too many requests"). Defaults:
  - 8s minimum between POST /api/searches/search
  - 25 results per query page (max practical for agent context)
  - Exponential backoff on 429 / rate-limit messages

Usage:
  python3 scripts/ri_patent_harvest.py
  python3 scripts/ri_patent_harvest.py --delay 12 --max-per-query 15
  python3 scripts/ri_patent_harvest.py --queries-file scripts/ri_patent_queries.txt

Output:
  data/ri_patents.json
  data/ri_patents.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

PPUBS_SEARCH_URL = "https://ppubs.uspto.gov/api/searches/search"
DEFAULT_QUERIES = [
    '"Brown University".ASNM.',
    '"Rhode Island Hospital".ASNM.',
    '"Warren Alpert".ASNM.',
    '"EpiVax".ASNM.',
    '"University of Rhode Island".ASNM.',
    '"Care New England".ASNM.',
    "RI.ASST.",
    '(chitinase OR chitin).ti. AND RI.ASST.',
    '(brain-computer OR "neural interface").ti. AND RI.ASST.',
    '(vaccine OR immunoinformatics OR epitope).ti. AND RI.ASST.',
    'IN/"El-Deiry". AND RI.INST.',
    'IN/"Elias". AND RI.INST.',
    'IN/"Borton". AND RI.INST.',
    'IN/"Chen". AND RI.INST.',
    'IN/"Petzschner". AND RI.INST.',
    'IN/"Hochberg". AND RI.INST.',
    'IN/"De Groot". AND RI.INST.',
]

RATE_LIMIT_RE = re.compile(r"too many requests", re.I)


@dataclass
class PatentRecord:
    patent_number: str
    title: str
    publication_date: str | None
    assignee: str | None
    inventors: str | None
    source_query: str
    document_id: str | None = None


def load_queries(path: Path | None) -> list[str]:
    if path is None:
        return DEFAULT_QUERIES
    lines = [
        ln.strip()
        for ln in path.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    return lines or DEFAULT_QUERIES


def ppubs_search(
    query: str,
    *,
    page: int = 1,
    size: int = 25,
    timeout: float = 60.0,
) -> dict:
    payload = json.dumps(
        {
            "query": query,
            "page": page,
            "size": size,
            "sort": "date_publ desc",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        PPUBS_SEARCH_URL,
        data=payload,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_records(data: dict, query: str) -> list[PatentRecord]:
    if isinstance(data.get("message"), str) and RATE_LIMIT_RE.search(data["message"]):
        raise RuntimeError(data["message"])

    items = data.get("patents") or data.get("results") or data.get("docs") or []
    out: list[PatentRecord] = []

    for item in items:
        if not isinstance(item, dict):
            continue
        num = (
            item.get("patentNumber")
            or item.get("patent_number")
            or item.get("documentId")
            or item.get("guid")
        )
        if not num:
            continue
        title = (
            item.get("inventionTitle")
            or item.get("title")
            or item.get("invention_title")
            or ""
        )
        pub = item.get("datePublished") or item.get("publicationDate") or item.get("date_publ")
        assignees = item.get("assignees") or item.get("assigneeName") or item.get("assignee")
        if isinstance(assignees, list):
            assignee = "; ".join(
                str(a.get("assigneeName", a) if isinstance(a, dict) else a) for a in assignees
            )[:500]
        else:
            assignee = str(assignees) if assignees else None

        inventors_raw = item.get("inventors") or item.get("inventorName")
        if isinstance(inventors_raw, list):
            inventors = "; ".join(
                str(i.get("inventorName", i) if isinstance(i, dict) else i) for i in inventors_raw
            )[:500]
        else:
            inventors = str(inventors_raw) if inventors_raw else None

        out.append(
            PatentRecord(
                patent_number=str(num).strip(),
                title=str(title).strip()[:300],
                publication_date=str(pub)[:32] if pub else None,
                assignee=assignee,
                inventors=inventors,
                source_query=query,
                document_id=str(item.get("documentId") or "") or None,
            )
        )
    return out


def harvest(
    queries: list[str],
    *,
    delay_sec: float,
    max_per_query: int,
    max_retries: int,
    backoff_factor: float,
) -> tuple[list[PatentRecord], list[str]]:
    seen: dict[str, PatentRecord] = {}
    errors: list[str] = []
    wait = delay_sec

    for i, query in enumerate(queries, 1):
        print(f"[{i}/{len(queries)}] {query}", flush=True)
        success = False
        for attempt in range(1, max_retries + 1):
            try:
                data = ppubs_search(query, size=max_per_query)
                batch = extract_records(data, query)
                for rec in batch:
                    key = rec.patent_number.upper()
                    if key not in seen:
                        seen[key] = rec
                print(f"  +{len(batch)} hits, {len(seen)} unique total", flush=True)
                success = True
                wait = delay_sec
                break
            except RuntimeError as e:
                msg = str(e)
                errors.append(f"{query}: {msg}")
                print(f"  rate limited (attempt {attempt}): {msg}", flush=True)
                wait = delay_sec * (backoff_factor ** attempt)
            except urllib.error.HTTPError as e:
                errors.append(f"{query}: HTTP {e.code}")
                print(f"  HTTP {e.code}", flush=True)
                wait = delay_sec * (backoff_factor ** attempt)
            except Exception as e:
                errors.append(f"{query}: {e}")
                print(f"  error: {e}", flush=True)
                wait = delay_sec * (backoff_factor ** attempt)

        if not success:
            print(f"  skipped after {max_retries} attempts", flush=True)

        if i < len(queries):
            print(f"  sleeping {wait:.1f}s", flush=True)
            time.sleep(wait)

    return list(seen.values()), errors


def write_outputs(records: list[PatentRecord], errors: list[str], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "harvested_at": datetime.now(timezone.utc).isoformat(),
        "count": len(records),
        "errors": errors,
        "patents": [asdict(r) for r in sorted(records, key=lambda x: x.patent_number)],
    }
    json_path = out_dir / "ri_patents.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md_lines = [
        "# Rhode Island patent harvest",
        "",
        f"Generated: {payload['harvested_at']}",
        f"Unique filings: **{len(records)}**",
        "",
        "| # | Patent | Title | Assignee | Query |",
        "|---|--------|-------|----------|-------|",
    ]
    for idx, r in enumerate(
        sorted(records, key=lambda x: (x.publication_date or "", x.patent_number)),
        1,
    ):
        title = r.title.replace("|", "/")[:80]
        asn = (r.assignee or "—").replace("|", "/")[:40]
        md_lines.append(
            f"| {idx} | {r.patent_number} | {title} | {asn} | `{r.source_query[:40]}` |"
        )
    if errors:
        md_lines.extend(["", "## Errors", ""])
        for err in errors:
            md_lines.append(f"- {err}")

    (out_dir / "ri_patents.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(f"Wrote {json_path} and {out_dir / 'ri_patents.md'}", flush=True)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Rate-limited RI patent harvest")
    parser.add_argument("--delay", type=float, default=8.0, help="Seconds between queries")
    parser.add_argument("--max-per-query", type=int, default=20)
    parser.add_argument("--max-retries", type=int, default=4)
    parser.add_argument("--backoff", type=float, default=1.8)
    parser.add_argument("--queries-file", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=root / "data")
    args = parser.parse_args()

    queries = load_queries(args.queries_file)
    records, errors = harvest(
        queries,
        delay_sec=args.delay,
        max_per_query=args.max_per_query,
        max_retries=args.max_retries,
        backoff_factor=args.backoff,
    )
    ppubs_count = len(records)
    curated_path = Path(__file__).resolve().parents[1] / "data" / "ri_patents_curated.json"
    if ppubs_count < 50 and curated_path.exists():
        existing = {r.patent_number.upper() for r in records}
        curated = json.loads(curated_path.read_text(encoding="utf-8"))
        for item in curated.get("patents", []):
            key = str(item.get("patent_number", "")).upper()
            if key and key not in existing:
                records.append(
                    PatentRecord(
                        patent_number=item["patent_number"],
                        title=item.get("title", ""),
                        publication_date=item.get("publication_date"),
                        assignee=item.get("assignee"),
                        inventors=item.get("inventors"),
                        source_query=item.get("source_query", "curated_fallback"),
                        document_id=None,
                    )
                )
                existing.add(key)
        errors.append(
            f"Merged curated fallback from {curated_path.name} (PPUBS returned {ppubs_count} unique filings)"
        )

    write_outputs(records, errors, args.out_dir)
    print(f"Done: {len(records)} unique patents, {len(errors)} query errors", flush=True)
    return 0 if len(records) >= 50 else 1


if __name__ == "__main__":
    sys.exit(main())
