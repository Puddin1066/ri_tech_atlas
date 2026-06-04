# RI Physician KOL Directory

**Version 1.1 · June 2026**

Five key opinion leader (KOL) candidates per **19** RI life-science opportunities (16 patent assets + 3 grant gaps), identified for **physician-led investment or advisory** roles: clinician **equity** on the cap table plus formal **KOL advisory** (SAB/CAB or [RI Clinician-Entrepreneur Network](https://ri-bio.org/clinician-entrepreneur-network/)).

Machine-readable source: [`data/ri_kol_directory.json`](../data/ri_kol_directory.json).

---

## Methodology

| Source | Use |
|--------|-----|
| **Patent inventors** | `data/ri_patent_investment_opportunities.json`, `data/ri_patents_curated.json` |
| **Publication / trial authors** | Diligence report, company press, NIH RePORTER, BrainGate/ProThera pages |
| **Company SAB / advisors** | Public team pages (MindImmune, Lenoss, EpiVax, etc.) |
| **Web search** | Affiliations, clinical programs, RI/Brown Health/VA/W&I anchors (June 2026) |

**`physician_led_fit`**

| Value | Meaning |
|-------|---------|
| **high** | MD/DO with strong RI anchor and direct asset relevance; suitable equity + SAB |
| **medium** | Relevant specialty; may be external or adjacent indication |
| **low** | Ecosystem/network value; not primary clinical KOL |
| **scientific_only** | PhD/scientific founder or inventor; pair with MD for physician-led formation |

This directory is **not** outreach or investment advice. Confirm conflicts of interest, employment, and licensure before engagement.

---

## Summary by opportunity

| ID | Entity | Top RI-anchored MD KOLs (ranks 1–3) |
|----|--------|-------------------------------------|
| `ip_iaip_neonatal` | ProThera Biologics | Lim MD PhD, Padbury MD, Stonestreet MD |
| `ip_ecm_morsels_xm` | XM Therapeutics | Sellke MD, Cunningham MD, Putman MD |
| `ip_nanopieces_rna` | NanoDe Therapeutics | Terek MD, Daniels MD, Chen PhD* |
| `ip_chitinase_ocf203` | Ocean/Elkurt newco | Elias MD, Putman MD, Shea MD |
| `ip_dendritic_ad_mindimmune` | MindImmune | Snyder PhD*, Gomez-Isla MD, Salloway MD |
| `ip_wireless_neurograins` | Brown OTL spinout | Hochberg MD PhD, Mernoff MD, Borton PhD* |
| `ip_speech_tablet_ibci` | BrainGate | Hochberg MD PhD, Mernoff MD, Salloway MD |
| `ip_spinal_isi_dbs` | Brown OTL / medtech | Fridley MD, Williamson MD, Borton PhD* |
| `ip_tregitope_immunomod` | EpiVax | De Groot MD, Ramos MD, Rosenberg MD |
| `ip_biglycan_msk` | BRF OTL newco | Stavros MD, Nie MD PhD, Fallon PhD* |
| `ip_neural_decoding_legacy` | BrainGate royalty | Hochberg MD PhD, Mernoff MD |
| `ip_osteopearl_vcf_lenoss` | Lenoss Medical | Lane MD, McGraw MD, Sichlau MD |
| `ip_af_mapping_ai` | Volta Medical | Kalifa MD PhD |
| `ip_genomics_hans` | Nabsys 2.0 | Bready MD, Kelsey MD, El-Deiry MD PhD |
| `ip_ect_ophthalmology` | Neurotech | Gupta MD |
| `ip_monaghan_deep_rna_dx` | RIH deep RNA Dx (forming) | Monaghan MD, Levy MD, Fairbrother PhD* |
| `gap_smurf2_oncology` | SMURF-Tx | El-Deiry MD PhD, Safran MD |
| `gap_soma_dtx` | SOMAScience | Li MD, Barker DO, Rusha MD |
| `gap_christensen_epigenetics` | HiTIMED / Dartmouth IP | Salas MD PhD, Kelsey MD, Christensen PhD* |

\*Scientific or PhD anchor—list MD co-KOL for physician-led cap table.

---

## Asset profiles

### `ip_iaip_neonatal` — ProThera Biologics (IAIP / neonatal sepsis)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Yow-Pin Lim | MD PhD | ProThera; Brown | high — founder-scientist |
| 2 | James F. Padbury | MD | Women & Infants; Brown | high — NICU PI, SBIR |
| 3 | Barbara S. Stonestreet | MD | W&I; Brown | high — HIE/NEC grants |
| 4 | Adam C. Levine | MD MPH | Brown EM; RIH | medium — pediatric sepsis digital |
| 5 | Stephanie C. Garbern | MD | Brown EM; RIH | medium — wearable sepsis mPI |

**Evidence:** ProThera team and NIH Fast Track/Phase II pages; inventors Hixson/Lim on IAIP patents.

---

### `ip_ecm_morsels_xm` — XM Therapeutics (ECM morsels)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Frank W. Sellke | MD | Brown Health CV Research | high — cardiac surgery, co-inventor network |
| 2 | Mark J. Cunningham | MD | Brown Health; Chief CV Surgery RIH | high |
| 3 | Rachel Putman | MD MPH | Brown Health ILD | high — if IPF indication |
| 4 | Corey E. Ventetuolo | MD MS | CALC Director | medium |
| 5 | Jeffrey R. Morgan | PhD | Brown; XM co-founder | scientific_only |

**Evidence:** Patent inventors Morgan/Sellke; Brown Health provider pages.

---

### `ip_nanopieces_rna` — NanoDe Therapeutics

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Richard Terek | MD | Lifespan Cancer; Brown Ortho | high — Nanopieces co-author |
| 2 | Alan H. Daniels | MD | Brown Ortho Spine Chief | high |
| 3 | Qian Chen | PhD | RIH/Brown; NanoDe founder | scientific_only |
| 4 | Bassel G. Diebo | MD | Brown Spine Center | medium |
| 5 | Adetokunbo Oyelese | MD PhD FAANS | Norman Prince Spine | medium |

**Evidence:** Brown news 2019 Nanopieces study; STTR R41TR002298.

---

### `ip_chitinase_ocf203` — CHIT1 / pulmonary fibrosis

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Jack A. Elias | MD | Brown Dean / Alpert | high — inventor US11717528B2 |
| 2 | Rachel Putman | MD MPH | ILD Program Director | high |
| 3 | Barry S. Shea | MD | MGH (founded RIH ILD) | high — fibrosis trials |
| 4 | Corey E. Ventetuolo | MD MS | CALC | medium |
| 5 | Caitlin Sarmanian | MD | CALC | medium |

**Evidence:** P01HL114501; ILD Collaborative RIH.

---

### `ip_dendritic_ad_mindimmune` — MindImmune Therapeutics

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Peter J. Snyder | PhD | URI; Consulting CMO | medium — not MD |
| 2 | M. Teresa Gomez-Isla | MD | MGH; MindImmune SAB | high |
| 3 | Stephen Salloway | MD MS | Butler/Brown | high — RI AD trials |
| 4 | Ole Isacson | MD | McLean; SAB | medium |
| 5 | Cynthia Lemere | PhD | Brigham; SAB | scientific_only |

**Evidence:** [mindimmune.com/about](https://www.mindimmune.com/about); Stevin Zorn patent family.

---

### `ip_wireless_neurograins` — Brown OTL spinout

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Leigh R. Hochberg | MD PhD | BrainGate; VA Providence | high |
| 2 | Stephen T. Mernoff | MD | VA Providence BrainGate | high |
| 3 | David Borton | PhD | Brown Engineering | scientific_only — inventor |
| 4 | Ziya Gokaslan | MD | Neurosurgeon-in-Chief RIH | medium |
| 5 | Theresa L. Williamson | MD | CINNR / NPSI | medium |

**Evidence:** DARPA neurograins; UH2NS095548; inventors Nurmikko/Borton/Rosenstein.

---

### `ip_speech_tablet_ibci` — BrainGate speech / tablet

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Leigh R. Hochberg | MD PhD | BrainGate PI | high — NEJM 2024 speech |
| 2 | Stephen T. Mernoff | MD | VA site | high |
| 3 | Stephen Salloway | MD MS | Butler/Brown | medium |
| 4 | John Simeral | PhD | Brown; decode co-inventor | scientific_only |
| 5 | David Brandman | MD PhD | UC Davis BrainGate | medium — external |

**Evidence:** U01DC017844; recruiting trials NCT05724173+.

---

### `ip_spinal_isi_dbs` — Intelligent Spine Interface

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | David Borton | PhD | ISI PI | scientific_only |
| 2 | Jared Fridley | MD | UT Austin (ex-RIH NPSI) | high — ISI clinical neurosurgeon |
| 3 | Theresa L. Williamson | MD | CINNR | high |
| 4 | Stephen T. Mernoff | MD | VA SCI/ALS | medium |
| 5 | Adetokunbo Oyelese | MD PhD | NPSI | medium |

**Evidence:** DARPA ISI; Nature BME 2026 SCI stimulation; NCT04302259 context.

---

### `ip_tregitope_immunomod` — EpiVax / Tregitope

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Anne S. De Groot | MD | EpiVax founder | high |
| 2 | Eleanor Ramos | MD | EpiVax Therapeutics | medium |
| 3 | Amy Rosenberg | MD | ex-FDA CDER | medium |
| 4 | Judy Lieberman | MD PhD | Harvard SAB | medium |
| 5 | Gary Steinberg | MD | EpiVax Therapeutics CMO track | medium |

**Evidence:** Tregitope patent inventors De Groot/Martin; [eva-therapeutics.com/team](https://www.eva-therapeutics.com/team).

---

### `ip_biglycan_msk` — Biglycan / DMD newco

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Justin R. Fallon | PhD | Brown; Tivorsan | scientific_only — inventor |
| 2 | Kara A. Stavros | MD | MDA Center RIH | high |
| 3 | Duyu A. Nie | MD PhD | Hasbro Pediatric Neuro | medium |
| 4 | James F. Padbury | MD | W&I | medium — RI anchor |
| 5 | Barbara S. Stonestreet | MD | W&I | medium |

**Evidence:** US8658596B2; MDA Clinical Care Center at Brown Health.

---

### `ip_neural_decoding_legacy` — BrainGate decode royalty

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Leigh R. Hochberg | MD PhD | BrainGate | high |
| 2 | Stephen T. Mernoff | MD | VA Providence | high |
| 3 | John Donoghue | PhD | Brown | scientific_only |
| 4 | Stephen Salloway | MD MS | Butler/Brown | medium |
| 5 | John Simeral | PhD | Brown/VA | scientific_only |

**Evidence:** Legacy US7212851 family; Donoghue/Hochberg inventors.

---

### `ip_osteopearl_vcf_lenoss` — Lenoss Medical (OsteoPearl)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Joseph Lane | MD | Lenoss Medical Advisors | high |
| 2 | J. Kevin McGraw | MD | Lenoss Advisors | high — IR |
| 3 | Michael Sichlau | MD | Lenoss Advisors | high — IR |
| 4 | Alan H. Daniels | MD | Brown Spine | medium — RI recruit |
| 5 | Bassel G. Diebo | MD | Brown Spine Center | medium |

**Evidence:** [lenoss.com/about-our-company](https://lenoss.com/about-our-company/) medical advisors.

---

### `ip_af_mapping_ai` — Volta Medical (VX1)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Jérôme Kalifa | MD PhD | Volta co-founder CMO; Brown/RIH EP | high |
| 2 | Corey E. Ventetuolo | MD MS | CALC | medium |
| 3 | Mark J. Cunningham | MD | CV Surgery | medium |
| 4 | Frank W. Sellke | MD | CV Research | medium |
| 5 | Kaushik Mandal | MD MS MPH | Brown CV | medium |

**Evidence:** Volta founder; Providence EP practice (growth-stage, paid KOL vs formation).

---

### `ip_genomics_hans` — Nabsys 2.0 (genomics / SV)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Barrett Bready | MD | Nabsys CEO | high — physician-founder |
| 2 | Karl T. Kelsey | MD | Brown cancer epi | medium |
| 3 | Wafik S. El-Deiry | MD PhD | Legorreta Cancer Center | medium |
| 4 | Lucas A. Salas | MD MPH PhD | Dartmouth; Brown collaborator | medium |
| 5 | Brock C. Christensen | PhD | Brown epi | scientific_only |

**Evidence:** Inventors Ling/Bready/Oliver; Brown adjunct Bready.

---

### `ip_ect_ophthalmology` — Neurotech (NT-501 ECT)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Gaurav Gupta | MD | Rhode Island Eye Institute | high — vitreoretinal |
| 2 | Peter J. McDonnell | MD | Wilmer; Neurotech board 2026 | medium — national |
| 3 | Magdalena Krzystolik | MD | Mass Eye and Ear region | medium |
| 4 | Stephen Salloway | MD MS | Butler/Brown | low |
| 5 | Barrett Bready | MD | Nabsys; RI entrepreneur | low |

**Evidence:** Neurotech corporate update 2026; Encelto/ECT program.

---

### `ip_monaghan_deep_rna_dx` — Deep RNA ICU diagnostics (RIH spinout forming)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Sean F. Monaghan | MD FACS | RIH / Brown Surgery; Monaghan Lab | high — physician-founder |
| 2 | Gerard J. Nau | PhD | Brown / RIH surgical research | scientific_only — co-inventor |
| 3 | Alger M. Fredericks | PhD | Monaghan Lab | scientific_only — RNA-seq methods |
| 4 | William G. Fairbrother | PhD | Brown; splicing/NMD | medium — SAB |
| 5 | Mitchell M. Levy | MD | Brown / RIH critical care | high — sepsis trials |

**Evidence:** US20220340972A1 family; R35GM142638; [PMID 41697057](https://pubmed.ncbi.nlm.nih.gov/41697057/); [LSA 2025](https://doi.org/10.26508/lsa.202503380).

---

### `gap_smurf2_oncology` — SMURF-Therapeutics

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Wafik S. El-Deiry | MD PhD FACP | SMURF-Tx founder; WIN | high |
| 2 | Howard P. Safran | MD | Brown Health Cancer Institute; Chief Hem/Onc | high |
| 3 | Lucas A. Salas | MD MPH PhD | Dartmouth | medium |
| 4 | Karl T. Kelsey | MD | Brown | medium |
| 5 | Stephen Salloway | MD MS | Butler/Brown | low |

**Evidence:** SMURF-Tx founded 2021; El-Deiry patent/oncology program.

---

### `gap_soma_dtx` — SOMAScience (pain digital therapeutic)

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Justin Y. Li | MD | NPSI pain medicine | high |
| 2 | Ross E. Barker | DO | NPSI pain | high |
| 3 | Laert Rusha | MD | NPSI pain | high |
| 4 | Alexios G. Carayannopoulos | DO MPH | Brown PM&R Chief | high |
| 5 | Frederike H. Petzschner | PhD | Brown Carney; SOMA PI | scientific_only |

**Evidence:** Carney SOMA project; COBRE pain pilots; Petzschner/Gunsilius grants.

---

### `gap_christensen_epigenetics` — HiTIMED / diagnostics spinout

| Rank | Name | Credentials | Affiliation | Physician-led fit |
|------|------|-------------|-------------|-------------------|
| 1 | Lucas A. Salas | MD MPH PhD | HiTIMED developer | high |
| 2 | Karl T. Kelsey | MD | Brown epi/pathology | high |
| 3 | Wafik S. El-Deiry | MD PhD | Cancer Center | medium |
| 4 | Howard Safran | MD | Lifespan oncology | medium |
| 5 | Brock C. Christensen | PhD | Brown PI R01CA253976 | scientific_only |

**Evidence:** **EP4505463A1** (HiTIMED, Dartmouth pending); Christensen–Salas–Kelsey network; [PMID 36348337](https://pubmed.ncbi.nlm.nih.gov/36348337/).

---

## Cross-links

- Physician-led gates: [`data/ri_physician_led_financing.json`](../data/ri_physician_led_financing.json)
- Opportunity registry: [`docs/RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md`](RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md)
- Venture landscape: [`docs/RI_VENTURE_DILIGENCE_MEMORANDUM.md`](RI_VENTURE_DILIGENCE_MEMORANDUM.md) §6

---

*RI Tech Atlas · Not for distribution as clinical or securities advice.*
