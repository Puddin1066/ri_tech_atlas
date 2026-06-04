import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CitationList } from "@/components/citation-chip";
import { TierBadge } from "@/components/tier-badge";
import { buildOpportunityCitations } from "@/lib/citations";
import type { Opportunity } from "@/lib/types";

type DossierTab =
  | "story"
  | "value"
  | "path"
  | "evidence"
  | "formation"
  | "people";

export function OpportunityCard({
  opportunity,
  persona = "investor",
  defaultTab,
}: {
  opportunity: Opportunity;
  persona?: "investor" | "expert";
  /** Overrides persona default (investor → value, expert → people). */
  defaultTab?: DossierTab;
}) {
  const citations = buildOpportunityCitations(opportunity).slice(0, 6);
  const tab =
    defaultTab ?? (persona === "expert" ? "people" : "value");
  const href = `/opportunities/${opportunity.id}?tab=${tab}${persona === "expert" ? "&persona=expert" : ""}`;

  return (
    <Card className={opportunity.is_gap ? "border-dashed" : undefined}>
      <CardHeader className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <TierBadge tier={opportunity.is_gap ? "A" : opportunity.promise_tier} />
          {opportunity.is_gap && (
            <span className="text-xs text-muted-foreground">Patent gap</span>
          )}
          <span className="font-mono text-xs text-muted-foreground">
            {opportunity.id}
          </span>
        </div>
        <CardTitle className="text-xl leading-snug">{opportunity.title}</CardTitle>
        {opportunity.headline && (
          <p className="text-sm font-medium leading-snug text-foreground">
            {opportunity.headline}
          </p>
        )}
      </CardHeader>
      <CardContent className="space-y-4">
        <p className="text-sm leading-relaxed text-muted-foreground">
          {opportunity.opportunity_hook ?? opportunity.thesis}
        </p>
        <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs text-muted-foreground">
          {opportunity.existing_entity && (
            <span>
              <span className="font-medium text-foreground">Entity:</span>{" "}
              {opportunity.company_url ? (
                <a
                  href={opportunity.company_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-primary hover:underline"
                >
                  {opportunity.display_name ?? opportunity.existing_entity}
                </a>
              ) : (
                opportunity.display_name ?? opportunity.existing_entity
              )}
            </span>
          )}
          <span>
            <span className="font-medium text-foreground">Patents:</span>{" "}
            {opportunity.patent_count || "—"}
          </span>
          <span>
            <span className="font-medium text-foreground">Stage:</span>{" "}
            {opportunity.clinical_stage.replace(/_/g, " ")}
          </span>
        </div>
        <CitationList citations={citations} empty="" />
        <Link
          href={href}
          className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline"
        >
          Open dossier
          <ArrowRight className="size-4" />
        </Link>
      </CardContent>
    </Card>
  );
}
