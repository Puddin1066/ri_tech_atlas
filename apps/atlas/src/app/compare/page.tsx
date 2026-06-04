import Link from "next/link";
import { Disclaimer } from "@/components/disclaimer";
import { comparablesData, getOpportunityById } from "@/lib/data";

export default function ComparePage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">Comparables matrix</h1>
      <p className="mt-2 max-w-2xl text-muted-foreground">
        Place each RI asset in national market and financing context. Click an asset
        ID for the full dossier; comp names link to third-party sites.
      </p>

      <div className="mt-10 overflow-x-auto rounded-lg border border-border">
        <table className="w-full min-w-[900px] text-left text-sm">
          <thead className="border-b bg-muted/50 text-xs uppercase tracking-wide text-muted-foreground">
            <tr>
              <th className="px-4 py-3 font-medium">Asset</th>
              <th className="px-4 py-3 font-medium">Market / SAM</th>
              <th className="px-4 py-3 font-medium">Comparables</th>
              <th className="px-4 py-3 font-medium">Comp financing</th>
              <th className="px-4 py-3 font-medium">RI path</th>
              <th className="px-4 py-3 font-medium">RI round</th>
            </tr>
          </thead>
          <tbody className="divide-y">
            {comparablesData.rows.map((row) => {
              const opp = getOpportunityById(row.asset_id);
              return (
                <tr key={row.asset_id} className="hover:bg-muted/30">
                  <td className="px-4 py-3 align-top">
                    <Link
                      href={`/opportunities/${row.asset_id}?tab=value`}
                      className="font-mono text-xs font-medium text-primary hover:underline"
                    >
                      {row.asset_id}
                    </Link>
                    {opp && (
                      <p className="mt-1 max-w-[180px] text-xs text-muted-foreground">
                        {opp.title}
                      </p>
                    )}
                  </td>
                  <td className="px-4 py-3 align-top text-muted-foreground">
                    <p>{row.market}</p>
                    <p className="mt-1 text-xs">{row.sam}</p>
                  </td>
                  <td className="px-4 py-3 align-top">
                    <ul className="space-y-1">
                      {row.comparables.map((c) => (
                        <li key={c.name}>
                          {c.url ? (
                            <a
                              href={c.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="font-medium text-primary hover:underline"
                            >
                              {c.name}
                            </a>
                          ) : (
                            <span className="font-medium">{c.name}</span>
                          )}
                        </li>
                      ))}
                    </ul>
                  </td>
                  <td className="px-4 py-3 align-top text-muted-foreground">
                    {row.comparable_financing}
                  </td>
                  <td className="px-4 py-3 align-top text-muted-foreground">
                    {row.ri_path}
                  </td>
                  <td className="px-4 py-3 align-top font-medium">
                    {row.ri_round}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <Disclaimer className="mt-16" />
    </div>
  );
}
