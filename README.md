# RI Tech Atlas

Research and patent intelligence for Rhode Island’s technology landscape.

## Investment diligence report

Citation-backed early-stage life sciences diligence (publications, trials, 57 RI-linked patents, company map, and RI expert directory):

**[docs/RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md](docs/RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md)** (v2.1 — 12 patent-defined investable assets, 16 grant-correlated themes, OTL/academic IP framing)

Grant data:

```bash
python3 scripts/fetch_nih_grants.py   # → data/ri_grants_nih.json
```

- Matrix: `data/ri_funding_matrix.json`
- Patent-defined opportunities: `data/ri_patent_investment_opportunities.json`

## Rate-limited patent research

PPUBS throttles aggressively (`HTTP 429`). Use the harvest script and workflow doc:

```bash
python3 scripts/ri_patent_harvest.py --delay 15 --max-per-query 15
```

- Queries: `scripts/ri_patent_queries.txt`
- Workflow: `docs/RATE_LIMITED_RESEARCH.md`
- Curated fallback (50+ RI-linked filings): `data/ri_patents_curated.json`

After a cooldown, merge live PPUBS results into reports; use MCP `ppubs_get_patent_by_number` only for top-priority assets.

---

## MCP servers

| Server | Purpose | Auth |
|--------|---------|------|
| **amass** | Publications & trials with PMID/DOI citations | Amass account (OAuth) |
| **uspto-patents** | US patents: search, claims, inventors, assignees | Optional ODP API key |

Open **Cursor → Settings → Tools & MCP** to connect or approve each server.

---

## Amass MCP (publications & citations)

Connects **[Amass](https://amass.tech)** — biomedical literature and clinical trials. Not OWASP Amass (subdomain recon).

1. Confirm **amass** appears under Tools & MCP.
2. Click **Connect** if prompted; sign in at `auth.amass.tech`.

OAuth fallback: see [`.cursor/mcp.remote.json.example`](.cursor/mcp.remote.json.example).

**Example prompts**

- *Find recent papers on marine robotics with citation counts and PMIDs.*
- *Papers from Brown University on photonics since 2022.*

---

## USPTO Patent MCP (filings, claims, parties)

Uses **[patent-mcp-server](https://github.com/riemannzeta/patent_mcp_server)** (PyPI `patent-mcp-server` v0.9.5) — the best-maintained open USPTO MCP as of 2026. Alternatives like [Patent Connector](https://patent.dev/patent-connector) are hosted/multi-office; this project uses the open server for direct USPTO access and no third-party relay.

### Why this server

- **Search & select patents:** `ppubs_search_patents`, `ppubs_search_applications` (no API key)
- **Claims & full spec:** `ppubs_get_patent_by_number`, `ppubs_get_full_document` (no API key)
- **Inventors / assignees / metadata:** `odp_get_application_metadata`, `odp_get_assignment` (needs ODP key)
- **Prosecution & family:** `odp_get_transactions`, `odp_get_continuity`, `odp_get_documents`
- **PTAB:** `ptab_search_proceedings`, etc. (needs ODP key)

PatentsView live API tools in this server are **shut down** (March 2026); use PPUBS + ODP instead.

### Setup

1. **Python 3.12** — `uvx` pins this in `.cursor/mcp.json` (3.14 breaks the package). Config uses `/opt/homebrew/bin/uvx` so Cursor finds it (GUI apps often lack Homebrew on `PATH`; if you see `spawn uvx ENOENT`, set `command` to your `which uvx` path).
2. **Optional ODP key** (recommended for assignee/inventor metadata):
   - Account at [data.uspto.gov](https://data.uspto.gov) → **My ODP** → copy API key.
   - `cp .env.example .env` and set `USPTO_API_KEY=...`
3. Reload Cursor; approve **uspto-patents** under Tools & MCP.

Config in this repo:

```json
{
  "mcpServers": {
    "uspto-patents": {
      "command": "/opt/homebrew/bin/uvx",
      "args": ["--python", "3.12", "patent-mcp-server"],
      "envFile": "${workspaceFolder}/.env"
    }
  }
}
```

### Typical workflow (agent)

1. **Find patents** — `ppubs_search_patents` with a PPUBS query.
2. **Pull claims** — `ppubs_get_patent_by_number` for the patent number from step 1.
3. **Enrich parties** — `odp_get_application_metadata` / `odp_get_assignment` (application number from search results).

### Rhode Island query examples (PPUBS)

| Goal | Query |
|------|--------|
| Assignees in RI | `RI.ASST.` |
| Inventors in RI | `RI.INST.` |
| Org + state | `"Brown University".ASNM. AND RI.ASST.` |
| Tech + RI | `(battery ADJ storage).ti. AND RI.ASST.)` |
| CPC + RI | `G06F17/00.cpc. AND RI.ASST.` |

Inventor search: `IN/"Smith".` or `(Smith NEAR2 John).in.`  
Assignee search: `AN/"company name".` or `"company".ASNM.`

### Example agent prompts

- *Search USPTO for patents assigned in Rhode Island mentioning "autonomous vessel" since 2020; list patent numbers and titles.*
- *Get independent claims for US patent 10,123,456.*
- *For application 16/123456, list inventors, assignees, and prosecution status.*

### Links

- [patent-mcp-server on GitHub](https://github.com/riemannzeta/patent_mcp_server)
- [USPTO searchable field codes](https://www.uspto.gov/patents/search/patent-public-search/searchable-indexes)
- [ODP getting started](https://data.uspto.gov/apis/getting-started)
