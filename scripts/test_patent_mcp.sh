#!/usr/bin/env bash
# Smoke-test patent MCP backend (same process Cursor starts).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Launcher exists and is executable"
test -x scripts/run_uspto_patent_mcp.sh

echo "==> Running Python tool smoke test"
set -a
# shellcheck disable=SC1091
[[ -f .env ]] && source .env
set +a

uvx --python 3.12 --from patent-mcp-server python3 - <<'PY'
import asyncio, json, os, sys
from pathlib import Path

async def main():
    import patent_mcp_server.patents as pm
    status = await pm.check_api_status()
    assert status.get("success"), status
    odp = (status.get("sources") or {}).get("odp") or {}
    assert odp.get("api_key_set"), "USPTO_API_KEY not set — check .env"
    r = await pm.odp_search_applications(inventor_name="El-Deiry", limit=1)
    assert r.get("success") and (r.get("total") or 0) > 0, r
    print("OK: check_api_status + odp_search_applications")

asyncio.run(main())
PY

echo "==> .cursor/mcp.json has stdio type for uspto-patents"
grep -q '"type": "stdio"' .cursor/mcp.json
grep -q 'run_uspto_patent_mcp.sh' .cursor/mcp.json

echo ""
echo "All checks passed. In Cursor: Reload Window, then enable uspto-patents under Tools & MCP."
