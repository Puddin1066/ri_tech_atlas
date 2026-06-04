import type { Opportunity, PatentRecord } from "./types";

/** Placeholder or assignee labels stored during harvest — not person names. */
const PLACEHOLDER_PATTERNS = [
  /^RIH\b/i,
  /^URI\b/i,
  /program$/i,
  /\bDx$/i,
  /^Neurotech$/i,
  /^Volta$/i,
  /^MindImmune$/i,
  /^EpiVax$/i,
  /^Goldberg$/i,
  /cardiopulmonary$/i,
  /regenerative medicine$/i,
  /neurodegeneration/i,
  /CNS delivery$/i,
  /orthopedics$/i,
  /neuro-oncology$/i,
  /cardiovascular$/i,
];

const COMPANY_SINGLE_TOKENS = new Set(
  ["Neurotech", "Volta", "MindImmune", "EpiVax", "Goldberg", "Chen"].map((s) =>
    s.toLowerCase()
  )
);

export function formatInventorName(raw: string): string {
  const s = raw.trim();
  if (!s) return s;
  if (s !== s.toUpperCase() || !/\s/.test(s)) return s;
  return s
    .split(/\s+/)
    .map((w) => {
      if (w.length <= 2 && /^[A-Z]\.?$/.test(w)) return w;
      return w.charAt(0) + w.slice(1).toLowerCase();
    })
    .join(" ");
}

export function isPlaceholderInventorString(raw: string): boolean {
  const s = raw.trim();
  if (!s) return true;
  if (PLACEHOLDER_PATTERNS.some((re) => re.test(s))) return true;
  if (!s.includes(" ") && !s.includes(";") && COMPANY_SINGLE_TOKENS.has(s.toLowerCase()))
    return true;
  return false;
}

export function parseInventorString(raw: string): string[] {
  if (isPlaceholderInventorString(raw)) return [];
  return raw
    .split(/[;,]/)
    .map((p) => formatInventorName(p.trim()))
    .filter(Boolean);
}

function inventorKey(name: string): string {
  return name.toLowerCase().replace(/\s+/g, " ");
}

export function mergeInventorLists(...lists: string[][]): string[] {
  const seen = new Set<string>();
  const out: string[] = [];
  for (const list of lists) {
    for (const name of list) {
      const formatted = formatInventorName(name);
      const key = inventorKey(formatted);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      out.push(formatted);
    }
  }
  return out;
}

export function inventorsFromPatents(patents: PatentRecord[]): string[] {
  return mergeInventorLists(
    ...patents.map((p) => parseInventorString(p.inventors))
  );
}

export function resolveOpportunityInventors(
  opportunity: Opportunity,
  patents: PatentRecord[]
): string[] {
  const fromOpp = opportunity.inventors ?? [];
  const fromPatents = inventorsFromPatents(patents);
  return mergeInventorLists(fromOpp, fromPatents);
}
