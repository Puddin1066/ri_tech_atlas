import Link from "next/link";
import { TierBadge } from "@/components/tier-badge";
import type { Opportunity } from "@/lib/types";

export function AssetIndex({
  opportunities,
  title = "All assets",
  description,
}: {
  opportunities: Opportunity[];
  title?: string;
  description?: string;
}) {
  return (
    <section className="rounded-lg border border-border bg-muted/20 p-4">
      <h2 className="text-sm font-semibold">{title}</h2>
      {description && (
        <p className="mt-1 text-xs text-muted-foreground">{description}</p>
      )}
      <ul className="mt-4 grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
        {opportunities.map((o) => (
          <li key={o.id}>
            <Link
              href={`/opportunities/${o.id}`}
              className="flex flex-col gap-1 rounded-md border border-border bg-background px-3 py-2 text-sm transition-colors hover:bg-muted"
            >
              <span className="font-medium leading-snug">
                {o.display_name ?? o.existing_entity ?? o.title}
              </span>
              <span className="flex flex-wrap items-center gap-2">
                <TierBadge tier={o.is_gap ? "A" : o.promise_tier} />
                {o.is_gap && (
                  <span className="text-[10px] uppercase tracking-wide text-muted-foreground">
                    Gap
                  </span>
                )}
              </span>
              <span className="font-mono text-[10px] text-muted-foreground">
                {o.id}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}
