---
tags: [pipeline, engine, analyze]
aliases: [Analyze, Analysis Stage]
---

# Pipeline — Analyze

The **analysis stage** is where Claude reads each video and turns it into structured
knowledge. Its authoritative spec is **`CLAUDE.md`** (see [[Engines]]); the workflow is
`.github/workflows/analyze.yml`. This is the *high-frequency ingest* arm (see [[Cadence]]).

## Input
[[Pipeline - Fetch]] writes one `data/_pending/<video_id>.json` per new video. Each record
carries: `title`, `description` (full), `transcript` (verbatim, up to 80k chars),
`transcript_lang`/`transcript_source`, `links`, and now the **surroundings** —
`stats` (views/likes/comments), `tags`, `duration`, and `top_comments`.

## What it does per video (CLAUDE.md steps)
1. **Step 1** — pick up the pending batch (oldest-first normally; newest-first in catch-up).
2. **Step 2** — relevance gate: non-AI videos are moved to `data/processed/` untouched.
3. **Step 2b** — rate the *source video's* quality (1–10) so weak videos can't inject bad
   data; low-quality sources are flagged and their extracted scores capped.
4. **Step 2c** — follow AI-relevant description **links** with `WebFetch` and mine them too
   (an "awesome-list" repo can yield many items). The only stage allowed on the network.
5. **Step 2d** — use the **surroundings**: mine `top_comments` for the real tool name /
   version corrections / links; use `stats` as a popularity tie-breaker (never the main
   score); use `duration`/`tags` for context. Transcript stays verbatim.
6. **Steps 3–8** — extract and route into the tabs: techniques → `skills.json`, products →
   `tools.json`, models → `models.json`, connectors → `connectors.json`, slash commands →
   `commands.json`, tips → `tips.json`. See [[Skills vs Tools]] for the #1 routing rule.
7. **Dedup** — compare-and-keep-best by `slug` (skills) / `name` (tools, connectors); merges
   are logged to `merge_log.json`, deletions snapshotted to `deleted_skills.json`. Never
   touches a [[Stars and Freezing|frozen]] record.
8. **SKILL.md** — every technique it keeps should get a `skills/<slug>/SKILL.md` package.
9. **Off-tab anecdotes** (Step 8b) → `data/tab_candidates.json`, the raw evidence for
   [[Dynamic Tabs]].

## Crash-safety
It **commits and pushes after each video** ("analyze: safety commit …" / "analyze: <id> …"),
so a timeout never loses work. Remaining videos stay in `_pending/` for the next run.

## Output
Updates the six core data files + `status.json.run_report` (the RUN REPORT box the dashboard
shows). See [[Data Files]] and [[Tabs]].
