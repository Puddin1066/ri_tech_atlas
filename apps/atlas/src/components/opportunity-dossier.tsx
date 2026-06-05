"use client";

import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { CitationChip, CitationList } from "@/components/citation-chip";
import { TierBadge } from "@/components/tier-badge";
import { makeCitation, parseAnchorTokens } from "@/lib/citations";
import { neutralizeFormationCopy } from "@/lib/formation-display";
import { parseInventorString } from "@/lib/inventors";
import type { OpportunityView } from "@/lib/types";

const DEFAULT_TAB_INVESTOR = "story";
const DEFAULT_TAB_EXPERT = "people";

export function OpportunityDossier({ view }: { view: OpportunityView }) {
  const searchParams = useSearchParams();
  const persona = searchParams.get("persona") === "expert" ? "expert" : "investor";
  const tabParam = searchParams.get("tab");
  const defaultTab =
    tabParam ??
    (persona === "expert" ? DEFAULT_TAB_EXPERT : DEFAULT_TAB_INVESTOR);
  const { opportunity: o, comparable: comp, physicianLed, kols, citations, patents, grants } =
    view;

  return (
    <div className="space-y-8">
      <div className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <TierBadge tier={o.is_gap ? "A" : o.promise_tier} />
          {o.is_gap && (
            <span className="rounded-md border border-dashed px-2 py-0.5 text-xs">
              {o.patent_count > 0
                ? "Grant-supported · patent-linked"
                : "Grant-supported · patent harvest pending"}
            </span>
          )}
          <span className="font-mono text-xs text-muted-foreground">{o.id}</span>
        </div>
        <h1 className="text-3xl font-semibold tracking-tight">{o.title}</h1>
        {o.headline && (
          <p className="text-lg font-medium leading-snug text-foreground">
            {o.headline}
          </p>
        )}
        {o.existing_entity && (
          <p className="text-muted-foreground">
            <span className="font-medium text-foreground">Entity:</span>{" "}
            {o.company_url ? (
              <a
                href={o.company_url}
                target="_blank"
                rel="noopener noreferrer"
                className="font-medium text-primary hover:underline"
              >
                {o.existing_entity}
              </a>
            ) : (
              o.existing_entity
            )}
          </p>
        )}
      </div>

      <Tabs defaultValue={defaultTab} className="w-full">
        <TabsList className="flex h-auto flex-wrap justify-start gap-1 bg-muted/50 p-1">
          <TabsTrigger value="story">Story</TabsTrigger>
          <TabsTrigger value="value">Value</TabsTrigger>
          <TabsTrigger value="path">Path</TabsTrigger>
          <TabsTrigger value="evidence">Evidence</TabsTrigger>
          <TabsTrigger value="formation">Formation</TabsTrigger>
          <TabsTrigger value="people">People</TabsTrigger>
        </TabsList>

        <TabsContent value="story" className="mt-6 space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="text-base">Thesis</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 text-sm leading-relaxed">
              {o.opportunity_hook && (
                <p className="font-medium text-foreground">{o.opportunity_hook}</p>
              )}
              <p>{o.thesis}</p>
              <Separator />
              <dl className="grid gap-3 sm:grid-cols-2">
                <div>
                  <dt className="text-xs font-medium text-muted-foreground">
                    Assignee
                  </dt>
                  <dd className="mt-0.5">{o.assignee}</dd>
                </div>
                <div>
                  <dt className="text-xs font-medium text-muted-foreground">
                    Vehicle
                  </dt>
                  <dd className="mt-0.5">{o.investment_vehicle.replace(/_/g, " ")}</dd>
                </div>
                <div>
                  <dt className="text-xs font-medium text-muted-foreground">
                    Inventors
                  </dt>
                  <dd className="mt-0.5">{o.inventors.join(", ") || "—"}</dd>
                </div>
                <div>
                  <dt className="text-xs font-medium text-muted-foreground">
                    Clinical stage
                  </dt>
                  <dd className="mt-0.5">{o.clinical_stage.replace(/_/g, " ")}</dd>
                </div>
              </dl>
            </CardContent>
          </Card>
          <div>
            <h3 className="mb-2 text-sm font-medium">Primary citations</h3>
            <CitationList citations={citations} />
          </div>
        </TabsContent>

        <TabsContent value="value" className="mt-6 space-y-6">
          {comp ? (
            <>
              <Card>
                <CardHeader>
                  <CardTitle className="text-base">Market context</CardTitle>
                </CardHeader>
                <CardContent className="space-y-2 text-sm">
                  <p>
                    <span className="font-medium">Market:</span> {comp.market}
                  </p>
                  <p>
                    <span className="font-medium">SAM / niche:</span> {comp.sam}
                  </p>
                  <p>
                    <span className="font-medium">RI round (indicative):</span>{" "}
                    {comp.ri_round}
                  </p>
                </CardContent>
              </Card>
              <div className="space-y-4">
                <h3 className="text-sm font-medium">Comparable companies</h3>
                {comp.comparables.map((c) => (
                  <Card key={c.name}>
                    <CardContent className="flex flex-col gap-2 pt-6 sm:flex-row sm:items-start sm:justify-between">
                      <div>
                        <p className="font-semibold">{c.name}</p>
                        <p className="mt-1 text-sm text-muted-foreground">
                          {c.financing}
                        </p>
                        <p className="mt-1 text-xs text-muted-foreground">
                          {c.path}
                        </p>
                      </div>
                      {c.url && (
                        <a
                          href={c.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="shrink-0 text-sm font-medium text-primary hover:underline"
                        >
                          Source →
                        </a>
                      )}
                    </CardContent>
                  </Card>
                ))}
              </div>
            </>
          ) : (
            <p className="text-sm text-muted-foreground">
              Comparables row not yet in matrix for this asset.
            </p>
          )}
        </TabsContent>

        <TabsContent value="path" className="mt-6">
          {comp ? (
            <Card>
              <CardContent className="space-y-4 pt-6 text-sm">
                <div>
                  <p className="text-xs font-medium uppercase text-muted-foreground">
                    Benchmark path
                  </p>
                  <p className="mt-1">{comp.benchmark_path}</p>
                </div>
                <div>
                  <p className="text-xs font-medium uppercase text-muted-foreground">
                    RI crystallized path
                  </p>
                  <p className="mt-1">{comp.ri_path}</p>
                </div>
                <div>
                  <p className="text-xs font-medium uppercase text-muted-foreground">
                    Comparable financing
                  </p>
                  <p className="mt-1">{comp.comparable_financing}</p>
                </div>
              </CardContent>
            </Card>
          ) : (
            <p className="text-sm text-muted-foreground">No path data.</p>
          )}
        </TabsContent>

        <TabsContent value="evidence" className="mt-6 space-y-8">
          <section>
            <h3 className="mb-3 text-sm font-medium">Patents ({patents.length})</h3>
            {patents.length ? (
              <ul className="space-y-2">
                {patents.map((p) => (
                  <li
                    key={p.patent_number}
                    className="flex flex-wrap items-start gap-2 text-sm"
                  >
                    <CitationChip
                      citation={makeCitation("patent", p.patent_number, p.patent_number)}
                    />
                    <span className="text-muted-foreground">
                      {p.title}
                      {parseInventorString(p.inventors).length > 0 && (
                        <span className="block text-xs">
                          Inventors: {parseInventorString(p.inventors).join("; ")}
                        </span>
                      )}
                    </span>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-muted-foreground">
                {o.is_gap
                  ? "Patents not yet in curated annex."
                  : "No matching records in curated patent set."}
              </p>
            )}
          </section>
          <section>
            <h3 className="mb-3 text-sm font-medium">Grants & funding</h3>
            {grants.length ? (
              <ul className="space-y-3">
                {grants.map((g, i) => (
                  <li key={`${g.id ?? g.title}-${i}`} className="text-sm">
                    <div className="flex flex-wrap items-center gap-2">
                      {g.id && (
                        <CitationChip
                          citation={makeCitation("grant", g.id, g.id)}
                        />
                      )}
                      <a
                        href={g.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-medium hover:underline"
                      >
                        {g.title}
                      </a>
                    </div>
                    <p className="mt-1 text-xs text-muted-foreground">
                      {g.agency} · {g.recipient}
                      {g.amount_usd != null &&
                        ` · $${g.amount_usd.toLocaleString()}`}
                    </p>
                  </li>
                ))}
              </ul>
            ) : (
              <CitationList citations={citations.filter((c) => c.kind !== "patent")} />
            )}
          </section>
        </TabsContent>

        <TabsContent value="formation" className="mt-6 space-y-6">
          {physicianLed ? (
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Physician-led formation</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4 text-sm leading-relaxed">
                <p>{neutralizeFormationCopy(physicianLed.physician_equity_model)}</p>
                {physicianLed.slater_fit && (
                  <p>
                    <span className="font-medium">Formation fit:</span>{" "}
                    {physicianLed.slater_fit.replace(/_/g, " ")}
                  </p>
                )}
                <div>
                  <p className="font-medium">18-month milestones</p>
                  <ul className="mt-2 list-inside list-disc space-y-1 text-muted-foreground">
                    {physicianLed.milestones_18mo.map((m) => (
                      <li key={m}>{neutralizeFormationCopy(m)}</li>
                    ))}
                  </ul>
                </div>
                {physicianLed.capital_stack && (
                  <p>
                    <span className="font-medium">Capital stack:</span>{" "}
                    {neutralizeFormationCopy(physicianLed.capital_stack)}
                  </p>
                )}
              </CardContent>
            </Card>
          ) : (
            <p className="text-sm text-muted-foreground">
              Growth-stage or royalty path — see{" "}
              <Link href="/physician-led" className="text-primary hover:underline">
                formation policy
              </Link>
              .
            </p>
          )}
          <Link
            href="/physician-led"
            className="text-sm font-medium text-primary hover:underline"
          >
            Formation policy & match requirements →
          </Link>
        </TabsContent>

        <TabsContent value="people" className="mt-6 space-y-4">
          {kols.length ? (
            kols.map((k) => (
              <Card key={k.rank}>
                <CardContent className="space-y-2 pt-6">
                  <div className="flex flex-wrap items-center gap-2">
                    <p className="font-semibold">
                      {k.rank}. {k.name}
                    </p>
                    <span className="text-xs text-muted-foreground">
                      {k.credentials}
                    </span>
                    <span className="rounded-md border px-1.5 py-0.5 text-xs capitalize">
                      {k.physician_led_fit.replace(/_/g, " ")}
                    </span>
                  </div>
                  <p className="text-sm text-muted-foreground">{k.affiliation}</p>
                  <p className="text-sm">{k.role_fit}</p>
                  {(() => {
                    const evCites = parseAnchorTokens(k.evidence);
                    return evCites.length ? (
                      <CitationList citations={evCites} />
                    ) : (
                      <p className="text-xs text-muted-foreground">{k.evidence}</p>
                    );
                  })()}
                  <div className="flex flex-wrap gap-2 pt-1">
                    {k.urls.map((u) => (
                      <CitationChip
                        key={u}
                        citation={makeCitation("url", u, "Profile")}
                      />
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))
          ) : (
            <p className="text-sm text-muted-foreground">
              No KOL records — see{" "}
              <Link href="/kol" className="text-primary hover:underline">
                KOL directory
              </Link>
              .
            </p>
          )}
        </TabsContent>
      </Tabs>
    </div>
  );
}
