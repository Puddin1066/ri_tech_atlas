#!/usr/bin/env python3
"""Add 10 new gap assets + patents from USPTO ODP harvest (June 2026)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

NEW_PATENTS: list[dict] = [
    {
        "patent_number": "WO2025171027A1",
        "title": "PHLIP-LNP for targeted intracellular delivery of nucleic acid therapeutics",
        "publication_date": "2025-08-28",
        "assignee": "University of Rhode Island",
        "inventors": "URI PHLIP program",
        "source_query": "odp URI PHLIP",
        "theme": "uri_phlip_lnp",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_uri_phlip_lnp"],
        "science_field": "Non-viral RNA / LNP delivery — pH-inserting peptide (PHLIP)",
        "association": "primary",
        "application_number": "PCTUS2025014619",
    },
    {
        "patent_number": "WO2025081077A1",
        "title": "Targeted intracellular delivery of dimeric MSA STING by two PHLIP peptides",
        "publication_date": "2025-04-17",
        "assignee": "University of Rhode Island",
        "inventors": "URI PHLIP program",
        "source_query": "odp URI STING",
        "theme": "uri_phlip_lnp",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_uri_phlip_lnp"],
        "science_field": "Innate immuno-oncology — STING agonist delivery",
        "association": "primary",
        "application_number": "PCTUS2024051097",
    },
    {
        "patent_number": "WO2024040027A1",
        "title": "PHLIP-mediated delivery of STING agonists",
        "publication_date": "2024-02-29",
        "assignee": "University of Rhode Island",
        "inventors": "URI PHLIP program",
        "source_query": "odp URI STING",
        "theme": "uri_phlip_lnp",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_uri_phlip_lnp"],
        "science_field": "Innate immuno-oncology — STING agonist delivery",
        "association": "adjacent",
        "application_number": "PCTUS2023072169",
    },
    {
        "patent_number": "US20260103757A1",
        "title": "Salivary extracellular vesicles as biomarkers for Alzheimer's disease",
        "publication_date": "2026-04-02",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH neurodegeneration Dx",
        "source_query": "odp RIH salivary Alzheimer",
        "theme": "rih_salivary_ev_ad",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_salivary_ev_ad"],
        "science_field": "Neuro diagnostics — salivary liquid biopsy",
        "association": "primary",
        "application_number": "19359020",
    },
    {
        "patent_number": "WO2026112526A1",
        "title": "Use of BX-912 for treatment of pulmonary hypertension",
        "publication_date": "2026-06-05",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH cardiopulmonary",
        "source_query": "odp RIH BX-912",
        "theme": "rih_bx912_pulmonary_htn",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_bx912_pulmonary_htn"],
        "science_field": "Cardiopulmonary therapeutics — PDE3/DAPK1 pathway (BX-912)",
        "association": "primary",
        "application_number": "PCTUS2025056723",
    },
    {
        "patent_number": "US20180094317A1",
        "title": "Diagnostics for pulmonary arterial hypertension and sudden cardiac death",
        "publication_date": "2018-04-05",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH cardiopulmonary",
        "source_query": "odp RIH PAH",
        "theme": "rih_pahtn_dx",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_pahtn_dx"],
        "science_field": "Cardiopulmonary diagnostics — PAH risk stratification",
        "association": "primary",
        "application_number": "15443762",
    },
    {
        "patent_number": "WO2025171161A1",
        "title": "Nucleic acid delivery crossing the blood-brain barrier and other blood-tissue barriers",
        "publication_date": "2025-08-28",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH CNS delivery",
        "source_query": "odp RIH BBB",
        "theme": "rih_bbb_nucleic_delivery",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_bbb_nucleic_delivery"],
        "science_field": "CNS delivery — BBB-crossing nucleic acid platform",
        "association": "primary",
        "application_number": "PCTUS2025014835",
    },
    {
        "patent_number": "WO2025155768A1",
        "title": "Motile injectable cell accelerates musculoskeletal connective tissue repair",
        "publication_date": "2025-07-31",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH regenerative medicine",
        "source_query": "odp RIH motile cell",
        "theme": "rih_motile_cell_msk",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_motile_cell_msk"],
        "science_field": "Regenerative medicine — motile cell therapy for MSK",
        "association": "primary",
        "application_number": "PCTUS2025011942",
    },
    {
        "patent_number": "US20240139376A1",
        "title": "Reconstitution of extracellular matrices for musculoskeletal joint tissue repair",
        "publication_date": "2024-05-02",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH ECM / orthopedics",
        "source_query": "odp RIH ECM joint",
        "theme": "rih_ecm_joint_repair",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_ecm_joint_repair"],
        "science_field": "MSK — biomimetic ECM for joint repair",
        "association": "primary",
        "application_number": "18276593",
    },
    {
        "patent_number": "US20230323349A1",
        "title": "Targeting enhancer RNAs for treatment of primary brain tumors",
        "publication_date": "2023-10-12",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH neuro-oncology",
        "source_query": "odp RIH brain tumor",
        "theme": "rih_enhancer_rna_glioma",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_enhancer_rna_glioma"],
        "science_field": "Neuro-oncology — eRNA-targeted therapeutics",
        "association": "primary",
        "application_number": "18043511",
    },
    {
        "patent_number": "WO2025245119A1",
        "title": "Therapeutic approach for treating elevated lipoprotein(a)",
        "publication_date": "2025-11-27",
        "assignee": "Rhode Island Hospital",
        "inventors": "RIH cardiovascular",
        "source_query": "odp RIH Lp(a)",
        "theme": "rih_lpa_therapeutic",
        "source": "uspto_odp_mcp",
        "asset_ids": ["gap_rih_lpa_therapeutic"],
        "science_field": "Cardiovascular therapeutics — Lp(a) lowering",
        "association": "primary",
        "application_number": "PCTUS2025030206",
    },
    {
        "patent_number": "US20260083330A1",
        "title": "Enhanced fluorescence tissue and cancer margin imaging (Kersey)",
        "publication_date": "2026-03-13",
        "assignee": "CytoVeris Inc.",
        "inventors": "Alan Kersey",
        "source_query": "odp CytoVeris",
        "theme": "oncolux_lumis_theranostic",
        "source": "uspto_odp_mcp",
        "asset_ids": ["ip_oncolux_lumis"],
        "science_field": "Surgical oncology — fluorescence margin imaging",
        "association": "primary",
        "application_number": "18893082",
        "note": "Kersey prior entity; maps to OncoLux LUMIS diligence",
    },
    {
        "patent_number": "US20250076201A1",
        "title": "Multispectral in-vivo imaging probe for enhanced tissue visualization",
        "publication_date": "2025-03-06",
        "assignee": "CytoVeris Inc.",
        "inventors": "Alan Kersey",
        "source_query": "odp CytoVeris",
        "theme": "oncolux_lumis_theranostic",
        "source": "uspto_odp_mcp",
        "asset_ids": ["ip_oncolux_lumis"],
        "science_field": "Surgical oncology — multispectral fluorescence",
        "association": "primary",
        "application_number": "18823616",
    },
    {
        "patent_number": "US20240310617A1",
        "title": "Mitigating specular highlights in imaging of biological tissue",
        "publication_date": "2024-09-19",
        "assignee": "CytoVeris Inc.",
        "inventors": "Alan Kersey",
        "source_query": "odp CytoVeris",
        "theme": "oncolux_lumis_theranostic",
        "source": "uspto_odp_mcp",
        "asset_ids": ["ip_oncolux_lumis"],
        "science_field": "Surgical imaging — optical artifact correction",
        "association": "adjacent",
        "application_number": "18575708",
    },
]

NEW_GAPS: list[dict] = [
    {
        "id": "gap_levine_pediatric_sepsis",
        "title": "Wearable pediatric sepsis ML (Levine / Garbern)",
        "note": "Grant-first (R33TW012211); no USPTO filing for Levine wearable sepsis product in ODP—orthogonal to Monaghan RNA Dx and ProThera IAIP biologic.",
        "grant_anchors": ["R33TW012211", "R01DK116163"],
        "existing_entity": None,
        "display_name": "Levine sepsis CDSS",
        "diligence_priority": 17,
        "headline": "Wearable ML lead-time for pediatric sepsis—R33-backed, SaMD path to US pilots.",
        "opportunity_hook": "FIC R33 Bangladesh validation → FDA SaMD classification → health-system pilot; pairs with RIH RNA Dx stack.",
        "key_patents_harvested": [],
        "patent_science_association": "none — publications + grants; not patent-defined today",
        "science_field": "Digital health — pediatric sepsis early warning",
    },
    {
        "id": "gap_uri_phlip_lnp",
        "title": "PHLIP peptide–LNP nucleic acid & STING delivery (URI)",
        "note": "URI Board of Trustees assignee; distinct from Brown/RIH Nanopieces—intracellular pH-triggered delivery.",
        "grant_anchors": [],
        "existing_entity": None,
        "display_name": "URI PHLIP platform",
        "diligence_priority": 18,
        "headline": "URI PHLIP–LNP intracellular delivery—STING and nucleic acid therapeutics.",
        "opportunity_hook": "URI tech transfer → RI spinout or license to genetic-medicine partner.",
        "key_patents_harvested": ["WO2025171027A1", "WO2025081077A1", "WO2024040027A1"],
        "patent_science_association": "primary — PHLIP delivery matches RNA/innate immuno asset science",
        "science_field": "Non-viral delivery — LNP / STING immuno-oncology",
    },
    {
        "id": "gap_rih_salivary_ev_ad",
        "title": "Salivary EV biomarkers for Alzheimer's disease (RIH)",
        "note": "RIH assignee; liquid biopsy from saliva—distinct from blood RNA-seq Monaghan line.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 19,
        "headline": "Salivary extracellular vesicle AD biomarkers—RIH diagnostic spinout.",
        "opportunity_hook": "Hospital lab validation → LDT or IVD partner → Slater seed after CLIA pilot.",
        "key_patents_harvested": ["US20260103757A1"],
        "patent_science_association": "primary",
        "science_field": "Neuro diagnostics — salivary liquid biopsy",
    },
    {
        "id": "gap_rih_bx912_pulmonary_htn",
        "title": "BX-912 for pulmonary hypertension (RIH)",
        "note": "PCT WO2026112526; small-molecule PH therapeutic—verify PI and hospital license chain.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 20,
        "headline": "BX-912 PH therapeutic—RIH-owned PCT family.",
        "opportunity_hook": "Preclinical PH model → IND-enabling → cardio therapeutics seed.",
        "key_patents_harvested": ["WO2026112526A1"],
        "patent_science_association": "primary",
        "science_field": "Cardiopulmonary therapeutics",
    },
    {
        "id": "gap_rih_pahtn_dx",
        "title": "PAH / sudden cardiac death diagnostics (RIH)",
        "note": "US20180094317 family; companion Dx to BX-912 PH program or standalone risk stratification.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 21,
        "headline": "PAH and SCD diagnostic panel—RIH patent family since 2018.",
        "opportunity_hook": "Biomarker validation → cardio Dx license or spinout.",
        "key_patents_harvested": ["US20180094317A1"],
        "patent_science_association": "primary",
        "science_field": "Cardiopulmonary diagnostics",
    },
    {
        "id": "gap_rih_bbb_nucleic_delivery",
        "title": "BBB-crossing nucleic acid delivery (RIH)",
        "note": "WO2025171161; CNS delivery platform—FTO vs AAV and other BBB approaches.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 22,
        "headline": "RIH platform for nucleic acid delivery across blood–brain barrier.",
        "opportunity_hook": "Rodent BBB PoC → gene-therapy or antisense partner license.",
        "key_patents_harvested": ["WO2025171161A1"],
        "patent_science_association": "primary",
        "science_field": "CNS / gene delivery",
    },
    {
        "id": "gap_rih_motile_cell_msk",
        "title": "Motile injectable cell for MSK repair (RIH)",
        "note": "WO2025155768; regenerative cell therapy for connective tissue—distinct from XM ECM morsels.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 23,
        "headline": "Motile injectable cell therapy accelerates MSK connective-tissue repair.",
        "opportunity_hook": "Large-animal tendon/ligament model → orthobiologics spinout.",
        "key_patents_harvested": ["WO2025155768A1"],
        "patent_science_association": "primary",
        "science_field": "Regenerative medicine / orthobiologics",
    },
    {
        "id": "gap_rih_ecm_joint_repair",
        "title": "Biomimetic ECM for joint tissue repair (RIH)",
        "note": "US20240139376; ECM reconstitution for joint repair—adjacent science to XM Therapeutics morsels.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 24,
        "headline": "RIH ECM reconstitution for musculoskeletal joint repair.",
        "opportunity_hook": "Orthopedic pilot → license vs XM field-of-use check.",
        "key_patents_harvested": ["US20240139376A1"],
        "patent_science_association": "primary",
        "science_field": "MSK — extracellular matrix therapeutics",
    },
    {
        "id": "gap_rih_enhancer_rna_glioma",
        "title": "Enhancer RNA targeting for primary brain tumors (RIH)",
        "note": "US20230323349; eRNA oncology—distinct from HiTIMED epigenetic deconvolution.",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 25,
        "headline": "eRNA-targeted therapeutics for primary brain tumors—RIH patent.",
        "opportunity_hook": "Glioma models → neuro-oncology biotech seed or pharma option.",
        "key_patents_harvested": ["US20230323349A1"],
        "patent_science_association": "primary",
        "science_field": "Neuro-oncology therapeutics",
    },
    {
        "id": "gap_rih_lpa_therapeutic",
        "title": "Lp(a)-lowering therapeutic approach (RIH)",
        "note": "WO2025245119 PCT; cardiovascular Lp(a)—crowded class (verify differentiation vs hepatocyte therapies).",
        "grant_anchors": [],
        "existing_entity": None,
        "diligence_priority": 26,
        "headline": "RIH therapeutic approach for elevated lipoprotein(a).",
        "opportunity_hook": "Mechanism validation → cardio metabolic seed or license.",
        "key_patents_harvested": ["WO2025245119A1"],
        "patent_science_association": "primary",
        "science_field": "Cardiovascular therapeutics — Lp(a)",
    },
]

FUNDING_THEMES: list[dict] = [
    {
        "id": "uri_phlip_lnp",
        "title": "PHLIP–LNP / STING delivery (URI)",
        "patent_theme": "uri_phlip_lnp",
        "patent_count": 3,
        "key_patents": ["WO2025171027A1", "WO2025081077A1", "WO2024040027A1"],
        "lead_entities": ["University of Rhode Island"],
        "grants": [],
    },
    {
        "id": "rih_salivary_ev_ad",
        "title": "Salivary EV Alzheimer's biomarkers (RIH)",
        "patent_theme": "rih_salivary_ev_ad",
        "patent_count": 1,
        "key_patents": ["US20260103757A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_bx912_pulmonary_htn",
        "title": "BX-912 pulmonary hypertension (RIH)",
        "patent_theme": "rih_bx912_pulmonary_htn",
        "patent_count": 1,
        "key_patents": ["WO2026112526A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_pahtn_dx",
        "title": "PAH / SCD diagnostics (RIH)",
        "patent_theme": "rih_pahtn_dx",
        "patent_count": 1,
        "key_patents": ["US20180094317A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_bbb_nucleic_delivery",
        "title": "BBB nucleic acid delivery (RIH)",
        "patent_theme": "rih_bbb_nucleic_delivery",
        "patent_count": 1,
        "key_patents": ["WO2025171161A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_motile_cell_msk",
        "title": "Motile cell MSK repair (RIH)",
        "patent_theme": "rih_motile_cell_msk",
        "patent_count": 1,
        "key_patents": ["WO2025155768A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_ecm_joint_repair",
        "title": "ECM joint repair (RIH)",
        "patent_theme": "rih_ecm_joint_repair",
        "patent_count": 1,
        "key_patents": ["US20240139376A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_enhancer_rna_glioma",
        "title": "eRNA glioma therapeutics (RIH)",
        "patent_theme": "rih_enhancer_rna_glioma",
        "patent_count": 1,
        "key_patents": ["US20230323349A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
    {
        "id": "rih_lpa_therapeutic",
        "title": "Lp(a) therapeutics (RIH)",
        "patent_theme": "rih_lpa_therapeutic",
        "patent_count": 1,
        "key_patents": ["WO2025245119A1"],
        "lead_entities": ["Rhode Island Hospital"],
        "grants": [],
    },
]

ONCOLUX_KEY_PATENTS = [
    "US20260083330A1",
    "US20250076201A1",
    "US20240310617A1",
]


def main() -> None:
    curated_path = ROOT / "data" / "ri_patents_curated.json"
    curated = json.loads(curated_path.read_text())
    by_num = {p["patent_number"].upper(): p for p in curated["patents"]}
    added = 0
    for rec in NEW_PATENTS:
        k = rec["patent_number"].upper()
        if k in by_num:
            by_num[k].update(rec)
        else:
            curated["patents"].append(rec)
            by_num[k] = rec
            added += 1
    curated["count"] = len(curated["patents"])
    curated["harvested_at"] = NOW
    curated["source_note"] = (
        "RI life-science corpus June 2026: 19 ip + 14 gaps; URI PHLIP; RIH hospital pipeline; "
        "CytoVeris→OncoLux linkage."
    )
    curated_path.write_text(json.dumps(curated, indent=2) + "\n")

    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    opp = json.loads(opp_path.read_text())
    existing_gap_ids = {g["id"] for g in opp["gaps_not_in_curated_patents"]}
    for gap in NEW_GAPS:
        if gap["id"] not in existing_gap_ids:
            opp["gaps_not_in_curated_patents"].append(gap)
    for o in opp["opportunities"]:
        if o["id"] == "ip_oncolux_lumis":
            o["key_patents"] = ONCOLUX_KEY_PATENTS
            o["patent_count"] = len(ONCOLUX_KEY_PATENTS)
            o["thesis"] = (
                "Multispectral fluorescence + in-situ photodynamic therapy (LUMIS); Kersey/CytoVeris "
                "patent family linked in curated annex; Mayo robotic bronchoscopy collaboration."
            )
    opp["version"] = "1.9"
    opp["updated_at"] = NOW
    opp["summary"]["curated_patent_filings_total"] = curated["count"]
    opp["summary"]["grant_supported_gaps"] = len(opp["gaps_not_in_curated_patents"])
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")

    fund_path = ROOT / "data" / "ri_funding_matrix.json"
    fund = json.loads(fund_path.read_text())
    fund["updated_at"] = NOW
    existing_ids = {t["id"] for t in fund["investment_themes"]}
    for theme in FUNDING_THEMES:
        if theme["id"] not in existing_ids:
            fund["investment_themes"].append(theme)
    fund_path.write_text(json.dumps(fund, indent=2) + "\n")

    print(f"Patents: {curated['count']} (+{added} new rows)")
    print(f"Gaps: {len(opp['gaps_not_in_curated_patents'])} total")
    print(f"OncoLux key patents: {len(ONCOLUX_KEY_PATENTS)}")


if __name__ == "__main__":
    main()
