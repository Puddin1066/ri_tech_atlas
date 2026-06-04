#!/usr/bin/env python3
"""Enrich comparables `market` + `sam` with investor-facing, web-sourced framing."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

# Sources: Grand View Research, WEF, Mordor Intelligence, Research and Markets, etc. (2024–2026 reports)
MARKET_CONTEXT: dict[str, dict[str, str]] = {
    "ip_iaip_neonatal": {
        "market": (
            "Sepsis diagnostics is marching toward ~$1.8B globally by 2030 (Grand View Research), "
            "with neonatal sepsis called out as a high-mortality segment where faster biomarkers beat "
            "culture turnaround. Host-response platforms like MeMed (>$200M raised) and biologic players "
            "like Inotrem (Phase 3) show investors will fund both Dx and therapy in the NICU."
        ),
        "sam": "Neonatal sepsis: IAIP biologic + rapid LFIA at the bedside—not another 48-hour blood culture workflow.",
    },
    "ip_ecm_morsels_xm": {
        "market": (
            "Cardiac remodeling and injectable matrix therapies sit inside a multi-billion regenerative "
            "cardiology wave—Heartseed (~$41M Series B, 2024) and historical Ventrix matrix programs "
            "validate investor appetite for preclinical→IND cell/matrix plays. XM Therapeutics already "
            "proved a Slater-backed RI path for injectable ECM in Providence."
        ),
        "sam": "Injectable ECM morsels for ventricular remodeling—Brown/XM field-of-use and large-animal PoC are the gates.",
    },
    "ip_nanopieces_rna": {
        "market": (
            "Genetic medicines are a trillion-dollar narrative, but the venture heat is in delivery: "
            "extrahepatic LNPs are forecast toward ~$4.7B by 2030 (Research and Markets, ~21% CAGR) as "
            "siRNA and gene editors escape liver-only tropism. Aera’s $193M raise is the comp; Generation "
            "Bio’s restructuring is the cautionary tale on non-viral scale-up."
        ),
        "sam": "NanoDe non-viral RNA particles—ortho/cartilage first, extrahepatic positioning vs liver-default LNPs.",
    },
    "ip_chitinase_ocf203": {
        "market": (
            "IPF pharmacotherapy is a ~$5–7B global market by 2030 (Grand View Research / TBRC) with "
            "entrenched antifibrotics—and fresh pain when programs like Pliant’s bexotegrast halt. "
            "CHIT1/CHI3L1 biology offers a differentiated anti-fibrotic angle if tox and biomarker "
            "strategy are crisp."
        ),
        "sam": "CHIT1/CHI3L1 small-molecule or biologic for fibrosis—license-first path after P01-enabling data.",
    },
    "ip_dendritic_ad_mindimmune": {
        "market": (
            "Alzheimer’s therapeutics is re-rating: analysts peg ~$9–15B by 2030 as anti-amyloid biologics "
            "and early Dx reshape the funnel (Grand View Research; FDA cleared first blood p-tau test in "
            "2025). Peripheral innate blockade (MindImmune $30M Series A, 2025) competes in a market "
            "where mechanism and trial design matter as much as TAM."
        ),
        "sam": "Peripheral innate immune blockade for AD—Brown spinout adjacent to MindImmune’s CNS-penetrant path.",
    },
    "ip_wireless_neurograins": {
        "market": (
            "Brain–computer interfaces are scaling from lab curiosity to ~$4.7B by 2030 (~14% CAGR, "
            "The Business Research Company) as assistive communication and neuromodulation go clinical. "
            "WEF cites ~$6.2B by 2030 with invasive clinical BCIs and consumer EEG both pulling capital."
        ),
        "sam": "Wireless neurograin mesh for distributed cortical recording—DARPA heritage, Brown neuroengineering.",
    },
    "ip_speech_tablet_ibci": {
        "market": (
            "Speech neuroprosthetics ride the same BCI tailwind (~$5B+ 2030, Emergen/WEF) but the nearer "
            "commercial proof points are tablet-based AAC and speech-BCI hybrids (Blackrock/BrainGate "
            "ecosystem). Stroke and ALS prevalence keep payer interest in communication restoration high."
        ),
        "sam": "Tablet speech BCI for paralysis—decoding + AAC interface with lower surgical burden than full implants.",
    },
    "ip_spinal_isi_dbs": {
        "market": (
            "Spinal cord injury neuromodulation sits inside the broader neuromodulation and neurotech "
            "spend (BCI ~$4–6B 2030; spinal stimulation devices multi-billion medtech). ISI-triggered "
            "DBS concepts target autonomic and motor recovery niches where epidural stimulation has "
            "shown clinical signals."
        ),
        "sam": "ISI-pattern spinal DBS for SCI autonomic/motor goals—device + algorithm package for neurosurgical partners.",
    },
    "ip_biglycan_msk": {
        "market": (
            "Duchenne and broader neuromuscular rare disease drugs are exploding toward ~$5–10B by 2030 "
            "(Grand View Research; gene therapy approvals like Elevidys reset pricing and access). "
            "Biglycan biology targets utrophin upregulation—a complement to exon-skipping and gene "
            "therapy, not a me-too steroid."
        ),
        "sam": "Biglycan-mediated utrophin upregulation for DMD—orphan biologic path with clear genetic stratification.",
    },
    "ip_tregitope_immunomod": {
        "market": (
            "Vaccine and immunomodulation platforms remain a ~$50B+ fragmented global market, but venture "
            "checks flow to de-risked adjuvant and tolerance mechanisms with human ex vivo data. "
            "EpiVax Tregitope science anchors computational immunogenicity—a licensable wedge for "
            "biologics and vaccine sponsors."
        ),
        "sam": "Tregitope tolerogenic peptides—partner licenses for immunogenicity reduction, not standalone vaccine SKU.",
    },
    "ip_neural_decoding_legacy": {
        "market": (
            "Neural decoding IP bundles into the same BCI/SaMD opportunity (~$5B 2030) where acquirers "
            "pay for speech and motor decoding libraries ahead of full device approvals. Legacy Brown "
            "decoding patents are option value for neurotech strategics."
        ),
        "sam": "Legacy neural decoding patent package—out-license to speech-BCI or neuromodulation platforms.",
    },
    "ip_osteopearl_vcf_lenoss": {
        "market": (
            "Vertebral compression fractures affect hundreds of thousands of patients annually in the U.S. "
            "alone; kyphoplasty/vertebroplasty devices and bone cements remain a steady medtech lane "
            "with Lenoss as the RI commercial anchor. Reimbursed procedures and ASC migration keep "
            "interest in differentiated cement/pearl technologies."
        ),
        "sam": "OsteoPearl VCF technology—RI-based Lenoss commercialization vs commodity kyphoplasty cement.",
    },
    "ip_af_mapping_ai": {
        "market": (
            "Atrial fibrillation ablation is a growth procedure set: AF surgery/ablation markets forecast "
            "~$5–13B by 2030 depending on scope (GII / Grand View ablation catheters ~$12B). CDC projects "
            "~12.1M Americans with AF by 2030—mapping AI that shortens fluoro time has clear hospital economics."
        ),
        "sam": "AI-assisted AF substrate mapping—hospital efficiency play on top of EP ablation volume growth.",
    },
    "ip_genomics_hans": {
        "market": (
            "Structural variant detection is the gap NGS still struggles with; optical genome mapping is "
            "~$200M today heading toward ~$566M by 2031 (Mordor Intelligence, ~23% CAGR). Nabsys electronic "
            "mapping (Hitachi-backed) competes on cost and resolution vs optical leaders like Bionano."
        ),
        "sam": "Nabsys electronic genome mapping—strategic exit/licensing, not Slater-style de novo startup.",
    },
    "ip_ect_ophthalmology": {
        "market": (
            "Retinal and anterior-segment device markets remain niche but durable: ECT-related ophthalmic "
            "platforms target surgical efficiency and outcomes in cataract/vitreoretinal workflows where "
            "single-product medtech exits are common. RI angle is license to an established ophthalmic "
            "commercial partner."
        ),
        "sam": "Electro-chemical ophthalmic technique—partner license after clinical utility and regulatory class clarity.",
    },
    "gap_smurf2_oncology": {
        "market": (
            "HIF pathway drugs went commercial with belzutifan (Welireg) in VHL-associated tumors, proving "
            "renal cell and HIF biology can support premium oncology pricing. SMURF2 sits adjacent as a "
            "degradation-pathway target—venture interest follows if biomarker-selected solid tumor PoC emerges."
        ),
        "sam": "SMURF2 oncology target—Brown biology; needs biomarker-defined tumor PoC before Series A scale.",
    },
    "gap_soma_dtx": {
        "market": (
            "Digital chronic pain therapeutics are projected toward ~$15–22B by 2033 (Growth Market Reports, "
            "~17–19% CAGR) as payers seek non-opioid, scalable behavioral + sensor programs. FDA’s expanding "
            "DTx precedent lowers regulatory risk versus novel small molecules."
        ),
        "sam": "SOMA digital pain program—Brown/RI clinical validation then reimbursement-first commercialization.",
    },
    "ip_monaghan_deep_rna_dx": {
        "market": (
            "Blood-based Alzheimer’s diagnostics are the fastest-moving Dx lane: ~$530M by 2033 (~17% CAGR, "
            "Grand View Research) after FDA’s 2025 clearance of plasma p-tau/Aβ ratio tests. Deep RNA "
            "signatures from whole blood compete on workflow fit for health-system screening."
        ),
        "sam": "Deep RNA blood panel for AD risk/stratification—Monaghan lab science vs plasma protein incumbents.",
    },
    "gap_christensen_epigenetics": {
        "market": (
            "Tumor microenvironment and epigenetic reprogramming are core IO themes—biomarker licensing "
            "and platform deals (not single-asset Ph3) dominate early academic oncology. Pharma pays for "
            "validated patient-selection signatures that de-risk combination trials."
        ),
        "sam": "Christensen TME epigenetics—signature licensing to IO sponsors, not standalone drug launch.",
    },
    "ip_bolden_musk_neurogenesis": {
        "market": (
            "Neurogenesis and CNS biologics ride the AD therapeutics expansion (~$10B+ 2030) and broader "
            "neurodegeneration spend, but capital is selective post-anti-amyloid rollercoaster. ASO/small-molecule "
            "neurorestoration requires crisp target biology and biomarker strategy."
        ),
        "sam": "MUSK-pathway neurogenesis modulators—Bolden lab CNS assets for license or disciplined seed.",
    },
    "ip_pax_aav_vegf_tendon": {
        "market": (
            "Soft-tissue injury burden is massive—~17M U.S. tendon/ligament injuries annually with multi‑tens‑of‑billions "
            "in indirect cost—while biologic ortho plays (PRP, allograft, gene therapy) consolidate. "
            "Local AAV-VEGF for tendon healing is a high-differentiation biologic if delivery and expression are controlled."
        ),
        "sam": "PAX3-driven AAV-VEGF tendon repair—preclinical ortho biologic with gene therapy regulatory path.",
    },
    "ip_oncolux_lumis": {
        "market": (
            "Fluorescence-guided surgery systems are forecast to ~$424M by 2034 (~13.5% CAGR, Insight Partners) "
            "as oncology resections demand better margins; intraoperative PDT adds a therapeutic layer NCI is "
            "actively trialing in colorectal recurrence. Dual FGS+PDT is the differentiated RI story."
        ),
        "sam": "OncoLux Lumis FGS + intraoperative PDT—resection guidance plus residual-tumor kill in one workflow.",
    },
    "gap_ni2o_kiwi_bci": {
        "market": (
            "Non-invasive BCI and neuromodulation for sleep/apnea and related conditions tap the same ~$5–6B "
            "BCI TAM (WEF / TBRC) but with consumer-grade form factors and shorter regulatory paths than "
            "implanted cortical arrays. Strategics buy optionality on EEG/fNIRS hybrids."
        ),
        "sam": "N₂O/Kiwi non-invasive neurostimulation—wellness/clinical niche before invasive BCI capital intensity.",
    },
    "gap_levine_pediatric_sepsis": {
        "market": (
            "Hospital sepsis early-warning and AI prediction markets are racing toward ~$1.5–2.4B by 2030–33 "
            "(Research and Markets; MarketIntel) as health systems chase mortality and ICU cost avoidance. "
            "Pediatric wearables + ML are under-served vs adult Epic-integrated rules engines."
        ),
        "sam": "Pediatric sepsis wearable + ML—prospective Bangladesh ICU data as bridge to U.S. SaMD pilot.",
    },
    "gap_uri_phlip_lnp": {
        "market": (
            "Tumor-selective delivery is the bottleneck for innate agonists and genetic payloads: extrahepatic "
            "LNP platforms are projected ~$4.7B by 2030 (~21% CAGR). PHLIP’s acid-targeted insertion is a "
            "mechanistic alternative to ligand-decorated LNPs (Aera $193M comp)."
        ),
        "sam": "URI PHLIP peptide delivery for LNP/STING—acid microenvironment selectivity vs systemic liver uptake.",
    },
    "gap_rih_salivary_ev_ad": {
        "market": (
            "Alzheimer’s blood diagnostics (~$530M by 2033, Grand View Research) just gained FDA legitimacy; "
            "salivary EV RNA is the next comfort-and-cost frontier versus plasma draws. Quanterix and C2N "
            "prove Dx platforms can raise $200M+ when biomarkers align with therapy trials."
        ),
        "sam": "Salivary EV liquid biopsy for AD—non-invasive sample type with R01AG074284 analytical backbone.",
    },
    "gap_rih_bx912_pulmonary_htn": {
        "market": (
            "PAH pharmacotherapy is an ~$8–13B global market by 2030 (Grand View / Strategic Market Research) "
            "reshaped by 2024’s first-in-class biologic approval (sotatercept). Small-molecule entrants need "
            "clear differentiation vs entrenched prostacyclin and ERA pathways."
        ),
        "sam": "BX-912 small-molecule PH—RIH PCT asset; crowded market but visible regulatory benchmarks.",
    },
    "gap_rih_pahtn_dx": {
        "market": (
            "Cardiopulmonary risk stratification benefits from AF and PAH procedure growth (~$5B+ ablation "
            "TAM; PAH drugs ~$8B+). AI-augmented Dx (Eko $125M+) shows hospitals pay for earlier structural "
            "heart and PH signals in outpatient workflows."
        ),
        "sam": "PAH/SCD diagnostic panel—mature RIH patent family; retrospective→prospective validation drives value.",
    },
    "gap_rih_bbb_nucleic_delivery": {
        "market": (
            "CNS genetic medicines are strategic for every large pharma, while BBB delivery remains the "
            "gating risk—Denali ATV and Voyager partnerships show billions flow to platforms that crack "
            "CNS exposure. Nucleic acid BBB tech is license/option economics, not retail therapeutics day one."
        ),
        "sam": "RIH BBB nucleic-acid delivery—rodent PoC then gene-therapy partnership, not standalone pill.",
    },
    "gap_rih_motile_cell_msk": {
        "market": (
            "Orthobiologics is a ~$7–10B global market by 2030 (Grand View / Mordor) fueled by sports injury, "
            "aging joints, and stem-cell/PRP adoption. Meniscus injury drives PTOA downstream costs—programs "
            "with NIAMS backing (R01AR080726) signal credible regenerative science."
        ),
        "sam": "Motile injectable cell therapy for meniscus/MSK—distinct from XM ECM morsels; large-animal gate next.",
    },
    "gap_rih_ecm_joint_repair": {
        "market": (
            "Joint repair and injectable matrices sit in the same orthobiologics growth (~5–6% CAGR to ~$8–10B "
            "2030) where XM Therapeutics already validated RI Slater path. Field-of-use clarity vs Brown/XM "
            "OTL is the commercial unlock."
        ),
        "sam": "Biomimetic ECM joint repair—RIH license only if FOU clears against XM injectable morsels.",
    },
    "gap_rih_enhancer_rna_glioma": {
        "market": (
            "Adult malignant glioma therapeutics head toward ~$4–5B by 2030 (~8–10% CAGR; GII/TBRC) with "
            "GBM still dominated by surgery, TMZ, and TTFields. eRNA mechanisms are early but fit the push "
            "for non-coding targets and precision neuro-oncology."
        ),
        "sam": "Enhancer RNA–targeted glioma therapy—Tapinos-led RIH/Brown science; IND-enabling is years out.",
    },
    "gap_rih_lpa_therapeutic": {
        "market": (
            "Lp(a) lowering is the next cardiovascular frontier: analysts model ~$3–11B therapeutic potential "
            "if outcomes trials succeed (HORIZON/OCEAN(a) readouts expected mid‑2020s). No approved Lp(a)-"
            "specific drug yet—RIH assets compete for pharma option dollars, not retail launch."
        ),
        "sam": "RIH Lp(a)-lowering approach—strategic license vs Novartis pelacarsen / Amgen olpasiran Phase 3 leaders.",
    },
}


def main() -> None:
    path = ROOT / "data" / "ri_comparables_matrix.json"
    data = json.loads(path.read_text())
    updated = 0
    for row in data["rows"]:
        aid = row["asset_id"]
        if aid not in MARKET_CONTEXT:
            print(f"warning: no market copy for {aid}")
            continue
        row["market"] = MARKET_CONTEXT[aid]["market"]
        row["sam"] = MARKET_CONTEXT[aid]["sam"]
        updated += 1
    data["updated_at"] = NOW
    data["version"] = "1.4"
    data["market_context_note"] = (
        "Market/SAM copy enriched via public industry reports (Grand View Research, "
        "Mordor Intelligence, WEF, Research and Markets, etc.); figures are illustrative TAM/SAM."
    )
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Enriched market context for {updated}/{len(data['rows'])} assets.")


if __name__ == "__main__":
    main()
