# Rhode Island Life Science Opportunity Atlas — Comprehensive Report

**Audience:** Early-stage investors (Slater Technology Fund, RightHill Ventures), physician-angels, clinical experts, and OTL operators.  
**Version:** 3.0 (June 2026)  
**Scope:** All **19 patent-defined investable assets** from `data/ri_patent_investment_opportunities.json` (v2.0) plus **14 grant-supported patent gaps** (**33** total units; **105** curated filings in `data/ri_patents_curated.json`).  
**Evidence:** Amass BiomedCore / TrialCore; NIH RePORTER; public financings and press.  
**Extended diligence:** [RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md) (v2.5) — grants §8, trial landscape §10, patent annex.

**Disclaimer:** Research synthesis, not investment advice. Verify cap tables, COI, trial enrollment, and license chains in data rooms.

---

## Table of contents

1. [Executive summary](#1-executive-summary)
2. [Master registry — all patent-based opportunities](#2-master-registry--all-patent-based-opportunities)
3. [Physician-led financing & Slater match](#3-physician-led-financing--slater-match)
4. [Markets & comparables matrix](#4-markets--comparables-matrix)
5. [Patent-defined opportunities (19)](#5-patent-defined-opportunities-19)
6. [Grant-supported patent gaps (14)](#6-grant-supported-patent-gaps-14)
7. [Rhode Island experts index](#7-rhode-island-experts-index)
8. [Data files & refresh](#8-data-files--refresh)

---

## 1. Executive summary

Rhode Island’s life-science investable surface clusters around **Brown / URI invention**, **Brown University Health** clinical sites, and a **Providence startup belt**. This atlas catalogs **every patent-based opportunity** in the curated registry: **19 scored assets** (promise tiers A/B/C) and **14 grant-supported gaps** (patent-linked or harvest-pending), including Ocean State Labs / RIH / URI cohort themes.

**IP-first framing.** University/hospital assignees (OTL/BRF/RIH license) and **company assignees** (seed through commercial). **105** discrete patent filings support diligence; independent claims require targeted USPTO review.

**Physician-led (this corpus):** clinician **equity** on cap table *and* formal **KOL advisory** ([RI Clinician-Entrepreneur Network](https://ri-bio.org/clinician-entrepreneur-network/)). See [§3](#3-physician-led-financing--slater-match).

**Default RI formation stack:** Academic/hospital IP → clinician match → **SBIR/STTR + [Innovate RI (STAC) match](https://stac.ri.gov/find-funding/innovate-ri-fund/)** and/or **[RI Commerce Innovation Voucher](https://commerceri.com/innovation-voucher/)** (up to $75K) → **RILSH Growth Catalyst / Lift** → **Slater seed ($200K–$400K) + third-party match** → **RightHill SPV / Series A**.

---

## 2. Master registry — all patent-based opportunities

### 2.1 Patent-defined assets (19)

| Prio | Asset ID | Title | Tier | Patents | Assignee | Vehicle | Entity | Federal / VC anchor |
|-----:|----------|-------|------|--------:|----------|---------|--------|---------------------|
| 1 | `ip_wireless_neurograins` | Wireless neurograins & cortical implants | **A** | 8 | Brown | OTL / spinout | — | DARPA ~$19M; UH2NS095548 |
| 2 | `ip_speech_tablet_ibci` | Speech & tablet iBCI | **A** | 6 | Brown | Consortium / SPV | BrainGate | U01DC017844; VA I01 |
| 3 | `ip_nanopieces_rna` | Nanopieces non-viral RNA | **A** | 4 | RIH | License / NanoDe | NanoDe | R41TR002298 |
| 4 | `ip_chitinase_ocf203` | Chitinase-1 antifibrosis | **A** | 1 | Brown→Ocean | Sublicense / newco | Ocean; Elkurt | P01HL114501 |
| 4 | `ip_ecm_morsels_xm` | Decellularized ECM morsels | **A** | 5 | Brown→XM | Seed / Series A | XM Therapeutics | BBII; Slater $375K |
| 5 | `ip_iaip_neonatal` | IAIP sepsis / NEC / LFIA | **A** | 4 | ProThera | Equity | ProThera | R44AI141283; R44NS084575 |
| 5 | `ip_osteopearl_vcf_lenoss` | Biological kyphoplasty (OsteoPearl) | **B** | 7 | Lenoss | Growth / strategic | Lenoss | Series A ~$4M |
| 5 | `ip_dendritic_ad_mindimmune` | AD dendritic-cell blockade | **A** | 3 | MindImmune | Series A co-invest | MindImmune | Series A $30M; RI Hub |
| 6 | `ip_spinal_isi_dbs` | Spinal interface & closed-loop DBS | **A** | 2 | Brown | Medtech license | — | DARPA $6.3M; NCT04302259 |
| 7 | `ip_tregitope_immunomod` | Tregitope immunomodulation | **B** | 10 | EpiVax | Platform / spinout | EpiVax | SBIR/U01 stack |
| 8 | `ip_biglycan_msk` | Biglycan MSK regeneration | **B** | 2 | BRF | OTL newco | — | Grant TBD |
| 9 | `ip_neural_decoding_legacy` | Core BMI decoding (legacy) | **B** | 5 | Brown | Royalty / FOU | BrainGate | Multi-IC |
| 10 | `ip_af_mapping_ai` | AI AF ablation (VX1) | **B** | 2 | Volta | Growth VC | Volta | ~€74M VC |
| 11 | `ip_genomics_hans` | Electronic genome mapping | **C** | 3 | Nabsys | Strategic M&A | Nabsys 2.0 | R43HG004433 |
| 12 | `ip_ect_ophthalmology` | Encapsulated cell therapy (CNTF) | **C** | 8 | Neurotech | Royalty / M&A | Neurotech | NEI historical |
| 5 | `ip_monaghan_deep_rna_dx` | Deep RNA ICU diagnostics | **A** | 4 | RIH | Hospital license / spinout | — | R35GM142638 |
| 8 | `ip_bolden_musk_neurogenesis` | MuSK ASO neurogenesis (Bolden) | **A** | 3 | Brown→Bolden | Seed equity | Bolden Therapeutics | NIA STTR; Slater pre-seed |
| 6 | `ip_pax_aav_vegf_tendon` | AAV2–VEGF tendon repair (PAX-001) | **A** | 1 | RIH→Pax | Seed equity | Pax Therapeutics | RILSH LIFT; seed ~$1.7M |
| 10 | `ip_oncolux_lumis` | LUMIS optical theranostics | **B** | 0* | OncoLux | Growth medtech | OncoLux | RILSH attraction; Mayo 2026 |

### 2.2 Grant-supported gaps (4) — patents not yet in annex

| Gap ID | Theme | Grant anchor | Entity | Patent action |
|--------|-------|--------------|--------|---------------|
| `gap_smurf2_oncology` | SMURF2–HIF1α oncology | R01CA173453 | SMURF-Therapeutics | Harvest El-Deiry assignee |
| `gap_soma_dtx` | SOMA pain / interoception DTx | P20GM103645 | SOMAScience forming | USPTO Petzschner/Gunsilius |
| `gap_christensen_epigenetics` | HiTIMED / immune epigenetics | R01CA253976; R01CA216265 | — | Dartmouth EP4505463 (pending); Brown sublicense TBD |
| `gap_ni2o_kiwi_bci` | KIWI wireless micro-implant BCI | — | ni2o Inc | Harvest ni2o/Howard; FTO vs BrainGate |

---

## 3. Physician-led financing & Slater match

**Definition:** Physician-led = **clinician equity** + **KOL advisory** (SAB/CAB or [RI Clinician-Entrepreneur Network](https://ri-bio.org/clinician-entrepreneur-network/)). Trial-site-only does not qualify.

**Slater Technology Fund (seed):** Early-stage Slater investment **requires a third-party financing match**. Practical Slater seed checks are **$200K–$400K** (Slater component only; total round = Slater + match from angels, RightHill SPV, strategic, or qualified co-investors). Machine-readable policy: `data/ri_physician_led_financing.json` → `slater_investment_policy`.

**State non-dilutive (formation bridge):** [RI Commerce Innovation Voucher](https://commerceri.com/innovation-voucher/) (up to **$75K** with Brown/RIH/university partner); [Innovate RI SBIR/STTR match](https://stac.ri.gov/find-funding/innovate-ri-fund/) (up to **$75K** Phase I / **$150K** Phase II); [RILSH Growth Catalyst](https://www.rilifescience.com/rhode-island-grow-catalyst-program) and [RI Lift](https://www.rilifescience.com/rhode-island-lift). Full stack in `data/ri_physician_led_financing.json` → `ecosystem_stack`.

**Universal 18-month gates:** G0 RI anchor → G1 physician equity → G2 KOL advisory → G3 technical PoC → G4 federal SBIR/STTR + STAC/Commerce non-dilutive + **match plan** → G5 Slater seed (with match) or RightHill/Series A.

Full per-asset milestones: `data/ri_physician_led_financing.json`. Diligence detail: report [§4.9](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#49-physician-led-financing-equity--kol-advisory--slater-match).

---

## 4. Markets & comparables matrix

| RI focus | Asset | Market (order of magnitude) | Comparables | RI benchmark path |
|----------|-------|----------------------------|-------------|-------------------|
| Immunoinformatics | `ip_tregitope_immunomod` | Vaccine/biologics de-risk spend (fragmented $B+) | AbCellera, Absci | Platform ARR → spinout |
| IPF / chitinase | `ip_chitinase_ocf203` | IPF **~$5B+** by 2030 | Pliant (caution), Boehringer | P01 → license → IND |
| ECM morsels | `ip_ecm_morsels_xm` | HF + IPF niche | Heartseed, Ventrix | BBII → Slater → Series A |
| Non-viral RNA | `ip_nanopieces_rna` | Extrahepatic delivery niche | Aera, Generation Bio | STTR → Slater → Series A |
| Speech/tablet iBCI | `ip_speech_tablet_ibci` | BCI **~$2B+** 2030 | Paradromics, Synchron | U01/VA → decode SPV |
| Wireless neurograins | `ip_wireless_neurograins` | BCI hardware subsegment | Paradromics, Blackrock | DARPA → OTL spinout |
| Spinal ISI | `ip_spinal_isi_dbs` | SCI neuromodulation | ONWARD Medical | DARPA → IDE → strategic |
| IAIP sepsis | `ip_iaip_neonatal` | Neonatal sepsis / Dx | Inotrem, MeMed | SBIR → Series A |
| AF SaMD | `ip_af_mapping_ai` | AF ablation volume | Volta (local), Acutus | FDA SaMD → Series B |
| Genomics | `ip_genomics_hans` | SV tools ~$30M rev peer | Bionano, Hitachi/Nabsys | SBIR → strategic |
| ECT ophthalmology | `ip_ect_ophthalmology` | Retinal therapy | Neurotech ENCELTO | Phase 3 → J-code |
| Biglycan MSK | `ip_biglycan_msk` | Rare neuromuscular multi-$B | Sarepta, Solid | BRF OTL → Series A |
| VCF biological | `ip_osteopearl_vcf_lenoss` | **~700K** US VCF/yr | Medtronic Kyphon | NEMIC → commercial |
| AD neuroinflammation | `ip_dendritic_ad_mindimmune` | AD **~$8B+** | Alector, anti-amyloid | $30M A → Phase 1 |
| SMURF2 (gap) | `gap_smurf2_oncology` | HIF pathway (Welireg commercial) | Merck Welireg | R01 → SMURF-Tx |
| SOMA (gap) | `gap_soma_dtx` | Pain DTx **~$15–24B** 2033 | Kaia, AppliedVR | COBRE → SaMD |
| Epigenetics (gap) | `gap_christensen_epigenetics` | IO biomarker niche | CIBERSORTx, Epicypher | R01 → OTL license |

---

## 5. Patent-defined opportunities (19)

Cards follow: **Technology → IP → Company & financing → Evidence → Market & comparables → Physician-led & Slater → Risks → Experts → Deep dive**.

---

### 5.1 `ip_wireless_neurograins` — Wireless neurograins & distributed cortical implants · Tier A · Priority 1

| | |
|--|--|
| **Assignee** | Brown University |
| **Vehicle** | Exclusive OTL license or hardware spinout |
| **Entity** | None (academic) |
| **Slater fit** | Medium — requires spinout |

**Technology.** DARPA-scale **wireless microscale sensor network** (“neurograins”) replaces tethered Utah arrays—distributed cortical sensing/stimulation nodes vs single shank.

**IP (8 filings).** US10433754B2, US11464964B2, WO2016187254A1, WO2020018571A1, US20200367749A1, US20200229704A1; inventors Nurmikko, Borton, Rosenstein, Mercier.

**Company & financing.** DARPA neurograins **~$19M**; NIH **UH2NS095548** (~$2M). No RI C-corp; OTL path to medtech or BCI hardware newco.

**Evidence.** Brown neurograins program ([Brown news 2017](https://www.brown.edu/news/2017-07-10/neurograins)).

**Market & comparables.** BCI **~$2.1B by 2030**. **Paradromics** ~$121M; **Blackrock** $200M Tether (2024). Path: **DARPA → OTL → $30–80M hardware spinout**.

**Physician-led & Slater.** Neurosurgeon **co-founder equity**; Hochberg/Borton **KOL SAB**. 18 mo: OTL term sheet; pre-IND package; DARPA/UH2 milestone; Slater **$200–400K** + third-party match (hardware may need SPV beyond Slater band).

**Risks.** FTO vs BrainGate consortium; capital intensity vs decode-only SPV; regulatory path for novel wireless implant.

**Experts.** Borton PhD; Nurmikko; Hochberg MD PhD (trial design).

**Deep dive:** Diligence [§4.2 wireless neurograins](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#wireless-neurograins-ip_wireless_neurograins), [§5.6](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#56-braingate--intracortical-bci-hochberg-borton-donoghue).

---

### 5.2 `ip_speech_tablet_ibci` — Speech decoding & multi-device tablet iBCI · Tier A · Priority 2

| | |
|--|--|
| **Assignee** | Brown University |
| **Vehicle** | Consortium license or decode SPV |
| **Entity** | BrainGate (trials) |
| **Slater fit** | Medium |

**Technology.** Cortical **speech neuroprosthesis** and **tablet control** from ventral/dorsal motor cortex—decoding algorithms licensable separate from implant hardware.

**IP (6 filings).** US12042303, US11972050, US12561001, US10448877B2, US18946156; Hochberg, Simeral, Hosman.

**Company & financing.** **U01DC017844**; VA **I01RX004820**, **I01RX002295**. Trials: **NCT05724173**, **NCT06094205**, **NCT06511934** (recruiting).

**Evidence.** [PMID 37612500](https://doi.org/10.1038/s41586-023-06377-x) (62 wpm speech); [PMID 39141853](https://doi.org/10.1056/NEJMoa2314132); [PMID 40506548](https://doi.org/10.1038/s41586-025-09127-3).

**Market & comparables.** **Synchron** ~$345M ($200M Series D 2025); **Paradromics** IDE path. Path: **U01/VA → decode SPV license**.

**Physician-led & Slater.** Hochberg-aligned **SPV physician equity**; BrainGate PIs on SAB. 18 mo: speech FOU license; U01 milestone; Slater + RightHill SPV.

**Risks.** Multi-center cost; CMS reimbursement unsettled; hardware partner dependency.

**Experts.** Hochberg MD PhD; Simeral PhD; Donoghue PhD.

**Deep dive:** [§5.6](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#56-braingate--intracortical-bci-hochberg-borton-donoghue).

---

### 5.3 `ip_nanopieces_rna` — Nanopieces non-viral RNA delivery · Tier A · Priority 3

| | |
|--|--|
| **Assignee** | Rhode Island Hospital |
| **Vehicle** | License to NanoDe or second newco |
| **Entity** | [NanoDe Therapeutics](https://nanodetherapeutics.com) |
| **Slater fit** | High |

**Technology.** **Janus nanotube / Nanopieces** non-viral RNA delivery with ECM penetration—orthogonal to LNP hepatic tropism.

**IP (4 filings).** US11701094B2, US11608340B2, US12357635B2, US20230183253A1; Chen.

**Company & financing.** STTR **R41TR002298**; COBRE **P20GM104416**; RI Life Science Hub award.

**Evidence.** STTR anchor (verify RIH OTL file for Chen).

**Market & comparables.** **Aera** $193M A+B (2023); **Generation Bio** restructuring caution. Path: **STTR → Slater → Series A**.

**Physician-led & Slater.** Ortho/NICU **PI angel**; procedural KOL SAB. 18 mo: STTR completion; in vivo biodistribution; Slater **$200–400K** + match (total seed often **$1–3M**).

**Risks.** Hospital OTL scope; indication focus beyond current NanoDe pipeline.

**Experts.** Qian Chen PhD.

**Deep dive:** [§5.5](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#55-nanode--nanopieces-non-viral-rna-qian-chen).

---

### 5.4 `ip_chitinase_ocf203` — Chitinase-1 antifibrosis (OCF-203) · Tier A · Priority 4

| | |
|--|--|
| **Assignee** | Brown → Ocean Biomedical (licensee) |
| **Vehicle** | Sublicense, newco, or asset deal |
| **Entity** | Ocean (OCEA); Elkurt Therapeutics |
| **Slater fit** | Medium (newco) |

**Technology.** **CHIT1 / CHI3L1** inhibition for pulmonary fibrosis—macrophage–fibroblast axis distinct from anti-TGF-β alone.

**IP.** **US11717528B2** (Elias, Brown origin).

**Company & financing.** NHLBI **P01HL114501** (Elias). **Mandatory:** confirm OCF-203 license chain post-2025 Ocean press.

**Evidence.** [PMID 35370755](https://doi.org/10.3389/fphar.2022.826471); [PMID 35679109](https://doi.org/10.1165/rcmb.2021-0156OC). **Do not cite** retracted [PMID 31085559](https://doi.org/10.26508/lsa.201900350) as primary efficacy.

**Market & comparables.** IPF **~$5B+** 2030; **Pliant** BEACON-IPF halt (2025 caution). Path: **P01 → license → IND**.

**Physician-led & Slater.** ILD **physician co-founder/angel**; Elias, Putman, Shea KOL SAB. 18 mo: license diligence; IND tox; CALC PI LOI; Slater **$200–400K** + third-party match.

**Risks.** Ocean public structure; Elkurt overlap; competitive IPF SoC.

**Experts.** Jack A. Elias MD; Rachel Putman MD; Barry Shea MD.

**Deep dive:** [§5.2](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#52-chitinase-inhibitors--pulmonary-fibrosis-jack-a-elias).

---

### 5.5 `ip_ecm_morsels_xm` — Decellularized ECM morsels (XM Therapeutics) · Tier A · Priority 4

| | |
|--|--|
| **Assignee** | Brown → XM Therapeutics |
| **Vehicle** | Seed / Series A equity |
| **Entity** | [XM Therapeutics](https://www.xmtherapeutics.com) |
| **Slater fit** | High (Slater $375K invested) |

**Technology.** Injectable **human ECM morsels** (~200 µm) from 3D microtissues for **HF** and **IPF** matrix remodeling.

**IP (5 filings).** US20230348859A1, WO2022140530A1, US8361781B2, US11286451B2, US12435312B2; Morgan, Ip.

**Company & financing.** Brown BBII; [Slater $375K](https://slaterfund.com/slater-invests-in-xm-therapeutics/) (press cites $750K total Slater).

**Evidence.** [PMID 39705507](https://doi.org/10.1152/ajpheart.00581.2024) (MI benefit); [PMID 40013741](https://doi.org/10.1080/03008207.2025.2469575).

**Market & comparables.** HF/IPF multi-$B; **Heartseed** ~$41M Series B (2024). Path: **Slater → $15–30M Series A** post large-animal PoP.

**Physician-led & Slater.** Recruit cardio/ILD **physician angel**; Sellke, Putman/Ventetuolo SAB. 18 mo: large-animal PoP; CMC; Series A.

**Risks.** CMC for human-cell ECM; vs chitinase mechanism overlap in IPF TAM.

**Experts.** Jeffrey R. Morgan PhD; Frank Ahmann; Frank W. Sellke MD.

**Deep dive:** [§5.13](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#513-ecm-morsels--cardiac--pulmonary-fibrosis-xm-therapeutics--jeffrey-r-morgan).

---

### 5.6 `ip_iaip_neonatal` — IAIP biologics & sepsis/NEC LFIA · Tier A · Priority 5

| | |
|--|--|
| **Assignee** | ProThera Biologics LLC |
| **Vehicle** | Equity in company |
| **Entity** | [ProThera Biologics](https://www.protherabiologics.com) |
| **Slater fit** | High archetype |

**Technology.** **Inter-α inhibitor proteins** for neonatal **sepsis, NEC, HIE**; companion **LFIA** point-of-care diagnostic.

**IP (4 filings).** US7932365B2, US9572872B2, USRE47972E1, US20070297982A1; Lim MD PhD, Hixson PhD.

**Company & financing.** **R44AI141283**, **R44NS084575** (~$2.8M track); ~$12M cumulative NIH cited in press. Slater **$100K → $500K milestone** (2008 archetype).

**Evidence.** [PMID 41674606](https://doi.org/10.64898/2026.01.30.26345077) (LFIA preprint); [PMID 31234704](https://doi.org/10.1177/0271678X19859465).

**Market & comparables.** **Inotrem** €39–58M Series B; **MeMed** >$200M. Path: **SBIR → Series A $5–10M**.

**Physician-led & Slater.** **Lim MD PhD founder equity**; Padbury, Stonestreet neonatal KOL SAB. 18 mo: LFIA NICU validation; SBIR tranche.

**Risks.** Neonatal trial heterogeneity; plasma-derived CMC.

**Experts.** Yow-Pin Lim PhD; James F. Padbury MD; Barbara S. Stonestreet MD.

**Deep dive:** [§5.7](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#57-prothera--iaip-sepsis--neonatal-inflammation).

---

### 5.7 `ip_osteopearl_vcf_lenoss` — Biological kyphoplasty (OsteoPearl) · Tier B · Priority 5

| | |
|--|--|
| **Assignee** | Lenoss Medical Inc |
| **Vehicle** | Growth equity / strategic |
| **Entity** | [Lenoss Medical](https://lenoss.com) |
| **Slater fit** | Low (growth stage) |

**Technology.** **100% cortical allograft** VBA vs PMMA cement; **Elevoss** transverse cavity creation (US10993756B2 family).

**IP (7 anchors).** US10993756B2, US10219851B1, US12029463B2, US20250099150A1, USD1106456S1, USD1106457S1; US8673010B2 (J&J-licensed lineage). **23** patents cited in press.

**Company & financing.** **~$4M Series A** (2025); NEMIC Activate; RI Commerce voucher; [Slater profile](https://slaterfund.com/lenoss-osteopearl/).

**Evidence.** Kyphoplasty context [PMID 29547939](https://doi.org/10.1093/neuros/nyy017) (EVOLVE).

**Market & comparables.** **~700K** US VCF/yr; **Medtronic Kyphon** incumbent. Path: **commercial scale-up**.

**Physician-led & Slater.** Spine **KOL SAB** + optional physician angel syndicate. 18 mo: registry study; CPT/reimbursement; 500+ procedures.

**Risks.** Reimbursement; allograft supply; surgeon workflow change.

**Experts.** Dom Messerli MBA (CEO).

**Deep dive:** [§5.14](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#514-biological-kyphoplasty--vcf-lenoss-medical--osteopearl).

---

### 5.8 `ip_dendritic_ad_mindimmune` — Alzheimer's dendritic-cell blockade (MITI-101) · Tier A · Priority 5

| | |
|--|--|
| **Assignee** | MindImmune Therapeutics Inc |
| **Vehicle** | Series A extension / co-invest |
| **Entity** | [MindImmune](https://mindimmune.com) |
| **Slater fit** | Low new seed (Series A $30M) |

**Technology.** **MITI-101** mAb blocks **CD11c+** peripheral innate cell recruitment into AD brain.

**IP (3 anchors).** US20210181185A1 (**abandoned**—verify continuations); US10124010B2; US10238654B2. Zorn, Nelson, Menniti, Campbell.

**Company & financing.** **$30M Series A** (Nov 2025); RI Life Science Hub IND grant (Jun 2025); Slater, RightHill, Pfizer Ventures in round.

**Evidence.** [PMID 38705533](https://doi.org/10.1016/j.bcp.2024.116258) (Zorn co-author).

**Market & comparables.** AD **~$8B+**; **Alector** innate immunity CNS. Path: **Phase 1 FIH**.

**Physician-led & Slater.** Memory-clinic **physician angel**; neurology KOL SAB. 18 mo: IND-enabling; Phase 1 biomarker protocol.

**Risks.** Abandoned method patent; anti-amyloid efficacy bar; CD11c target safety.

**Experts.** Stevin Zorn PhD; Robert Nelson PhD; URI Ryan Institute.

**Deep dive:** [§5.15](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#515-alzheimers-neuroinflammation-mindimmune--stevin-zorn).

---

### 5.9 `ip_spinal_isi_dbs` — Intelligent spinal interface & closed-loop DBS · Tier A · Priority 6

| | |
|--|--|
| **Assignee** | Brown University |
| **Vehicle** | Medtech license / SPV |
| **Entity** | — |
| **Slater fit** | Medium |

**Technology.** **Intelligent spinal interface** for SCI rehabilitation; closed-loop DBS facilitation (WO2019027517A1).

**IP.** WO2019027517A1, US20170042713A1; Borton, Eskandar, Widge.

**Company & financing.** DARPA ISI **$6.3M**; **NCT04302259** IDE at RIH.

**Market & comparables.** **ONWARD Medical** €50M (2024); ARC-EX cleared. Path: **IDE → strategic license**.

**Physician-led & Slater.** PM&R/neurosurgery **co-founder**; SCI rehab KOL. 18 mo: IDE enrollment; strategic LOI.

**Risks.** Distinct from cortical BCI capital needs; device regulatory path.

**Experts.** David Borton PhD; RIH SCI rehab.

**Deep dive:** [§4.2 spinal ISI](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#intelligent-spinal-interface-ip_spinal_isi_dbs), [§5.6](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#56-braingate--intracortical-bci-hochberg-borton-donoghue).

---

### 5.10 `ip_tregitope_immunomod` — Tregitope immunomodulation (EpiVax) · Tier B · Priority 7

| | |
|--|--|
| **Assignee** | EpiVax Inc |
| **Vehicle** | Platform equity / therapeutic spinout |
| **Entity** | EpiVax; EpiVax Therapeutics |
| **Slater fit** | Low (mature platform) |

**Technology.** **Tregitope** regulatory epitope removal and **iVAX** in silico immunogenicity for vaccines and biologics.

**IP (10 filings).** US7884184B2, US10213496B2, US11844826B2, US10751397B2, US10925939B2; De Groot, Martin.

**Company & financing.** **R43AI174486**, **U01FD007760**, **R01AI132205**, **R43TR002441**.

**Evidence.** [PMID 32318055](https://doi.org/10.3389/fimmu.2020.00442) (iVAX 20-year Providence platform).

**Market & comparables.** **AbCellera** platform→pipeline pivot; **Absci** $247M AZ deal. Path: **platform ARR → spinout or strategic**.

**Physician-led & Slater.** Therapeutic spinout with **oncology PI equity** if formed. 18 mo: spinout cap table if IND path.

**Risks.** Platform competition; customer concentration.

**Experts.** Anne S. De Groot MD; Leonard Moise PhD.

**Deep dive:** [§5.1](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#51-immunoinformatics--epitope-driven-vaccines-epivax).

---

### 5.11 `ip_biglycan_msk` — Biglycan musculoskeletal regeneration · Tier B · Priority 8

| | |
|--|--|
| **Assignee** | Brown University Research Foundation |
| **Vehicle** | BRF OTL → newco |
| **Entity** | None |
| **Slater fit** | High if newco |

**Technology.** **Biglycan** for neuromuscular / MSK regeneration (Fallon program).

**IP.** US8658596B2, US20110183910A1.

**Company & financing.** Grant linkage TBD—harvest RePORTER PI Fallon.

**Market & comparables.** Rare disease **multi-$B**; **Sarepta**, **Solid Biosciences** (DMD lessons). Path: **BRF OTL → Slater $200–400K + match → Series A**.

**Physician-led & Slater.** Neuromuscular **physician co-founder (5–15%)** + KOL SAB before seed.

**Risks.** No RI startup; preclinical academic stage.

**Experts.** Justin Fallon PhD (Brown).

**Deep dive:** [§4.2 biglycan](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#biglycan-regeneration-ip_biglycan_msk).

---

### 5.12 `ip_neural_decoding_legacy` — Core BMI decoding (legacy) · Tier B · Priority 9

| | |
|--|--|
| **Assignee** | Brown University |
| **Vehicle** | Royalty / field-of-use license |
| **Entity** | BrainGate; Blackrock (external) |
| **Slater fit** | Low |

**Technology.** Foundational **motor cortex decoding** and cortical interface patents (Donoghue era)—may encumber new BCI entrants.

**IP.** US7212851, US7392079, US7280870, US20200104689A1, US9851795.

**Company & financing.** Multi-IC BrainGate grants; VA I01 family.

**Market & comparables.** Same BCI comparables as §5.1–5.2. Path: **royalty stack**, not newco seed.

**Physician-led & Slater.** Hochberg BrainGate affiliate; **FOU sublicense** milestones only.

**Risks.** Encumbrance vs wireless/speech sub-families.

**Experts.** Hochberg MD PhD; Donoghue PhD.

**Deep dive:** [§5.6](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#56-braingate--intracortical-bci-hochberg-borton-donoghue).

---

### 5.13 `ip_af_mapping_ai` — AI AF ablation mapping (Volta VX1) · Tier B · Priority 10

| | |
|--|--|
| **Assignee** | Volta Medical Inc |
| **Vehicle** | Growth VC / strategic |
| **Entity** | [Volta Medical](https://www.volta-medical.us) |
| **Slater fit** | Low |

**Technology.** **VX1** AI maps dispersed EGMs during **atrial fibrillation** ablation—FDA-cleared SaMD.

**IP.** US10750967B2, US20210121118A1.

**Company & financing.** **>€90M** total; **€36M Series B** (2023); TAILORED-AF RCT.

**Market & comparables.** AF ablation **$billions** procedure volume. Path: **commercial expansion / M&A**.

**Physician-led & Slater.** EP physician **paid KOL SAB** (growth, not formation). 18 mo: RCT readout commercialization.

**Experts.** Volta clinical science; RIH EP.

**Deep dive:** [§5.11](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#511-digital-health--cardiac-ep-volta-medical).

---

### 5.14 `ip_genomics_hans` — Electronic genome mapping (Nabsys) · Tier C · Priority 11

| | |
|--|--|
| **Assignee** | Nabsys 2.0 LLC |
| **Vehicle** | Strategic M&A / royalty |
| **Entity** | [Nabsys](https://www.nabsys.com) (Hitachi majority 2024) |
| **Slater fit** | Low |

**Technology.** **OhmX** electronic genome mapping for structural variation—Brown-origin HANS hybridization IP.

**IP.** US20070190542A1, WO2007041621A2, US20140248183A1.

**Company & financing.** **R43HG004433**; Slater/Point Judith historical $4M (2009).

**Market & comparables.** **Bionano** ~$30.8M FY24 revenue. Path: **Hitachi strategic pull-through**.

**Physician-led & Slater.** Not physician-led formation.

**Experts.** Nabsys leadership.

**Deep dive:** [§5.12](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#512-genomics-nabsys).

---

### 5.15 `ip_ect_ophthalmology` — Encapsulated cell therapy (CNTF) · Tier C · Priority 12

| | |
|--|--|
| **Assignee** | Neurotech USA Inc |
| **Vehicle** | Royalty / M&A |
| **Entity** | [Neurotech Pharmaceuticals](https://www.neurotechpharmaceuticals.com) (Cumberland RI) |
| **Slater fit** | Low |

**Technology.** **ECT** delivers **CNTF** for retinal degeneration; **ENCELTO** MacTel approval 2025.

**IP (8 filings).** US12485087B2, US9149427B2, US9925219B2, US10004804B2, others in annex.

**Company & financing.** **FDA approval MacTel 2025**; **J-code J3403** (Oct 2025).

**Market & comparables.** Retinal therapy niche; Luxturna gene therapy comparison. Path: **commercial rollout**, not seed.

**Physician-led & Slater.** Retina **KOL SAB**; royalty/M&A only.

**Experts.** Neurotech medical affairs; RIH retina.

**Deep dive:** [§5.10](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#510-ophthalmology-encapsulated-biologics-neurotech).

---

### 5.16 `ip_monaghan_deep_rna_dx` — Deep RNA ICU diagnostics · Tier A · Priority 5

| | |
|--|--|
| **Assignee** | Rhode Island Hospital |
| **Vehicle** | Hospital license or physician-founder spinout |
| **Entity** | Forming (Monaghan Lab / RIH Surgery) |
| **Slater fit** | High |

**Technology.** Deep RNA-seq (**>100M reads**) from ICU blood: host immune transcriptome (DGE, alternative splicing, NMD) plus pathogen and AMR RNA from unmapped reads; PCR/ddPCR translation for rapid pathogen ID.

**IP (4 filings).** US20220340972A1, US20250034234A1, EP4599084A1, CN120344677A; Monaghan, Nau, Fredericks.

**Grants & evidence.** **R35GM142638** (NIGMS MIRA); Brown RNA Center; [PMID 41697057](https://pubmed.ncbi.nlm.nih.gov/41697057/) (Shock pathogen PCR); [LSA 2025](https://doi.org/10.26508/lsa.202503380) (NMD sepsis); [Sci Rep 2022](https://doi.org/10.1038/s41598-022-20139-1) (methods).

**Market & comparables.** **Karius**, **Day Zero**, **MeMed** — blood-based sepsis/pathogen Dx **>$100M** VC each. Path: R35 + cohort → LDT → **$3–8M** seed.

**Physician-led & Slater.** **Monaghan MD** physician-founder; Fredericks/Nau translational; Levy/Fairbrother KOL SAB. 18 mo: RIH license; sepsis LDT validation; Slater **$200–400K** + match. Orthogonal to **ProThera IAIP** (biologic) and Levine wearable sepsis ML.

**Experts.** Monaghan Lab; RIH critical care; Brown RNA Center.

**Deep dive:** Venture memo [OP-16](RI_VENTURE_DILIGENCE_MEMORANDUM.md#op-16--ip_monaghan_deep_rna_dx--deep-rna-icu-diagnostics).

---

### 5.17 `ip_bolden_musk_neurogenesis` — MuSK ASO neurogenesis (Bolden Therapeutics) · Tier A · Priority 8

| | |
|--|--|
| **Assignee** | Brown University (licensed to Bolden Therapeutics) |
| **Vehicle** | Seed equity in startup |
| **Entity** | [Bolden Therapeutics](https://www.boldentherapeutics.com/) |
| **Slater fit** | High |

**Technology.** **MuSK** Ig3 exon-skipping ASOs to promote adult hippocampal neurogenesis—distinct from BRF biglycan MSK and MindImmune AD innate-immunity path.

**IP (3 filings).** US12458657B2, US20220193114A1, WO20200214987A1; Fallon, Webb, Page.

**Company & financing.** NIA **$500K** STTR; **$1.5M** pre-seed (Jan 2024, Slater, Lifespan Vision, Resolute).

**Market & comparables.** Biogen/Ionis CNS ASO franchise; MindImmune **$30M** A. Path: OTL → in vivo PoC → **Slater $200–400K + match** → Series A.

**Physician-led & Slater.** Salloway ADRC KOL SAB; Fallon/Webb scientific founders. 18 mo: STTR milestones; neurology SAB.

**Experts.** Stephen Salloway MD MS; Justin Fallon PhD; Ashley Webb PhD.

**Deep dive:** [OP-20](RI_VENTURE_DILIGENCE_MEMORANDUM.md#op-20--ip_bolden_musk_neurogenesis--bolden-therapeutics).

---

### 5.18 `ip_pax_aav_vegf_tendon` — AAV2–VEGF tendon repair (Pax Therapeutics) · Tier A · Priority 6

| | |
|--|--|
| **Assignee** | Rhode Island Hospital (Pax licensee) |
| **Vehicle** | Seed equity |
| **Entity** | [Pax Therapeutics](https://www.paxtherapeutics.com/) |
| **Slater fit** | High |

**Technology.** Local **AAV2–VEGF** for flexor tendon repair (**PAX-001**); pre-IND complete per company.

**IP.** WO2019146830A1; Liu MD, Wu PhD.

**Company & financing.** **~$1.7M** seed (2025); **RILSH LIFT** for IND documentation; Ocean State Labs tenant.

**Market & comparables.** ~17M US tendon injuries/yr; Organogenesis soft-tissue precedent. Path: IND → hand flexor Phase 1 → **$5–15M** Series A.

**Physician-led & Slater.** **Paul Liu MD** physician-chairman; hand surgery KOL SAB. 18 mo: IND acceptance; Slater **$200–400K + match**.

**Experts.** Paul Y. Liu MD; Jin Bo Tang MD (advisor).

**Deep dive:** [OP-21](RI_VENTURE_DILIGENCE_MEMORANDUM.md#op-21--ip_pax_aav_vegf_tendon--pax-therapeutics).

---

### 5.19 `ip_oncolux_lumis` — LUMIS optical theranostics · Tier B · Priority 10

| | |
|--|--|
| **Assignee** | OncoLux Inc |
| **Vehicle** | Growth equity / strategic medtech |
| **Entity** | [OncoLux](https://oncoluxinc.com/) |
| **Slater fit** | Low (growth-stage) |

**Technology.** Multispectral fluorescence + in-situ photodynamic therapy (**LUMIS**); colorectal and robotic bronchoscopy paths.

**IP.** **0** in curated annex—harvest Kersey/OncoLux family.

**Company & financing.** RILSH **New Business Attraction** (CT→RI, 2025); **Mayo Clinic** know-how (2026 PR).

**Market & comparables.** Fluorescence-guided surgery; growth medtech strategic. Path: clinical validation → 510(k)/De Novo memo → growth round.

**Physician-led & Slater.** Surgical oncology KOL advisors (paid); not physician-founder seed.

**Experts.** Alan Kersey (CEO); thoracic/oncology adjacent KOLs.

**Deep dive:** [OP-22](RI_VENTURE_DILIGENCE_MEMORANDUM.md#op-22--ip_oncolux_lumis--oncolux).

---

## 6. Grant-supported patent gaps (4)

Patent harvest pending; included here as **investable themes** with grant signal.

---

### 6.1 `gap_smurf2_oncology` — SMURF2–HIF1α oncology · Tier A (grant-only)

**Technology.** VHL-independent **HIF1α degradation** via SMURF2 E3 ligase; synergy with CDK4/6 and HSP90 inhibitors.

**IP.** ~19 El-Deiry patents per CV—not in curated annex; harvest assignee.

**Entity.** [SMURF-Therapeutics](https://smurftherapeutics.com) (Providence, 2021).

**Grants.** **R01CA173453**; SMURF-Tx NIH submission 2024.

**Evidence.** [PMID 39697237](https://doi.org/10.3389/fonc.2024.1484515); [PMID 34611473](https://doi.org/10.18632/oncotarget.28081).

**Market & comparables.** **Welireg** commercial HIF pathway; **Inotrem** financing proxy. Path: **R01 → spinout → Slater seed**.

**Physician-led & Slater.** Medical oncologist **co-founder** + WIN KOL SAB. 18 mo: patent harvest; biomarker PoC; Slater seed.

**Experts.** Wafik S. El-Deiry MD PhD; Lifespan/WIN.

**Deep dive:** [§5.3](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#53-smurf2hif1α-oncology-wafik-s-el-deiry).

---

### 6.2 `gap_soma_dtx` — SOMA pain / interoception digital therapeutic

**Technology.** Computational **interoception** for chronic pain—consumer/research app toward FDA SaMD.

**IP.** Software/trade secret expected; USPTO Petzschner/Gunsilius.

**Entity.** SOMAScience spinout forming (Carney).

**Grants.** COBRE **P20GM103645** pilots; Carney innovation award.

**Market & comparables.** Pain DTx **~$15–24B** 2033; **Kaia** $75M Series C; **Pear** Ch.11 lesson. Path: **COBRE → spinout → SaMD**.

**Physician-led & Slater.** Psychiatry/pain **physician angel** + Petzschner/Gunsilius KOL. 18 mo: pilot data; FDA path memo.

**Experts.** Frederike Petzschner PhD; Chloe Gunsilius PhD.

**Deep dive:** [§5.4](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#54-soma-pain-interoception--computational-psychiatry-frederike-h-petzschner).

---

### 6.3 `gap_christensen_epigenetics` — HiTIMED / immune epigenetic deconvolution

**Technology.** **HiTIMED** (Hierarchical Tumor Immune Microenvironment Epigenetic Deconvolution)—tumor-type-specific DNA methylation deconvolution of **17 TME cell types** across **~20 carcinoma types**; [SalasLab/HiTIMED](https://github.com/SalasLab/HiTIMED) R package.

**IP.** **EP4505463A1** (pending, **Dartmouth College**, priority 2022-04-06)—in curated set; inventors Christensen, Salas, Zhang, Kelsey, Wiencke, Koestler. Gov’t rights cite **R01CA216265**, **P20GM104416**, DOD **W81XWH-20-1-0778**. **Brown OTL** may hold collaborator rights only—diligence **Dartmouth OTT vs Brown sublicense** before license deal. Related blood deconvolution: US prov. **63/148,695** (EPIC IDOL-Ext, Dartmouth).

**Grants.** **R01CA253976**, **R01CA216265**; **P20GM104416** (COBRE ecosystem).

**Market & comparables.** IO biomarker licensing; **CIBERSORTx** model. Path: **R01 → OTL pharma license**.

**Physician-led & Slater.** Oncology PI **diagnostics spinout equity** + Salas MD PhD KOL.

**Experts.** Brock C. Christensen PhD; Lucas A. Salas MD PhD.

**Deep dive:** [§5.8](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#58-tumor-microenvironment-epigenetics-brock-christensen).

---

### 6.4 `gap_ni2o_kiwi_bci` — KIWI wireless micro-implant BCI

**Technology.** **KIWI** wireless micro-implant BCI with AI closed-loop—Oxford/MIT-origin **Newton Howard** stack; Providence HQ (460 Rochambeau).

**IP.** **0** RI assignee filings in curated set—harvest ni2o/Howard USPTO; **FTO vs Brown BrainGate** patents required before RI institutional capital.

**Entity.** [ni2o Inc](https://ni2o.com/)

**Financing / BD.** Nurosene partnership (2021); ~**$1.3M** total funding cited in profiles (verify in data room).

**Market & comparables.** **Paradromics** (~$121M); **Blackrock Neurotech** ($200M, 2024). Path: preclinical → strategic partnership (not Slater-first).

**Physician-led & Slater.** Not physician-led formation; neurology KOL advisors if IDE path emerges.

**Experts.** Newton Howard PhD; Hochberg/Borton network for FTO diligence.

**Deep dive:** [OP-23](RI_VENTURE_DILIGENCE_MEMORANDUM.md#op-23--gap_ni2o_kiwi_bci--ni2o).

---

## 7. Rhode Island experts index

| Field | Expert | Affiliation | Assets |
|-------|--------|-------------|--------|
| Immunoinformatics | Anne S. De Groot MD | EpiVax | `ip_tregitope_immunomod` |
| Fibrosis | Jack A. Elias MD | Brown | `ip_chitinase_ocf203` |
| ILD clinical | Rachel Putman MD | Brown Health | chitinase, XM IPF |
| RNA delivery | Qian Chen PhD | RIH/Brown | `ip_nanopieces_rna` |
| iBCI | Leigh Hochberg MD PhD | BrainGate | speech, wireless, legacy |
| iBCI engineering | David Borton PhD | Brown | neurotech cluster |
| Neonatal IAIP | Yow-Pin Lim PhD | ProThera | `ip_iaip_neonatal` |
| ECM / XM | Jeffrey R. Morgan PhD | Brown/XM | `ip_ecm_morsels_xm` |
| AD neuroimmune | Stevin Zorn PhD | MindImmune | `ip_dendritic_ad_mindimmune` |
| Kyphoplasty | Dom Messerli MBA | Lenoss | `ip_osteopearl_vcf_lenoss` |
| Oncology | Wafik S. El-Deiry MD PhD | SMURF-Tx | `gap_smurf2_oncology` |
| Pain DTx | Frederike Petzschner PhD | Carney | `gap_soma_dtx` |
| Epigenetics | Brock Christensen PhD | Brown | `gap_christensen_epigenetics` |
| MSK | Justin Fallon PhD | Brown BRF | `ip_biglycan_msk` |
| ASO neurogenesis | Justin Fallon PhD; Ashley Webb PhD | Bolden | `ip_bolden_musk_neurogenesis` |
| Tendon gene therapy | Paul Y. Liu MD | Pax / RIH | `ip_pax_aav_vegf_tendon` |
| Surgical theranostics | Alan Kersey | OncoLux | `ip_oncolux_lumis` |
| BCI (non-Brown) | Newton Howard PhD | ni2o | `gap_ni2o_kiwi_bci` |
| Deep RNA Dx | Sean F. Monaghan MD | RIH | `ip_monaghan_deep_rna_dx` |
| Tech transfer | Brown OTL | Providence | all OTL assets |

Full table: diligence [§6](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md#6-rhode-island-experts-for-diligence-calls).

---

## 8. Data files & refresh

| File | Contents |
|------|----------|
| `data/ri_patent_investment_opportunities.json` | 19 patent-defined assets + metadata |
| `data/ri_physician_led_financing.json` | Physician-led definition + Slater gates per asset |
| `data/ri_patents_curated.json` | 105 patent filings |
| `data/ri_funding_matrix.json` | 23 investment themes, grants/VC |
| `data/ri_grants_nih.json` | RePORTER harvest |

**Refresh:** `python3 scripts/fetch_nih_grants.py`; `python3 scripts/ri_patent_harvest.py` after PPUBS cooldown; Amass MCP for literature/trials.

---

*Opportunity Atlas v2.3 — **23** investable units (19 patent-defined + 4 grant gaps). Full §5/§6 cards + venture IC profiles [RI_VENTURE_DILIGENCE_MEMORANDUM.md](RI_VENTURE_DILIGENCE_MEMORANDUM.md) v2.2. Extended diligence: [RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md](RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md).*
