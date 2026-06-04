# Rate-limited research workflow (RI Tech Atlas)

USPTO Patent Public Search (PPUBS) and some MCP endpoints throttle aggressively. This workflow keeps harvests reliable for agent and human runs.

## Principles

1. **One query per sleep window** — default **8 seconds** between PPUBS `POST /api/searches/search` calls (use **12–15s** if you still see `Too many requests`).
2. **Small page sizes** — `--max-per-query 15–20` reduces burst load and keeps context manageable.
3. **Exponential backoff** — on rate limits, wait `delay × backoff^attempt` before retry (script default backoff 1.8).
4. **Deduplicate by patent number** — the same filing may appear in assignee and inventor queries.
5. **MCP after bulk harvest** — use `uspto-patents` MCP for **claims, prosecution, assignments** on a short list of numbers from `data/ri_patents.json`, not for hundreds of searches.
6. **Amass without throttling** — BiomedCore/TrialCore searches can run in parallel; batch by **author**, **institution**, and **topic** separately.

## Commands

```bash
# Full harvest (aim for 50+ unique filings; ~3–5 min with 8s delay × 22 queries)
python3 scripts/ri_patent_harvest.py --delay 8 --max-per-query 20

# Conservative (slower, fewer 429s)
python3 scripts/ri_patent_harvest.py --delay 15 --max-per-query 12

# Custom query list
python3 scripts/ri_patent_harvest.py --queries-file scripts/ri_patent_queries.txt
```

Outputs:

- `data/ri_patents.json` — machine-readable deduped set
- `data/ri_patents.md` — table for reports

Exit code **1** if fewer than 50 unique patents (re-run with higher delay or supplement from Brown OTL / assignee exports).

## MCP sequence (when `uspto-patents` is enabled)

1. `ppubs_search_patents` — **≤3 queries per agent turn**, 10s pause between calls.
2. `ppubs_get_patent_by_number` — top 5–10 priority assets only.
3. `odp_get_application_metadata` / `odp_get_assignment` — requires `USPTO_API_KEY` in `.env`.

## Amass sequence

| Step | Tool | Example |
|------|------|---------|
| Topic | `search_amass_biomedcore_records` | `chitinase CHI3L1 pulmonary fibrosis` + `authorNames: ["Jack Elias"]` |
| Trials | `search_amass_trialcore_records` | sponsor or facility + `minStartDate` |
| Deep dive | `get_amass_biomedcore_record` | known PMID from search |

## Web search (companies)

Use for **entity resolution** (legal name, HQ, funding), not for patent counts. Cross-check company names against assignee fields in `ri_patents.json`.

## NIH / VA grants (RePORTER API)

```bash
python3 scripts/fetch_nih_grants.py --delay 0.5 --limit 25
```

Outputs `data/ri_grants_nih.json`. Curated patent–grant mapping: `data/ri_funding_matrix.json`.

- No API key required; respect ~0.5s delay between theme queries.
- VA awards often omit `award_amount` in API—use project title + agency.
- Disambiguate common names (e.g. filter **Chen Qian** with org RIH + STTR **R41TR002298**).

## Report assembly

1. Run patent harvest → `data/ri_patents.json`
2. Run grant fetch → `data/ri_grants_nih.json`
3. Amass passes for named PIs (Elias, El-Deiry, Petzschner, Chen, etc.)
4. Web search for RI company directories (BioPharmGuy, RI Life Science Hub, Ocean State Labs cohort)
5. Merge into investment memo; cite **patent number + grant ID + PMID/NCT** per theme
