import { Suspense } from "react";
import { OpportunityCard } from "@/components/opportunity-card";
import { Disclaimer } from "@/components/disclaimer";
import { ExploreToolbar } from "@/components/explore-toolbar";
import {
  filterOpportunitiesByQuery,
  getAllOpportunities,
  MODALITY_FILTERS,
} from "@/lib/data";

export default async function ExplorePage({
  searchParams,
}: {
  searchParams: Promise<{ tier?: string; modality?: string; assignee?: string; q?: string }>;
}) {
  const params = await searchParams;
  let list = getAllOpportunities();

  if (params.tier) {
    list = list.filter(
      (o) => o.is_gap || o.promise_tier === params.tier?.toUpperCase()
    );
  }
  if (params.modality) {
    const mod = MODALITY_FILTERS.find((m) => m.id === params.modality);
    if (mod) {
      list = list.filter((o) => mod.assetIds.includes(o.id));
    }
  }
  if (params.assignee === "academic") {
    list = list.filter(
      (o) =>
        o.assignee_type === "university" ||
        o.assignee_type === "hospital" ||
        o.assignee_type === "licensed_from_university" ||
        o.assignee_type === "licensed_from_hospital" ||
        o.assignee_type === "gap"
    );
  }
  if (params.q) {
    list = filterOpportunitiesByQuery(list, params.q);
  }

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">Explore opportunities</h1>
      <p className="mt-2 max-w-2xl text-muted-foreground">
        Search by company name (Bolden, Pax, OncoLux, Nabsys), asset id, or title.
        Each card links to a full dossier with cited evidence.
      </p>

      <div className="mt-8">
        <Suspense fallback={<p className="text-sm text-muted-foreground">Loading filters…</p>}>
          <ExploreToolbar resultCount={list.length} />
        </Suspense>
      </div>

      <div className="mt-6 space-y-8">
        {list.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            No assets match this filter. Try{" "}
            <a href="/explore" className="text-primary hover:underline">
              clearing filters
            </a>{" "}
            or search for &quot;Bolden&quot;, &quot;Pax&quot;, or &quot;OncoLux&quot;.
          </p>
        ) : (
          list.map((o) => <OpportunityCard key={o.id} opportunity={o} />)
        )}
      </div>

      <Disclaimer className="mt-16" />
    </div>
  );
}
