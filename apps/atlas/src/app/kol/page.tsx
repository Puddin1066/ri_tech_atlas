import Link from "next/link";
import { Disclaimer } from "@/components/disclaimer";
import { CitationChip } from "@/components/citation-chip";
import { makeCitation } from "@/lib/citations";
import { getAllOpportunityIds, kolData } from "@/lib/data";

export default function KolDirectoryPage() {
  const assetIds = getAllOpportunityIds().filter((id) => kolData.assets[id]);

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">KOL directory</h1>
      <p className="mt-2 max-w-2xl text-muted-foreground">
        Five physician and scientific KOL candidates per asset for physician-led
        equity and advisory roles. Profile links open third-party sources.
      </p>
      <p className="mt-2 text-xs text-muted-foreground">{kolData.methodology}</p>

      <div className="mt-12 space-y-16">
        {assetIds.map((assetId) => {
          const block = kolData.assets[assetId];
          return (
            <section key={assetId} id={assetId}>
              <div className="flex flex-wrap items-baseline gap-3">
                <Link
                  href={`/opportunities/${assetId}?tab=people&persona=expert`}
                  className="font-mono text-sm font-medium text-primary hover:underline"
                >
                  {assetId}
                </Link>
                <span className="text-sm text-muted-foreground">
                  {block.entity}
                </span>
              </div>
              <ul className="mt-6 space-y-6">
                {block.kols.map((k) => (
                  <li
                    key={k.rank}
                    className="rounded-lg border border-border p-4"
                  >
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="font-semibold">
                        {k.rank}. {k.name}
                      </span>
                      <span className="text-xs text-muted-foreground">
                        {k.credentials}
                      </span>
                      <span className="rounded border px-1.5 py-0.5 text-xs capitalize">
                        {k.physician_led_fit.replace(/_/g, " ")}
                      </span>
                    </div>
                    <p className="mt-1 text-sm text-muted-foreground">
                      {k.affiliation}
                    </p>
                    <p className="mt-2 text-sm">{k.role_fit}</p>
                    <div className="mt-3 flex flex-wrap gap-2">
                      {k.urls.map((u) => (
                        <CitationChip
                          key={u}
                          citation={makeCitation("url", u, "Source")}
                        />
                      ))}
                    </div>
                  </li>
                ))}
              </ul>
            </section>
          );
        })}
      </div>

      <Disclaimer className="mt-16" />
    </div>
  );
}
