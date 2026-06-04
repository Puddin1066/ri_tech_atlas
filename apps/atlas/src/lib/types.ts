export type PromiseTier = "A" | "B" | "C";

export type CitationKind =
  | "patent"
  | "grant"
  | "trial"
  | "pmid"
  | "doi"
  | "url"
  | "darpa"
  | "anchor";

export interface CitationRef {
  kind: CitationKind;
  id: string;
  label: string;
  href: string;
  context?: string;
}

export interface Opportunity {
  id: string;
  title: string;
  promise_tier: PromiseTier;
  patent_count: number;
  key_patents: string[];
  assignee: string;
  assignee_type: string;
  inventors: string[];
  investment_vehicle: string;
  existing_entity: string | null;
  grant_anchors: string[];
  clinical_stage: string;
  thesis: string;
  diligence_priority: number;
  trial_anchors?: string[];
  evidence_anchors?: string[];
  is_gap?: boolean;
  gap_note?: string;
  headline?: string;
  opportunity_hook?: string;
  company_url?: string | null;
  display_name?: string | null;
}

export interface ComparableCompany {
  name: string;
  financing: string;
  path: string;
  url: string | null;
}

export interface ComparableRow {
  asset_id: string;
  market: string;
  sam: string;
  comparables: ComparableCompany[];
  comparable_financing: string;
  benchmark_path: string;
  ri_path: string;
  ri_round: string;
}

export interface GrantRecord {
  agency: string;
  id: string | null;
  title: string;
  recipient: string;
  type: string;
  fy: number | null;
  amount_usd: number | null;
  url: string;
  note?: string;
}

export interface FundingTheme {
  id: string;
  title: string;
  patent_theme?: string;
  patent_count?: number;
  key_patents?: string[];
  lead_entities: string[];
  grants: GrantRecord[];
}

export interface PatentRecord {
  patent_number: string;
  title: string;
  assignee: string;
  inventors: string;
  theme?: string;
  asset_ids?: string[];
  science_field?: string;
  association?: "primary" | "adjacent" | "background_fto" | "none";
  application_number?: string;
  note?: string;
}

export interface KolEntry {
  rank: number;
  name: string;
  credentials: string;
  affiliation: string;
  role_fit: string;
  physician_led_fit: "high" | "medium" | "low" | "scientific_only";
  evidence: string;
  urls: string[];
}

export interface PhysicianLedAsset {
  slater_fit?: string;
  physician_equity_model: string;
  kol_advisory_targets: string[];
  milestones_18mo: string[];
  capital_stack?: string;
  precedent?: string;
}

export interface OpportunityView {
  opportunity: Opportunity;
  comparable?: ComparableRow;
  physicianLed?: PhysicianLedAsset;
  kols: KolEntry[];
  citations: CitationRef[];
  patents: PatentRecord[];
  grants: GrantRecord[];
}

export interface GapEntry {
  id: string;
  title: string;
  note: string;
  grant_anchors: string[];
  key_patents_harvested?: string[];
  existing_entity: string | null;
  company_url?: string | null;
  display_name?: string | null;
  diligence_priority?: number;
  headline?: string;
  opportunity_hook?: string;
  evidence_anchors?: string[];
  science_field?: string;
  patent_science_association?: string;
  assignee_label?: string;
  inventors?: string[];
  thesis?: string;
}
