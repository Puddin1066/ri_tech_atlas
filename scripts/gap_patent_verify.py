#!/usr/bin/env python3
"""Verify gap assets via patent-mcp-server PPUBS (same API as MCP ppubs_search_patents)."""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

QUERIES: dict[str, list[str]] = {
    "gap_smurf2_oncology": [
        'AN/"SMURF-Therapeutics"',
        'IN/"El-Deiry". AND (SMURF2 OR HIF).ti.',
        "(SMURF2 OR SMURF).ti. AND RI.ASST.",
    ],
    "gap_soma_dtx": [
        'IN/"Petzschner". AND RI.INST.',
        '(interoception OR "computational psychiatry").ti. AND RI.INST.',
    ],
    "gap_christensen_epigenetics": [
        'IN/"Christensen". AND AN/"Dartmouth"',
        'AN/"Dartmouth College". AND HiTIMED.ti.',
        "EP4505463",
    ],
    "gap_ni2o_kiwi_bci": [
        '"ni2o".ASNM.',
        'IN/"Howard". AND (BCI OR "brain computer").ti.',
    ],
    "gap_levine_pediatric_sepsis": [
        'IN/"Levine". AND pediatric.ti. AND sepsis.ti.',
        'IN/"Garbern". AND wearable.ti. AND sepsis.ti.',
    ],
    "ip_oncolux_lumis": [
        '"OncoLux".ASNM.',
        'IN/"Kersey". AND (theranostic OR fluorescence).ti.',
    ],
}


def load_env() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def extract_hits(data: dict) -> list[dict]:
    items: list = []
    for key in ("searchResults", "patents", "results", "docs"):
        val = data.get(key)
        if isinstance(val, list):
            items = val
            break
        if isinstance(val, dict):
            for sub in ("patents", "results", "docs"):
                if isinstance(val.get(sub), list):
                    items = val[sub]
                    break
    if not items:
        for v in data.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                items = v
                break

    out = []
    for it in items:
        if not isinstance(it, dict):
            continue
        num = (
            it.get("patentNumber")
            or it.get("publicationNumber")
            or it.get("documentId")
            or it.get("guid")
        )
        title = (it.get("inventionTitle") or it.get("title") or "")[:140]
        assignee = it.get("assigneeName") or it.get("assignee") or ""
        if isinstance(assignee, list):
            assignee = "; ".join(str(x) for x in assignee[:3])
        out.append(
            {
                "number": str(num) if num else None,
                "title": title,
                "assignee": str(assignee)[:100],
            }
        )
    return out


async def run() -> dict:
    from patent_mcp_server.uspto.ppubs_uspto_gov import PpubsClient

    load_env()
    results: dict = {}
    async with PpubsClient() as client:
        for gap_id, queries in QUERIES.items():
            gap_rows = []
            for q in queries:
                try:
                    raw = await client.run_query(q, limit=20)
                    if isinstance(raw, dict) and raw.get("error"):
                        gap_rows.append({"query": q, "error": raw})
                    else:
                        hits = extract_hits(raw)
                        gap_rows.append({"query": q, "count": len(hits), "hits": hits})
                except Exception as exc:
                    gap_rows.append({"query": q, "error": str(exc)})
                await asyncio.sleep(4)
            results[gap_id] = gap_rows
    return results


def main() -> None:
    data = asyncio.run(run())
    out_path = ROOT / "data" / "gap_patent_verify_ppubs.json"
    out_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
    print(f"\nWrote {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
