#!/usr/bin/env python3
"""
Sync inventors across ri_patents_curated.json, opportunities, gaps, and KOL anchors.
Enriches placeholder patent inventor strings from USPTO ODP inventorBag (embedded overrides).
Run after harvest: python3 scripts/sync_dossier_inventors.py
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

# USPTO ODP inventorNameText — keyed by patent_number (June 2026 refresh)
PATENT_INVENTOR_OVERRIDES: dict[str, str] = {
    "WO2025155768A1": "Chathuraka Teekshana Jayasuriya; Jay Trivedi",
    "US20240139376A1": "Chathuraka Teekshana Jayasuriya; Daniel S. Yang",
    "US20230323349A1": "Nikolaos Tapinos; Blessing Akobundu",
    "US20180094317A1": "Samuel C. Dudley Jr.; Corey E. Ventetuolo",
    "WO2025171161A1": "Qian Chen",
    "WO2026112526A1": "Olin D. Liang; James R. Klinger; Christopher James Rhodes; Eleni Vasilaki; Rachel Walters; Lan Zhao; Martin R. Wilkins",
    "WO2025245119A1": "Wenliang Song; Siarhei Salamevich",
    "US20260103757A1": "Jill Kreiling; Peter Quesenberry; Zhijin Wu",
    "WO2025171027A1": "Yana K. Reshetnyak; Oleg A. Andreev; Donald M. Engelman; Umberto Romeo; Eleonora Fratus; Mathieu Giraud",
    "WO2025081077A1": "Yana K. Reshetnyak; Oleg A. Andreev; Donald M. Engelman",
    "WO2024040027A1": "Yana K. Reshetnyak; Oleg A. Andreev; Donald M. Engelman",
}

# Grant-only or non-patent assets — scientific founders / PI anchors
ASSET_INVENTOR_ANCHORS: dict[str, list[str]] = {
    "gap_levine_pediatric_sepsis": ["Adam C. Levine", "Stephanie C. Garbern"],
    "gap_soma_dtx": ["Frederike Petzschner", "Chloe Gunsilius"],
}

PLACEHOLDER_RE = re.compile(
    r"^(RIH|URI)\b|program$|Dx$|Neurotech$|Volta$|MindImmune$|^Goldberg$|cardiopulmonary$|"
    r"regenerative medicine$|neurodegeneration|CNS delivery$|orthopedics$|neuro-oncology$|cardiovascular$",
    re.I,
)


def is_placeholder(s: str) -> bool:
    s = s.strip()
    if not s:
        return True
    if PLACEHOLDER_RE.search(s):
        return True
    if " " not in s and ";" not in s and s.lower() in {"neurotech", "volta", "mindimmune", "epivax", "goldberg", "chen"}:
        return True
    return False


def parse_inventors(raw: str) -> list[str]:
    if is_placeholder(raw):
        return []
    return [p.strip() for p in re.split(r"[;,]", raw) if p.strip()]


def merge_lists(*lists: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for lst in lists:
        for name in lst:
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            out.append(name)
    return out


def main() -> None:
    patents_path = ROOT / "data" / "ri_patents_curated.json"
    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    kol_path = ROOT / "data" / "ri_kol_directory.json"

    patents_doc = json.loads(patents_path.read_text())
    opp = json.loads(opp_path.read_text())
    kol = json.loads(kol_path.read_text())

    theme_to_assets: dict[str, list[str]] = {}
    patent_by_num: dict[str, dict] = {}

    for p in patents_doc["patents"]:
        num = p["patent_number"].upper()
        patent_by_num[num] = p
        if num in PATENT_INVENTOR_OVERRIDES:
            p["inventors"] = PATENT_INVENTOR_OVERRIDES[num]
        theme = p.get("theme")
        if theme:
            theme_to_assets.setdefault(theme, [])
            for aid in p.get("asset_ids") or []:
                if aid not in theme_to_assets[theme]:
                    theme_to_assets[theme].append(aid)

    ASSET_TO_THEME = {
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
        "gap_smurf2_oncology": "smurf2_oncology_hif",
        "gap_christensen_epigenetics": "hitimed_tme_epigenetic_dx",
        "gap_ni2o_kiwi_bci": "ni2o_kiwi_bci",
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

    def patents_for_asset(asset_id: str, key_patents: list[str] | None) -> list[dict]:
        keys = {k.upper() for k in (key_patents or [])}
        theme = ASSET_TO_THEME.get(asset_id)
        matched = []
        for p in patents_doc["patents"]:
            if p["patent_number"].upper() in keys:
                matched.append(p)
                continue
            if asset_id in (p.get("asset_ids") or []):
                matched.append(p)
                continue
            if theme and p.get("theme") == theme:
                matched.append(p)
        return matched

    def inventors_for_asset(asset_id: str, existing: list[str], key_patents: list[str] | None) -> list[str]:
        plist = patents_for_asset(asset_id, key_patents)
        from_patents = []
        for p in plist:
            from_patents.extend(parse_inventors(p.get("inventors", "")))
        manual = ASSET_INVENTOR_ANCHORS.get(asset_id, [])
        return merge_lists(existing, from_patents, manual)

    report: list[str] = []

    for o in opp["opportunities"]:
        merged = inventors_for_asset(o["id"], o.get("inventors") or [], o.get("key_patents"))
        if merged != (o.get("inventors") or []):
            o["inventors"] = merged
            report.append(f"  ip {o['id']}: {len(merged)} inventors")
        if o["id"] == "ip_genomics_hans" and not o.get("headline"):
            o["headline"] = "Electronic genome mapping (Nabsys 2.0)—commercial structural-variant tools, Brown-origin IP."
            o["opportunity_hook"] = "NHGRI R43 + Hitachi interest—strategic M&A or royalty, not Slater seed formation."

    for g in opp["gaps_not_in_curated_patents"]:
        merged = inventors_for_asset(
            g["id"],
            g.get("inventors") or [],
            g.get("key_patents_harvested"),
        )
        g["inventors"] = merged
        report.append(f"  gap {g['id']}: {len(merged)} inventors — {', '.join(merged[:4])}{'…' if len(merged) > 4 else ''}")
        asset = kol["assets"].get(g["id"])
        if asset and merged:
            asset["inventors_anchors"] = merged[:5]

    patents_doc["updated_at"] = NOW
    opp["updated_at"] = NOW
    kol["updated_at"] = NOW

    patents_path.write_text(json.dumps(patents_doc, indent=2) + "\n")
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")
    kol_path.write_text(json.dumps(kol, indent=2) + "\n")

    print("Inventor sync complete.")
    for line in report:
        print(line)


if __name__ == "__main__":
    main()
