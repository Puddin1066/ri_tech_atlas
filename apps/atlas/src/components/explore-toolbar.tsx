"use client";

import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Badge } from "@/components/ui/badge";
import { MODALITY_FILTERS } from "@/lib/catalog-constants";

export function ExploreToolbar({ resultCount }: { resultCount: number }) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const tier = searchParams.get("tier") ?? "";
  const modality = searchParams.get("modality") ?? "";
  const q = searchParams.get("q") ?? "";

  const buildHref = (patch: Record<string, string | null>) => {
    const params = new URLSearchParams(searchParams.toString());
    for (const [key, value] of Object.entries(patch)) {
      if (value == null || value === "") params.delete(key);
      else params.set(key, value);
    }
    const qs = params.toString();
    return qs ? `/explore?${qs}` : "/explore";
  };

  return (
    <div className="space-y-4">
      <form
        className="flex flex-col gap-2 sm:flex-row sm:items-center"
        onSubmit={(e) => {
          e.preventDefault();
          const fd = new FormData(e.currentTarget);
          const next = String(fd.get("q") ?? "").trim();
          router.push(buildHref({ q: next || null }));
        }}
      >
        <input
          name="q"
          type="search"
          defaultValue={q}
          placeholder="Search company, title, or id (e.g. Bolden, Pax, Nabsys)…"
          className="h-10 flex-1 rounded-md border border-input bg-background px-3 text-sm"
        />
        <button
          type="submit"
          className="rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground"
        >
          Search
        </button>
        {(q || tier || modality) && (
          <Link
            href="/explore"
            className="text-center text-sm text-muted-foreground hover:text-foreground sm:px-2"
          >
            Clear
          </Link>
        )}
      </form>

      <div className="flex flex-wrap gap-2">
        <span className="text-xs font-medium text-muted-foreground self-center">
          Tier:
        </span>
        {["A", "B", "C"].map((t) => (
          <Link key={t} href={buildHref({ tier: tier === t ? null : t })}>
            <Badge variant={tier === t ? "default" : "outline"}>{t}</Badge>
          </Link>
        ))}
        <Link href={buildHref({ tier: null })}>
          <Badge variant={!tier ? "default" : "outline"}>All</Badge>
        </Link>
      </div>

      <div className="flex flex-wrap gap-2">
        <span className="text-xs font-medium text-muted-foreground self-center">
          Modality:
        </span>
        {MODALITY_FILTERS.map((m) => (
          <Link
            key={m.id}
            href={buildHref({ modality: modality === m.id ? null : m.id })}
          >
            <Badge variant={modality === m.id ? "default" : "outline"}>
              {m.label}
            </Badge>
          </Link>
        ))}
      </div>

      <p className="text-sm text-muted-foreground">
        {resultCount} asset{resultCount === 1 ? "" : "s"}
        {q ? ` matching “${q}”` : ""}
      </p>
    </div>
  );
}
