---
tags: [reference, data]
---

# Data Files

Everything the dashboard shows lives in `data/*.json`, committed to the repo and
served (read-only) to the browser. Grouped by purpose:

## Content (the tabs)
- `skills.json` — techniques ([[Skills vs Tools|skills]]) for the Skills Library.
- `tools.json` — products/apps/services for the Tools tab.
- `models.json` — ranked models (a mirror/subset of tools) for the podium.
- `connectors.json` — MCP servers/connectors.
- `commands.json` — slash commands.
- `tips.json` — curated tips grouped by tool.
- `agent_catalog.json` — catalog of agents seen across videos.

## News
- `daily_news.json`, `weekly_news.json`, `monthly_news.json` — video-derived news.
- `daily_web_news.json`, `weekly_web_news.json`, `monthly_web_news.json` — web news.
- `web_news_store.json` — the dedup store behind the web feeds.
- `feeds_health.json` — health of the news sources.

## Pipeline state & health
- `status.json` — headline counters (skills/tools/connectors/videos) + reliability
  flags (`analyze_ok`, `review_ok`, token hints) the dashboard banners read.
- `index.json` — index of processed videos.
- `catch_up.json` — [[Cadence|catch-up]] mode state (`active`, `mode`, `last_pending`).
- `health.json` — the [[Self-Improvement Loop]] health report (score /100 + metrics).
- `_pending/` — one JSON per fetched-but-not-yet-analyzed video.
- `processed/` — analyzed video files (moved out of `_pending`).

## Self-improvement & review
- `self_check.json` — [[Reference Self-Check]] results (score **X/50**, per-question answers).
- `improvement_tasks.json` — fix tasks opened for each self-check gap (applied next run).
- `improvement_suggestions.json` — proposed risky changes awaiting approval.
- `approvals.json` — which suggestion ids the user approved/dismissed.
- `improvement_audit.json` — log of every improve run.
- `review_findings.json` — [[Three-Agent Review]] output (scores, benchmark, findings).
- `review_state.json` — the **first-week window anchor** shared by improve + review.
- `tab_candidates.json` — off-tab anecdotes captured by analyze for [[Dynamic Tabs]].
- `extra_tabs.json` — the dynamic tabs that were actually created (with `badge_until`).

## Frozen records & housekeeping
- `stars.json` — starred/frozen records, **never auto-changed** ([[Stars and Freezing]]).
- `deleted_skills.json` — tombstones so deleted items don't get re-added.
- `merge_log.json` — record of dedup merges.

> Some files (e.g. `health.json`, `improvement_suggestions.json`, `approvals.json`,
> `review_state.json`, `stars.json`) only appear after the relevant stage first runs.
> The dashboard handles their absence gracefully (renders nothing rather than breaking).

## Related
- [[Tabs]] · [[Config Reference]] · [[Architecture]]
