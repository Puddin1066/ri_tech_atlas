import { ExternalLink } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import type { CitationRef } from "@/lib/types";

const KIND_STYLES: Record<string, string> = {
  patent: "border-violet-500/40 bg-violet-500/5",
  grant: "border-emerald-500/40 bg-emerald-500/5",
  trial: "border-sky-500/40 bg-sky-500/5",
  pmid: "border-amber-500/40 bg-amber-500/5",
  url: "border-border",
  darpa: "border-orange-500/40 bg-orange-500/5",
  anchor: "border-border",
};

export function CitationChip({
  citation,
  className,
}: {
  citation: CitationRef;
  className?: string;
}) {
  const style = KIND_STYLES[citation.kind] ?? KIND_STYLES.anchor;
  const external = citation.href.startsWith("http");

  return (
    <a
      href={citation.href}
      target={external ? "_blank" : undefined}
      rel={external ? "noopener noreferrer" : undefined}
      title={citation.context ?? `Open ${citation.kind}: ${citation.id}`}
      className={`inline-flex items-center gap-1 rounded-md border px-2 py-0.5 text-xs font-medium transition-colors hover:bg-muted ${style} ${className ?? ""}`}
    >
      <span className="max-w-[200px] truncate">{citation.label}</span>
      {external && <ExternalLink className="size-3 shrink-0 opacity-60" />}
    </a>
  );
}

export function CitationList({
  citations,
  empty = "No linked citations yet.",
}: {
  citations: CitationRef[];
  empty?: string;
}) {
  if (!citations.length) {
    return <p className="text-sm text-muted-foreground">{empty}</p>;
  }
  return (
    <div className="flex flex-wrap gap-2">
      {citations.map((c) => (
        <CitationChip key={`${c.kind}-${c.id}`} citation={c} />
      ))}
    </div>
  );
}
