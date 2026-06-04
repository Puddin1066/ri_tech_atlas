#!/usr/bin/env python3
"""Full corpus parity for 33 investable units (19 ip_* + 14 gap_*)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

ASSIGNEE_LABELS: dict[str, str] = {
    "gap_smurf2_oncology": "Brown University",
    "gap_soma_dtx": "Brown University (COBRE)",
    "gap_christensen_epigenetics": "Dartmouth College",
    "gap_ni2o_kiwi_bci": "Genesis Intelligence, LLC (ni2o license path)",
    "gap_levine_pediatric_sepsis": "Brown University / Rhode Island Hospital",
    "gap_uri_phlip_lnp": "University of Rhode Island",
    "gap_rih_salivary_ev_ad": "Rhode Island Hospital",
    "gap_rih_bx912_pulmonary_htn": "Rhode Island Hospital",
    "gap_rih_pahtn_dx": "Rhode Island Hospital",
    "gap_rih_bbb_nucleic_delivery": "Rhode Island Hospital",
    "gap_rih_motile_cell_msk": "Rhode Island Hospital",
    "gap_rih_ecm_joint_repair": "Rhode Island Hospital",
    "gap_rih_enhancer_rna_glioma": "Rhode Island Hospital",
    "gap_rih_lpa_therapeutic": "Rhode Island Hospital",
}

EVIDENCE_PATCH: dict[str, list[str]] = {
    "gap_levine_pediatric_sepsis": ["PMID39475844", "PMID41252746"],
    "gap_uri_phlip_lnp": ["https://web.uri.edu/research/"],
    "gap_rih_salivary_ev_ad": ["US20260103757A1"],
}

COMPARABLES_NEW = [
    {
        "asset_id": "gap_levine_pediatric_sepsis",
        "market": "Hospital early-warning / predictive analytics",
        "sam": "Pediatric sepsis wearable + ML CDSS",
        "comparables": [
            {"name": "Epic sepsis models", "financing": "EHR-embedded", "path": "Health-system SaaS", "url": None},
            {"name": "PeraHealth (Rothman Index)", "financing": "Acquired by Vocera", "path": "Early warning scores", "url": None},
        ],
        "comparable_financing": "Enterprise health IT",
        "benchmark_path": "R33 LMIC validation → FDA SaMD → US pilot",
        "ri_path": "Brown/RIH → digital health spinout",
        "ri_round": "Grant-first; Slater after SaMD path",
    },
    {
        "asset_id": "gap_uri_phlip_lnp",
        "market": "Genetic medicines $B+; innate immuno-oncology delivery",
        "sam": "PHLIP peptide–LNP / STING intracellular delivery",
        "comparables": [
            {"name": "Aera Therapeutics", "financing": "$193M A+B (2023)", "path": "Extrahepatic LNP", "url": "https://aeratx.com/"},
            {"name": "Moderna / BioNTech LNP", "financing": "Commercial scale", "path": "mRNA LNP", "url": None},
        ],
        "comparable_financing": "Aera-scale genetic medicine VC",
        "benchmark_path": "URI license → rodent PoC → seed",
        "ri_path": "URI tech transfer → RI spinout",
        "ri_round": "Slater $200–400K + match",
    },
    {
        "asset_id": "gap_rih_salivary_ev_ad",
        "market": "AD diagnostics multi-$B",
        "sam": "Salivary EV liquid biopsy",
        "comparables": [
            {"name": "Quanterix Simoa", "financing": "Public Dx", "path": "Blood biomarker platforms", "url": "https://www.quanterix.com/"},
            {"name": "C2N Diagnostics", "financing": "VC-backed blood AD tests", "path": "Plasma Aβ/tau", "url": "https://c2ndiagnostics.com/"},
        ],
        "comparable_financing": "Dx platform VC",
        "benchmark_path": "CLIA pilot → LDT → Series A",
        "ri_path": "RIH license → Dx spinout",
        "ri_round": "$3–8M seed",
    },
    {
        "asset_id": "gap_rih_bx912_pulmonary_htn",
        "market": "PAH therapeutics niche",
        "sam": "BX-912 small-molecule PH",
        "comparables": [
            {"name": "Merck Winrevair", "financing": "Approved 2024", "path": "PAH biologic", "url": None},
            {"name": "Liquidia Yutrepia", "financing": "Commercial PAH", "path": "Inhaled treprostinil", "url": None},
        ],
        "comparable_financing": "Approved PAH benchmarks",
        "benchmark_path": "Preclinical PH → IND",
        "ri_path": "RIH license → cardio newco",
        "ri_round": "Seed / Series A",
    },
    {
        "asset_id": "gap_rih_pahtn_dx",
        "market": "Cardio risk stratification",
        "sam": "PAH / SCD diagnostic panel",
        "comparables": [
            {"name": "HeartTest Laboratories", "financing": "Public micro-vascular Dx", "path": "Cardio screening", "url": None},
            {"name": "Eko Health", "financing": "$125M+ raised", "path": "AI cardiac auscultation", "url": "https://www.ekohealth.com/"},
        ],
        "comparable_financing": "Cardio Dx VC",
        "benchmark_path": "Retrospective validation → prospective",
        "ri_path": "RIH stratification license",
        "ri_round": "License or seed Dx",
    },
    {
        "asset_id": "gap_rih_bbb_nucleic_delivery",
        "market": "CNS genetic medicine",
        "sam": "BBB-crossing nucleic acid platform",
        "comparables": [
            {"name": "Denali ATV", "financing": "Big-pharma partnered", "path": "BBB shuttle biologics", "url": None},
            {"name": "Voyager AAV CNS", "financing": "Strategic gene therapy", "path": "CNS gene therapy", "url": None},
        ],
        "comparable_financing": "Strategic CNS delivery deals",
        "benchmark_path": "Rodent BBB PoC → partner option",
        "ri_path": "RIH → gene therapy license",
        "ri_round": "Option / upfront license",
    },
    {
        "asset_id": "gap_rih_motile_cell_msk",
        "market": "Orthobiologics / regenerative MSK",
        "sam": "Motile injectable cell therapy",
        "comparables": [
            {"name": "Orthocell CelGro", "financing": "ASX-listed", "path": "Cell matrix tendon", "url": None},
            {"name": "MiMedx", "financing": "Public", "path": "Amniotic orthobiologics", "url": None},
        ],
        "comparable_financing": "Orthobiologics public comps",
        "benchmark_path": "Large-animal tendon → IND",
        "ri_path": "RIH spinout",
        "ri_round": "$5–15M A",
    },
    {
        "asset_id": "gap_rih_ecm_joint_repair",
        "market": "Joint repair / matrix",
        "sam": "Biomimetic ECM reconstitution",
        "comparables": [
            {"name": "XM Therapeutics", "financing": "Slater $375K", "path": "Injectable ECM morsels", "url": "https://www.xmtherapeutics.com/"},
            {"name": "Anika Orthobiologics", "financing": "Public", "path": "Joint viscosupplementation", "url": None},
        ],
        "comparable_financing": "XM Slater path",
        "benchmark_path": "Ortho pilot → field-of-use check vs XM",
        "ri_path": "RIH license (FOU vs Brown/XM)",
        "ri_round": "Slater $200–400K + match",
    },
    {
        "asset_id": "gap_rih_enhancer_rna_glioma",
        "market": "Glioma therapeutics",
        "sam": "eRNA-targeted brain tumor therapy",
        "comparables": [
            {"name": "Day One ONC201", "financing": "Public glioma path", "path": "H3 K27M", "url": None},
            {"name": "Chimerix ONC201 lineage", "financing": "Clinical-stage", "path": "Diffuse glioma", "url": None},
        ],
        "comparable_financing": "Neuro-oncology VC",
        "benchmark_path": "Glioma models → IND-enabling",
        "ri_path": "RIH → neuro-onc startup",
        "ri_round": "Series A",
    },
    {
        "asset_id": "gap_rih_lpa_therapeutic",
        "market": "Lp(a) cardiovascular",
        "sam": "Lp(a)-lowering therapeutic",
        "comparables": [
            {"name": "Novartis pelacarsen", "financing": "Phase 3 Lp(a)", "path": "Antisense Lp(a)", "url": None},
            {"name": "Amgen olpasiran", "financing": "Phase 3", "path": "siRNA Lp(a)", "url": None},
        ],
        "comparable_financing": "Big-pharma Lp(a) programs",
        "benchmark_path": "Mechanism PoC → partner",
        "ri_path": "RIH cardio license",
        "ri_round": "Strategic / Series A",
    },
]

PHYSICIAN_NEW = {
    "gap_levine_pediatric_sepsis": {
        "slater_fit": "high",
        "physician_equity_model": "Adam Levine MD MPH physician-founder equity + Garbern MD co-PI KOL SAB for wearable sepsis CDSS.",
        "kol_advisory_targets": ["Adam C. Levine MD MPH", "Stephanie C. Garbern MD"],
        "milestones_18mo": ["SaMD classification memo", "US health-system pilot design", "Slater $200–400K + match"],
        "capital_stack": "FIC R33 → Innovate RI match → Slater",
        "precedent": "R33TW012211 Bangladesh wearable ML",
    },
    "gap_uri_phlip_lnp": {
        "slater_fit": "medium",
        "physician_equity_model": "Oncology/translational MD KOL SAB if STING-oncology spinout; scientific founders from URI PHLIP group.",
        "kol_advisory_targets": ["URI PHLIP PI", "Oncology KOL for STING trials"],
        "milestones_18mo": ["URI exclusive license", "Rodent delivery PoC", "STING-oncology partner outreach"],
        "capital_stack": "URI license → SBIR/STTR → Slater",
        "precedent": "PHLIP–LNP WO2025171027",
    },
    "gap_rih_salivary_ev_ad": {
        "slater_fit": "medium",
        "physician_equity_model": "Neurology/geriatrics physician KOL SAB + hospital lab PI equity in Dx spinout.",
        "kol_advisory_targets": ["Memory clinic neurology KOL", "RIH pathology/lab medicine"],
        "milestones_18mo": ["CLIA analytical validation", "Prospective AD cohort", "Slater seed + match"],
        "capital_stack": "RIH license → LDT → seed",
        "precedent": "US20260103757A1",
    },
    "gap_rih_bx912_pulmonary_htn": {
        "slater_fit": "medium",
        "physician_equity_model": "Pulmonary hypertension cardiologist KOL SAB + scientific PI equity if newco.",
        "kol_advisory_targets": ["Pulmonary hypertension center PI", "Cardiology translational"],
        "milestones_18mo": ["PH model PoC", "IND-enabling tox", "Cardio KOL SAB"],
        "capital_stack": "RIH license → seed",
        "precedent": "WO2026112526 BX-912 PH",
    },
    "gap_rih_pahtn_dx": {
        "slater_fit": "low_medium",
        "physician_equity_model": "Cardiology EP / heart failure KOL SAB for risk stratification adoption.",
        "kol_advisory_targets": ["Cardiac electrophysiology", "Heart failure clinic"],
        "milestones_18mo": ["Retrospective validation", "Prospective registry", "Dx license deal"],
        "capital_stack": "RIH license → strategic Dx",
        "precedent": "US20180094317 PAH/SCD Dx",
    },
    "gap_rih_bbb_nucleic_delivery": {
        "slater_fit": "medium",
        "physician_equity_model": "Neurology/neurosurgery KOL SAB for CNS delivery translation.",
        "kol_advisory_targets": ["Neuro-oncology", "Gene therapy neurology"],
        "milestones_18mo": ["BBB rodent PoC", "Partner option with gene therapy co", "FTO memo"],
        "capital_stack": "RIH license → upfront/partner",
        "precedent": "WO2025171161 BBB nucleic acid",
    },
    "gap_rih_motile_cell_msk": {
        "slater_fit": "high",
        "physician_equity_model": "Orthopedic / sports medicine surgeon KOL SAB + physician co-founder option.",
        "kol_advisory_targets": ["Orthopedic surgery", "Sports medicine"],
        "milestones_18mo": ["Large-animal tendon repair", "RIH license", "Slater $200–400K + match"],
        "capital_stack": "RIH → seed → Series A",
        "precedent": "WO2025155768 motile cell MSK",
    },
    "gap_rih_ecm_joint_repair": {
        "slater_fit": "medium",
        "physician_equity_model": "Orthopedic surgeon KOL SAB; field-of-use diligence vs XM Therapeutics.",
        "kol_advisory_targets": ["Orthopedic surgery KOL", "Jeffrey R. Morgan PhD (XM peer)"],
        "milestones_18mo": ["FOU vs XM OTL", "Joint repair pilot", "License or spinout"],
        "capital_stack": "RIH license → Slater if clear FOU",
        "precedent": "US20240139376 ECM joint",
    },
    "gap_rih_enhancer_rna_glioma": {
        "slater_fit": "medium",
        "physician_equity_model": "Neuro-oncology physician KOL SAB + scientific PI equity.",
        "kol_advisory_targets": ["Neuro-oncology", "Brain tumor center PI"],
        "milestones_18mo": ["Glioma model efficacy", "IND path memo", "Neuro-onc KOL SAB"],
        "capital_stack": "RIH → seed/Series A",
        "precedent": "US20230323349 eRNA glioma",
    },
    "gap_rih_lpa_therapeutic": {
        "slater_fit": "low",
        "physician_equity_model": "Preventive cardiology KOL SAB; likely strategic pharma path vs Slater seed.",
        "kol_advisory_targets": ["Preventive cardiology", "Lipid clinic"],
        "milestones_18mo": ["Differentiation vs siRNA Lp(a)", "Partner discussions", "Phase 1 design"],
        "capital_stack": "RIH license → pharma option",
        "precedent": "WO2025245119 Lp(a)",
    },
}

KOL_NEW = {
    "gap_levine_pediatric_sepsis": {
        "entity": "Brown / RIH pediatric sepsis CDSS",
        "inventors_anchors": ["Adam C. Levine", "Stephanie C. Garbern"],
        "kols": [
            {"rank": 1, "name": "Adam C. Levine", "credentials": "MD MPH FACEP", "affiliation": "Brown EM; RIH", "role_fit": "PI wearable pediatric sepsis ML", "physician_led_fit": "high", "evidence": "R33TW012211; PMID39475844", "urls": ["https://vivo.brown.edu/display/al16"]},
            {"rank": 2, "name": "Stephanie C. Garbern", "credentials": "MD", "affiliation": "Brown EM; RIH", "role_fit": "mPI pediatric sepsis wearable", "physician_led_fit": "high", "evidence": "FIC R33 co-PI", "urls": ["https://www.fic.nih.gov/Grants/Search/Pages/mhealth-R21TW012211.aspx"]},
            {"rank": 3, "name": "Sean F. Monaghan", "credentials": "MD FACS", "affiliation": "RIH Surgery", "role_fit": "Complementary RNA Dx (orthogonal)", "physician_led_fit": "medium", "evidence": "ip_monaghan_deep_rna_dx", "urls": ["https://www.brownhealth.org/providers/sean-monaghan-md"]},
            {"rank": 4, "name": "Yow-Pin Lim", "credentials": "MD PhD", "affiliation": "ProThera", "role_fit": "Neonatal sepsis biologic peer", "physician_led_fit": "medium", "evidence": "ip_iaip_neonatal", "urls": ["https://www.protherabiologics.com/"]},
            {"rank": 5, "name": "Mitchell M. Levy", "credentials": "MD", "affiliation": "Brown critical care", "role_fit": "Sepsis guidelines network", "physician_led_fit": "high", "evidence": "Surviving Sepsis adjacent", "urls": ["https://vivo.brown.edu/display/mlevy"]},
        ],
    },
    "gap_uri_phlip_lnp": {
        "entity": "URI PHLIP platform (spinout forming)",
        "inventors_anchors": ["URI PHLIP inventors"],
        "kols": [
            {"rank": 1, "name": "Wafik S. El-Deiry", "credentials": "MD PhD", "affiliation": "Brown/Lifespan", "role_fit": "STING-oncology trial design peer", "physician_led_fit": "medium", "evidence": "Innate immuno-oncology network", "urls": ["https://wafik-el-deiry.com/"]},
            {"rank": 2, "name": "Howard P. Safran", "credentials": "MD", "affiliation": "Brown Health Cancer", "role_fit": "Oncology translational", "physician_led_fit": "medium", "evidence": "Cancer institute trials", "urls": ["https://www.brownhealth.org/providers/howard-p-safran-md"]},
            {"rank": 3, "name": "Qian Chen", "credentials": "PhD", "affiliation": "RIH; NanoDe", "role_fit": "RNA delivery peer (distinct chemistry)", "physician_led_fit": "scientific_only", "evidence": "ip_nanopieces_rna", "urls": ["https://nanodetherapeutics.com/"]},
            {"rank": 4, "name": "Karl T. Kelsey", "credentials": "MD", "affiliation": "Brown", "role_fit": "Cancer biomarker trials", "physician_led_fit": "medium", "evidence": "Oncology epi", "urls": ["https://vivo.brown.edu/display/ktkelsey"]},
            {"rank": 5, "name": "Peter J. Snyder", "credentials": "PhD", "affiliation": "URI", "role_fit": "RI research leadership adjacent", "physician_led_fit": "low", "evidence": "URI life-science", "urls": ["https://web.uri.edu/research/"]},
        ],
    },
    "gap_rih_salivary_ev_ad": {
        "entity": "RIH salivary EV AD Dx",
        "inventors_anchors": ["RIH neurology/lab inventors"],
        "kols": [
            {"rank": 1, "name": "Stephen Salloway", "credentials": "MD MS", "affiliation": "Butler/Brown ADRC", "role_fit": "AD trial network", "physician_led_fit": "high", "evidence": "Brown AD research", "urls": ["https://vivo.brown.edu/display/ssallowa"]},
            {"rank": 2, "name": "Stevin H. Zorn", "credentials": "PhD", "affiliation": "MindImmune", "role_fit": "AD therapeutic peer", "physician_led_fit": "low", "evidence": "ip_dendritic_ad_mindimmune", "urls": ["https://www.mindimmune.com/"]},
            {"rank": 3, "name": "Peter J. Snyder", "credentials": "PhD", "affiliation": "URI/Brown network", "role_fit": "AD biomarker expertise", "physician_led_fit": "medium", "evidence": "RI neurodegeneration", "urls": ["https://vivo.brown.edu/display/psnyder"]},
            {"rank": 4, "name": "Sean F. Monaghan", "credentials": "MD FACS", "affiliation": "RIH", "role_fit": "Hospital translational PI peer", "physician_led_fit": "medium", "evidence": "RIH Dx spinout pattern", "urls": ["https://www.brownhealth.org/providers/sean-monaghan-md"]},
            {"rank": 5, "name": "Rachel Putman", "credentials": "MD MPH", "affiliation": "Brown Health", "role_fit": "Pulmonary/neuro adjacent", "physician_led_fit": "low", "evidence": "Brown clinical research", "urls": ["https://www.brownhealth.org/centers-services/center-advanced-lung-care"]},
        ],
    },
    "gap_rih_bx912_pulmonary_htn": {
        "entity": "RIH BX-912 PH program",
        "inventors_anchors": ["RIH cardiopulmonary"],
        "kols": [
            {"rank": 1, "name": "Rachel Putman", "credentials": "MD MPH", "affiliation": "Brown Health ILD/PH", "role_fit": "Pulmonary hypertension clinical", "physician_led_fit": "high", "evidence": "Advanced lung care center", "urls": ["https://www.brownhealth.org/centers-services/center-advanced-lung-care"]},
            {"rank": 2, "name": "Jack A. Elias", "credentials": "MD", "affiliation": "Brown", "role_fit": "Pulmonary medicine leadership", "physician_led_fit": "medium", "evidence": "ip_chitinase_ocf203 PI", "urls": ["https://vivo.brown.edu/display/jelias"]},
            {"rank": 3, "name": "Frank W. Sellke", "credentials": "MD", "affiliation": "Brown Health CV", "role_fit": "Cardiac surgery / vascular", "physician_led_fit": "medium", "evidence": "Cardiovascular research", "urls": ["https://vivo.brown.edu/display/fsellke"]},
            {"rank": 4, "name": "Mitchell M. Levy", "credentials": "MD", "affiliation": "Brown", "role_fit": "Critical care cardiopulmonary", "physician_led_fit": "medium", "evidence": "RI critical care", "urls": ["https://vivo.brown.edu/display/mlevy"]},
            {"rank": 5, "name": "Howard P. Safran", "credentials": "MD", "affiliation": "Brown Health", "role_fit": "Oncology-cardio interface", "physician_led_fit": "low", "evidence": "Clinical trials infrastructure", "urls": ["https://www.brownhealth.org/providers/howard-p-safran-md"]},
        ],
    },
    "gap_rih_pahtn_dx": {
        "entity": "RIH PAH/SCD diagnostics",
        "inventors_anchors": ["RIH cardiology"],
        "kols": [
            {"rank": 1, "name": "Rachel Putman", "credentials": "MD MPH", "affiliation": "Brown Health", "role_fit": "PH/ILD diagnostics adoption", "physician_led_fit": "high", "evidence": "Pulmonary clinic", "urls": ["https://www.brownhealth.org/centers-services/center-advanced-lung-care"]},
            {"rank": 2, "name": "Frank W. Sellke", "credentials": "MD", "affiliation": "Brown Health CV", "role_fit": "Cardiac risk / SCD", "physician_led_fit": "high", "evidence": "Cardiovascular outcomes", "urls": ["https://vivo.brown.edu/display/fsellke"]},
            {"rank": 3, "name": "Mark A. Turco", "credentials": "MD", "affiliation": "RI Life Science Hub", "role_fit": "State clinical network", "physician_led_fit": "medium", "evidence": "RI ecosystem", "urls": ["https://www.rilifescience.com/"]},
            {"rank": 4, "name": "Mitchell M. Levy", "credentials": "MD", "affiliation": "Brown", "role_fit": "ICU risk tools", "physician_led_fit": "medium", "evidence": "Critical care", "urls": ["https://vivo.brown.edu/display/mlevy"]},
            {"rank": 5, "name": "Jack A. Elias", "credentials": "MD", "affiliation": "Brown", "role_fit": "Pulmonary research", "physician_led_fit": "medium", "evidence": "Pulmonary medicine", "urls": ["https://vivo.brown.edu/display/jelias"]},
        ],
    },
    "gap_rih_bbb_nucleic_delivery": {
        "entity": "RIH BBB nucleic acid delivery",
        "inventors_anchors": ["RIH CNS delivery"],
        "kols": [
            {"rank": 1, "name": "Stephen Salloway", "credentials": "MD MS", "affiliation": "Brown ADRC", "role_fit": "CNS trial design", "physician_led_fit": "high", "evidence": "Neurodegeneration trials", "urls": ["https://vivo.brown.edu/display/ssallowa"]},
            {"rank": 2, "name": "Leigh Hochberg", "credentials": "MD PhD", "affiliation": "Brown BrainGate", "role_fit": "CNS intervention peer", "physician_led_fit": "medium", "evidence": "Neurotech clinical", "urls": ["https://www.braingate.org/"]},
            {"rank": 3, "name": "Stevin H. Zorn", "credentials": "PhD", "affiliation": "MindImmune", "role_fit": "CNS therapeutic peer", "physician_led_fit": "low", "evidence": "AD program", "urls": ["https://www.mindimmune.com/"]},
            {"rank": 4, "name": "Justin R. Fallon", "credentials": "PhD", "affiliation": "Brown", "role_fit": "Neuroscience translation", "physician_led_fit": "scientific_only", "evidence": "ip_bolden_musk", "urls": ["https://vivo.brown.edu/display/jfallonp"]},
            {"rank": 5, "name": "David Borton", "credentials": "PhD", "affiliation": "Brown", "role_fit": "Neural engineering", "physician_led_fit": "scientific_only", "evidence": "Brown neurotech", "urls": ["https://vivo.brown.edu/display/dborton"]},
        ],
    },
    "gap_rih_motile_cell_msk": {
        "entity": "RIH motile cell MSK repair",
        "inventors_anchors": ["RIH regenerative ortho"],
        "kols": [
            {"rank": 1, "name": "Paul Y. Liu", "credentials": "MD FACS", "affiliation": "Brown; Pax", "role_fit": "Hand/MSK surgery KOL", "physician_led_fit": "high", "evidence": "ip_pax_aav_vegf_tendon", "urls": ["https://www.paxtherapeutics.com/"]},
            {"rank": 2, "name": "Jin Bo Tang", "credentials": "MD", "affiliation": "Pax advisor", "role_fit": "Tendon outcomes KOL", "physician_led_fit": "high", "evidence": "Flexor tendon expertise", "urls": ["https://www.paxtherapeutics.com/the-science"]},
            {"rank": 3, "name": "Dom Messerli", "credentials": "—", "affiliation": "Lenoss", "role_fit": "Spine/ortho entrepreneur peer", "physician_led_fit": "low", "evidence": "ip_osteopearl_vcf_lenoss", "urls": ["https://lenoss.com/"]},
            {"rank": 4, "name": "Jeffrey R. Morgan", "credentials": "PhD", "affiliation": "Brown/XM", "role_fit": "Matrix biology peer", "physician_led_fit": "scientific_only", "evidence": "ip_ecm_morsels_xm", "urls": ["https://vivo.brown.edu/display/jmorgan"]},
            {"rank": 5, "name": "Jack A. Elias", "credentials": "MD", "affiliation": "Brown", "role_fit": "Translational medicine", "physician_led_fit": "low", "evidence": "RI physician-scientist network", "urls": ["https://vivo.brown.edu/display/jelias"]},
        ],
    },
    "gap_rih_ecm_joint_repair": {
        "entity": "RIH ECM joint repair",
        "inventors_anchors": ["RIH orthopedics"],
        "kols": [
            {"rank": 1, "name": "Paul Y. Liu", "credentials": "MD FACS", "affiliation": "Brown Surgery", "role_fit": "Joint/tendon clinical KOL", "physician_led_fit": "high", "evidence": "MSK RI ecosystem", "urls": ["https://vivo.brown.edu/display/pliu"]},
            {"rank": 2, "name": "Jeffrey R. Morgan", "credentials": "PhD", "affiliation": "Brown/XM", "role_fit": "ECM platform peer—FOU diligence", "physician_led_fit": "scientific_only", "evidence": "ip_ecm_morsels_xm", "urls": ["https://vivo.brown.edu/display/jmorgan"]},
            {"rank": 3, "name": "Jin Bo Tang", "credentials": "MD", "affiliation": "Hand surgery", "role_fit": "Orthopedic clinical outcomes", "physician_led_fit": "high", "evidence": "Pax network", "urls": ["https://www.paxtherapeutics.com/"]},
            {"rank": 4, "name": "Dom Messerli", "credentials": "—", "affiliation": "Lenoss", "role_fit": "Spine MSK devices", "physician_led_fit": "low", "evidence": "Lenoss Series A", "urls": ["https://lenoss.com/"]},
            {"rank": 5, "name": "Qian Chen", "credentials": "PhD", "affiliation": "NanoDe", "role_fit": "Delivery/materials peer", "physician_led_fit": "scientific_only", "evidence": "Nanopieces ortho", "urls": ["https://nanodetherapeutics.com/"]},
        ],
    },
    "gap_rih_enhancer_rna_glioma": {
        "entity": "RIH eRNA glioma therapeutics",
        "inventors_anchors": ["RIH neuro-oncology"],
        "kols": [
            {"rank": 1, "name": "Howard P. Safran", "credentials": "MD", "affiliation": "Brown Health Cancer", "role_fit": "Neuro-oncology trials", "physician_led_fit": "high", "evidence": "Cancer institute", "urls": ["https://www.brownhealth.org/providers/howard-p-safran-md"]},
            {"rank": 2, "name": "Wafik S. El-Deiry", "credentials": "MD PhD", "affiliation": "Lifespan/Brown", "role_fit": "Oncology translational", "physician_led_fit": "medium", "evidence": "Precision oncology", "urls": ["https://wafik-el-deiry.com/"]},
            {"rank": 3, "name": "Stephen Salloway", "credentials": "MD MS", "affiliation": "Brown", "role_fit": "CNS trial network", "physician_led_fit": "medium", "evidence": "Neuro trials", "urls": ["https://vivo.brown.edu/display/ssallowa"]},
            {"rank": 4, "name": "Lucas A. Salas", "credentials": "MD MPH PhD", "affiliation": "Dartmouth", "role_fit": "Brain tumor epi peer", "physician_led_fit": "medium", "evidence": "gap_christensen_epigenetics", "urls": ["https://geiselmed.dartmouth.edu/epidemiology/profile/lucas-salas-md-mph-phd/"]},
            {"rank": 5, "name": "Alan Kersey", "credentials": "—", "affiliation": "OncoLux", "role_fit": "Surgical oncology imaging peer", "physician_led_fit": "low", "evidence": "ip_oncolux_lumis", "urls": ["https://oncoluxinc.com/"]},
        ],
    },
    "gap_rih_lpa_therapeutic": {
        "entity": "RIH Lp(a) therapeutics",
        "inventors_anchors": ["RIH cardiovascular"],
        "kols": [
            {"rank": 1, "name": "Frank W. Sellke", "credentials": "MD", "affiliation": "Brown Health CV", "role_fit": "Cardiovascular outcomes KOL", "physician_led_fit": "high", "evidence": "Cardiac surgery research", "urls": ["https://vivo.brown.edu/display/fsellke"]},
            {"rank": 2, "name": "Mark A. Turco", "credentials": "MD", "affiliation": "RI Life Science Hub", "role_fit": "Cardio metabolic network", "physician_led_fit": "medium", "evidence": "RI clinical ecosystem", "urls": ["https://www.rilifescience.com/"]},
            {"rank": 3, "name": "Jack A. Elias", "credentials": "MD", "affiliation": "Brown", "role_fit": "Pulmonary-vascular interface", "physician_led_fit": "medium", "evidence": "Vascular biology", "urls": ["https://vivo.brown.edu/display/jelias"]},
            {"rank": 4, "name": "Mitchell M. Levy", "credentials": "MD", "affiliation": "Brown", "role_fit": "Critical care cardiology", "physician_led_fit": "medium", "evidence": "RI hospital medicine", "urls": ["https://vivo.brown.edu/display/mlevy"]},
            {"rank": 5, "name": "Howard P. Safran", "credentials": "MD", "affiliation": "Brown Health", "role_fit": "Clinical trials infrastructure", "physician_led_fit": "low", "evidence": "Oncology-cardio", "urls": ["https://www.brownhealth.org/providers/howard-p-safran-md"]},
        ],
    },
}


def main() -> None:
    opp_path = ROOT / "data" / "ri_patent_investment_opportunities.json"
    opp = json.loads(opp_path.read_text())
    for gap in opp["gaps_not_in_curated_patents"]:
        gid = gap["id"]
        if gid in ASSIGNEE_LABELS:
            gap["assignee_label"] = ASSIGNEE_LABELS[gid]
        if gid in EVIDENCE_PATCH:
            gap["evidence_anchors"] = EVIDENCE_PATCH[gid]
    opp["version"] = "2.0"
    opp["updated_at"] = NOW
    opp["summary"]["curated_patent_filings_total"] = json.loads(
        (ROOT / "data" / "ri_patents_curated.json").read_text()
    )["count"]
    opp["summary"]["grant_supported_gaps"] = len(opp["gaps_not_in_curated_patents"])
    opp["summary"]["total_investable_units"] = (
        opp["summary"]["patent_defined_opportunities"]
        + opp["summary"]["grant_supported_gaps"]
    )
    # Fix smurf2/ni2o/christensen patent counts in summary narrative via gap data
    for o in opp["opportunities"]:
        if o["id"] == "ip_oncolux_lumis":
            o["patent_count"] = 3
    opp_path.write_text(json.dumps(opp, indent=2) + "\n")

    comp_path = ROOT / "data" / "ri_comparables_matrix.json"
    comp = json.loads(comp_path.read_text())
    existing = {r["asset_id"] for r in comp["rows"]}
    for row in COMPARABLES_NEW:
        if row["asset_id"] not in existing:
            comp["rows"].append(row)
    comp["version"] = "1.2"
    comp["updated_at"] = NOW
    comp_path.write_text(json.dumps(comp, indent=2) + "\n")

    pl_path = ROOT / "data" / "ri_physician_led_financing.json"
    pl = json.loads(pl_path.read_text())
    pl["slater_physician_match_by_asset"].update(PHYSICIAN_NEW)
    pl["updated_at"] = NOW
    pl_path.write_text(json.dumps(pl, indent=2) + "\n")

    kol_path = ROOT / "data" / "ri_kol_directory.json"
    kol = json.loads(kol_path.read_text())
    kol["assets"].update(KOL_NEW)
    kol["updated_at"] = NOW
    kol_path.write_text(json.dumps(kol, indent=2) + "\n")

    print(f"Opportunities v2.0: {opp['summary']['total_investable_units']} units")
    print(f"Comparables rows: {len(comp['rows'])}")
    print(f"Physician-led assets: {len(pl['slater_physician_match_by_asset'])}")
    print(f"KOL assets: {len(kol['assets'])}")


if __name__ == "__main__":
    main()
