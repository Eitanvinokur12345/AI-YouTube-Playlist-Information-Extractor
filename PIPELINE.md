# Pipeline Specification

Confirmed settings:
- **Output language:** English for everything written by the pipeline.
- **Transcripts:** try **English first, then Hebrew** (`config.transcript_languages`),
  then the video description, then the title. Text is used **exactly as YouTube provides
  it** — never edited, translated, or rephrased. First 8000 chars.
- **Quality score:** integer 1–10 per skill (rubric in CLAUDE.md). Compare-and-keep-best.
- **Video quality:** integer 1–10 per source video (AI content review + recency penalty).
  Below `low_quality_threshold` (5) ⇒ still mined, but flagged + score-capped (never deleted).
- **Model ranking:** rank **every** model found in each category (not just a top N).
- **First run:** process **all** videos in the playlist.
- **News:** US Eastern (America/New_York); always merges **video-mentioned** news with
  **50 official sources** pulled directly via public RSS/Atom ($0, no keys).
- **Cadence:** fetch every **48 hours**; analyze every **3 hours** in batches of
  `analyze_batch_size` (50), committing after each video; web news every **12 hours**. On a
  **massive addition** of videos, analyze switches to a **catch-up sprint** (large batch,
  every 30 min, newest-first) until the backlog clears, then auto-returns to normal.

## Architecture — cloud builds, local viewing

```
GitHub Actions (cloud, runs even when the PC is off)
  fetch.yml   (every 48h)  ──>  data/_pending/*.json + video news + status ─ commit ─┐
  analyze.yml (every few h) ──> Claude reads CLAUDE.md, fills 6 tabs + video-quality ┤
  news.yml    (every 12h)   ──> src/news.py: 50 official RSS/Atom ─> *_web_news.json ┤
  improve.yml (daily)       ──> Claude reads IMPROVE.md: curate/dedup/star/trend/health
                                                                                     v
                                                                          GitHub repo (main)
                                                                                     │
Local Windows (sync/, runs on a schedule)                                            │
  sync-skills.ps1  ── git pull ──>  copies results to Desktop folders  <─────────────┘
     skills/            -> "claude skills of eitan"
     other-skills/<t>/  -> "<t> skills of eitan"   (gemini, chatgpt, ...)
     data/              -> "AI Skills Data"          (read by the MCP server, offline)
```

The News Feed is the merge of two streams that never touch each other's files: `fetch.yml`
rebuilds the **video-mentioned** news (`daily_news.json` …) every run, while `news.yml`
independently writes the **official-source** news (`daily_web_news.json` …). The dashboard and
the MCP server load both and merge + sort by timestamp at display time, so neither stage can
clobber the other.

The fetch stage is deterministic Python. The analyze stage is Claude Code driven entirely
by **CLAUDE.md** (the authoritative analysis instructions). The daily self-improvement stage
is Claude Code driven by **IMPROVE.md**. Viewing/querying (dashboard + MCP server) works
fully **offline** from the synced `AI Skills Data` folder; only building new results needs
the cloud.

## Self-improvement stage (daily, IMPROVE.md)

A separate daily run *curates* what already exists (it never fetches videos). Governed by the
`self_improvement` block in `config.json` with a **safe-auto / suggest-risky** split:
- **Auto (safe):** build a compact `data/index.json`, repair malformed records, recreate
  missing SKILL.md packages, merge **exact** duplicates, fill missing news summaries, fix
  cross-tab counts, stamp starred records, and write `data/health.json`.
- **Suggest only (risky):** fuzzy/near-duplicate merges, rescoring outliers, recategorizing,
  dashboard/UX changes, and star suggestions are written to
  `data/improvement_suggestions.json` for you to approve — never applied automatically.
- **Stars = freeze.** A skill whose slug is in `data/stars.json` (or with `starred`/`locked`
  true) is **proven best-in-class** and is *never* changed, merged, rescored, or deleted by
  any stage. You star/unstar and approve/dismiss suggestions via the MCP tools; approvals
  land in `data/approvals.json` and are applied on the next improve run.
