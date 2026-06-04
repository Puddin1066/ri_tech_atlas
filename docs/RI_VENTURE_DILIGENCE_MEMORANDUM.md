# Rhode Island Life Science Venture Diligence Memorandum

**Document objective:** Provide an **exhaustive, IP-backed Rhode Island opportunity landscape** and place each distinct asset in **quantitative and qualitative context** using **comparable commercial company financing and benchmark development paths**—so investors and clinical experts can crystallize what each opportunity is, what it is worth benchmarking against, and what financing trajectory is realistic.

**Audience:** Investment committees, Slater Technology Fund, RightHill Ventures, physician-angels, Brown OTL / RIH licensing, strategic partners.  
**Version:** 2.4 (June 2026)  
**Evidence:** `data/ri_patents_curated.json` (**105** filings), `data/ri_patent_investment_opportunities.json` v2.0 (**19** IP assets + **14** gaps = **33** units), `data/ri_funding_matrix.json`, Amass BiomedCore / TrialCore, public financings (press, SEC where applicable).

**Companion docs:** [Diligence report](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md) (grants §8, trials §10, patent annex) · [Opportunity atlas](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md) (registry cards)

**Disclaimer:** Public-source synthesis—not investment advice. Market sizes and comparable financings are order-of-magnitude; verify round status and license chains in data rooms.

---

## Table of contents

