import type { CitationKind, CitationRef, Opportunity } from "./types";

/** Resolve external URLs for diligence chips */
export function resolveHref(kind: CitationKind, id: string): string {
  const clean = id.trim();
  switch (kind) {
    case "patent": {
      const num = clean.replace(/\s/g, "");
      return `https://patents.google.com/patent/${num}`;
    }
    case "grant": {
      const g = clean.toUpperCase().replace(/[^A-Z0-9]/g, "");
      if (g.startsWith("R") || g.startsWith("U") || g.startsWith("P") || g.startsWith("I")) {
        return `https://reporter.nih.gov/search/${g}/project-details`;
      }
      return `https://reporter.nih.gov/search/${encodeURIComponent(clean)}/project-details`;
    }
    case "trial":
      return `https://clinicaltrials.gov/study/${clean.toUpperCase()}`;
    case "pmid": {
      const n = clean.replace(/^PMID/i, "").trim();
      return `https://pubmed.ncbi.nlm.nih.gov/${n}/`;
    }
    case "doi":
      return `https://doi.org/${clean}`;
    case "darpa":
      return clean.startsWith("http") ? clean : "https://www.darpa.mil/";
    case "url":
      return clean;
    default:
      return clean.startsWith("http") ? clean : "#";
  }
}

export function makeCitation(
  kind: CitationKind,
  id: string,
  label?: string,
  context?: string
): CitationRef {
  const display = label ?? id;
  return {
    kind,
    id,
    label: display,
    href: resolveHref(kind, kind === "url" ? id : id),
    context,
  };
}

function parseEvidenceAnchor(raw: string): CitationRef | null {
  const s = raw.trim();
  if (/^PMID\d+/i.test(s)) {
    const n = s.replace(/^PMID/i, "");
    return makeCitation("pmid", n, `PMID ${n}`);
  }
  if (/^NCT\d+/i.test(s)) {
    return makeCitation("trial", s.toUpperCase(), s.toUpperCase());
  }
  if (/^US[A-Z0-9]+/i.test(s) || /^WO\d/i.test(s) || /^EP\d/i.test(s)) {
    return makeCitation("patent", s, s);
  }
  const doi = s.replace(/^doi:\s*/i, "");
  if (/^10\.\d{4,}\//.test(doi)) {
    return makeCitation("doi", doi, `DOI ${doi}`);
  }
  if (s.startsWith("http")) {
    return makeCitation("url", s, "Source");
  }
  return null;
}

/** Parse semicolon/comma-separated diligence tokens (KOL evidence lines). */
export function parseAnchorTokens(raw: string): CitationRef[] {
  const seen = new Set<string>();
  const out: CitationRef[] = [];
  for (const part of raw.split(/[;,]/)) {
    const t = part.trim();
    if (!t) continue;
    const c =
      parseEvidenceAnchor(t) ??
      (/^R\d|^U\d|^P\d|^I\d/i.test(t.replace(/-/g, ""))
        ? parseGrantAnchor(t)
        : null);
    if (!c) continue;
    const key = `${c.kind}:${c.id}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(c);
  }
  return out;
}

function parseGrantAnchor(raw: string): CitationRef {
  if (raw.startsWith("http")) {
    return makeCitation("url", raw, raw.includes("brown") ? "Brown news" : "Source");
  }
  if (/DARPA/i.test(raw)) {
    const m = raw.match(/\$[\d.]+M|\d+M/i);
    return makeCitation(
      "darpa",
      "https://www.brown.edu/news/2017-07-10/neurograins",
      m ? `DARPA ${m[0]}` : "DARPA neurograins",
      raw
    );
  }
  if (/^R\d|^U\d|^P\d|^I\d/i.test(raw.replace(/-/g, ""))) {
    const id = raw.split("_")[0];
    return makeCitation("grant", id, id);
  }
  return makeCitation("anchor", raw, raw);
}

export function buildOpportunityCitations(opp: Opportunity): CitationRef[] {
  const seen = new Set<string>();
  const out: CitationRef[] = [];

  const add = (c: CitationRef | null) => {
    if (!c) return;
    const key = `${c.kind}:${c.id}`;
    if (seen.has(key)) return;
    seen.add(key);
    out.push(c);
  };

  for (const p of opp.key_patents ?? []) {
    add(makeCitation("patent", p, p));
  }
  for (const g of opp.grant_anchors ?? []) {
    add(parseGrantAnchor(g));
  }
  for (const t of opp.trial_anchors ?? []) {
    add(makeCitation("trial", t, t));
  }
  for (const e of opp.evidence_anchors ?? []) {
    add(parseEvidenceAnchor(e));
  }

  return out;
}
