---
tags: [cadence, ops]
---

# Cadence

The system runs on two rhythms: **high-frequency ingest** and **one weekly deep
pass at night Israel time**, with an **intensive first week**. All schedules are
cron in the workflow files (UTC); `config.json`'s `cadence` block documents intent.

## Ingest — frequent (analyze.yml)
- `0 */3 * * *` — every 3 hours, analyze a batch (`analyze_batch_size`, default 50)
  oldest-first.
- `*/30 * * * *` — a "sprint" cron that **only does work during [[#Catch-up mode]]**
  and otherwise no-ops cheaply.
- Throughput target: ~**100 videos within 48 hours** (`cadence.throughput_target`).

## Deep pass — weekly, at night Israel time
The deep pass is two staged stages on Saturday night (UTC), which is ~Sunday
~01:00–02:00 in Israel (UTC+2 winter / UTC+3 summer):
- **improve.yml** at `0 20 * * 6` (Sat 20:00 UTC) — tidy first.
- **review.yml** at `0 23 * * 6` (Sat 23:00 UTC) — critique the freshly-tidied data.

The 3-hour gap means they never fight over the git tree.

## First-week intensive
For the first 7 days, both improve and review **also run every other night** to
iterate harder and lower the severity bar (surface medium/low issues early):
- improve: `0 20 * * 0-5`, review: `0 23 * * 0-5` (guards no-op after week 1).

The window is **anchored once** in `data/review_state.json` (`first_run_at`) by
whichever stage runs first, and **shared** by both — so they agree on when week 1
ends. An explicit `config.cadence.first_week.started_at` overrides the anchor.

## Catch-up mode
When a big burst of videos lands at once, `src/fetch.py` flips `catch_up.json` to
`active`. Analyze then switches to a **large batch, newest-first**, and the `*/30`
sprint cron drains the backlog back-to-back until `data/_pending` is empty, then
auto-returns to the normal 3-hour cadence. Manual `forced_on`/`forced_off` (via the
offline MCP) are respected.

## Why night Israel time
The owner is in Israel; the heavy weekly work happens while they sleep, so a busy
run never competes with interactive use, and the dashboard is fresh by morning.

## Related
- [[Architecture]] · [[Pipeline - Improve]] · [[Pipeline - Review]] · [[Config Reference]]