- **Caps & budget:** per-run caps (merges/deletes/rescores, UI changes/week) and a token
  budget keep each run cheap and safe. Everything is logged to `data/improvement_audit.json`.
- **Dynamic trend tabs.** When ≥ `dynamic_tabs.min_evidence_videos` (5) videos converge on a
  topic that doesn't fit an existing tab, the improve stage may **auto-create and announce** a
  new tab (capped at one/week, `max_total_active` 6). It appends `{id,title,items,created_at}`
  to `data/extra_tabs.json` and a one-line banner to `health.json.new_tab_announcement`; the
  dashboard injects the nav button (with a green **NEW** badge for 7 days). Dismiss a tab via
  the MCP tool `dismiss_dynamic_tab` (sets its status to `dismissed`).

## Video-quality review (analyze stage, CLAUDE.md Step 2b)

Not every source video is trustworthy, so each video gets a 1–10 **video-quality score**
before its skills are written:
1. **AI content review** — Claude rates the transcript's depth/credibility 1–10 (capped at 3
   if only the title was available, i.e. `transcript_source=="title"`).
2. **Recency adjustment** — subtract `video_quality.recency_penalty_points` based on age of
   `publishedAt`: −0 (≤6mo), −1 (≤12mo), −2 (≤2y), −3 (older). `score = clamp(rating − penalty, 1, 10)`.

If the score is below `low_quality_threshold` (5) the action is **`downweight_and_flag`** (never
delete): every skill / connector / news item from that video gets `low_quality_source: true`
and its own `quality_score` is **capped at the video's score**. Each record also carries the raw
`video_quality_score`. The dashboard shows a green **vid N/10** badge (amber when low), a red
**low-quality source** badge, and a **"Hide low-quality sources"** toggle; compare-and-keep-best
prefers the keeper with the higher `video_quality_score` on a tie.

## Catch-up protocol (massive additions)

When a large batch of videos lands at once (e.g. merging another playlist into the tracked
one), the system treats it like a fresh first run — governed by the `catch_up` block in
`config.json` and the live switch `data/catch_up.json` (`mode`: `auto` | `forced_on` |
`forced_off`):
- **Detect (fetch.py):** if one fetch finds ≥ `surge_threshold` (100) new videos, it sets
  `catch_up.json.active = true` and records the reason; it also surfaces this in
  `status.json.catch_up` for the dashboard banner.
- **Sprint (analyze.yml):** a second `*/30` cron is added that **no-ops unless catch-up is
  active**. While active, the analyze run uses a large batch (`catch_up.batch_size`, process all
  remaining) and **newest-published-first** order, committing after every video. Because the
  concurrency group keeps at most one run queued behind the running one, the */30 cron drains
  the backlog back-to-back without piling up. A post-step flips `active` back to `false` once
  `data/_pending` is empty → **auto-return to normal** (3h cron, batch 50, oldest-first).
- **Light curation (IMPROVE.md):** while `active` and `catch_up.curation ==
  "light_until_caught_up"`, the daily improve run does only Steps 2/8/9 (hygiene, health,
  audit) and skips dedup/rescore/stars/UX/trend-tabs, so it never curates half-ingested data.
- **Manual control (MCP):** `catch_up_status` reports state; `set_catch_up('on'|'off'|'auto')`
  forces a sprint, stops it, or restores automatic behavior (writes `catch_up.json`, needs the
  optional `GITHUB_PAT`). Everything stays $0 (public-repo Actions + your subscription token).

## The 6 tabs (see CLAUDE.md for exact logic)

1. **Skills Library** — extract every AI tool/skill/technique; quality score 1–10;
   compare-and-keep-best (merge tips, log discards). Write a SKILL.md package per reusable
   skill. **Flat layout:** `skills/<slug>/SKILL.md` for Claude skills. Packaged skills for
   other tools (Gemini Gems, ChatGPT Custom GPTs, …) go to
   `other-skills/<tool>/<slug>/SKILL.md`.
