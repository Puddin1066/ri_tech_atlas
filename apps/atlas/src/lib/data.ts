import { existsSync, readFileSync } from "fs";
import path from "path";
import { buildOpportunityCitations } from "./citations";
import { resolveOpportunityInventors } from "./inventors";
import { MODALITY_FILTERS, QUICK_ACCESS_ASSET_IDS } from "./catalog-constants";

export { MODALITY_FILTERS, QUICK_ACCESS_ASSET_IDS };
import type {
  ComparableRow,
  FundingTheme,
  GapEntry,
  KolEntry,
  Opportunity,
  OpportunityView,
  GrantRecord,
  PatentRecord,
  PhysicianLedAsset,
} from "./types";

const DATA_DIR = path.resolve(
  process.cwd(),
  process.env.DATA_DIR ?? (existsSync(path.join(process.cwd(), "data")) ? "data" : "../../data")
);

function loadJson<T>(filename: string): T {
  const raw = readFileSync(path.join(DATA_DIR, filename), "utf-8");
  return JSON.parse(raw) as T;
}

const ASSET_TO_FUNDING_THEME: Record<string, string> = {
  ip_iaip_neonatal: "iaip_sepsis",
  ip_ecm_morsels_xm: "ecm_morsels_xm",
  ip_nanopieces_rna: "nanode_rna",
  ip_chitinase_ocf203: "chitinase_fibrosis",
  ip_dendritic_ad_mindimmune: "neuroinflammation_mindimmune",
  ip_wireless_neurograins: "neurotech_wireless",
  ip_speech_tablet_ibci: "neurotech_speech_tablet",
  ip_spinal_isi_dbs: "neurotech_spinal_dbs",
  ip_tregitope_immunomod: "immunoinformatics",
  ip_biglycan_msk: "musculoskeletal_biglycan",
  ip_neural_decoding_legacy: "neurotech_speech_tablet",
  ip_osteopearl_vcf_lenoss: "kyphoplasty_lenoss",
  ip_af_mapping_ai: "af_digital_health",
  ip_genomics_hans: "genomics_nabsys",
  ip_ect_ophthalmology: "ophthalmology_ect",
  ip_monaghan_deep_rna_dx: "monaghan_deep_rna_dx",
  ip_bolden_musk_neurogenesis: "bolden_musk_neurogenesis",
  ip_pax_aav_vegf_tendon: "pax_aav_tendon",
  ip_oncolux_lumis: "oncolux_lumis",
  gap_smurf2_oncology: "smurf2_oncology",
  gap_soma_dtx: "soma_pain_dtx",
  gap_christensen_epigenetics: "tme_epigenetics",
  gap_ni2o_kiwi_bci: "ni2o_kiwi_bci",
  gap_levine_pediatric_sepsis: "pediatric_digital_sepsis",
  gap_uri_phlip_lnp: "uri_phlip_lnp",
  gap_rih_salivary_ev_ad: "rih_salivary_ev_ad",
  gap_rih_bx912_pulmonary_htn: "rih_bx912_pulmonary_htn",
  gap_rih_pahtn_dx: "rih_pahtn_dx",
  gap_rih_bbb_nucleic_delivery: "rih_bbb_nucleic_delivery",
  gap_rih_motile_cell_msk: "rih_motile_cell_msk",
  gap_rih_ecm_joint_repair: "rih_ecm_joint_repair",
  gap_rih_enhancer_rna_glioma: "rih_enhancer_rna_glioma",
  gap_rih_lpa_therapeutic: "rih_lpa_therapeutic",
};

export const opportunitiesData = loadJson<{
  version: string;
  updated_at: string;
  framing: string;
  physician_led_definition: string;
  summary: {
    patent_defined_opportunities: number;
    academic_or_hospital_assignee_primary: number;
    company_assignee_with_univ_origin: number;
    curated_patent_filings_total: number;
    grant_supported_gaps?: number;
    total_investable_units?: number;
  };
  opportunities: Opportunity[];
  gaps_not_in_curated_patents: GapEntry[];
}>("ri_patent_investment_opportunities.json");

export const comparablesData = loadJson<{
  version: string;
  updated_at: string;
  rows: ComparableRow[];
}>("ri_comparables_matrix.json");

