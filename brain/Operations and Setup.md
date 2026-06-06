---
tags: [reference, setup, operations, secrets]
aliases: [Operations and Setup, Setup, Operations]
---

# Operations and Setup

Everything needed to run Excavatortron — all free, no babysitting (see
[[Standing Constraints]]).

## Secrets (names only — never values)
Set these in **GitHub → repo → Settings → Secrets and variables → Actions**:
| Secret | Used by | Notes |
|---|---|---|
| `YOUTUBE_API_KEY` | [[Pipeline - Fetch]] | YouTube Data API v3 key. |
| `CLAUDE_CODE_OAUTH_TOKEN_REAL` | analyze / improve / review | Your **Pro/Max subscription** token (NOT paid API). Make with `claude setup-token`; renew ~yearly. |
| `EXTERNAL_REVIEW_API_KEY` | [[Three-Agent Review]] | Gemini free tier. Optional — graceful-skip if absent. |

Never print or commit secrets. Local runs read the same keys from **environment variables**.

## Turn it on
1. Add the secrets above.
2. **Enable GitHub Pages** → Settings → Pages → deploy from branch, folder **`/docs`**. The
   dashboard then serves at the Pages URL, reading `../data/*.json`.
3. The crons start running on schedule (see [[Cadence]]). To kick a stage now: Actions tab →
   pick the workflow → **Run workflow** (`workflow_dispatch`).

## Local fetch runner (residential IP, optional)
YouTube can throttle datacenter IPs. A Windows **Task Scheduler** job can fetch from home:
`git pull` → `python -m src.fetch` (needs `YOUTUBE_API_KEY` env var) → commit + push the new
`data/_pending/*` → optionally mirror `brain/` → Desktop and read the skills folder. Helpers
live in `sync/`. (Task #6 — see [[Excavatortron Brain|home]] / SESSION_HANDOFF.)

## The offline MCP server (`mcp_server/`)
`server.py` exposes dashboard operations to Claude Desktop (approve/dismiss suggestions,
star/unstar, run_improve, dismiss a dynamic tab, etc.). Configure via
`claude_desktop_config.example.json`. This is **separate** from vault access
([[Obsidian Access (MCP)]]).

## Routine checks (rare — it's meant to self-run)
- Dashboard shows a recent run + a `Self-check score` ([[Reference Self-Check]]).
- `data/status.json` timestamps advancing; `_pending/` not growing unbounded.
- Once a year: renew `CLAUDE_CODE_OAUTH_TOKEN_REAL`.
