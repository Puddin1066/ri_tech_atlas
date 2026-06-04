import { Badge } from "@/components/ui/badge";
import type { PromiseTier } from "@/lib/types";

export function TierBadge({ tier }: { tier: PromiseTier | string }) {
  const variant =
    tier === "A"
      ? "default"
      : tier === "B"
        ? "secondary"
        : "outline";
  return (
    <Badge variant={variant} className="font-mono text-xs">
      Tier {tier}
    </Badge>
  );
}
