import Link from "next/link";
import { OpportunityCard } from "@/components/opportunity-card";
import { Disclaimer } from "@/components/disclaimer";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  getFormationPriorityOpportunities,
  getLandscapeUpdatedAt,
  physicianLedData,
  opportunitiesData,
} from "@/lib/data";
import { formatFormationFit } from "@/lib/formation-display";

const ATLAS_PILLARS = [
  {
    title: "Patent-defined packages",
    body: "Each investable unit is a technology package anchored in curated USPTO filings—Brown, RIH, URI, or RI companies with clear assignees—not a generic list of local biotech names.",
  },
  {
    title: "Thorough diligence narrative",
    body: "Every dossier synthesizes thesis, market context, comparable financing paths, NIH and trial evidence, and license or spinout vehicles so you can judge fit without re-harvesting public databases.",
  },
  {
    title: "Physician-led formation lens",
    body: "Formation tabs score early-stage fit, clinician equity models, 18-month milestones, and KOL depth—aligned with RI Clinician-Entrepreneur Network practice and typical third-party match expectations.",
  },
] as const;

const WORKFLOW = [
  {
    title: "Start with Formation policy",
    description:
      "Review what counts as physician-led (equity plus formal KOL advisory—not trial site only), universal 18-month gates, and the RI non-dilutive stack.",
    href: "/physician-led",
    cta: "Formation policy",
  },
  {
    title: "Open a priority dossier",
    description:
      "Use the Formation tab for fit, milestones, and capital stack; Value and Evidence for comps and cited grants; People for KOL chips.",
    href: "/opportunities/ip_iaip_neonatal?tab=formation",
    cta: "Example — ProThera / IAIP",
  },
  {
    title: "Stress-test against peers",
    description:
      "Comparables matrix places each asset’s market story next to financed benchmark paths and indicative round staging.",
    href: "/compare",
    cta: "Comparables matrix",
  },
  {
    title: "Search the full atlas",
    description:
      "Explore every unit by modality, tier, or keyword when you need coverage beyond the formation priority queue.",
    href: "/explore",
    cta: "Full opportunity catalog",
  },
] as const;

export default function HomePage() {
  const formationPriority = getFormationPriorityOpportunities();
  const updated = new Date(getLandscapeUpdatedAt()).toLocaleDateString(
    undefined,
    { month: "short", day: "numeric", year: "numeric" }
  );
  const totalCount =
    opportunitiesData.summary.total_investable_units ??
    formationPriority.length;

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <section className="rounded-2xl border border-border bg-muted/30 px-8 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-muted-foreground">
          For physician-angels · clinicians · early-stage RI investors
        </p>
        <h1 className="mt-3 max-w-3xl text-4xl font-semibold tracking-tight leading-tight">
          RI Life Science Opportunity Atlas
        </h1>
        <p className="mt-2 max-w-2xl text-base font-medium text-foreground/90">
          Exhaustive, IP-backed diligence for physician-led formation
        </p>
        <p className="mt-4 max-w-2xl text-lg leading-relaxed text-muted-foreground">
          A curated map of patent-defined Rhode Island packages—not a generic
          market scan or deal room. {opportunitiesData.framing}
        </p>
        <p className="mt-4 max-w-2xl text-base leading-relaxed text-muted-foreground">
          The atlas is built for formation diligence: which packages can support
          clinician equity, which need an OTL or hospital license first, and which
          are better suited to growth equity or strategic exit. Early-stage
          investors use the same dossiers to align syndicate, angel, and state
          non-dilutive capital.
        </p>
        <p className="mt-4 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          RI seed programs typically require co-investors alongside any
          institutional lead; see Formation policy for match mechanics and
          per-asset fit—not a term sheet or offering document.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link
            href="/physician-led"
            className="inline-flex rounded-lg bg-primary px-5 py-2.5 text-sm font-medium text-primary-foreground hover:opacity-90"
          >
            Physician-led formation
          </Link>
          <Link
            href="/explore"
            className="inline-flex rounded-lg border border-border bg-background px-5 py-2.5 text-sm font-medium hover:bg-muted"
          >
            Explore atlas
          </Link>
          <Link
            href="/opportunities/ip_iaip_neonatal?tab=formation"
            className="inline-flex rounded-lg border border-border bg-background px-5 py-2.5 text-sm font-medium hover:bg-muted"
          >
            Sample Formation tab
          </Link>
        </div>
        <p className="mt-6 text-xs text-muted-foreground">
          Full atlas corpus: {totalCount} investable units (refreshed {updated}).
          Promise tiers and formation-fit labels are analytical judgments—not
          investment advice or an offer to sell securities.
        </p>
      </section>

      <section className="mt-14">
        <h2 className="text-xl font-semibold">What this atlas covers</h2>
        <p className="mt-2 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          Qualitative coverage first: why each package exists, how it could be
          financed, and whether physician-led formation is realistic.
        </p>
        <div className="mt-6 grid gap-4 md:grid-cols-3">
          {ATLAS_PILLARS.map((p) => (
            <Card key={p.title} size="sm">
              <CardHeader>
                <CardTitle className="text-base">{p.title}</CardTitle>
                <CardDescription className="leading-relaxed">
                  {p.body}
                </CardDescription>
              </CardHeader>
            </Card>
          ))}
        </div>
      </section>

      <section className="mt-16 space-y-8">
        <div>
          <h2 className="text-xl font-semibold">
            Physician-led formation priority
          </h2>
          <p className="mt-2 max-w-2xl text-sm leading-relaxed text-muted-foreground">
            Ranked for clinician-founder potential, active federal signal, and a
            credible early-stage path with third-party match—not every asset is a
            new seed formation (growth, royalty, and strategic assets are flagged
            low in Formation).
          </p>
        </div>
        <div className="space-y-10">
          {formationPriority.map((o) => {
            const pl =
              physicianLedData.slater_physician_match_by_asset[o.id];
            const fitLabel = formatFormationFit(pl?.slater_fit);
            return (
              <div key={o.id} className="space-y-2">
                {fitLabel && (
                  <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
                    Formation fit · {fitLabel}
                  </p>
                )}
                <OpportunityCard
                  opportunity={o}
                  defaultTab="formation"
                />
              </div>
            );
          })}
        </div>
        <p className="text-center text-sm text-muted-foreground">
          Per-asset formation notes and ecosystem stack —{" "}
          <Link
            href="/physician-led"
            className="font-medium text-primary hover:underline"
          >
            full formation policy
          </Link>
        </p>
      </section>

      <section className="mt-16">
        <h2 className="text-xl font-semibold">Recommended workflow</h2>
        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          {WORKFLOW.map((item) => (
            <Card key={item.href} className="transition-colors hover:bg-muted/20">
              <CardHeader>
                <CardTitle className="text-base">{item.title}</CardTitle>
                <CardDescription className="leading-relaxed">
                  {item.description}
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Link
                  href={item.href}
                  className="text-sm font-medium text-primary hover:underline"
                >
                  {item.cta} →
                </Link>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section className="mt-14 rounded-xl border border-border bg-muted/20 px-6 py-8">
        <h2 className="text-lg font-semibold">Physician-led definition</h2>
        <p className="mt-3 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          {physicianLedData.definition.physician_led}
        </p>
        <p className="mt-3 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          {physicianLedData.definition.not_physician_led}
        </p>
        <Link
          href="/kol"
          className="mt-4 inline-flex text-sm font-medium text-primary hover:underline"
        >
          KOL directory →
        </Link>
      </section>

      <Disclaimer className="mt-24" />
    </div>
  );
}