export const physicianLedData = loadJson<{
  version: string;
  updated_at: string;
  slater_investment_policy: {
    summary: string;
    third_party_match_required: boolean;
    practical_seed_range_usd: [number, number];
    url: string;
  };
  definition: { physician_led: string; not_physician_led: string };
  ecosystem_stack: {
    id: string;
    name: string;
    role: string;
    url: string;
    note?: string;
    typical_award_usd?: number | [number, number];
    typical_seed_range_usd?: [number, number];
    third_party_match_required?: boolean;
  }[];
  universal_gates_18mo: { id: string; gate: string; milestone: string }[];
  slater_physician_match_by_asset: Record<string, PhysicianLedAsset>;
  priority_slater_physician_match_ranked: string[];
}>("ri_physician_led_financing.json");

export const kolData = loadJson<{
  version: string;
  updated_at: string;
  methodology: string;
  assets: Record<
    string,
    { entity: string; inventors_anchors: string[]; kols: KolEntry[] }
  >;
}>("ri_kol_directory.json");

const fundingThemes = loadJson<{ investment_themes: FundingTheme[] }>(
  "ri_funding_matrix.json"
).investment_themes;
const allPatents = loadJson<{ patents: PatentRecord[] }>(
  "ri_patents_curated.json"
).patents;

const comparablesByAsset = new Map(
  comparablesData.rows.map((r) => [r.asset_id, r])
);

function sortByPriority(list: Opportunity[]): Opportunity[] {
  return [...list].sort((a, b) => a.diligence_priority - b.diligence_priority);
}

function gapToOpportunity(g: GapEntry): Opportunity {
  const harvested = g.key_patents_harvested ?? [];
  return {
    id: g.id,
    title: g.title,
    promise_tier: "A",
    patent_count: harvested.length,
    key_patents: harvested,
    assignee:
      g.assignee_label ??
      (harvested.length > 0
        ? "Patent-linked (see curated annex)"
        : "Grant-supported (patent harvest pending)"),
    assignee_type: "gap",
    investment_vehicle: "spinout_forming",
    existing_entity: g.existing_entity,
    display_name: g.display_name ?? g.existing_entity,
    company_url: g.company_url ?? null,
    grant_anchors: g.grant_anchors,
    clinical_stage: "preclinical_grant",
    thesis: g.thesis ?? g.note,
    diligence_priority: g.diligence_priority ?? 20,
    is_gap: true,
    gap_note: g.note,
    inventors: g.inventors ?? [],
    headline: g.headline,
    opportunity_hook: g.opportunity_hook,
    evidence_anchors: g.evidence_anchors,
  };
}

export function filterOpportunitiesByQuery(
  list: Opportunity[],
  query: string
): Opportunity[] {
  const q = query.trim().toLowerCase();
  if (!q) return list;
  return list.filter((o) => {
    const haystack = [
      o.id,
      o.title,
      o.existing_entity,
      o.display_name,
      o.assignee,
      ...o.inventors,
    ]
      .filter(Boolean)
      .join(" ")
      .toLowerCase();
    return haystack.includes(q);
  });
}

export function getAllOpportunityIds(): string[] {
  return [
    ...opportunitiesData.opportunities.map((o) => o.id),
    ...opportunitiesData.gaps_not_in_curated_patents.map((g) => g.id),
  ];
}

export function getOpportunities(): Opportunity[] {
  return sortByPriority(opportunitiesData.opportunities);
}

export function getGapOpportunities(): Opportunity[] {
  return sortByPriority(
    opportunitiesData.gaps_not_in_curated_patents.map(gapToOpportunity)
  );
}

export function getAllOpportunities(): Opportunity[] {
  return sortByPriority(
    [...getOpportunities(), ...getGapOpportunities()].map(withResolvedInventors)
  );
}

export function getTierAOpportunities(): Opportunity[] {
  return getOpportunities().filter((o) => o.promise_tier === "A");
}

export function getQuickAccessOpportunities(): Opportunity[] {
  const byId = new Map(getAllOpportunities().map((o) => [o.id, o]));
  return QUICK_ACCESS_ASSET_IDS.map((id) => byId.get(id)).filter(
    (o): o is Opportunity => o != null
  );
}

