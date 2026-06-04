import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { OpportunityDossier } from "@/components/opportunity-dossier";
import { Disclaimer } from "@/components/disclaimer";
import {
  buildOpportunityView,
  getAllOpportunityIds,
  getAllOpportunities,
} from "@/lib/data";

export function generateStaticParams() {
  return getAllOpportunityIds().map((id) => ({ id }));
}

export default async function OpportunityPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const view = buildOpportunityView(id);
  if (!view) notFound();

  const all = getAllOpportunities();
  const idx = all.findIndex((o) => o.id === id);
  const prev = idx > 0 ? all[idx - 1] : null;
  const next = idx >= 0 && idx < all.length - 1 ? all[idx + 1] : null;

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <div className="mb-8 flex flex-wrap items-center justify-between gap-4 text-sm">
        <Link href="/explore" className="text-muted-foreground hover:text-foreground">
          ← Explore
        </Link>
        <div className="flex gap-4">
          {prev && (
            <Link
              href={`/opportunities/${prev.id}`}
              className="text-primary hover:underline"
            >
              ← {prev.id}
            </Link>
          )}
          {next && (
            <Link
              href={`/opportunities/${next.id}`}
              className="text-primary hover:underline"
            >
              {next.id} →
            </Link>
          )}
        </div>
      </div>

      <Suspense fallback={<p className="text-muted-foreground">Loading dossier…</p>}>
        <OpportunityDossier view={view} />
      </Suspense>

      <Disclaimer className="mt-16" />
    </div>
  );
}
