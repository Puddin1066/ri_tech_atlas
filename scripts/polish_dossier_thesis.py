#!/usr/bin/env python3
"""Polish investor-facing thesis copy for all 33 dossier assets."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

THESIS: dict[str, str] = {
    "ip_wireless_neurograins": (
        "Brown’s wireless neurograin stack replaces tethered Utah arrays with a scalable "
        "microscale mesh—backed by DARPA-scale funding and a dense continuation family through "
        "the 2020s. Value is an OTL spinout or exclusive license to a hardware partner before "
        "cortical BCI consolidates around a few implant vendors."
    ),
    "ip_speech_tablet_ibci": (
        "BrainGate-era decode IP is separating from electrode hardware: recruiting speech and "
        "tablet trials (NCT05724173 family) plus fresh U01/VA awards de-risk software and "
        "algorithm licensing. Best fit is consortium or co-development with device strategics "
        "(Blackrock, Synchron)—not a capital-intensive implant startup."
    ),
    "ip_nanopieces_rna": (
        "RIH-owned non-viral RNA nanocarriers sit inside an active STTR track at NanoDe but "
        "retain licensable field-of-use beyond the startup’s current scope. Extrahepatic and "
        "ortho/CNS indications are the venture wedge—partner with NanoDe or stand up a second "
        "newco after rodent delivery PoC."
    ),
    "ip_chitinase_ocf203": (
        "A single composition-of-matter-style CHIT1/CHI3L1 asset anchors decades of NHLBI P01 "
        "fibrosis science (Jack Elias, Brown origin). Near-term value is sublicense or asset "
        "purchase diligence on OCF-203 status inside the Ocean Biomedical / Elkurt stack—not "
        "greenfield discovery."
    ),
    "ip_ecm_morsels_xm": (
        "Human MSC-derived ECM morsels (~200 µm) are injectable matrix therapy with published "
        "functional benefit in MI models (PMID 39705507) and a live Slater-backed RI spinout "
        "(XM Therapeutics). Formation capital funds large-animal PoP; exit comps are cardiac "
        "matrix and regenerative medtech strategics."
    ),
    "ip_iaip_neonatal": (
        "ProThera’s four-filing estate plus ~$3.7M active SBIR supports parallel paths: "
        "plasma-derived IAIP biologic and rapid LFIA for NICU sepsis/NEC. Physician-founder "
        "equity and MeMed/Inotrem comps frame a $5–10M Series A once clinical-enabling "
        "milestones land."
    ),
    "ip_osteopearl_vcf_lenoss": (
        "Lenoss commercializes 100% cortical allograft kyphoplasty—no PMMA balloon—with linked "
        "OsteoPearl pearls and a deep granted patent stack (23+ cited in 2025 press). This is "
        "growth equity or strategic medtech, not university OTL formation."
    ),
    "ip_dendritic_ad_mindimmune": (
        "MITI-101 blocks recruitment of CD11c+ peripheral innate cells into the AD brain—a "
        "mechanism orthogonal to amyloid mAbs—with URI Ryan Institute roots and a $30M Series A "
        "(Nov 2025). Co-invest or extension alongside Slater/RightHill fits after IND-enabling "
        "clarity."
    ),
    "ip_spinal_isi_dbs": (
        "The intelligent spinal interface program is cortically distinct: DARPA-funded SCI "
        "rehab with an IDE path at RIH (NCT04302259). Capital expects a medtech strategic, SPV, "
        "or field-of-use license—not a consumer neurotech story."
    ),
    "ip_tregitope_immunomod": (
        "EpiVax holds RI’s deepest immunoinformatics patent cluster—platform services ARR plus "
        "Tregitope therapeutic options. Investors should underwrite growth/strategic capital on "
        "license revenue, not a classic $400K Slater seed newco."
    ),
    "ip_biglycan_msk": (
        "BRF-held biglycan biology targets utrophin upregulation for neuromuscular restoration "
        "with no mapped RI startup—classic Brown OTL out-license. A physician KOL SAB plus "
        "Slater seed follows in vivo PoC, not before."
    ),
    "ip_neural_decoding_legacy": (
        "Donoghue-era foundational BMI patents may gate FTO for every new cortical interface "
        "entrant. Diligence on encumbrances versus wireless and speech sub-families determines "
        "whether value is royalty stack, narrow field-of-use license, or defensive acquisition."
    ),
    "ip_af_mapping_ai": (
        "Volta’s FDA-cleared VX1 SaMD shortens AF ablation cases with AI substrate mapping—"
        "protected claims on a ~€74M VC trajectory. Formation is complete; opportunity is growth "
        "or strategic medtech, not Slater physician-match."
    ),
    "ip_genomics_hans": (
        "Brown-origin electronic genome mapping (Nabsys, Hitachi-backed) competes in structural "
        "variant detection where NGS leaves gaps. Exit logic is strategic M&A or royalty on "
        "OhmX adoption—not seed-stage company formation."
    ),
    "ip_ect_ophthalmology": (
        "A broad encapsulated cell therapy (CNTF) estate in Cumberland RI underpins late-stage "
        "ophthalmology commercialization (including 2025 MacTel approval). Investors pursue "
        "secondary liquidity, royalties, or asset M&A—not de novo spinout capital."
    ),
    "ip_monaghan_deep_rna_dx": (
        "One ICU blood draw yields >100M-read deep RNA: host immune deconvolution (splicing, NMD) "
        "plus pathogen/AMR signal from unmapped reads—orthogonal to ProThera biologic and Levine "
        "wearable ML. RIH patents and NIGMS R35 support a physician-led Dx spinout before "
        "national blood-RNA platforms scale."
    ),
    "ip_bolden_musk_neurogenesis": (
        "Bolden holds Brown OTL rights to MuSK Ig3 exon-skipping ASOs that release adult "
        "hippocampal neurogenesis—distinct from biglycan MSK and MindImmune innate blockade. "
        "Slater/Lifespan pre-seed capital buys IND-enabling runway in a re-opened neuro "
        "restoration niche."
    ),
    "ip_pax_aav_vegf_tendon": (
        "Pax Therapeutics delivers local AAV2–VEGF at tendon repair sites, with preclinical "
        "signals of accelerated collagen maturation (~350% tensile strength in flexor models). "
        "RIH-origin IP, ~$1.7M seed, and pre-IND work position hand flexor first, then ACL/"
        "Achilles—with chairman-surgeon governance."
    ),
    "ip_oncolux_lumis": (
        "LUMIS combines multispectral fluorescence guidance with intraoperative photodynamic "
        "therapy—see-and-treat in one OR workflow—with Kersey/CytoVeris patent linkage and Mayo "
        "bronchoscopy collaboration. Medtech growth or strategic partnership fits after "
        "clinical validation, not university OTL seed."
    ),
    "gap_smurf2_oncology": (
        "Brown’s SMURF2–HIF1α oncology estate (El-Deiry) aligns with Welireg-era proof that "
        "HIF biology can support premium oncology pricing—while assignee diligence still maps "
        "SMURF-Therapeutics to OTL. Slater-scale capital follows biomarker-selected solid-tumor "
        "PoC, not platform hype."
    ),
    "gap_soma_dtx": (
        "SOMAScience translates Carney COBRE interoception science into a chronic-pain digital "
        "therapeutic—grant-first (P20GM103645) without USPTO product filings today. Reimbursement "
        "and pivotal pilot design are the gates; comps are Kaia-scale DTx raises, with Pear "
        "Chapter 11 as payer-risk lesson."
    ),
    "gap_christensen_epigenetics": (
        "HiTIMED immune epigenetic deconvolution (Dartmouth EP/PCT; Brown collaborator on "
        "R01CA253976) packages tumor microenvironment signatures for pharma trial enrichment. "
        "Economics are signature licensing and sponsored research—not a standalone therapeutic "
        "Series A."
    ),
    "gap_ni2o_kiwi_bci": (
        "Genesis Intelligence’s KIWI wireless micro-implant family (19+ filings; ni2o Providence "
        "HQ) targets low-burden BCI with Nurosene partnership momentum. BrainGate/Brown wireless "
        "FTO diligence is mandatory before strategic or growth capital."
    ),
    "gap_levine_pediatric_sepsis": (
        "Wearable vitals plus ML flagged advanced pediatric sepsis hours ahead of routine "
        "documentation in prospective Bangladesh ICU work (PMID 39475844, 41252746)—grant-backed "
        "via R33TW012211. US value is SaMD classification and health-system pilot, complementing "
        "Monaghan RNA Dx and ProThera biologic in a stacked sepsis portfolio."
    ),
    "gap_uri_phlip_lnp": (
        "PHLIP peptides insert at acidic pH to deliver LNPs and STING payloads without classical "
        "endocytosis—URI’s WO family competes on tumor microenvironment selectivity versus "
        "liver-default genetic medicine. URI tech transfer → RI spinout or license after rodent "
        "tumor delivery PoC."
    ),
    "gap_rih_salivary_ev_ad": (
        "Salivary EV RNA offers a less invasive Alzheimer’s liquid-biopsy lane as plasma "
        "p-tau tests gain FDA traction—RIH/Brown R01AG074284 funds analytical work toward "
        "CLIA LDT, then Dx spinout. US20260103757A1 anchors assignee IP distinct from Monaghan "
        "deep blood RNA."
    ),
    "gap_rih_bx912_pulmonary_htn": (
        "RIH’s BX-912 PAH program (WO2026112526) enters a market reset by 2024’s first-in-class "
        "biologic approval—clear regulatory benchmarks, crowded chemistry. Value is IND-enabling "
        "PoC plus cardio newco or license after PI and hospital chain-of-title diligence."
    ),
    "gap_rih_pahtn_dx": (
        "A mature RIH Dx family (US20180094317; Dudley/Ventetuolo) targets PAH and sudden cardiac "
        "death risk stratification—companion to BX-912 or standalone. Retrospective cohort success "
        "must convert to prospective registry data before license or seed Dx pricing power."
    ),
    "gap_rih_bbb_nucleic_delivery": (
        "Qian Chen’s BBB nucleic-delivery PCT (WO2025171161) addresses the bottleneck for CNS "
        "genetic medicines—rodent PoC unlocks gene-therapy option deals, not near-term product "
        "revenue. FTO versus Denali/Voyager-style shuttles is the partner conversation starter."
    ),
    "gap_rih_motile_cell_msk": (
        "Motile injectable cell therapy for meniscus and connective tissue (WO2025155768) pairs "
        "NIAMS awards (R01AR080726, R21AR077326) with peer-reviewed meniscus/PTOA signals "
        "(PMID 36312551, 39763468). Distinct from XM ECM morsels; large-animal data is the "
        "Slater gate."
    ),
    "gap_rih_ecm_joint_repair": (
        "RIH ECM reconstitution filings (US20240139376) target joint repair adjacent to XM "
        "Therapeutics’ injectable morsels—field-of-use clearance versus Brown/XM OTL is the "
        "commercial unlock. No investor formation until FOU and orthopedic pilot design are "
        "documented."
    ),
    "gap_rih_enhancer_rna_glioma": (
        "Enhancer-RNA targeting (US20230323349; Tapinos) opens a non-coding axis in glioma "
        "where standard of care still fails most patients. R21CA235415-backed translational "
        "planning precedes neuro-onc seed—efficacy in relevant models is the milestone investors "
        "will underwrite."
    ),
    "gap_rih_lpa_therapeutic": (
        "RIH’s Lp(a) PCT (WO2025245119) lands as Novartis and Amgen run Phase 3 outcomes "
        "trials—no approved Lp(a)-specific drug yet, so pharma option economics dominate. Song "
        "lab R01HL159204 supplies cardio lipid credibility; differentiation versus siRNA/antisense "
        "leaders is the diligence centerpiece."
    ),
}


def main() -> None:
    path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    data = json.loads(path.read_text())

    n_opp = 0
    for o in data["opportunities"]:
        if o["id"] in THESIS:
            o["thesis"] = THESIS[o["id"]]
            n_opp += 1

    n_gap = 0
    for g in data["gaps_not_in_curated_patents"]:
        if g["id"] in THESIS:
            g["thesis"] = THESIS[g["id"]]
            n_gap += 1

    data["updated_at"] = NOW
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Polished thesis: {n_opp} opportunities, {n_gap} gaps.")


if __name__ == "__main__":
    main()
