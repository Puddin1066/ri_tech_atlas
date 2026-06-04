#!/usr/bin/env python3
"""Tag gap-harvest patents with asset_ids, science_field, association; sync gaps + funding matrix."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

NEW_PATENTS: list[dict] = [
    {
        "patent_number": "WO2024192252A1",
        "title": "Use of small molecules to increase hypoxia inducible factor (HIF) activity",
        "publication_date": "2024-09-12",
        "assignee": "Brown University",
        "inventors": "Wafik S. El-Deiry",
        "source_query": "odp inventor El-Deiry query HIF",
        "theme": "smurf2_oncology_hif",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_smurf2_oncology"],
        "science_field": "Oncology — HIF-1α pathway small molecules",
        "association": "primary",
        "application_number": "PCTUS2024019955",
        "note": "SMURF-Tx science; assignee Brown (not SMURF-Therapeutics Inc in USPTO)",
    },
    {
        "patent_number": "US20230183356A1",
        "title": "HIF-1α modulators and uses thereof",
        "publication_date": "2023-06-15",
        "assignee": "Brown University",
        "inventors": "Wafik S. El-Deiry",
        "source_query": "odp inventor El-Deiry",
        "theme": "smurf2_oncology_hif",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_smurf2_oncology"],
        "science_field": "Oncology — HIF-1α pathway small molecules",
        "association": "primary",
        "application_number": "18080452",
    },
    {
        "patent_number": "US20230219957A1",
        "title": "Small molecule CB002-analogues restore the p53 pathway and target S-phase checkpoint",
        "publication_date": "2023-07-13",
        "assignee": "Brown University",
        "inventors": "Wafik S. El-Deiry",
        "source_query": "odp inventor El-Deiry",
        "theme": "smurf2_oncology_hif",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_smurf2_oncology"],
        "science_field": "Oncology — p53-pathway restoration (El-Deiry program)",
        "association": "primary",
        "application_number": "17996493",
    },
    {
        "patent_number": "US20250372198A1",
        "title": "System and method for hierarchical tumor immune microenvironment epigenetic deconvolution (HiTIMED)",
        "publication_date": "2025-12-04",
        "assignee": "Dartmouth College",
        "inventors": "Brock C. Christensen; Lucas A. Salas; Ze Zhang; Karl T. Kelsey; John K. Wiencke; Devin C. Koestler",
        "source_query": "odp Christensen Dartmouth HiTIMED",
        "theme": "hitimed_tme_epigenetic_dx",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_christensen_epigenetics"],
        "science_field": "Immuno-oncology diagnostics — TME epigenetic deconvolution",
        "association": "primary",
        "application_number": "18854472",
        "note": "US national phase of PCTUS2023012438; pairs with EP4505463A1",
    },
    {
        "patent_number": "WO2023196051A1",
        "title": "System and method for hierarchical tumor immune microenvironment epigenetic deconvolution",
        "publication_date": "2023-10-19",
        "assignee": "Dartmouth College",
        "inventors": "Brock C. Christensen; Lucas A. Salas; Ze Zhang",
        "source_query": "odp Christensen Dartmouth",
        "theme": "hitimed_tme_epigenetic_dx",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_christensen_epigenetics"],
        "science_field": "Immuno-oncology diagnostics — TME epigenetic deconvolution",
        "association": "primary",
        "application_number": "PCTUS2023012438",
        "note": "Intl. HiTIMED family; priority 2022-04-06",
    },
    {
        "patent_number": "WO2024187092A1",
        "title": "Hierarchical tumor AI classifier traces tissue of origin and tumor type using DNA methylation",
        "publication_date": "2024-09-12",
        "assignee": "Dartmouth College",
        "inventors": "Brock C. Christensen; Lucas A. Salas; Ze Zhang",
        "source_query": "odp Christensen Dartmouth",
        "theme": "hitimed_tme_epigenetic_dx",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_christensen_epigenetics"],
        "science_field": "Cancer diagnostics — DNA methylation deconvolution (platform-adjacent)",
        "association": "adjacent",
        "application_number": "PCTUS2024019077",
    },
    {
        "patent_number": "WO2026096333A1",
        "title": "Estimating cell-type proportions from DNA methylation microarray data to determine glioma immune microenvironment",
        "publication_date": "2026-05-07",
        "assignee": "Dartmouth College",
        "inventors": "Lucas A. Salas; Brock C. Christensen; Ze Zhang",
        "source_query": "odp Salas HiTIMED",
        "theme": "hitimed_tme_epigenetic_dx",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_christensen_epigenetics"],
        "science_field": "Neuro-oncology diagnostics — glioma immune methylation deconvolution",
        "association": "adjacent",
        "application_number": "PCTUS2025052585",
    },
    {
        "patent_number": "US20260137929A1",
        "title": "Kinetic intelligent wireless implant",
        "publication_date": "2026-05-21",
        "assignee": "Genesis Intelligence, LLC",
        "inventors": "Newton Howard",
        "source_query": "odp Howard KIWI",
        "theme": "ni2o_kiwi_bci",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_ni2o_kiwi_bci"],
        "science_field": "Neurotechnology — wireless micro-implant BCI (KIWI)",
        "association": "primary",
        "application_number": "19450252",
        "note": "Howard/Genesis Intelligence estate; ni2o commercial path — not ni2o assignee in USPTO",
    },
    {
        "patent_number": "US20210196980A1",
        "title": "Kinetic intelligent wireless implant / neurons on augmented human",
        "publication_date": "2021-07-01",
        "assignee": "Genesis Intelligence, LLC",
        "inventors": "Newton Howard",
        "source_query": "odp Howard KIWI",
        "theme": "ni2o_kiwi_bci",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_ni2o_kiwi_bci"],
        "science_field": "Neurotechnology — wireless micro-implant BCI (KIWI)",
        "association": "primary",
        "application_number": "17198518",
    },
    {
        "patent_number": "US20210263589A1",
        "title": "Transcranial kinetic intelligent wireless implant",
        "publication_date": "2021-08-26",
        "assignee": "Genesis Intelligence, LLC",
        "inventors": "Newton Howard",
        "source_query": "odp Howard KIWI",
        "theme": "ni2o_kiwi_bci",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_ni2o_kiwi_bci"],
        "science_field": "Neurotechnology — cranial wireless BCI (KIWI variant)",
        "association": "primary",
        "application_number": "17175680",
    },
]

EXISTING_PATCH: dict[str, dict] = {
    "EP4505463A1": {
        "asset_ids": ["gap_christensen_epigenetics"],
        "science_field": "Immuno-oncology diagnostics — TME epigenetic deconvolution (HiTIMED)",
        "association": "primary",
        "source": "google_patents+uspto_odp_mcp",
    },
}

GAP_PATCH: dict[str, dict] = {
    "gap_smurf2_oncology": {
        "note": "3 primary Brown HIF/p53 filings linked (USPTO ODP); no SMURF-Therapeutics assignee — license from Brown OTL. Penn State p53 background families excluded from key list.",
        "key_patents_harvested": [
            "WO2024192252A1",
            "US20230183356A1",
            "US20230219957A1",
        ],
        "patent_science_association": "primary — HIF-1α / p53 oncology matches SMURF2–HIF1α asset science; assignee mismatch vs company name",
        "science_field": "Oncology — hypoxia / tumor suppressor pathway therapeutics",
    },
    "gap_soma_dtx": {
        "note": "No USPTO applications for Petzschner/Gunsilius (ODP 404). COBRE P20GM103645 — interoception/pain DTx likely SaMD/trade secret, not patent-defined unit.",
        "key_patents_harvested": [],
        "patent_science_association": "none — digital therapeutic / computational psychiatry field has no matching US patent annex",
        "science_field": "Digital health — interoception / chronic pain DTx",
    },
    "gap_christensen_epigenetics": {
        "note": "HiTIMED US+EP+PCT linked (Dartmouth assignee). Brown collaborator on grants — OTL sublicense diligence. Adjacent methylation classifier + glioma PCT in curated annex.",
        "key_patents_harvested": [
            "EP4505463A1",
            "US20250372198A1",
            "WO2023196051A1",
        ],
        "patent_science_association": "primary — immune TME epigenetic deconvolution matches HiTIMED asset science",
        "science_field": "Diagnostics — tumor immune microenvironment epigenetics",
    },
    "gap_ni2o_kiwi_bci": {
        "note": "19+ Howard/Genesis Intelligence KIWI filings (representative 3 in key list). No ni2o assignee — map company via Howard license. Brown BrainGate wireless patents are separate FTO (theme neurotech).",
        "key_patents_harvested": [
            "US20260137929A1",
            "US20210196980A1",
            "US20210263589A1",
        ],
        "patent_science_association": "primary — wireless cranial micro-implant BCI matches KIWI asset science; corporate assignee is Genesis Intelligence not ni2o Inc",
        "science_field": "Neurotechnology — wireless brain-computer interface implants",
    },
}

FUNDING_PATCH: dict[str, dict] = {
    "smurf2_oncology": {
        "patent_theme": "smurf2_oncology_hif",
        "patent_count": 3,
        "key_patents": ["WO2024192252A1", "US20230183356A1", "US20230219957A1"],
    },
    "soma_pain_dtx": {
        "patent_theme": None,
        "patent_count": 0,
        "key_patents": [],
        "patent_science_association": "none — grant/SaMD path; no US patents for SOMA inventors",
    },
    "tme_epigenetics": {
        "patent_theme": "hitimed_tme_epigenetic_dx",
        "patent_count": 3,
        "key_patents": ["EP4505463A1", "US20250372198A1", "WO2023196051A1"],
    },
    "ni2o_kiwi_bci": {
        "patent_theme": "ni2o_kiwi_bci",
        "patent_count": 3,
        "key_patents": ["US20260137929A1", "US20210196980A1", "US20210263589A1"],
    },
}


def main() -> None:
    curated_path = ROOT / "data" / "ri_patents_curated.json"
    curated = json.loads(curated_path.read_text())
    by_num = {p["patent_number"].upper(): p for p in curated["patents"]}

    added = 0
    for rec in NEW_PATENTS:
        key = rec["patent_number"].upper()
        if key in by_num:
            by_num[key].update(rec)
        else:
            curated["patents"].append(rec)
            by_num[key] = rec
            added += 1

    for num, patch in EXISTING_PATCH.items():
        if num.upper() in by_num:
            by_num[num.upper()].update(patch)

    curated["count"] = len(curated["patents"])
    curated["harvested_at"] = NOW
    curated["source_note"] = (
        "Curated filings tied to RI institutions/companies. Gap harvest June 2026: "
        "El-Deiry/Brown HIF-p53 (gap_smurf2); Christensen/Salas HiTIMED US+WO (gap_christensen); "
        "Howard/Genesis KIWI (gap_ni2o); SOMA — no US patents."
    )
    curated_path.write_text(json.dumps(curated, indent=2) + "\n")

    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    opp = json.loads(opp_path.read_text())
    for gap in opp["gaps_not_in_curated_patents"]:
        if gap["id"] in GAP_PATCH:
            gap.update(GAP_PATCH[gap["id"]])
    opp["version"] = "1.8"
    opp["updated_at"] = NOW
    opp["summary"]["curated_patent_filings_total"] = curated["count"]
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")

    fund_path = ROOT / "data" / "ri_funding_matrix.json"
    fund = json.loads(fund_path.read_text())
    for theme in fund["investment_themes"]:
        if theme["id"] in FUNDING_PATCH:
            theme.update(FUNDING_PATCH[theme["id"]])
    fund_path.write_text(json.dumps(fund, indent=2) + "\n")

    print(f"Curated: {curated['count']} patents ({added} new)")
    print("Updated gaps, opportunities v1.8, funding_matrix themes")


if __name__ == "__main__":
    main()
