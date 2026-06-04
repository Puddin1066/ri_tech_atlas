#!/usr/bin/env python3
"""
Harvest NIH RePORTER awards for funding-matrix themes with empty grants[],
convert to GrantRecord shape, and merge into data/ri_funding_matrix.json.
Also syncs grant_anchors on gap entries in ri_patent_investment_opportunities.json.

Run: python3 scripts/sync_funding_grants.py
Optional: python3 scripts/fetch_nih_grants.py  (updates ri_grants_nih.json first)
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.reporter.nih.gov/v2/projects/search"
FY = list(range(2015, 2027))
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

# Funding-matrix theme id -> RePORTER search (+ optional title filter for disambiguation)
THEME_SEARCH: dict[str, dict] = {
    "uri_phlip_lnp": {
        "criteria": {
            "pi_names": [{"any_name": "Engelman Donald"}],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"transmembrane|peptide|membrane|insertion", re.I),
    },
    "rih_salivary_ev_ad": {
        "criteria": {
            "pi_names": [
                {"any_name": "Kreiling Jill"},
                {"any_name": "Quesenberry Peter"},
                {"any_name": "Wu Zhijin"},
            ],
            "org_names": ["RHODE ISLAND HOSPITAL", "BROWN UNIVERSITY"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"salivary|extracellular vesicle|Alzheimer|biomarker", re.I),
    },
    "rih_bx912_pulmonary_htn": {
        "criteria": {
            "pi_names": [{"any_name": "Liang Olin"}, {"any_name": "Klinger James"}],
            "org_names": ["RHODE ISLAND HOSPITAL"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"pulmonary hypertension|BX-912|BX912|PH\b", re.I),
    },
    "rih_pahtn_dx": {
        "criteria": {
            "pi_names": [
                {"any_name": "Dudley Samuel"},
                {"any_name": "Ventetuolo Corey"},
            ],
            "org_names": ["RHODE ISLAND HOSPITAL"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"pulmonary arterial|sudden cardiac|PAH|diagnostic", re.I),
    },
    "rih_bbb_nucleic_delivery": {
        "criteria": {
            "pi_names": [{"any_name": "Chen Qian"}],
            "org_names": ["RHODE ISLAND HOSPITAL"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"blood.?brain|BBB|nucleic acid delivery|barrier", re.I),
    },
    "rih_motile_cell_msk": {
        "criteria": {
            "pi_names": [
                {"any_name": "Jayasuriya Chathuraka"},
                {"any_name": "Trivedi Jay"},
            ],
            "org_names": ["RHODE ISLAND HOSPITAL"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"motile|musculoskeletal|connective tissue|tendon|ligament", re.I),
    },
    "rih_ecm_joint_repair": {
        "criteria": {
            "pi_names": [
                {"any_name": "Jayasuriya Chathuraka"},
                {"any_name": "Yang Daniel"},
            ],
            "org_names": ["RHODE ISLAND HOSPITAL"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"extracellular matrix|ECM|joint|musculoskeletal", re.I),
    },
    "rih_enhancer_rna_glioma": {
        "criteria": {
            "pi_names": [{"any_name": "Tapinos Nikolaos"}],
            "org_names": ["RHODE ISLAND HOSPITAL", "BROWN UNIVERSITY"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"enhancer RNA|brain tumor|glioma|eRNA", re.I),
    },
    "rih_lpa_therapeutic": {
        "criteria": {
            "pi_names": [{"any_name": "Song Wenliang"}],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"thromb|lipid|lipoprotein|cardiovascular|HDL|EPA|DHA", re.I),
    },
    "musculoskeletal_biglycan": {
        "criteria": {
            "pi_names": [{"any_name": "Fallon Justin"}],
            "org_names": ["BROWN UNIVERSITY"],
            "org_states": ["RI"],
            "fiscal_years": FY,
        },
        "title_hint": re.compile(r"biglycan|muscle|dystrophin|MSK|musculoskeletal", re.I),
    },
}

# Known project numbers to always try (grant anchors + dossier cites)
KNOWN_PROJECT_NUMS: dict[str, list[str]] = {
    "pediatric_digital_sepsis": ["R33TW012211", "R01DK116163"],
    "smurf2_oncology": ["R01CA173453"],
    "soma_pain_dtx": ["P20GM103645"],
    "tme_epigenetics": ["R01CA253976", "R01CA216265"],
    "monaghan_deep_rna_dx": ["R35GM142638"],
    "chitinase_fibrosis": ["P01HL114501"],
    "genomics_nabsys": ["R43HG004433"],
}

ASSET_TO_THEME: dict[str, str] = {
    "gap_uri_phlip_lnp": "uri_phlip_lnp",
    "gap_rih_salivary_ev_ad": "rih_salivary_ev_ad",
    "gap_rih_bx912_pulmonary_htn": "rih_bx912_pulmonary_htn",
    "gap_rih_pahtn_dx": "rih_pahtn_dx",
    "gap_rih_bbb_nucleic_delivery": "rih_bbb_nucleic_delivery",
    "gap_rih_motile_cell_msk": "rih_motile_cell_msk",
    "gap_rih_ecm_joint_repair": "rih_ecm_joint_repair",
    "gap_rih_enhancer_rna_glioma": "rih_enhancer_rna_glioma",
    "gap_rih_lpa_therapeutic": "rih_lpa_therapeutic",
    "ip_biglycan_msk": "musculoskeletal_biglycan",
}


def search(criteria: dict, limit: int = 30) -> list[dict]:
    body = json.dumps(
        {
            "criteria": criteria,
            "limit": limit,
            "sort_field": "fiscal_year",
            "sort_order": "desc",
        }
    ).encode()
    req = urllib.request.Request(
        API, data=body, headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.load(resp)
    return data.get("results", [])


def search_project_nums(nums: list[str]) -> list[dict]:
    if not nums:
        return []
    return search({"project_nums": nums, "fiscal_years": FY}, limit=len(nums) + 5)


def slim(row: dict) -> dict:
    org = row.get("organization") or {}
    ic = (row.get("agency_ic_admin") or {}).get("abbreviation") or row.get("agency_code") or "NIH"
    return {
        "project_num": row.get("project_num") or row.get("core_project_num"),
        "core_project_num": row.get("core_project_num"),
        "fiscal_year": row.get("fiscal_year"),
        "award_amount": row.get("award_amount") or row.get("direct_cost_amt"),
        "agency": ic,
        "activity_code": row.get("activity_code"),
        "title": (row.get("project_title") or "")[:220],
        "pi": row.get("contact_pi_name"),
        "org": org.get("org_name"),
        "url": row.get("project_detail_url") or "https://reporter.nih.gov",
    }


def dedupe_by_core(grants: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for g in grants:
        core = normalize_core_id(g.get("core_project_num") or g.get("project_num"))
        if not core:
            continue
        prev = best.get(core)
        if not prev or (g.get("fiscal_year") or 0) > (prev.get("fiscal_year") or 0):
            best[core] = g
    return sorted(best.values(), key=lambda x: (-(x.get("fiscal_year") or 0), x.get("title", "")))


def normalize_core_id(raw: str | None) -> str | None:
    if not raw:
        return None
    s = re.sub(r"^\d+", "", str(raw).strip().upper()).split("-")[0].replace(" ", "")
    return s if len(s) >= 6 else None


def to_grant_record(g: dict, note: str | None = None) -> dict:
    core = normalize_core_id(g.get("core_project_num") or g.get("project_num"))
    activity = g.get("activity_code") or (re.match(r"^[A-Z]+\d+", core or "") and core[:3] or "Grant")
    agency = g.get("agency") or "NIH"
    agency_label = f"NIH/{agency}" if agency and not str(agency).startswith("NIH") else str(agency)
    if agency in ("NCI", "NIGMS", "NINDS", "NHLBI", "NIDDK", "FIC", "NHGRI", "NEI", "NIAID"):
        agency_label = f"NIH/{agency}"
    pi = (g.get("pi") or "").title().replace(", ", " ").strip() or "—"
    return {
        "agency": agency_label,
        "id": core,
        "title": g.get("title") or "NIH award",
        "recipient": pi,
        "type": activity,
        "fy": g.get("fiscal_year"),
        "amount_usd": int(g["award_amount"]) if g.get("award_amount") else None,
        "url": g.get("url") or "https://reporter.nih.gov",
        **({"note": note} if note else {}),
    }


def harvest_theme(theme_id: str, cfg: dict) -> list[dict]:
    rows = [slim(r) for r in search(cfg["criteria"], limit=40)]
    hint = cfg.get("title_hint")
    if hint:
        filtered = [r for r in rows if hint.search(r.get("title") or "")]
        rows = filtered if filtered else rows[:8]
    else:
        rows = rows[:12]
    return dedupe_by_core(rows)


def _needs_reporter_refresh(grants: list[dict]) -> bool:
    """Replace placeholder or truncated RePORTER ids from a prior buggy harvest."""
    if not grants:
        return False
    return any(
        (g.get("id") in (None, "R01A", "R21A"))
        or (g.get("note") and "not harvested" in g.get("note", "").lower())
        for g in grants
    )


def merge_grant_lists(existing: list[dict], new: list[dict]) -> list[dict]:
    by_id: dict[str, dict] = {}
    for g in existing + new:
        key = (g.get("id") or g.get("title", "")).upper()
        if not key:
            continue
        prev = by_id.get(key)
        if not prev or (g.get("fy") or 0) > (prev.get("fy") or 0):
            by_id[key] = g
    return sorted(by_id.values(), key=lambda x: (-(x.get("fy") or 0), x.get("title", "")))


def main() -> None:
    fm_path = ROOT / "data" / "ri_funding_matrix.json"
    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    fm = json.loads(fm_path.read_text())
    opp = json.loads(opp_path.read_text())

    harvested: dict[str, list[dict]] = {}

    for theme_id, cfg in THEME_SEARCH.items():
        print(f"Harvest {theme_id}…")
        harvested[theme_id] = harvest_theme(theme_id, cfg)
        print(f"  → {len(harvested[theme_id])} awards")
        time.sleep(0.45)

    # Curated fallbacks when RePORTER has no PHLIP/Lp(a)-specific award titles
    harvested["uri_phlip_lnp"] = merge_grant_lists(
        harvested.get("uri_phlip_lnp", []),
        dedupe_by_core(
            [slim(r) for r in search_project_nums(["R01GM073857"])]
        ),
    )
    harvested["rih_lpa_therapeutic"] = merge_grant_lists(
        harvested.get("rih_lpa_therapeutic", []),
        dedupe_by_core(
            [slim(r) for r in search_project_nums(["R01HL159204"])]
        ),
    )

    for theme_id, nums in KNOWN_PROJECT_NUMS.items():
        rows = dedupe_by_core([slim(r) for r in search_project_nums(nums)])
        if rows:
            harvested[theme_id] = merge_grant_lists(
                harvested.get(theme_id, []),
                rows,
            )

    for theme in fm["investment_themes"]:
        tid = theme["id"]
        if tid not in harvested:
            continue
        notes = {
            "uri_phlip_lnp": "Engelman/Reshetnyak PHLIP–membrane insertion science; add URI-specific awards when listed in RePORTER.",
            "rih_lpa_therapeutic": "Song RIH cardiovascular lipid program; verify overlap with WO Lp(a) therapeutic PCT.",
        }
        records = [
            to_grant_record(g, notes.get(tid)) for g in harvested[tid]
        ]
        records = [r for r in records if r.get("id") and len(str(r["id"])) >= 6]
        if not records:
            continue
        theme["grants"] = merge_grant_lists(
            [] if _needs_reporter_refresh(theme.get("grants", [])) else theme.get("grants", []),
            records,
        )

    # Sync grant_anchors on gaps from matrix + opportunities
    theme_by_id = {t["id"]: t for t in fm["investment_themes"]}
    for gap in opp["gaps_not_in_curated_patents"]:
        asset_id = gap["id"]
        theme_id = ASSET_TO_THEME.get(asset_id)
        if not theme_id:
            continue
        theme = theme_by_id.get(theme_id)
        if not theme:
            continue
        ids = [g["id"] for g in theme.get("grants", []) if g.get("id")]
        if ids:
            existing = gap.get("grant_anchors") or []
            merged = list(dict.fromkeys(existing + ids))
            gap["grant_anchors"] = merged[:6]

    fm["updated_at"] = NOW
    fm["version"] = "2.2"
    opp["updated_at"] = NOW

    fm_path.write_text(json.dumps(fm, indent=2) + "\n")
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")

    empty = [t["id"] for t in fm["investment_themes"] if not t.get("grants")]
    print(f"Updated funding matrix. Themes still without grants: {empty}")


if __name__ == "__main__":
    main()
