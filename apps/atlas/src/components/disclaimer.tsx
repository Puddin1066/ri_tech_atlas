export function Disclaimer({ className }: { className?: string }) {
  return (
    <footer
      className={`rounded-lg border border-border bg-muted/30 px-4 py-3 text-xs leading-relaxed text-muted-foreground ${className ?? ""}`}
    >
      Research synthesis from public sources (NIH RePORTER, ClinicalTrials.gov,
      PubMed, USPTO, company press). Not investment advice, legal opinion, or
      clinical guidance. Verify cap tables, license chains, and trial status in
      data rooms before term sheets.
    </footer>
  );
}
