# RI Tech Atlas

Research and patent intelligence for Rhode Island’s technology landscape.

## Interactive opportunity atlas (Next.js + shadcn)

**[RI Life Science Opportunity Atlas](http://localhost:3000)** — exhaustive, IP-backed diligence for physician-led formation and early-stage investors: comparables matrix, **33** asset dossiers (19 `ip_*` + 14 `gap_*`) with citation chips (NIH, USPTO, PubMed, trials), Slater formation policy, and KOL directory.

```bash
cd apps/atlas && npm install && npm run dev
```

Open [http://localhost:3000](http://localhost:3000). Data loads from `data/*.json` (including `ri_comparables_matrix.json`).

**Production (BioticaBio):** [bioticabio.com/ri-life-science-atlas](https://bioticabio.com/ri-life-science-atlas) — deployed via Vercel project `ri-life-science-atlas`, proxied from the main BioticaBio site (same pattern as `/ev-atlas`).

```bash
cd apps/atlas && npm run build   # prebuild copies ../../data → apps/atlas/data
vercel --prod                    # from repo root (see vercel.json)
```

---

## Investment diligence report

Citation-backed early-stage life sciences diligence (publications, trials, **105** RI-linked patents, company map, and RI expert directory):

- **[docs/RI_VENTURE_DILIGENCE_MEMORANDUM.md](docs/RI_VENTURE_DILIGENCE_MEMORANDUM.md)** (v2.4 — **33** opportunity units: quantitative/qualitative crystallization profiles, comparables, benchmark paths)
- **[docs/RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md](docs/RI_LIFE_SCIENCE_OPPORTUNITY_ATLAS.md)** (v2.3 — **19** patent-based opportunities + **4** grant gaps; full §5/§6 cards, markets, physician-led + KOL)
- **[docs/RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md](docs/RI_LIFE_SCIENCE_INVESTMENT_DILIGENCE_REPORT.md)** (v2.5 — extended grants, trials, patent annex; §4.9 physician-led financing)

Grant data:

```bash
python3 scripts/fetch_nih_grants.py   # → data/ri_grants_nih.json
```

- Matrix: `data/ri_funding_matrix.json`
- Patent-defined opportunities: `data/ri_patent_investment_opportunities.json`
- Physician-led / Slater match: `data/ri_physician_led_financing.json` (Slater seed **$200K–$400K**, **third-party match required**; ecosystem stack includes **RI Commerce** vouchers, **Innovate RI (STAC) SBIR match**, **RILSH** Lift/Catalyst)
- Physician KOL directory (5 KOLs × 33 assets): **[docs/RI_PHYSICIAN_KOL_DIRECTORY.md](docs/RI_PHYSICIAN_KOL_DIRECTORY.md)** · `data/ri_kol_directory.json`
- Comparables matrix (venture memo §3): `data/ri_comparables_matrix.json` → `/compare` in the atlas app

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
3. **Reload Cursor** (Cmd+Shift+P → “Reload Window”, or quit and reopen).
4. **Tools & MCP** → enable **uspto-patents** (must show green).

Config in this repo (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "uspto-patents": {
      "type": "stdio",
      "command": "${workspaceFolder}/scripts/run_uspto_patent_mcp.sh"
    }
  }
}
```

The `"type": "stdio"` field is required — without it Cursor may not register the server. The launcher script sources `.env` then runs `uvx patent-mcp-server`.

Verify locally: `./scripts/test_patent_mcp.sh`. In Cursor: **Output → MCP Logs** if the server fails to start.

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
