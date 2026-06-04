#!/usr/bin/env python3
"""Polish dossier copy + citation anchors (PMID, grants, patents, URLs). Minimal schema changes."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

# Comparable company name → canonical URL (public sources)
COMP_URLS: dict[str, str] = {
    "Moderna / BioNTech LNP": "https://www.modernatx.com/",
    "Merck Winrevair": "https://www.merck.com/",
    "Liquidia Yutrepia": "https://www.liquidia.com/",
    "HeartTest Laboratories": "https://www.hearttestlabs.com/",
    "Denali ATV": "https://www.denalitherapeutics.com/",
    "Voyager AAV CNS": "https://www.voyagertherapeutics.com/",
    "Orthocell CelGro": "https://www.orthocell.com/",
    "MiMedx": "https://www.mimedx.com/",
    "Anika Orthobiologics": "https://www.anikatherapeutics.com/",
    "Day One ONC201": "https://www.dayonebio.com/",
    "Chimerix ONC201 lineage": "https://www.chimerix.com/",
    "Novartis pelacarsen": "https://www.novartis.com/",
    "Amgen olpasiran": "https://www.amgen.com/",
    "Ventrix": "https://www.ventrixmedical.com/",
}

# Full comparables row polish for thin / new assets (citation-backed via evidence_anchors on asset)
COMP_ROWS: dict[str, dict] = {
    "gap_uri_phlip_lnp": {
        "market": "Tumor-targeted delivery; acidic microenvironment enables selective uptake",
        "sam": "PHLIP peptide delivery for LNP / STING payloads (URI)",
        "comparables": [
            {
                "name": "Aera Therapeutics",
                "financing": "$193M Series A+B (2023)",
                "path": "Extrahepatic LNP → IND",
                "url": "https://aeratx.com/",
            },
            {
                "name": "pHLIP Therapeutics",
                "financing": "Clinical-stage imaging",
                "path": "Acidosis-targeted peptide delivery",
                "url": "https://www.phlip.com/",
            },
        ],
        "comparable_financing": "Aera $193M; pHLIP clinical imaging path",
        "benchmark_path": "Rodent tumor delivery PoC → URI license",
        "ri_path": "URI OTL → RI genetic-medicine spinout",
        "ri_round": "Slater $200–400K + match",
    },
    "gap_rih_salivary_ev_ad": {
        "market": "AD liquid biopsy; blood Dx peers raised $200M+",
        "sam": "Salivary EV biomarkers (non-invasive)",
        "comparables": [
            {
                "name": "Quanterix Simoa",
                "financing": "Public (NASDAQ: QTRX)",
                "path": "Ultra-sensitive blood immunoassays",
                "url": "https://www.quanterix.com/",
            },
            {
                "name": "C2N Diagnostics",
                "financing": "VC-backed AD blood tests",
                "path": "Plasma Aβ/tau commercialization",
                "url": "https://c2ndiagnostics.com/",
            },
        ],
        "comparable_financing": "Public Dx platforms; C2N VC path",
        "benchmark_path": "Analytical validation → CLIA pilot",
        "ri_path": "RIH/Brown license → Dx spinout",
        "ri_round": "$3–8M seed",
    },
    "gap_rih_bx912_pulmonary_htn": {
        "market": "PAH therapeutics; new biologic approved 2024",
        "sam": "BX-912 small-molecule PH program",
        "comparables": [
            {
                "name": "Merck Winrevair (sotatercept)",
                "financing": "FDA-approved 2024",
                "path": "Activin signaling PAH biologic",
                "url": "https://www.merck.com/",
            },
            {
                "name": "Liquidia Yutrepia",
                "financing": "Commercial inhaled PH",
                "path": "Treprostinil dry powder",
                "url": "https://www.liquidia.com/",
            },
        ],
        "comparable_financing": "Approved PAH benchmarks",
        "benchmark_path": "PH model PoC → IND-enabling",
        "ri_path": "RIH license → cardio therapeutics",
        "ri_round": "Seed / Series A",
    },
    "gap_rih_pahtn_dx": {
        "market": "Cardiopulmonary risk stratification",
        "sam": "PAH / sudden cardiac death Dx panel",
        "comparables": [
            {
                "name": "Eko Health",
                "financing": "$125M+ raised",
                "path": "AI cardiac auscultation FDA-cleared",
                "url": "https://www.ekohealth.com/",
            },
            {
                "name": "HeartTest Laboratories",
                "financing": "Public micro-vascular Dx",
                "path": "Endothelial function screening",
                "url": "https://www.hearttestlabs.com/",
            },
        ],
        "comparable_financing": "Cardio Dx VC / public comps",
        "benchmark_path": "Retrospective cohort → prospective registry",
        "ri_path": "RIH diagnostic license",
        "ri_round": "License or seed Dx",
    },
    "gap_rih_bbb_nucleic_delivery": {
        "market": "CNS genetic medicines; BBB delivery strategic",
        "sam": "RIH nucleic acid BBB platform (Chen)",
        "comparables": [
            {
                "name": "Denali Therapeutics (ATV)",
                "financing": "Big-pharma partnerships",
                "path": "BBB transport vehicle biologics",
                "url": "https://www.denalitherapeutics.com/",
            },
            {
                "name": "Voyager Therapeutics",
                "financing": "Strategic CNS gene therapy",
                "path": "AAV CNS programs",
                "url": "https://www.voyagertherapeutics.com/",
            },
        ],
        "comparable_financing": "Strategic CNS delivery deals",
        "benchmark_path": "Rodent BBB delivery PoC",
        "ri_path": "RIH → pharma option/license",
        "ri_round": "Upfront / option",
    },
    "gap_rih_motile_cell_msk": {
        "market": "Orthobiologics; meniscus injury drives PTOA risk",
        "sam": "Motile injectable cell therapy for MSK",
        "comparables": [
            {
                "name": "Orthocell (CelGro)",
                "financing": "ASX-listed orthobiologics",
                "path": "Collagen scaffold tendon repair",
                "url": "https://www.orthocell.com/",
            },
            {
                "name": "MiMedx",
                "financing": "Public amniotic products",
                "path": "Orthobiologics commercial",
                "url": "https://www.mimedx.com/",
            },
        ],
        "comparable_financing": "Public orthobiologics comps",
        "benchmark_path": "Large-animal meniscus repair → IND path",
        "ri_path": "RIH spinout after NIAMS-funded PoC",
        "ri_round": "$5–15M Series A",
    },
    "gap_rih_ecm_joint_repair": {
        "market": "Joint repair / injectable matrix",
        "sam": "ECM reconstitution for joint tissue",
        "comparables": [
            {
                "name": "XM Therapeutics",
                "financing": "Slater $375K + BBII",
                "path": "Injectable ECM morsels (Brown/XM)",
                "url": "https://www.xmtherapeutics.com/",
            },
            {
                "name": "Anika Therapeutics",
                "financing": "Public orthobiologics",
                "path": "Joint viscosupplementation",
                "url": "https://www.anikatherapeutics.com/",
            },
        ],
        "comparable_financing": "XM Slater-backed RI precedent",
        "benchmark_path": "Ortho pilot; FOU diligence vs XM OTL",
        "ri_path": "RIH license if FOU clear",
        "ri_round": "Slater $200–400K + match",
    },
    "gap_rih_enhancer_rna_glioma": {
        "market": "Neuro-oncology; diffuse glioma high unmet need",
        "sam": "eRNA-targeted glioma therapeutics",
        "comparables": [
            {
                "name": "Day One (ONC201)",
                "financing": "Public glioma program",
                "path": "Diffuse midline glioma",
                "url": "https://www.dayonebio.com/",
            },
            {
                "name": "Chimerix (ONC201 lineage)",
                "financing": "Clinical-stage heritage",
                "path": "Imipridone glioma path",
                "url": "https://www.chimerix.com/",
            },
        ],
        "comparable_financing": "Neuro-onc public/clinical comps",
        "benchmark_path": "Glioma models → IND-enabling tox",
        "ri_path": "RIH → neuro-onc biotech",
        "ri_round": "Series A",
    },
    "gap_rih_lpa_therapeutic": {
        "market": "Lp(a) cardiovascular; Phase 3 siRNA/antisense leaders",
        "sam": "RIH Lp(a)-lowering approach",
        "comparables": [
            {
                "name": "Novartis pelacarsen",
                "financing": "Phase 3 Lp(a) antisense",
                "path": "Lp(a) lowering outcomes trials",
                "url": "https://www.novartis.com/",
            },
            {
                "name": "Amgen olpasiran",
                "financing": "Phase 3 siRNA Lp(a)",
                "path": "Lp(a) cardiovascular outcomes",
                "url": "https://www.amgen.com/",
            },
        ],
        "comparable_financing": "Big-pharma Lp(a) programs",
        "benchmark_path": "Mechanism PoC → partner discussions",
        "ri_path": "RIH license → pharma option",
        "ri_round": "Strategic / Series A",
    },
}

# Gap story: short investor copy; technical detail stays in gap_note
STORY_GAPS: dict[str, dict] = {
    "gap_uri_phlip_lnp": {
        "headline": "URI PHLIP delivers cargo into acidic tissues—LNP and STING programs without classic endocytosis.",
        "opportunity_hook": "URI tech transfer → RI spinout or license; Engelman/Reshetnyak PHLIP science (PMID 24659971).",
        "thesis": "PHLIP peptides insert into membranes at low pH, enabling targeted intracellular delivery of LNPs and STING agonists. URI holds the WO patent family; differentiation is tumor/acid microenvironment selectivity versus systemic LNP players.",
        "evidence_anchors": [
            "PMID24659971",
            "PMID32411684",
            "PMID33443162",
            "R01GM073857",
            "https://web.uri.edu/research/",
        ],
    },
    "gap_rih_salivary_ev_ad": {
        "headline": "Salivary extracellular vesicles as a non-invasive Alzheimer's liquid biopsy.",
        "opportunity_hook": "RIH/Brown R01AG074284 supports analytical development; path to CLIA LDT then spinout.",
        "thesis": "Salivary EV RNA cargo can reflect neurodegeneration pathways, offering a less invasive alternative to plasma assays. RIH and Brown co-applicant on active NIH award; US20260103757A1 anchors the IP.",
        "evidence_anchors": [
            "PMID41602168",
            "US20260103757A1",
            "R01AG074284",
        ],
    },
    "gap_rih_bx912_pulmonary_htn": {
        "headline": "BX-912 program for pulmonary hypertension—RIH PCT with multi-center inventor team.",
        "opportunity_hook": "Preclinical PH models → IND-enabling; benchmark against 2024 PAH biologic approval.",
        "thesis": "BX-912 is being developed for PAH with RIH as assignee on WO2026112526. Strategic context is crowded PAH market but clear regulatory benchmarks for clinical development paths.",
        "evidence_anchors": ["WO2026112526A1"],
    },
    "gap_rih_pahtn_dx": {
        "headline": "RIH diagnostic panel for pulmonary arterial hypertension and sudden cardiac death risk.",
        "opportunity_hook": "Mature US20180094317 family; retrospective → prospective validation.",
        "thesis": "Assignee Rhode Island Hospital on a long-running Dx patent family (Dudley/Ventetuolo). Commercial path is risk stratification licensing or a Dx spinout after clinical validation.",
        "evidence_anchors": ["US20180094317A1"],
    },
    "gap_rih_bbb_nucleic_delivery": {
        "headline": "RIH platform for nucleic acid delivery across the blood–brain barrier.",
        "opportunity_hook": "Qian Chen (NanoDe peer) leads BBB nucleic delivery PCT; partner or license path.",
        "thesis": "WO2025171161 describes materials and methods for nucleic acid delivery across the BBB. Near-term value is rodent PoC plus gene-therapy partnership options rather than immediate product revenue.",
        "evidence_anchors": ["WO2025171161A1", "PMID37513879"],
    },
    "gap_rih_motile_cell_msk": {
        "headline": "Motile injectable cell therapy to accelerate meniscus and connective-tissue repair.",
        "opportunity_hook": "NIAMS R01AR080726 + R21AR077326 (Jayasuriya); large-animal next gate.",
        "thesis": "RIH patents cover motile injectable cell therapy for MSK repair. Peer-reviewed work links Jayasuriya lab programs to meniscus healing and reduced post-traumatic osteoarthritis (PMID 36312551, 39763468).",
        "evidence_anchors": [
            "WO2025155768A1",
            "PMID36312551",
            "PMID39763468",
            "R01AR080726",
            "R21AR077326",
        ],
        "grant_anchors": ["R01AR080726", "R21AR077326"],
    },
    "gap_rih_ecm_joint_repair": {
        "headline": "Biomimetic ECM reconstitution for musculoskeletal joint repair.",
        "opportunity_hook": "Field-of-use diligence vs XM Therapeutics before Slater-scale spinout.",
        "thesis": "US20240139376 and related RIH filings describe ECM reconstitution for joint repair. XM Therapeutics (Brown/XM) is the closest RI comp—license geography must be resolved before investor formation.",
        "evidence_anchors": ["US20240139376A1", "PMID29542287"],
    },
    "gap_rih_enhancer_rna_glioma": {
        "headline": "Enhancer RNA–targeted approach for primary brain tumors.",
        "opportunity_hook": "Tapinos-led RIH/Brown program; glioma model efficacy before neuro-onc seed.",
        "thesis": "US20230323349 targets enhancer RNAs in brain tumors with Nikolaos Tapinos as PI-inventor. Grant-supported Brown/RIH neuro-oncology ecosystem supports translational planning.",
        "evidence_anchors": ["US20230323349A1", "PMID40068999"],
    },
    "gap_rih_lpa_therapeutic": {
        "headline": "RIH therapeutic approach to lower lipoprotein(a)—cardiovascular metabolic niche.",
        "opportunity_hook": "Differentiate vs Phase 3 siRNA/antisense leaders; Song lab R01HL159204 anchors cardio lipid biology.",
        "thesis": "WO2025245119 PCT from RIH describes Lp(a)-lowering approaches. Likely strategic pharma path given competitive Lp(a) landscape (Novartis, Amgen Phase 3 programs).",
        "evidence_anchors": ["WO2025245119A1", "R01HL159204"],
    },
    "gap_levine_pediatric_sepsis": {
        "headline": "Wearable ML for earlier pediatric sepsis recognition—validated in Bangladesh ICU cohort.",
        "opportunity_hook": "FIC R33TW012211 → US SaMD path; pairs with RIH RNA Dx stack.",
        "thesis": "Prospective work shows wearable vitals plus ML can flag advanced sepsis hours before routine documentation (PMID 39475844, 41252746). Grant-backed program with Brown/RIH clinical leads.",
        "evidence_anchors": [
            "PMID39475844",
            "PMID41252746",
            "R33TW012211",
            "R01DK116163",
        ],
        "trial_anchors": [],
    },
    "gap_soma_dtx": {
        "evidence_anchors": ["PMID33378658", "P20GM103645"],
    },
}

STORY_IP_PATCH: dict[str, dict] = {
    "ip_genomics_hans": {
        "headline": "Electronic genome mapping (Nabsys)—commercial Brown-origin IP with strategic exit paths.",
        "opportunity_hook": "NHGRI R43HG004433 heritage; Hitachi interest—M&A/royalty, not Slater seed.",
    },
}

KOL_EVIDENCE: dict[str, list[str]] = {
    "gap_uri_phlip_lnp": ["PMID24659971", "R01GM073857"],
    "gap_rih_salivary_ev_ad": ["PMID41602168", "R01AG074284"],
    "gap_rih_motile_cell_msk": ["PMID36312551", "R01AR080726"],
    "gap_levine_pediatric_sepsis": ["PMID39475844", "R33TW012211"],
    "gap_rih_bbb_nucleic_delivery": ["WO2025171161A1"],
    "gap_rih_lpa_therapeutic": ["R01HL159204", "WO2025245119A1"],
}

ASSET_TO_FUNDING_THEME: dict[str, str] = {
    "ip_iaip_neonatal": "iaip_sepsis",
    "ip_ecm_morsels_xm": "ecm_morsels_xm",
    "ip_nanopieces_rna": "nanode_rna",
    "ip_chitinase_ocf203": "chitinase_fibrosis",
    "ip_dendritic_ad_mindimmune": "neuroinflammation_mindimmune",
    "ip_wireless_neurograins": "neurotech_wireless",
    "ip_speech_tablet_ibci": "neurotech_speech_tablet",
    "ip_spinal_isi_dbs": "neurotech_spinal_dbs",
    "ip_tregitope_immunomod": "immunoinformatics",
    "ip_biglycan_msk": "musculoskeletal_biglycan",
    "ip_neural_decoding_legacy": "neurotech_speech_tablet",
    "ip_osteopearl_vcf_lenoss": "kyphoplasty_lenoss",
    "ip_af_mapping_ai": "af_digital_health",
    "ip_genomics_hans": "genomics_nabsys",
    "ip_ect_ophthalmology": "ophthalmology_ect",
    "ip_monaghan_deep_rna_dx": "monaghan_deep_rna_dx",
    "ip_bolden_musk_neurogenesis": "bolden_musk_neurogenesis",
    "ip_pax_aav_vegf_tendon": "pax_aav_tendon",
    "ip_oncolux_lumis": "oncolux_lumis",
    "gap_smurf2_oncology": "smurf2_oncology",
    "gap_soma_dtx": "soma_pain_dtx",
    "gap_christensen_epigenetics": "tme_epigenetics",
    "gap_ni2o_kiwi_bci": "ni2o_kiwi_bci",
    "gap_levine_pediatric_sepsis": "pediatric_digital_sepsis",
    "gap_uri_phlip_lnp": "uri_phlip_lnp",
    "gap_rih_salivary_ev_ad": "rih_salivary_ev_ad",
    "gap_rih_bx912_pulmonary_htn": "rih_bx912_pulmonary_htn",
    "gap_rih_pahtn_dx": "rih_pahtn_dx",
    "gap_rih_bbb_nucleic_delivery": "rih_bbb_nucleic_delivery",
    "gap_rih_motile_cell_msk": "rih_motile_cell_msk",
    "gap_rih_ecm_joint_repair": "rih_ecm_joint_repair",
    "gap_rih_enhancer_rna_glioma": "rih_enhancer_rna_glioma",
    "gap_rih_lpa_therapeutic": "rih_lpa_therapeutic",
}

PHYSICIAN_PATCH: dict[str, dict] = {
    "gap_rih_motile_cell_msk": {
        "physician_equity_model": "Orthopedic surgeon KOL on SAB; Jayasuriya/Trivedi inventors anchor NIH meniscus repair awards (R01AR080726).",
        "milestones_18mo": [
            "Complete RIH exclusive license",
            "Large-animal meniscus repair data package",
            "Slater $200–400K + third-party match",
        ],
    },
    "gap_levine_pediatric_sepsis": {
        "physician_equity_model": "Levine MD MPH founder equity; Garbern MD co-PI on R33; hospital pilot design with RIH critical care.",
        "milestones_18mo": [
            "SaMD regulatory classification memo",
            "US health-system pilot protocol",
            "Innovate RI match + Slater seed filing",
        ],
    },
}


def merge_anchors(existing: list[str] | None, new: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in (existing or []) + new:
        key = raw.strip().upper()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(raw.strip())
    return out


def valid_grant_id(gid: str | None) -> bool:
    if not gid:
        return False
    g = gid.upper().strip()
    if len(g) < 8:
        return False
    return bool(re.match(r"^[RUPID]\d{2}[A-Z]{2}\d{5,}", g))


def clean_grant_anchors(anchors: list[str] | None) -> list[str]:
    return [a for a in (anchors or []) if valid_grant_id(a.split("_")[0])]


def main() -> None:
    comp_path = ROOT / "data" / "ri_comparables_matrix.json"
    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    fm_path = ROOT / "data" / "ri_funding_matrix.json"
    kol_path = ROOT / "data" / "ri_kol_directory.json"
    pl_path = ROOT / "data" / "ri_physician_led_financing.json"

    comp = json.loads(comp_path.read_text())
    opp = json.loads(opp_path.read_text())
    fm = json.loads(fm_path.read_text())
    kol = json.loads(kol_path.read_text())
    pl = json.loads(pl_path.read_text())

    theme_grants: dict[str, list[str]] = {}
    for t in fm["investment_themes"]:
        ids = [g["id"] for g in t.get("grants", []) if valid_grant_id(g.get("id"))]
        if ids:
            theme_grants[t["id"]] = ids

    asset_theme = ASSET_TO_FUNDING_THEME

    for row in comp["rows"]:
        aid = row["asset_id"]
        if aid in COMP_ROWS:
            row.update(COMP_ROWS[aid])
        for c in row.get("comparables", []):
            if c.get("name") in COMP_URLS and not c.get("url"):
                c["url"] = COMP_URLS[c["name"]]

    for g in opp["gaps_not_in_curated_patents"]:
        aid = g["id"]
        if aid in STORY_GAPS:
            patch = STORY_GAPS[aid]
            for k, v in patch.items():
                if k == "evidence_anchors":
                    g["evidence_anchors"] = merge_anchors(g.get("evidence_anchors"), v)
                elif k == "grant_anchors":
                    g["grant_anchors"] = merge_anchors(g.get("grant_anchors"), v)
                else:
                    g[k] = v
        tid = asset_theme.get(aid)
        if tid and tid in theme_grants:
            g["grant_anchors"] = merge_anchors(
                clean_grant_anchors(g.get("grant_anchors")), theme_grants[tid][:5]
            )
        else:
            g["grant_anchors"] = clean_grant_anchors(g.get("grant_anchors"))

    for o in opp["opportunities"]:
        if o["id"] in STORY_IP_PATCH:
            o.update(STORY_IP_PATCH[o["id"]])
        tid = asset_theme.get(o["id"])
        if tid and tid in theme_grants:
            o["grant_anchors"] = merge_anchors(
                clean_grant_anchors(o.get("grant_anchors")), theme_grants[tid][:5]
            )
        else:
            o["grant_anchors"] = clean_grant_anchors(o.get("grant_anchors"))

    for aid, ev in KOL_EVIDENCE.items():
        if aid in kol.get("assets", {}):
            kol["assets"][aid]["evidence"] = "; ".join(ev)

    for aid, patch in PHYSICIAN_PATCH.items():
        if aid in pl.get("slater_physician_match_by_asset", {}):
            pl["slater_physician_match_by_asset"][aid].update(patch)

    comp["updated_at"] = NOW
    comp["version"] = "1.3"
    opp["updated_at"] = NOW
    kol["updated_at"] = NOW
    pl["updated_at"] = NOW

    comp_path.write_text(json.dumps(comp, indent=2) + "\n")
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")
    kol_path.write_text(json.dumps(kol, indent=2) + "\n")
    pl_path.write_text(json.dumps(pl, indent=2) + "\n")
    print("Polished comparables, opportunities, KOL evidence, physician-led copy.")


if __name__ == "__main__":
    main()
