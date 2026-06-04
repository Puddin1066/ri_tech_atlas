/** Neutral labels for formation UI (avoids fund-specific names in chrome). */

export function formatFormationFit(fit: string | undefined): string | null {
  if (!fit) return null;
  return fit.replace(/_/g, " ");
}

/** Soften fund names and check sizes in per-asset formation notes shown in dossiers. */
export function neutralizeFormationCopy(text: string): string {
  return text
    .replace(/\bSlater Technology Fund\b/gi, "state seed programs")
    .replace(/\bSlater\b/g, "state seed")
    .replace(/\$[\d,.]+[KMB]?(?:\s*[–-]\s*\$[\d,.]+[KMB]?)?/g, "institutional seed")
    .replace(/\s+/g, " ")
    .trim();
}
