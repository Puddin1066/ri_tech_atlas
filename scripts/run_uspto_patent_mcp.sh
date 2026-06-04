#!/usr/bin/env bash
# Launcher for Cursor MCP (uspto-patents). Loads .env then execs patent-mcp-server via uvx.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

exec /opt/homebrew/bin/uvx --python 3.12 patent-mcp-server