1. [How to read this memorandum](#1-how-to-read-this-memorandum)
2. [Exhaustive IP-backed landscape](#2-exhaustive-ip-backed-landscape)
3. [Master comparables matrix](#3-master-comparables-matrix)
4. [Benchmark development paths by modality](#4-benchmark-development-paths-by-modality)
5. [Opportunity crystallization profiles (33)](#5-opportunity-crystallization-profiles-33)
6. [RI financing context](#6-ri-financing-context)
7. [Portfolio risks & data refresh](#7-portfolio-risks--data-refresh)

---

## 1. How to read this memorandum

Each RI opportunity is defined by a **patent package** (or pending harvest for grant gaps), not by geography alone. For every asset, Section 5 provides:

| Layer | What it answers |
|-------|-----------------|
| **Quantitative snapshot** | Patents, cited non-dilutive $, market TAM/SAM, comparable company financing totals, benchmark stage, realistic RI check size |
| **Qualitative snapshot** | Technology differentiation, assignee/vehicle, clinical/regulatory position, RI ecosystem anchors |
| **Comparable paths** | Named companies: how they financed and developed—milestones investors can map to RI |
| **Crystallized RI path** | Forward-looking 0–36 month ladder from today’s IP + grant position to next institutional round |

**Quantitative figures** come from NIH RePORTER obligations, DARPA/press announcements, and public VC/IPO disclosures (June 2026). **Qualitative** judgments use promise tier (A/B/C), assignee type, and clarity of transaction path from `ri_patent_investment_opportunities.json`.

**Slater Technology Fund.** Early-stage Slater equity **requires a third-party financing match**. Practical Slater seed: **$200K–$400K** (not the full round). Policy: `data/ri_physician_led_financing.json` → `slater_investment_policy`.

---

## 2. Exhaustive IP-backed landscape

### 2.1 Corpus summary

| Metric | Value |
|--------|------:|
| Curated patent filings | **105** |
| Patent-defined investable assets | **19** |
| Grant-anchored gaps (patent-linked or harvest-pending) | **14** |
| **Total opportunity units in this memorandum** | **33** |
| University / hospital primary assignee | **8** |
| Company or licensed startup assignee | **11** |
| Tier **A** (formation / seed–A fit) | **13** |
| Tier **B** (platform, growth, BRF license) | **7** |
| Tier **C** (commercial / liquidity) | **2** |
| Cited federal + DARPA on Brown neurotech cluster alone | **>$25M** |

### 2.2 Complete opportunity registry

| # | Asset ID | Title | Tier | Patents | Assignee | Entity | Stage (today) | Cited non-dilutive anchor |
|---|----------|-------|------|--------:|----------|--------|---------------|---------------------------|
| 1 | `ip_wireless_neurograins` | Wireless neurograins & cortical implants | A | 8 | Brown | — | Preclinical → spinout | DARPA **~$19M**; UH2 **~$2.0M** |
| 2 | `ip_speech_tablet_ibci` | Speech & tablet iBCI decoding | A | 6 | Brown | BrainGate | Trials recruiting | U01 **~$0.8M/yr**; VA I01 |
| 3 | `ip_nanopieces_rna` | Nanopieces non-viral RNA | A | 4 | RIH | NanoDe | STTR preclinical | R41TR002298; COBRE |
| 4 | `ip_chitinase_ocf203` | Chitinase-1 IPF (OCF-203) | A | 1 | Brown→licensee | Ocean; Elkurt | Pre-IND | P01HL114501 **~$0.34M/yr** |
| 5 | `ip_ecm_morsels_xm` | Decellularized ECM morsels | A | 5 | Brown→XM | XM Therapeutics | Preclinical PoP | Slater **$375K**; BBII |
| 6 | `ip_iaip_neonatal` | IAIP biologics + NICU LFIA | A | 4 | ProThera | ProThera | SBIR clinical-enabling | SBIR track **~$3.7M+** active |
| 7 | `ip_dendritic_ad_mindimmune` | AD dendritic blockade (MITI-101) | A | 3 | MindImmune | MindImmune | Post–Series A | **$30M** Series A; RI Hub |
| 8 | `ip_spinal_isi_dbs` | Intelligent spinal interface | A | 2 | Brown | — | IDE early | DARPA **$6.3M**; NCT04302259 |
| 9 | `ip_tregitope_immunomod` | Tregitope immunomodulation | B | 10 | EpiVax | EpiVax | Platform + therapeutics | NIH stack **~$4M+** cited |
| 10 | `ip_biglycan_msk` | Biglycan MSK regeneration | B | 2 | BRF | — | Academic preclinical | Grant TBD |
| 11 | `ip_neural_decoding_legacy` | Core BMI decoding (legacy) | B | 5 | Brown | BrainGate | Clinical legacy | Multi-IC BrainGate |
| 12 | `ip_osteopearl_vcf_lenoss` | Biological kyphoplasty | B | 7 | Lenoss | Lenoss | Commercial early | NEMIC; **~$4M** Series A |
| 13 | `ip_af_mapping_ai` | AI AF ablation (VX1) | B | 2 | Volta | Volta | FDA-cleared | VC **~$74M** |
| 14 | `ip_genomics_hans` | Electronic genome mapping | C | 3 | Nabsys | Nabsys 2.0 | Commercial | R43HG; Slater **$4M** hist. |
| 15 | `ip_ect_ophthalmology` | Encapsulated cell therapy (CNTF) | C | 8 | Neurotech | Neurotech | Approved 2025 | Mature commercial |
| 16 | `ip_monaghan_deep_rna_dx` | Deep RNA ICU diagnostics | A | 4 | RIH | — (spinout forming) | Translational LDT | R35GM142638; RNA Center |
| 17 | `gap_smurf2_oncology` | SMURF2–HIF1α oncology | A* | 0→~19 | TBD harvest | SMURF-Tx | Grant + preclinical | R01 **~$2.4M** |
| 18 | `gap_soma_dtx` | SOMA pain / interoception DTx | B* | 0 | TBD | SOMAScience | COBRE pilots | COBRE **~$12M** phase |
| 19 | `gap_christensen_epigenetics` | HiTIMED IO epigenetics | B* | 1* | Dartmouth (EP4505463 pending) | — | R01 academic | R01 **~$1.1M/yr** combined |
| 20 | `ip_bolden_musk_neurogenesis` | MuSK ASO neurogenesis (Bolden) | A | 3 | Brown→Bolden | Bolden Therapeutics | Preclinical in vivo | NIA **$500K** STTR; **$1.5M** pre-seed |
| 21 | `ip_pax_aav_vegf_tendon` | AAV2–VEGF tendon (PAX-001) | A | 1 | RIH→Pax | Pax Therapeutics | Pre-IND | Seed **~$1.7M**; RILSH LIFT |
| 22 | `ip_oncolux_lumis` | LUMIS optical theranostics | B | 0* | OncoLux | OncoLux | Clinical validation | RILSH attraction; Mayo 2026 |
| 23 | `gap_ni2o_kiwi_bci` | KIWI wireless micro-implant BCI | A* | 3+ | Genesis / Howard | ni2o Inc | Preclinical / partnership | Nurosene 2021; ~$1.3M cited |
| 24 | `gap_levine_pediatric_sepsis` | Pediatric sepsis wearable + ML CDSS | A* | 0 | Brown / RIH | — (spinout forming) | Grant-first SaMD path | FIC **R33TW012211** |
| 25 | `gap_uri_phlip_lnp` | PHLIP peptide–LNP / STING delivery | A* | 1+ | URI | — | Preclinical | URI tech transfer |
| 26 | `gap_rih_salivary_ev_ad` | Salivary EV AD liquid biopsy | A* | 1+ | RIH | — | Dx forming | US20260103757A1 |
| 27 | `gap_rih_bx912_pulmonary_htn` | BX-912 pulmonary hypertension | A* | 1+ | RIH | — | Preclinical | WO2026112526 |
| 28 | `gap_rih_pahtn_dx` | PAH / SCD risk stratification Dx | B* | 1+ | RIH | — | Retrospective validation | US20180094317 |
| 29 | `gap_rih_bbb_nucleic_delivery` | BBB nucleic acid delivery | A* | 1+ | RIH | — | Rodent PoC | WO2025171161 |
| 30 | `gap_rih_motile_cell_msk` | Motile injectable cell MSK repair | A* | 1+ | RIH | — | Large-animal next | WO2025155768 |
| 31 | `gap_rih_ecm_joint_repair` | Biomimetic ECM joint repair | B* | 1+ | RIH | — | FOU vs XM diligence | US20240139376 |
| 32 | `gap_rih_enhancer_rna_glioma` | eRNA-targeted glioma therapy | A* | 1+ | RIH | — | Preclinical | US20230323349 |
| 33 | `gap_rih_lpa_therapeutic` | Lp(a)-lowering therapeutic | B* | 1+ | RIH | — | Partner path | WO2025245119 |

\*Gap rows: investable on grant + inventor/patent signal; counts from curated annex + `key_patents_harvested`. SMURF2/Christensen/ni2o: USPTO-linked families in corpus. OncoLux: **3** CytoVeris filings linked.

### 2.3 IP assignee map (qualitative structure)

| Assignee bucket | Assets | Typical transaction |
|-----------------|--------|---------------------|
| **Brown University OTL** | neurograins, speech/tablet, spinal ISI, legacy decode, chitinase (origin) | Exclusive license, spinout, SPV, royalty |
| **Rhode Island Hospital** | Nanopieces, Monaghan deep RNA Dx | License to NanoDe or physician-founder Dx spinout |
| **Brown Research Foundation** | biglycan | OTL → newco |
| **Licensed from Brown** | ECM (XM), chitinase (Ocean path) | Equity or sublicense newco |
| **RI startup (IP on cap table)** | ProThera, MindImmune, Lenoss, Volta, EpiVax, Nabsys, Neurotech, Bolden, Pax, OncoLux, ni2o | Seed through M&A |

### 2.4 Patent cluster concentration

| Cluster | Filings (approx.) | Representative assets |
|---------|------------------:|----------------------|
| Brown neurotech (BCI + spinal + legacy) | **~21** | neurograins, speech, spinal, legacy |
| EpiVax Tregitope / iVAX | **10** | `ip_tregitope_immunomod` |
| Neurotech ECT ophthalmology | **8** | `ip_ect_ophthalmology` |
| Lenoss VCF / kyphoplasty | **7** | `ip_osteopearl_vcf_lenoss` |
| Wireless neurograins only | **8** | `ip_wireless_neurograins` |
| Morgan ECM morsels | **5** | `ip_ecm_morsels_xm` |
| Speech/tablet only | **6** | `ip_speech_tablet_ibci` |

---

## 3. Master comparables matrix

*Use this table to place any RI asset in market and financing context before reading Section 5 profiles.*

| RI asset | Market (quant.) | SAM / niche | Primary comparable(s) | Comparable financing (quant.) | Comparable development path | RI crystallized path | RI round (quant.) |
|----------|-----------------|-------------|----------------------|------------------------------|------------------------------|---------------------|-------------------|
| `ip_iaip_neonatal` | Host-response NICU; Dx peers **$200M+** scale | Neonatal sepsis biologic + LFIA | **Inotrem**, **MeMed** | Inotrem **€39–58M** Series B; MeMed **>$200M**, **$93M** Series E (2022) | Biologic Phase 3 / 510(k) Dx parallel | SBIR → Series A | **$5–10M** A |
| `ip_ecm_morsels_xm` | IPF **~$5B+** 2030; HF remodeling niche | Injectable matrix biologic | **Heartseed**, Ventrix | Heartseed **~$41M** Series B (2024) | iPSC / matrix preclinical → IND | Slater $375K → large-animal → A | **$15–30M** A |
| `ip_nanopieces_rna` | Genetic medicines **$B+**; extrahepatic niche | Non-viral RNA delivery | **Aera**, **Eascra**, Generation Bio | Aera **$193M** A+B (2023); **Eascra ~$2.2M** grants (NASA **$1.8M**, NSF SBIR); GBIO restructure → XOMA **2025** | STTR/grants → ortho IND-enabling → A | STTR → Slater **$200–400K** + match → A | **$1–3M** total seed |
| `ip_chitinase_ocf203` | IPF **~$3.7–5B** (2024–30) | CHIT1/CHI3L1 small molecule / biologic | **Pliant**, Boehringer | Pliant public; **bexotegrast halted 2025** | P01 → license → IND tox | License diligence → seed newco | Slater **$200–400K** + match |
| `ip_dendritic_ad_mindimmune` | AD therapeutics **~$8B+** 2030 | Peripheral innate blockade | **Alector**, anti-amyloid leaders | MindImmune **$30M** A (2025); Alector **$100M+** rounds | IND → Phase 1 biomarkers | Post-A → Phase 1 FIH | Co-invest |
| `ip_wireless_neurograins` | BCI **~$2.1B** 2030 | Wireless cortical hardware | **Paradromics**, **Blackrock** | Paradromics **~$121M**; Blackrock **$200M** (2024) | DARPA → IDE → strategic | DARPA $19M → OTL spinout | Slater **$200–400K** + match (+ SPV) |
| `ip_speech_tablet_ibci` | BCI **~$2.1–3.1B** 2030 | Cortical speech / tablet decode | **Synchron**, Paradromics | Synchron **~$345M**, **$200M** D (2025) | Trials → decode license SPV | U01/VA → FOU SPV | **$3–8M** SPV |
| `ip_spinal_isi_dbs` | SCI neuromodulation **$B+** medtech | Closed-loop spinal interface | **ONWARD Medical** | **€50M** (Oct 2024); ARC-EX cleared | DARPA → IDE → strategic | ISI IDE → license/SPV | SPV / strategic |
| `ip_biglycan_msk` | Rare neuromuscular **multi-$B** | Biglycan regeneration | **Sarepta**, Solid Biosciences | Sarepta commercial gene therapy; Solid restructuring lessons | BRF OTL → IND → A | Academic → newco | Slater **$200–400K** + match |
| `ip_tregitope_immunomod` | Vaccine/biologic de-risk **~$50B+** fragmented | In silico immunogenicity | **AbCellera**, **Absci** | ABCL **~$555M** IPO; ABSI **$86M** + AZ **$247M** deal | Platform ARR → spinout | SBIR/U01 → spinout/strategic | Growth / strategic |
| `ip_neural_decoding_legacy` | Same BCI TAM | Foundational decode IP | BrainGate / Blackrock ecosystem | N/A (royalty) | Consortium → sublicense | Royalty / FOU only | N/A |
| `ip_osteopearl_vcf_lenoss` | **~700K** US VCF/yr | Biological BKP vs PMMA | **Medtronic Kyphon** | Lenoss **~$4M** A; **~$12.6M** total cited | J&J license → NEMIC → commercial | Registry + scale | Growth |
| `ip_af_mapping_ai` | AF ablation **$B+** procedures | AI mapping SaMD | Volta (local), Acutus hist. | Volta **>€90M**; **€36M** B (2023) | CE/FDA SaMD → Series B | Commercial expansion | Growth VC |
| `ip_genomics_hans` | SV tools; OGM **~$31M** rev peer | Electronic genome mapping | **Bionano**, Hitachi/Nabsys | Bionano **$30.8M** FY24 rev; Hitachi majority **2024** | SBIR → strategic | Hitachi pull-through | M&A / royalty |
| `ip_ect_ophthalmology` | Retinal therapy niche | ECT CNTF | Neurotech ENCELTO | Private; **FDA 2025** MacTel | Phase 3 → BLA → J-code | J3403 commercial | Royalty / M&A |
| `gap_smurf2_oncology` | HIF pathway commercial (**Welireg**) | SMURF2 degradation | **Merck Welireg**, Inotrem (financing proxy) | Welireg **~$199M/qtr** (2026); Inotrem **~€58M** B | R01 → biomarker → seed | SMURF-Tx spinout | Slater **$200–400K** + match |
| `gap_soma_dtx` | Pain DTx **~$15–24B** 2033 | Interoception SaMD | **Kaia**, AppliedVR, Pear | Kaia **$125M** / **$75M** C; Pear **Ch.11 2023** | COBRE → SaMD pivotal | Carney → spinout | Seed post-pilot |
| `gap_christensen_epigenetics` | IO biomarker licensing | HiTIMED deconvolution | CiberSortX, Epicypher | Software / reagent models | R01 → pharma license | OTL stratification deal | Upfront + milestones |

---

## 4. Benchmark development paths by modality

*Typical **commercial** milestone ladders—not RI promises. Map RI asset to closest row.*

### 4.1 Biologic / matrix therapeutics

| Phase | Inotrem (sepsis) | Heartseed (cardiac cell) | **RI analog: ProThera / XM** |
|-------|------------------|--------------------------|------------------------------|
| Discovery | Academic target | iPSC platform | IAIP / ECM morsels academic PoP |
| Seed / SBIR | EU grants | Series A/B Japan | Slater + SBIR / BBII |
| IND-enabling | Phase 2/3 design | Large-animal | LFIA + tox / large-animal cardiac |
| Clinical | Phase 3 ACCURATE | FIH cell therapy | NICU LFIA + biologic IND |
| Financing inflection | **€39–58M** B | **~$41M** B | **$5–10M** (ProThera) / **$15–30M** (XM) |

### 4.2 Non-viral RNA / delivery

| Phase | Aera Therapeutics | **Eascra Biotech** | Generation Bio (caution) | **RI analog: NanoDe** |
|-------|-------------------|--------------------|--------------------------|------------------------|
| Platform PoC | PNP / tLNP **$193M** | JBNp™ Janus DNA-nanotube; **~$2.2M** grants | **~$236M** → restructure | STTR Nanopieces |
| IND-enabling | Extrahepatic IND | OA / cartilage, solid tumor RNA | Failed scale-up | In vivo biodistribution |
| Financing | 2023 A+B | NASA + NSF + MassVentures (non-dilutive) | IPO → XOMA 2025 | Slater **$200–400K** + match → **$30–80M** A |

### 4.3 Cortical BCI (hardware vs decode)

| Phase | Paradromics (implant) | Synchron (endovascular) | **RI: neurograins** | **RI: speech/tablet** |
|-------|----------------------|-------------------------|---------------------|-------------------------|
| Non-dilutive | NIH + private | **$200M** D 2025 | DARPA **$19M** | U01 + VA |
| Regulatory | IDE 2025 | Clinical expansion | Pre-IND | Recruiting NCTs |
| Financing | **~$121M** total | **~$345M** total | Slater **$200–400K** + match | Decode SPV **$3–8M** (beyond Slater band) |
| Exit path | Strategic / IPO | Strategic | Hardware license | Algorithm license |

### 4.4 SCI neuromodulation

| Phase | ONWARD Medical | **RI analog: spinal ISI** |
|-------|----------------|---------------------------|
| De-risk | ARC-EX clearance | DARPA **$6.3M** + IDE |
| Financing | **€50M** 2024 | SPV or strategic upfront |
| Exit | F-1 / Nasdaq path | License to ONWARD-class |

### 4.5 IPF / fibrosis

| Phase | Pliant (caution) | Boehringer (Ofev) | **RI: chitinase / XM IPF** |
|-------|------------------|-------------------|----------------------------|
| Clinical | BEACON halted 2025 | Approved SOC | Preclinical / PoP |
| Financing | Public → halt | Pharma scale | Seed or Series A after license/PoP |

### 4.6 Digital therapeutics (pain)

| Phase | Kaia Health | Pear Therapeutics | **RI: SOMA gap** |
|-------|-------------|-------------------|------------------|
| Evidence | **$75M** Series C | FDA clearance → **Ch.11** | COBRE pilots |
| Payer | Acquired | Reimbursement failure | Payer-first design required |
| RI path | — | Lesson | SaMD before growth equity |

---

## 5. Opportunity crystallization profiles (33)

*Standard template: **quantitative snapshot → qualitative snapshot → comparable paths → benchmark ladder → crystallized RI opportunity**.*

---

### OP-01 · `ip_iaip_neonatal` — ProThera IAIP

**Crystallization.** RI’s strongest **physician-founder, dual-product** play: **IAIP biologic** + **NICU LFIA**, with **~$3.7M+** active SBIR and **~$12M** cumulative NIH cited—benchmark against **Inotrem** / **MeMed**, target **$5–10M Series A**.

| Quantitative | |
|--------------|--|
| Patents | **4** (US7932365B2, US9572872B2, USRE47972E1, US20070297982A1) |
| Cited non-dilutive | R44AI141283 **~$0.95M**; R44NS084575 **~$2.78M**; R43HD114348 **~$50K**; ~**$12M** cumulative NIH (company) |
| Market | Host-response NICU; Dx comparables **>$200M** raised |
| Comparable financing | Inotrem **€39–58M** B; MeMed **$93M** E (2022) |
| RI round band | **$5–10M** Series A |

| Qualitative | |
|-------------|--|
| Differentiation | Dual therapeutic + rapid LFIA; plasma-derived IAIP vs single-marker Dx |
| Stage | SBIR clinical-enabling; historical Slater milestone (ProThera); new Slater deals **$200–400K + match** |
| RI anchors | Women & Infants; Lim MD PhD founder equity |
| Vehicle | Equity in ProThera |

**Comparable development paths**

| Company | Path | Milestone that re-priced | Lesson for RI |
|---------|------|--------------------------|---------------|
| **Inotrem** | EU grants → **€39–58M** B → Phase 3 ACCURATE | Phase 3 start | Biologic needs pivotal design + KOL SAB early |
| **MeMed** | R&D → **$93M** E → **510(k)** BV | FDA Dx clearance | LFIA regulatory path can lead financing |

**Benchmark ladder (RI)**

| Month | Milestone | Financing gate |
|------:|-----------|----------------|
| 0–12 | LFIA NICU validation | SBIR tranche |
| 12–18 | SAB + physician equity refresh | Slater optional milestone |
| 18–24 | Series A materials | **$5–10M** A |

**Evidence.** [PMID 41674606](https://doi.org/10.64898/2026.01.30.26345077); [§5.7](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#57-prothera--iaip-sepsis--neonatal-inflammation)

---

### OP-02 · `ip_ecm_morsels_xm` — XM Therapeutics

**Crystallization.** **Injectable human ECM morsels** (~200 µm) for HF/IPF—Brown IP in Slater-backed newco; benchmark **Heartseed** (**~$41M** B), not cell-therapy CMC; **$15–30M Series A** after large-animal PoP.

| Quantitative | |
|--------------|--|
| Patents | **5** (US20230348859A1, WO2022140530A1, US8361781B2, US11286451B2, US12435312B2) |
| Non-dilutive / seed | Slater **$375K** (press cites **$750K** total Slater XM) |
| Market | HF + IPF **~$5B+** IPF segment by 2030 |
| Comparable | Heartseed **~$41M** Series B (2024, Japan) |
| RI round band | **$15–30M** Series A |

| Qualitative | |
|-------------|--|
| Differentiation | All-human decellularized ECM particles vs iPSC transplant manufacturing |
| Evidence | [PMID 39705507](https://doi.org/10.1152/ajpheart.00581.2024) MI functional benefit |
| Gap | Recruit cardio/ILD physician angel + Sellke-aligned SAB |

**Comparable paths:** Heartseed (cell) and Ventrix (ECM gel, historical Phase 2)—XM is **matrix biologic** between device and cell therapy.

**Benchmark ladder:** Large-animal PoP (12 mo) → CMC plan (18 mo) → Series A (24–30 mo).

---

### OP-03 · `ip_nanopieces_rna` — Nanopieces / NanoDe

**Crystallization.** **RIH-owned** non-viral delivery; **Aera $193M** validates genetic medicine TAM; **Eascra** is the closest **modality peer** (Janus base nanoparticles, cartilage/ECM RNA—orthogonal to LNP). RI path **STTR → Slater $200–400K + third-party match → Series A** with ortho/NICU KOL.

| Quantitative | Patents **4**; STTR R41TR002298; comparables **Aera $193M**, **Eascra ~$2.2M** grants, GBIO caution |
| Qualitative | ECM-penetrating Janus nanotubes (Nanopieces); field-of-use license beyond NanoDe; Eascra JBNp™ targets same hard-to-penetrate tissues |
| Slater band | **$200–400K** (requires match); total seed often **$1–3M** |

**Comparable paths**

| Company | Financing | Development path |
|---------|-----------|------------------|
| **Aera** | **$193M** A+B (2023) | Extrahepatic LNP/PNP → IND |
| **Eascra** | **~$2.2M** (NASA **$1.8M** 2022, NSF SBIR, MassVentures) | JBNp™ RNA to cartilage/tumor; grant → ortho preclinical ([eascrabiotech.com](https://eascrabiotech.com)) |
| **Generation Bio** | IPO → **restructure 2023** → XOMA 2025 | Non-viral scale-up risk lesson |

---

### OP-04 · `ip_chitinase_ocf203` — Chitinase IPF

**Crystallization.** Single flagship **US11717528B2** + **P01HL114501**; **Pliant 2025 halt** is cautionary comp; value hinges on **OCF-203 license chain** (Ocean/Elkurt)—**Slater $200–400K + third-party match** into RI newco.

| Quantitative | Patents **1**; P01 **~$337K/yr** (FY25 obligation cited); IPF TAM **~$5B+** 2030 |
| Qualitative | CHIT1 axis distinct from anti-TGF-β-only; Elias engine; ILD at Brown Health CALC |
| Risk (qual.) | Do not use retracted PMID 31085559 as efficacy anchor |

**Comparable paths:** Boehringer (Ofev)—decades to approval; Pliant—integrin path **discontinued 2025** after safety signal.

---

### OP-05 · `ip_dendritic_ad_mindimmune` — MindImmune MITI-101

**Crystallization.** **$30M Series A (Nov 2025)** already sets pricing; RI role is **co-invest at IND/Phase 1**—benchmark **Alector** innate CNS; **US20210181185A1 abandoned** requires FTO before next check.

| Quantitative | Patents **3**; **$30M** A; RI Hub IND grant (2025) |
| Qualitative | CD11c+ peripheral blockade; Zorn CSO; Slater/RightHill/Pfizer in syndicate |
| RI round | Series A extension / co-invest (not seed) |

**Comparable path:** Alector—innate immunity CNS, multi-round VC before Phase 1 readouts; anti-amyloid sets high efficacy bar.

---

### OP-06 · `ip_wireless_neurograins` — Wireless cortical implants

**Crystallization.** **$21M+** cited federal on hardware alone; **Paradromics ~$121M** / **Blackrock $200M** frame exit; RI needs **OTL spinout** + **Slater $200–400K with match** (hardware scale may need SPV/strategic beyond Slater band)—not speech SPV.

| Quantitative | Patents **8**; DARPA **~$19M**; UH2 **~$2.0M**; BCI TAM **~$2.1B** 2030 |
| Qualitative | Distributed wireless nodes vs tethered Utah array |
| Slater band | **$200–400K** + match → **$30–80M** strategic (benchmark) |

**Comparable paths:** Paradromics (high-channel IDE); Blackrock (Utah Array FDA-cleared in humans); Neuralink (different risk/capital).

---

### OP-07 · `ip_speech_tablet_ibci` — Speech & tablet decode

**Crystallization.** **Human speech BCI data** in recruiting trials; **Synchron ~$345M** prices decode + interface; RI asset is **algorithm/FOU license**, **$3–8M SPV**.

| Quantitative | Patents **6**; U01 **~$797K** (FY25); trials **NCT05724173**, **NCT06094205**, **NCT06511934** |
| Qualitative | Decode IP separable from implant vendor; NEJM/Nature speech papers |
| RI round | **$3–8M** SPV |

**Evidence.** [PMID 37612500](https://doi.org/10.1038/s41586-023-06377-x); [PMID 39141853](https://doi.org/10.1056/NEJMoa2314132)

**Comparable paths:** Synchron **$200M** D (2025); Paradromics IDE 2025—both ahead on implant; Brown leads on **decode + tablet control** IP.

---

### OP-08 · `ip_spinal_isi_dbs` — Intelligent spinal interface

**Crystallization.** **DARPA $6.3M** + **NCT04302259** IDE; **ONWARD €50M (2024)** and ARC-EX clearance define strategic comp—license or **$20–40M** medtech SPV benchmark.

| Quantitative | Patents **2**; DARPA **$6.3M** |
| Qualitative | SCI + bladder rehab; shorter path than cortical BCI |
| RI round | SPV seed or strategic upfront |

---

### OP-09 · `ip_biglycan_msk` — Biglycan MSK

**Crystallization.** **Unlicensed BRF package**—rare neuromuscular **multi-$B** TAM; **Sarepta** commercial path vs **Solid** restructuring lesson; **Slater $200–400K + match** after OTL.

| Quantitative | Patents **2**; Series A benchmark **$20–50M** (post-IND) |
| Qualitative | Fallon program; no RI startup in map |
| Slater band | **$200–400K** + third-party match |

---

### OP-10 · `ip_tregitope_immunomod` — EpiVax

**Crystallization.** **Deepest RI patent cluster (10)**; **AbCellera ~$555M IPO** / **Absci $247M AZ deal** frame platform→pipeline; growth/strategic, not Slater seed.

| Quantitative | Patents **10**; NIH cited stack **~$4M+** on key awards |
| Qualitative | iVAX services ARR + EpiVax Therapeutics spinout option |
| RI round | Growth / strategic |

---

### OP-11 · `ip_neural_decoding_legacy` — Legacy BMI decode

**Crystallization.** **Royalty / FOU license** asset—foundational Donoghue patents; diligence encumbrance vs wireless/speech sub-families; **not** seed newco.

| Quantitative | Patents **5** |
| Qualitative | BrainGate consortium; Blackrock external |
| RI transaction | Royalty strip / sublicense only |

---

### OP-12 · `ip_osteopearl_vcf_lenoss` — Lenoss OsteoPearl

**Crystallization.** **Commercial-stage** biological kyphoplasty—**~700K** US VCF/yr; **~$4M Series A (2025)**; **23** patents (press); comp **Medtronic Kyphon** (PMMA incumbent).

| Quantitative | Patents **7+**; **~$4M** A; **~$12.6M** total cited; **150+** implants (2025 PR) |
| Qualitative | 100% cortical allograft; Elevoss transverse cavity; NEMIC |
| RI round | Growth / strategic (not formation) |

---

### OP-13 · `ip_af_mapping_ai` — Volta VX1

**Crystallization.** **FDA-cleared SaMD** with **>€90M** VC—local Providence growth story; TAILORED-AF RCT drives next inflection.

| Quantitative | Patents **2**; **€36M** Series B (2023); **~$74M** total VC cited |
| Qualitative | Dispersed EGM AI mapping during AF ablation |
| RI round | Growth VC |

---

### OP-14 · `ip_genomics_hans` — Nabsys

**Crystallization.** Brown-origin **HANS** IP inside **Hitachi-majority** commercial story—**Bionano $30.8M FY24 revenue** peer; M&A/royalty, not seed.

| Quantitative | Patents **3**; historical Slater/Point Judith **$4M** (2009) |
| Qualitative | OhmX electronic genome mapping for SV |
| RI round | Strategic / royalty |

---

### OP-15 · `ip_ect_ophthalmology` — Neurotech ECT

**Crystallization.** **8-patent** ECT estate; **FDA MacTel approval 2025**; **J-code J3403**—liquidity/royalty, formation capital inappropriate.

| Quantitative | Patents **8** |
| Qualitative | ENCELTO commercial rollout 2025–26 |
| RI round | Royalty / M&A |

---

### OP-16 · `ip_monaghan_deep_rna_dx` — Deep RNA ICU diagnostics

**Crystallization.** **RIH-owned** deep RNA-seq from ICU blood deconvolutes **host** immune transcriptome (DGE, splicing, NMD) and **pathogen/AMR** RNA from unmapped reads—benchmark **Karius**, **Day Zero**, **MeMed**; orthogonal to **ProThera IAIP** and **Levine** wearable sepsis ML. **Sean F. Monaghan MD** physician-founder + **R35GM142638** → hospital license → **Slater $200–400K + match** → **$3–8M** seed.

| Quantitative | Patents **4**; R35GM142638; comparables **>$100M** VC each |
| Qualitative | Shock 2026 pathogen PCR ([PMID 41697057](https://pubmed.ncbi.nlm.nih.gov/41697057/)); NMD/splicing sepsis biomarkers ([LSA 2025](https://doi.org/10.26508/lsa.202503380)) |
| Slater band | **$200–400K** + third-party match |

**Benchmark ladder:** RIH license (6 mo) → LDT validation (12 mo) → SAB + Slater seed (18 mo).

---

### OP-17 · `gap_smurf2_oncology` — SMURF-Therapeutics

**Crystallization.** Grant-anchored (**R01 ~$2.4M**) with **Welireg ~$199M/qtr** proving HIF commercial relevance—harvest **~19** El-Deiry patents; **Slater $200–400K + match** after biomarker PoC.

| Quantitative | Patents **0** in annex → **~19** expected; R01CA173453 |
| Qualitative | SMURF-Tx Providence 2021; WIN oncology network |
| Slater band | **$200–400K** + third-party match |

**Comparable paths:** Merck Welireg (Phase 3→commercial); Inotrem (biologic financing proxy).

---

### OP-18 · `gap_soma_dtx` — SOMA pain DTx

**Crystallization.** **COBRE ~$12M** phase + Carney pilots; pain DTx **~$15–24B** 2033—**Kaia $75M Series C** vs **Pear Ch.11 2023** payer lesson.

| Quantitative | COBRE P20GM103645; pilot **~$393K** (Petzschner) |
| Qualitative | Interoception computational psychiatry; SOMAScience forming |
| RI round | Seed after pivotal pilot + payer strategy |

---

### OP-19 · `gap_christensen_epigenetics` — HiTIMED

**Crystallization.** **R01 ~$1.1M/yr** combined IO epigenetics + **pending EP4505463A1** (HiTIMED, Dartmouth)—**software/pharma license** model (CiberSortX-like), not classic biotech VC. Confirm **Dartmouth OTT** vs **Brown OTL** field-of-use before term sheet.

| Quantitative | **EP4505463A1** pending (priority 2022-04-06); R01CA253976 **~$661K**; R01CA216265 **~$472K** |
| Qualitative | 17-cell TME deconvolution; [PMID 36348337](https://pubmed.ncbi.nlm.nih.gov/36348337/); immune/angiogenic hot-cold subtypes |
| RI transaction | Dartmouth/Brown license → upfront + milestones |

---

### OP-20 · `ip_bolden_musk_neurogenesis` — Bolden Therapeutics

**Crystallization.** Brown OTL **MuSK** ASO neurogenesis licensed to **Bolden**—benchmark **Biogen/Ionis** CNS ASO paths and **MindImmune** ($30M AD round); **NIA $500K STTR** + **$1.5M** pre-seed (Slater in round) → **Slater $200–400K + match** follow-on after in vivo PoC.

| Quantitative | Patents **3** (US12458657B2 family); NIA STTR **$500K**; pre-seed **$1.5M** |
| Qualitative | Fallon/Webb science; Salloway ADRC KOL; distinct from BRF biglycan and MindImmune innate path |
| Slater band | **$200–400K** + third-party match |

**Comparable paths:** Biogen/Ionis ASO franchise; MindImmune Series A.

**Benchmark ladder:** OTL scope confirm (6 mo) → STTR milestones (12 mo) → neurology SAB (18 mo) → Series A.

**Evidence.** [Bolden Therapeutics](https://www.boldentherapeutics.com/); [Opportunity Atlas §5.17](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md#517-ip_bolden_musk_neurogenesis--musk-aso-neurogenesis-bolden-therapeutics--tier-a--priority-8).

---

### OP-21 · `ip_pax_aav_vegf_tendon` — Pax Therapeutics

**Crystallization.** **RIH** AAV2–**VEGF** flexor tendon gene therapy (**PAX-001**)—physician-chairman **Liu MD**; **~$1.7M** seed + **RILSH LIFT**; pre-IND complete → **$5–15M** Series A post-IND acceptance.

| Quantitative | Patents **1** (WO2019146830A1); seed **~$1.7M**; RILSH LIFT |
| Qualitative | Ocean State Labs; hand surgery KOL network (Tang advisor) |
| Slater band | **$200–400K** + match post-IND |

**Comparable paths:** Organogenesis soft-tissue repair; orthobiologic precedents.

**Benchmark ladder:** RIH license confirm → IND filed → hand flexor Phase 1 plan (18–24 mo).

**Evidence.** [Pax Therapeutics](https://www.paxtherapeutics.com/); [Opportunity Atlas §5.18](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md#518-ip_pax_aav_vegf_tendon--aav2vegf-tendon-repair-pax-therapeutics--tier-a--priority-6).

---

### OP-22 · `ip_oncolux_lumis` — OncoLux

**Crystallization.** **LUMIS** multispectral fluorescence + in-situ PDT—relocated **CT→RI** via RILSH; **Mayo** robotic bronchoscopy know-how (2026)—**growth medtech**, not OTL seed formation.

| Quantitative | Patents **0** in annex (harvest pending); RILSH attraction (undisclosed per co.) |
| Qualitative | Ocean State Labs; surgical oncology KOL advisors |
| RI round | Growth equity / strategic |

**Comparable paths:** Fluorescence-guided surgery (Medtronic VISUALIZE class); multispectral imaging peers.

**Benchmark ladder:** Colorectal + bronchoscopy readouts (12 mo) → regulatory path memo (18 mo) → growth partner.

**Evidence.** [OncoLux](https://oncoluxinc.com/); [Opportunity Atlas §5.19](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md#519-ip_oncolux_lumis--lumis-optical-theranostics--tier-b--priority-10).

---

### OP-23 · `gap_ni2o_kiwi_bci` — ni2o

**Crystallization.** **KIWI** wireless micro-implant BCI (Providence HQ)—**FTO vs Brown BrainGate** essential; benchmark **Paradromics** (~$121M) and **Blackrock** ($200M 2024)—strategic financing, not Slater-first formation.

| Quantitative | Patents **0** RI assignee in annex; ~**$1.3M** funding cited (verify) |
| Qualitative | Newton Howard CEO; Nurosene 2021 partnership |
| RI round | Strategic / large seed if clean FTO |

**Comparable paths:** Paradromics IDE path; Blackrock Utah Array commercial.

**Benchmark ladder:** USPTO harvest (6 mo) → FTO memo vs Brown (12 mo) → partnership or IDE path (18 mo).

**Evidence.** [ni2o](https://ni2o.com/); [Opportunity Atlas §6.4](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md#64-gap_ni2o_kiwi_bci--kiwi-wireless-micro-implant-bci).

---

## 6. RI financing context — Slater Technology Fund

### 6.1 Slater seed policy (formation equity)

| Parameter | Policy |
|-----------|--------|
| **Third-party match** | **Required** — Slater early-stage investment is not typically a standalone full seed; other qualified equity or program capital must match. |
| **Practical Slater check** | **$200K–$400K** per seed investment |
| **Total round sizing** | Slater component + match (e.g., angels, **RightHill** SPV, physician syndicate, strategic, **RI Life Science Hub** programs) |
| **Historical deals** | Press cites XM **$375K** Slater (within band); ProThera **milestone** archetype ($100K→$500K) predates current framing—use **$200–400K + match** for new term sheets |

**Example formation close (illustrative):**

| Source | Amount |
|--------|-------:|
| Slater Technology Fund | **$300K** |
| Third-party match (angels + RightHill SPV) | **$700K** |
| **Total seed** | **$1.0M** |

### 6.2 Ecosystem stack

| Layer | Role | Typical quant. |
|-------|------|----------------|
| [Clinician-Entrepreneur Network](https://ri-bio.org/clinician-entrepreneur-network/) | KOL match | Qualitative (equity + SAB) |
| [RI Commerce Innovation Voucher](https://commerceri.com/innovation-voucher/) | R&D with knowledge partner | Up to **$75K** |
| [RI Commerce Invention Incentive](https://commerceri.com/business-assistance/innovation/) | Patent filing reimbursement | Up to **$5K** |
| [Innovate RI Fund (STAC)](https://stac.ri.gov/find-funding/innovate-ri-fund/) | SBIR/STTR application + Phase I/II match | **$3K** app; **$75K** / **$150K** match |
| [RILSH Growth Catalyst](https://www.rilifescience.com/rhode-island-grow-catalyst-program) | Commercialization / scale | Up to **25%** of project |
| [RILSH RI Lift](https://www.rilifescience.com/rhode-island-lift) | Post-close non-dilutive boost | **$100K–$200K** by stage |
| [Slater Technology Fund](https://slaterfund.com/) | Seed (partial) | **$200K–$400K** + **required match** |
| [RightHill Ventures](https://righthill.vc/) | Match + SPV / Series A | Often the syndicate partner for Slater match |
| Physician angels | Match + KOL | Variable |

**Physician-led (qual.):** clinician **equity** + **KOL SAB**—gates G0–G5 in `data/ri_physician_led_financing.json` (v1.3 `ecosystem_stack`).

---

## 7. Portfolio risks & data refresh

| Risk | Quant./qual. impact | Mitigation |
|------|---------------------|------------|
| Incomplete patent harvest | **4** gaps / OncoLux at **0** annex patents | Assignee searches; PPUBS harvest |
| License chain | chitinase, BrainGate | Counsel memo before seed |
| Abandoned patents | MindImmune | Family continuation search |
| Comparable staleness | VC rounds drift | Quarterly §3 matrix refresh |

**Data artifacts:** `data/ri_patent_investment_opportunities.json`, `data/ri_patents_curated.json`, `data/ri_funding_matrix.json`, `data/ri_grants_nih.json`

```bash
python3 scripts/fetch_nih_grants.py
python3 scripts/ri_patent_harvest.py --delay 15 --max-per-query 15
```

**Document lineage**

| Document | Role |
|----------|------|
| **This memorandum (v2.2)** | Exhaustive IP landscape + comparables + crystallization profiles (**23** units) |
| [Opportunity Atlas](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md) | Registry cards |
| [Diligence Report](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md) | Grants, trials, patent annex |

---

*Venture Diligence Memorandum v2.2 — **23** opportunity units; Slater seed **$200K–$400K** with required third-party match (June 2026).*