2. **Models Ranking** — `data/models.json`: per category an ASCII podium + a **full ranked
   table of ALL models** (sorted by score). Match by exact name+version; never duplicate.
3. **Skills Improvement** — merge overlapping same-tool skills into the stronger one; back
   up removals to `data/deleted_skills.json`; log to `data/merge_log.json`.
4. **Tips & Commands** — `data/tips.json` (`by_tool` + `general` topics) and
   `data/commands.json` (master slash-command list). No duplicates.
5. **News Feed** — classify by publish date vs run time (US Eastern): ≤24h daily, ≤7d
   weekly, ≤30d monthly. **Two merged streams:** (a) video-mentioned news Claude writes to
   `data/daily_news.json` / `weekly_news.json` / `monthly_news.json` (run-time + covered-range
   header, newest→oldest, 2-sentence summaries), and (b) official-source news `src/news.py`
   writes to `data/daily_web_news.json` / `weekly_web_news.json` / `monthly_web_news.json` from
   the **50 feeds** in `config.news_sources`. Both views merge at display time; web summaries
   are **verbatim** excerpts (no tokens spent). Video-derived entries carry the source video's
   `low_quality_source` / `video_quality_score` flags.
6. **Connectors** — `data/connectors.json`: Claude connectors & MCP servers mentioned in
   videos (name, type, provider, what it does, install/source, official, score). Dedup by
   name.

The dashboard adds a 7th view, **Self-Improvement** (read-only): the health score + metrics,
the suggestion queue awaiting your approval, the starred/frozen list, any new-tab announcement,
and the last audit run. Starred skills show a ★ and sort first across the library and
connectors. Beyond these seven, the improve stage may inject extra **dynamic trend tabs**
(see above) that appear in the nav with a NEW badge.

## Run report

Shown every run as an ASCII box (stored in `data/status.json` → `run_report.ascii`):
run time, total in playlist, already seen, new found, analyzed this run, skipped (not
relevant), skipped (no transcript), errors, pending remaining, total analyzed (all time).

## State files (`data/`)
- `skills.json` — `videos_seen` + full skill records.
- `models.json` — rankings per category (podium + full + ascii_podium).
- `tips.json`, `commands.json` — Tab 4.
- `daily_news.json`, `weekly_news.json`, `monthly_news.json` — Tab 5 (video-mentioned).
- `daily_web_news.json`, `weekly_web_news.json`, `monthly_web_news.json` — Tab 5
  (official sources, written by `src/news.py`); `web_news_store.json` — the 30-day dedup store.
- `connectors.json` — Tab 6.
- `deleted_skills.json`, `merge_log.json` — improvement audit trail.
- `status.json` — `last_run`, `last_fetch`, `last_analyze`, `last_improved_at`,
  `last_ux_review`, `next_run`, `videos_seen`, `total_skills`, `total_videos_analyzed`
  (cumulative), `new_videos_this_run`, `pending_count`, the `catch_up` summary, and the
  `run_report` block (incl. `ascii`).
- `catch_up.json` — the massive-addition switch: `active`, `mode`
  (`auto`/`forced_on`/`forced_off`), `reason`, `surge_threshold`, `batch_size`, `last_pending`.
- **Self-improvement files:** `stars.json` (frozen best-in-class slugs), `approvals.json`
  (`approved_ids` / `dismissed_ids`), `improvement_suggestions.json` (risky proposals),
  `improvement_audit.json` (per-run log), `health.json` (score + metrics + advice +
  `new_tab_announcement`), `extra_tabs.json` (auto-created dynamic trend tabs),
  `index.json` (compact skill index for cheap reads).
- `_pending/` — fetched-but-not-yet-analyzed records. `processed/` — done.
