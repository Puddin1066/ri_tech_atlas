"use client";

import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";
import { cn } from "@/lib/utils";

const NAV = [
  { href: "/", label: "Atlas" },
  { href: "/explore", label: "Explore" },
  { href: "/compare", label: "Compare" },
  { href: "/physician-led", label: "Formation" },
  { href: "/kol", label: "KOLs" },
];

export function SiteHeader() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const persona = searchParams.get("persona") === "expert" ? "expert" : "investor";

  const withPersona = (href: string) => {
    if (persona === "investor") return href;
    const sep = href.includes("?") ? "&" : "?";
    return `${href}${sep}persona=expert`;
  };

  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/80">
      <div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-4 px-6 py-4">
        <Link href={withPersona("/")} className="space-y-0.5">
          <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
            Rhode Island
          </p>
          <p className="text-lg font-semibold tracking-tight">
            Life Science Opportunity Atlas
          </p>
          <p className="text-xs text-muted-foreground">
            IP-backed formation diligence
          </p>
        </Link>

        <nav className="flex flex-wrap items-center gap-1 text-sm">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={withPersona(item.href)}
              className={cn(
                "rounded-md px-3 py-1.5 font-medium transition-colors hover:bg-muted",
                pathname === item.href && "bg-muted text-foreground"
              )}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="flex rounded-lg border border-border p-0.5 text-xs">
          <Link
            href={pathname}
            className={cn(
              "rounded-md px-2.5 py-1 font-medium transition-colors",
              persona === "investor" && "bg-primary text-primary-foreground"
            )}
          >
            Investor
          </Link>
          <Link
            href={`${pathname}?persona=expert`}
            className={cn(
              "rounded-md px-2.5 py-1 font-medium transition-colors",
              persona === "expert" && "bg-primary text-primary-foreground"
            )}
          >
            Clinical expert
          </Link>
        </div>
      </div>
    </header>
  );
}
