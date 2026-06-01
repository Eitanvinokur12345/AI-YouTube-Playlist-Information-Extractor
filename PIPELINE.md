# Pipeline Specification

Confirmed settings (2026-06-01):
- **Output language:** English for everything.
- **Quality score:** 1–10 per skill, based on consistent judgment + review notes.
- **Model ranking:** rank **every** model found in each category (not just a top 10).
- **First run:** process **all** videos in the playlist.
- **News timezone:** US Eastern (America/New_York).
- **Transcripts:** English only (fallback: description, then title).
- **Cadence:** every 48 hours.

## Tab 1 — Skills Library
For each new video: fetch transcript (first 8000 chars) → analyze → extract
exact tool name + version, category, 2-sentence description, use case, output,
quality score 1–10, model version, company, country, open-source flag, source
type/URL, is-Claude-skill flag, 3 tips, slash commands, general tips, relevance.
Compare to existing skills of same name; keep the best, merge tips/commands,
log discards. Write `skills/<category>/<skill-name>/SKILL.md`.

## Tab 2 — Models Ranking
Maintain `data/models.json`. Per category: podium (top 3) + full ranked table of
ALL models, sorted by score desc. Match by exact name+version; never duplicate.

## Tab 3 — Skills Improvement
Scan all skills; merge overlapping same-category skills into the stronger one;
back up to `data/deleted_skills.json` before deleting; log to `data/merge_log.json`.

## Tab 4 — Tips & Commands
`data/tips.json` with `by_tool` and `general` (topics: prompt engineering,
automation, agents, code, parallel tasks, self-improving systems, harness code).
No duplicates. Master slash-command list in `data/commands.json`.

## Tab 5 — News Feed
Classify each video by publish date vs run time (US Eastern):
last 24h = daily, last 7d = weekly, last 30d = monthly. Write
`data/daily_news.json`, `weekly_news.json`, `monthly_news.json` with run time +
covered range header, entries newest→oldest.

## State files
- `data/skills.json` — seen video IDs + skill records.
- `data/status.json` — last_run, next_run, videos_seen, total_skills, paths.
