#!/usr/bin/env python3
"""Fetch NIH/VA grants from RePORTER API v2 into data/ri_grants_nih.json."""

from __future__ import annotations

import argparse
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.reporter.nih.gov/v2/projects/search"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "ri_grants_nih.json"

# Theme key -> search criteria (extend as needed)
THEME_QUERIES: dict[str, dict] = {
    "neurotech_bci": {"pi_names": [{"any_name": "Hochberg Leigh"}], "fiscal_years": list(range(2018, 2027))},
    "neurotech_borton": {"pi_names": [{"any_name": "Borton David"}], "fiscal_years": list(range(2018, 2027))},
    "neurotech_nurmikko": {"pi_names": [{"any_name": "Nurmikko Arto"}], "fiscal_years": list(range(2015, 2027))},
    "oncology_eldeiry": {"pi_names": [{"any_name": "El-Deiry Wafik"}], "fiscal_years": list(range(2015, 2027))},
    "fibrosis_elias": {"pi_names": [{"any_name": "Elias Jack"}], "fiscal_years": list(range(2015, 2027))},
    "immunoinformatics_epivax": {"org_names": ["EPIVAX INC"], "fiscal_years": list(range(2015, 2027))},
    "inflammation_prothera": {"org_names": ["PROTHERA BIOL"], "fiscal_years": list(range(2013, 2027))},
    "nanode_chen": {"pi_names": [{"any_name": "Chen Qian"}], "fiscal_years": list(range(2015, 2027))},
    "epigenetics_christensen": {"pi_names": [{"any_name": "Christensen Brock"}], "fiscal_years": list(range(2018, 2027))},
    "digital_health_levine": {"pi_names": [{"any_name": "Levine Adam"}], "fiscal_years": list(range(2015, 2027))},
    "psychiatry_petzschner": {"pi_names": [{"any_name": "Petzschner Frederike"}], "fiscal_years": list(range(2018, 2027))},
    "uri_phlip_lnp": {
        "pi_names": [{"any_name": "Reshetnyak Yana"}, {"any_name": "Engelman Donald"}],
        "org_names": ["UNIVERSITY OF RHODE ISLAND"],
        "org_states": ["RI"],
        "fiscal_years": list(range(2015, 2027)),
    },
    "rih_jayasuriya_msk": {
        "pi_names": [{"any_name": "Jayasuriya Chathuraka"}, {"any_name": "Trivedi Jay"}],
        "org_names": ["RHODE ISLAND HOSPITAL"],
        "org_states": ["RI"],
        "fiscal_years": list(range(2018, 2027)),
    },
    "rih_tapinos_glioma": {
        "pi_names": [{"any_name": "Tapinos Nikolaos"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2015, 2027)),
    },
    "rih_dudley_cardio": {
        "pi_names": [{"any_name": "Dudley Samuel"}, {"any_name": "Ventetuolo Corey"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2015, 2027)),
    },
    "rih_kreiling_ad": {
        "pi_names": [{"any_name": "Kreiling Jill"}, {"any_name": "Quesenberry Peter"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2018, 2027)),
    },
    "rih_liang_ph": {
        "pi_names": [{"any_name": "Liang Olin"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2018, 2027)),
    },
    "rih_song_lpa": {
        "pi_names": [{"any_name": "Song Wenliang"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2018, 2027)),
    },
    "msk_fallon_biglycan": {
        "pi_names": [{"any_name": "Fallon Justin"}],
        "org_states": ["RI"],
        "fiscal_years": list(range(2010, 2027)),
    },
}


def search(criteria: dict, limit: int = 25) -> dict:
    body = json.dumps(
        {"criteria": criteria, "limit": limit, "sort_field": "fiscal_year", "sort_order": "desc"}
    ).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def slim(row: dict) -> dict:
    org = row.get("organization") or {}
    return {
        "project_num": row.get("project_num") or row.get("core_project_num"),
        "core_project_num": row.get("core_project_num"),
        "fiscal_year": row.get("fiscal_year"),
        "award_amount": row.get("award_amount") or row.get("direct_cost_amt"),
        "agency": (row.get("agency_ic_admin") or {}).get("abbreviation") or row.get("agency_code"),
        "activity_code": row.get("activity_code"),
        "title": (row.get("project_title") or "")[:220],
        "pi": row.get("contact_pi_name"),
        "org": org.get("org_name"),
        "org_state": org.get("org_state"),
        "start": (row.get("project_start_date") or "")[:10],
        "end": (row.get("project_end_date") or "")[:10],
        "url": row.get("project_detail_url"),
    }


def dedupe_by_core(grants: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for g in grants:
        core = g.get("core_project_num") or g.get("project_num")
        if not core:
            continue
        prev = best.get(core)
        if not prev or (g.get("fiscal_year") or 0) > (prev.get("fiscal_year") or 0):
            best[core] = g
    return sorted(best.values(), key=lambda x: (-(x.get("fiscal_year") or 0), x.get("title", "")))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", type=float, default=0.4, help="Seconds between API calls")
    parser.add_argument("--limit", type=int, default=25)
    args = parser.parse_args()

    out = {
        "harvested_at": datetime.now(timezone.utc).isoformat(),
        "source": "NIH RePORTER API v2 (https://api.reporter.nih.gov)",
        "note": "Dedupe by core_project_num in ri_funding_matrix.json; verify PI/org disambiguation manually.",
        "themes": {},
    }
    for theme, crit in THEME_QUERIES.items():
        data = search(crit, limit=args.limit)
        grants = dedupe_by_core([slim(r) for r in data.get("results", [])])
        out["themes"][theme] = {"count": len(grants), "grants": grants}
        print(f"{theme}: {len(grants)} unique core awards")
        time.sleep(args.delay)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