/** Physician-led formation priority order from ri_physician_led_financing.json */
export function getFormationPriorityOpportunities(): Opportunity[] {
  const byId = new Map(getAllOpportunities().map((o) => [o.id, o]));
  return physicianLedData.priority_slater_physician_match_ranked
    .map((id) => byId.get(id))
    .filter((o): o is Opportunity => o != null);
}

/** @deprecated Use getFormationPriorityOpportunities */
export const getSlaterPriorityOpportunities = getFormationPriorityOpportunities;

export function getOpportunityById(id: string): Opportunity | undefined {
  const core = getOpportunities().find((o) => o.id === id);
  if (core) return withResolvedInventors(core);
  const gap = opportunitiesData.gaps_not_in_curated_patents.find((g) => g.id === id);
  return gap ? withResolvedInventors(gapToOpportunity(gap)) : undefined;
}

function grantsFromAnchors(anchors: string[] | undefined): GrantRecord[] {
  if (!anchors?.length) return [];
  return anchors
    .filter((a) => /^[RUPID]\d/i.test(a.trim().replace(/-/g, "")))
    .map((raw) => {
      const id = raw.trim().split("_")[0].toUpperCase();
      const type = id.match(/^([A-Z]+\d+)/)?.[1]?.slice(0, 3) ?? "Grant";
      return {
        agency: "NIH",
        id,
        title: id,
        recipient: "See RePORTER",
        type,
        fy: null,
        amount_usd: null,
        url: `https://reporter.nih.gov/search/${encodeURIComponent(id)}/project-details`,
        note: "Linked from grant_anchors; run scripts/sync_funding_grants.py to enrich.",
      };
    });
}

function getGrantsForAsset(assetId: string, opportunity?: Opportunity): GrantRecord[] {
  const themeId = ASSET_TO_FUNDING_THEME[assetId];
  if (!themeId) return grantsFromAnchors(opportunity?.grant_anchors);
  const theme = fundingThemes.find((t) => t.id === themeId);
  const matrix = theme?.grants ?? [];
  if (matrix.length) return matrix;
  return grantsFromAnchors(opportunity?.grant_anchors);
}

function getPatentThemeForAsset(assetId: string): string | undefined {
  const fundingThemeId = ASSET_TO_FUNDING_THEME[assetId];
  if (!fundingThemeId) return undefined;
  return fundingThemes.find((t) => t.id === fundingThemeId)?.patent_theme ?? undefined;
}

function getPatentsForOpportunity(opp: Opportunity): PatentRecord[] {
  const patentTheme = getPatentThemeForAsset(opp.id);
  const themePatents = allPatents.filter(
    (p) =>
      p.asset_ids?.includes(opp.id) ||
      (patentTheme != null && p.theme === patentTheme)
  );

  if (!opp.key_patents?.length) {
    if (!opp.is_gap) return [];
    return themePatents;
  }
  const keys = new Set(opp.key_patents.map((k) => k.toUpperCase()));
  const keyed = allPatents.filter((p) => keys.has(p.patent_number.toUpperCase()));
  const merged = new Map(
    [...keyed, ...themePatents].map((p) => [p.patent_number.toUpperCase(), p])
  );
  return [...merged.values()];
}

function withResolvedInventors(opp: Opportunity): Opportunity {
  const patents = getPatentsForOpportunity(opp);
  const inventors = resolveOpportunityInventors(opp, patents);
  if (
    inventors.length === (opp.inventors?.length ?? 0) &&
    inventors.every((n, i) => n === opp.inventors?.[i])
  ) {
    return opp;
  }
  return { ...opp, inventors };
}

export function buildOpportunityView(id: string): OpportunityView | null {
  const opportunity = getOpportunityById(id);
  if (!opportunity) return null;

  const kolAsset = kolData.assets[id];

  return {
    opportunity,
    comparable: comparablesByAsset.get(id),
    physicianLed: physicianLedData.slater_physician_match_by_asset[id],
    kols: kolAsset?.kols ?? [],
    citations: buildOpportunityCitations(opportunity),
    patents: getPatentsForOpportunity(opportunity),
    grants: getGrantsForAsset(id, opportunity),
  };
}

export function getLandscapeUpdatedAt(): string {
  return opportunitiesData.updated_at;
}

