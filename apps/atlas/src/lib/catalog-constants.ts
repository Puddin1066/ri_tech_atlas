/** Client-safe constants (no Node fs). */

export const QUICK_ACCESS_ASSET_IDS = [
  "ip_pax_aav_vegf_tendon",
  "ip_oncolux_lumis",
  "ip_dendritic_ad_mindimmune",
  "ip_ecm_morsels_xm",
  "gap_smurf2_oncology",
  "ip_bolden_musk_neurogenesis",
  "gap_ni2o_kiwi_bci",
] as const;

export const MODALITY_FILTERS: { id: string; label: string; assetIds: string[] }[] = [
  {
    id: "neuro",
    label: "Neuro / BCI",
    assetIds: [
      "ip_wireless_neurograins",
      "ip_speech_tablet_ibci",
      "ip_spinal_isi_dbs",
      "ip_neural_decoding_legacy",
      "ip_bolden_musk_neurogenesis",
      "gap_ni2o_kiwi_bci",
    ],
  },
  {
    id: "rna",
    label: "RNA / delivery",
    assetIds: ["ip_nanopieces_rna", "gap_uri_phlip_lnp", "gap_rih_bbb_nucleic_delivery"],
  },
  {
    id: "fibrosis",
    label: "Fibrosis / matrix",
    assetIds: ["ip_chitinase_ocf203", "ip_ecm_morsels_xm"],
  },
  {
    id: "neonatal",
    label: "Neonatal / sepsis",
    assetIds: [
      "ip_iaip_neonatal",
      "ip_monaghan_deep_rna_dx",
      "gap_levine_pediatric_sepsis",
    ],
  },
  {
    id: "transcriptomic_dx",
    label: "RNA transcriptomic Dx",
    assetIds: ["ip_monaghan_deep_rna_dx"],
  },
  {
    id: "oncology",
    label: "Oncology / epi",
    assetIds: [
      "gap_smurf2_oncology",
      "gap_christensen_epigenetics",
      "gap_uri_phlip_lnp",
      "gap_rih_enhancer_rna_glioma",
      "ip_tregitope_immunomod",
    ],
  },
  {
    id: "medtech",
    label: "Medtech / SaMD",
    assetIds: [
      "ip_osteopearl_vcf_lenoss",
      "ip_af_mapping_ai",
      "ip_oncolux_lumis",
      "ip_pax_aav_vegf_tendon",
      "gap_soma_dtx",
      "gap_levine_pediatric_sepsis",
      "gap_rih_salivary_ev_ad",
      "gap_rih_pahtn_dx",
      "gap_rih_bx912_pulmonary_htn",
    ],
  },
  {
    id: "ocean_state_labs",
    label: "Ocean State Labs",
    assetIds: [
      "ip_pax_aav_vegf_tendon",
      "ip_oncolux_lumis",
      "ip_dendritic_ad_mindimmune",
      "ip_ecm_morsels_xm",
      "gap_smurf2_oncology",
    ],
  },
  {
    id: "genomics",
    label: "Genomics",
    assetIds: ["ip_genomics_hans"],
  },
  {
    id: "ophthalmology",
    label: "Ophthalmology",
    assetIds: ["ip_ect_ophthalmology"],
  },
  {
    id: "msk",
    label: "MSK / ortho",
    assetIds: [
      "ip_biglycan_msk",
      "ip_osteopearl_vcf_lenoss",
      "ip_pax_aav_vegf_tendon",
      "gap_rih_motile_cell_msk",
      "gap_rih_ecm_joint_repair",
      "gap_rih_lpa_therapeutic",
    ],
  },
];
