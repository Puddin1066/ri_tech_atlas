import Link from "next/link";
import { Disclaimer } from "@/components/disclaimer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { physicianLedData } from "@/lib/data";
import { neutralizeFormationCopy } from "@/lib/formation-display";

const GATE_MILESTONE_DISPLAY: Record<string, string> = {
  G4: "Federal SBIR/STTR plus Innovate RI (STAC) match and/or RI Commerce Innovation Voucher; RILSH Growth Catalyst or Lift when eligible; documented third-party co-investor(s) for institutional seed match",
  G5: "Institutional seed close (with required match) or syndicate Series A with physician-validated clinical plan",
};

export default function PhysicianLedPage() {
  const policy = physicianLedData.slater_investment_policy;

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">
        Physician-led formation
      </h1>
      <p className="mt-2 max-w-2xl text-muted-foreground">
        Clinician equity plus formal KOL advisory—aligned with the RI
        Clinician-Entrepreneur Network and typical RI early-stage match
        requirements.
      </p>

      <Card className="mt-10">
        <CardHeader>
          <CardTitle className="text-base">Early-stage seed policy (summary)</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3 text-sm leading-relaxed text-muted-foreground">
          <p>
            RI institutional seed equity commonly requires a third-party financing
            match; the lead check is usually one component of a larger seed round,
            not the full close. Confirm current fund terms directly with the
            manager before relying on this atlas for term-sheet work.
          </p>
          <p>{neutralizeFormationCopy(policy.summary)}</p>
          <a
            href={policy.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block font-medium text-primary hover:underline"
          >
            External fund policy (official site) →
          </a>
        </CardContent>
      </Card>

      <Card className="mt-6">
        <CardHeader>
          <CardTitle className="text-base">Definition</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3 text-sm leading-relaxed text-muted-foreground">
          <p>{physicianLedData.definition.physician_led}</p>
          <p>{physicianLedData.definition.not_physician_led}</p>
        </CardContent>
      </Card>

      <h2 className="mt-12 text-lg font-semibold">18-month gates (universal)</h2>
      <ol className="mt-4 space-y-3">
        {physicianLedData.universal_gates_18mo.map((g) => (
          <li key={g.id} className="flex gap-3 text-sm">
            <span className="font-mono font-medium text-primary">{g.id}</span>
            <div>
              <p className="font-medium">{g.gate}</p>
              <p className="text-muted-foreground">
                {GATE_MILESTONE_DISPLAY[g.id] ?? g.milestone}
              </p>
            </div>
          </li>
        ))}
      </ol>

      <h2 className="mt-12 text-lg font-semibold">Ecosystem stack</h2>
      <p className="mt-2 max-w-2xl text-sm text-muted-foreground">
        Non-dilutive state programs (Commerce, STAC, Hub) often bridge federal
        SBIR/STTR to matched institutional seed.
      </p>
      <ul className="mt-4 grid gap-4 sm:grid-cols-2">
        {physicianLedData.ecosystem_stack.map((e) => (
          <li key={e.id} className="rounded-lg border p-4 text-sm">
            <a
              href={e.url}
              target="_blank"
              rel="noopener noreferrer"
              className="font-semibold text-primary hover:underline"
            >
              {e.name}
            </a>
            <p className="mt-1 text-muted-foreground">{e.role}</p>
            {e.third_party_match_required && (
              <p className="mt-1 text-xs font-medium text-foreground">
                Match may be required
              </p>
            )}
            {e.note && (
              <p className="mt-2 text-xs text-muted-foreground">
                {neutralizeFormationCopy(e.note)}
              </p>
            )}
          </li>
        ))}
      </ul>

      <h2 className="mt-12 text-lg font-semibold">Per-asset formation notes</h2>
      <ul className="mt-4 space-y-2">
        {Object.keys(physicianLedData.slater_physician_match_by_asset).map(
          (assetId) => (
            <li key={assetId}>
              <Link
                href={`/opportunities/${assetId}?tab=formation`}
                className="font-mono text-sm text-primary hover:underline"
              >
                {assetId}
              </Link>
            </li>
          )
        )}
      </ul>

      <Disclaimer className="mt-16" />
    </div>
  );
}
