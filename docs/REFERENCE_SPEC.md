# REFERENCE SPEC — the authoritative quality checklist

This file is the **canonical reference** the self-improvement stage returns to on
every deep pass (`reference_self_check` in `config.json`, read by `IMPROVE.md`).
It has three parts:

1. **Part A — the original reference** the project owner supplied, preserved
   faithfully ("the format I sent"). The self-check must verify the system still
   honours its intent.
2. **Part B — the cloud-architecture mapping.** The original describes a *local*
   Claude-Code routine. This project runs in the *cloud* (GitHub Actions) with a
   *static dashboard*. Part B translates every local-only concept to its cloud
   equivalent so the 50-question self-check is answerable here.
3. **Part C — the 50 self-check questions**, verbatim, each annotated with how it
   is verified in this architecture and which data file proves it.

> How it is used: every deep pass, `IMPROVE.md` answers all 50 questions
> (yes/no), writes `data/self_check.json` (`{n, question, answer, evidence}` +
> totals), and for every **no** writes a one-line fix task to
> `data/improvement_tasks.json`. The next run reads that file first and tries to
> fix each task, then re-answers the question. The dashboard's Self-Improvement
> tab shows `Self-check score: X/50 — Y improvements logged`.

---

## Part A — Original reference (preserved)

**YouTube Skills Tracker — System Prompt.** An automated AI-skills tracker that
runs every 48 hours without human intervention, managing seven tabs, each with
its own files and update logic. Runs inside Claude Code; performs all analysis
itself (no separate analysis API key). The only key required is the YouTube Data
API key, used to read the playlist `PLxtsVIUtYhNo6pY9FrVqVe2xh---Y8rxB`.

**Global rules (original):** never stop mid-run unless a critical error; never
print API keys; wait 0.5 s between videos; require internet, retry every 30 min
if offline; check last-run timestamp hourly and start when ≥48 h have passed.

**Opening RUN REPORT** (shown every run, before any tab):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUTUBE SKILLS TRACKER — RUN REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Run time:                      [exact date and time]
Total videos in playlist:      [total count]
Videos already seen:           [count]
New videos found:              [count]
Videos analyzed this run:      [count]
Videos skipped (not relevant): [count]
Videos skipped (no transcript):[count]
Errors:                        [count]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Tab 1 — Skills Library.** Fetch the playlist; keep only unseen IDs (vs
`skills.json`); fetch the auto transcript (English then Hebrew) and use it
**exactly as YouTube provides — never correct, rephrase, or translate**; use the
first 8000 chars, else fall back to description, else title. Extract: exact tool
name **with version** (never "Gemini" → "Gemini 2.5 Pro"; never "Claude" →
"Claude Sonnet 3.7"), category, two-sentence description, use case, output,
quality 1–10, model-version string, company, country, open-source y/n, source
type, source URL, is-Claude-skill, three actionable tips, slash commands as
`/command` + what it does, general tips by topic, and is-relevant. Skip if not
about an AI tool. **Compare and keep the best:** higher score replaces + merges
tips/commands and logs the deletion; equal score keeps existing + adds new
tips/commands; lower score is discarded and logged; no match → add new. Write a
`SKILL.md` per added/updated skill.

**Tab 2 — Models Ranking.** Maintain `models.json`; sort by score desc within
each category; rank from 1; never duplicate (match by exact name+version); show
a top-3 **podium** per category:

```
          🥇
       [1st place]
    🥈              🥉
 [2nd place]    [3rd place]
1st: [model] — score [X]/10 — [company] — [country]
2nd: [model] — score [X]/10 — [company] — [country]
3rd: [model] — score [X]/10 — [company] — [country]
```

Categories: design, code, automation, agents, image creation, video creation,
writing, marketing, social, music, integration, research, productivity, other.

**Tab 3 — Skills Improvement.** Scan all skills; within a category find
overlapping use cases/descriptions; keep the better one, merge unique
tips/commands, delete the weaker file, log to `merge_log.json`; never delete
without first saving full data to `deleted_skills.json`.

**Tab 4 — Tips & Commands.** Store per-tool tips + slash commands in `tips.json`
under `by_tool`; never duplicate. Maintain a `general` section by topic: prompt
engineering, automation, agents, code, parallel tasks, self-improving systems,
harness code. Every slash command is `/command` + a clear description. Maintain a
master `commands.json`.

**Tab 5 — News Feed.** Using run time as the reference point: <24 h = daily,
<7 d = weekly, <30 d = monthly, older = excluded. Extract publish date, title,
two-sentence summary, tool/model name, and content type (release / update /
comparison / tutorial). News and skills are separate outputs. Write
`daily_news.json`, `weekly_news.json`, `monthly_news.json`, each with a date-range
header, sorted newest→oldest.

**Tab 6 — Connectors.** For every connector/MCP server: exact name, source
(Claude official / GitHub / company / other), one-sentence "what it does",
free y/n, free token/request allowance, paid allowance + cost, official URL, and
works-in (Claude chat / Claude Code / both). Write `connectors.json`, never
duplicate. Always display the "How To Connect" instructions at the end (chat:
Settings → Connectors → Connect; Code: edit `claude_desktop_config.json`
`mcpServers`, save, restart).

Connector display format:

```
[Connector Name]
Source:       [Claude official / GitHub / company website / other]
URL:          [official URL]
What it does: [one sentence]
Free:         [yes / no]
Free tokens:  [number or requests included, or "not applicable"]
Paid version: [token or request limit and cost, or "none"]
Works in:     [Claude chat / Claude Code / both]
```

**Tab 7 — Trend Recognition (original).** Group all processed videos by
tool/category/topic; for anything with ≥3 mentions compute weekly frequency;
classify rising (+50%), stable (±20%), declining (−50%), emerging (first seen);
write `trends.json`; display grouped 🚀 RISING / 🆕 EMERGING / 📊 STABLE / 📉
DECLINING.

**Tools available (when run as MCP):** run / force-run the pipeline; get skills
in category X; ranking table; merge log; tips for tool X; general tips on topic
X; all commands; daily/weekly/monthly news; connectors; find connector X;
trends; rising tools; self-check results; pipeline status; search skills for X;
show deleted log.

---

## Part B — Cloud-architecture mapping

This project is **not** a single local Claude-Code routine. It is:

- **`fetch.yml`** (Python, YouTube API key) → writes pending records to
  `data/_pending/` + the news buckets.
- **`analyze.yml`** (Claude reads `CLAUDE.md`) → the real Tab-1…Tab-6 engine;
  commits per video.
- **`news.yml`** → refreshes news from RSS sources + playlist.
- **`improve.yml`** (Claude reads `IMPROVE.md`) → Tab-3 curation, ratings, stars,
  dynamic tabs, **this self-check**, health, and the 3-agent review.
- **`docs/`** static dashboard (GitHub Pages) → renders the tabs from `data/`.

Translation table (original → this system). When a self-check question refers to
a local-only concept, evaluate the **cloud equivalent**:

| Original concept | Cloud equivalent (what to actually check) |
|---|---|
| "runs every 48 h", "start within the 48-h window" | `analyze.yml` every 3 h + `*/30` catch-up sprint; throughput target = 100 videos / 48 h (`cadence.throughput_target`). Q1 = "did ingest+analyze keep pace / no stalled backlog". |
| "wait 0.5 s between videos" | `config.rate_limit_seconds` honoured by `fetch.py`. Q41 = rate-limit respected, no 429s. |
| "retry every 30 min if offline" | GitHub Actions scheduled retries + catch-up sprint cron. Q42 = failed/duped runs recover on the next scheduled tick. |
| "complete the run in under 30 min" | Cloud commits **per video**, so partial work is never lost; "fast enough" = backlog not growing. Q45 = no unbounded backlog (`data/_pending` count trend). |
| "save run timestamp to `last_run.json`" | `data/status.json` (`last_analyze_ok_at`, `last_improved_at`). Q43 = status timestamps updated. |
| "opening RUN REPORT printed before tabs" | `data/status.json.run_report` block, rendered at the top of the dashboard. Q2–Q5 = run_report present and numerically correct. |
| "six data tabs" / "seven tabs" | **Six core tabs + auto-discovered dynamic tabs** (see Part B deltas). |
| "Skills folder `C:\…\claude skills of eitan`" | Cloud reads `./skills` + `./other-skills`; the local runner also reads the owner's local skills folder and the curated `SKILL.md` packages (`skills_folder_learning`). |
| "MCP tool requests" | The dashboard surfaces the same views (ranking table, connectors, news, self-check, status). Treat each MCP request as "is this view available on the dashboard". |

### Deltas that EXTEND or SUPERSEDE the original (owner decisions)

1. **Skills = techniques only; Tools = products.** The #1 quality rule. The
   original "Skills Library" conflated techniques and tools. This system splits
   them: `skills.json` holds **techniques/workflows you apply**; `tools.json`
   holds **products / models / apps / services**. Models remain a subset mirrored
   into `models.json`. (Self-check Q10–Q11 now check *routing correctness*, not
   just "has a version".)
2. **Trend Recognition (Tab 7) → Dynamic Tab Discovery.** Instead of a fixed
   trends tab, the backend inspects raw extracted data *before* routing and, when
   it finds a coherent run of information that fits none of the core tabs,
   **spawns a brand-new tab**. A new tab carries a "NEW" badge + a one-line
   topic description for `new_badge_days` (7) days, tied to the anecdotes found
   during the two days it was created (`tab_candidates.json` →
   `extra_tabs.json`). Q37–Q40 now verify dynamic-tab discovery + badge expiry.
3. **Extract everything the video AND its surroundings offer.** Beyond the 8000
   char transcript: up to `extraction.transcript_chars` (80000), plus
   AI-relevant links in the description followed with WebFetch
   (`link_following`), plus connectors/MCP servers hunted actively.
4. **Batch speed.** Designed to analyze ~50–100 videos at a high level within
   48 h, with a catch-up sprint when a surge lands; falls back to a weekly deep
   night pass (Israel time) if needed (`cadence.mode`).
5. **3-agent review every deep pass:** usability/UX (competitor-benchmarked),
   "cut the bullshit", deep code-bug researcher — Claude first, then an external
   engine if a free token is present (graceful-skip if absent). First week runs
   at higher intensity.
6. **Stars / freezing.** Up to 10 proven-excellent records are starred and
   **frozen** (`data/stars.json`); never modify, merge, rescore, or delete them.

---

## Part C — The 50 self-check questions (verbatim + verification)

Answer each **yes/no** every deep pass and write to `data/self_check.json` as
`{ "n", "question", "answer", "evidence" }`. `evidence` is the file/field that
proves it. For local-only items, evaluate the Part-B cloud equivalent.

1. Did the routine start on time within the 48-hour window? → *cloud:* ingest+analyze kept pace, no stalled backlog (`status.json`, `_pending` trend).
2. Did the opening summary display before any tab loaded? → `status.json.run_report` present and rendered top-of-dashboard.
3. Did the opening summary show the correct total video count from the playlist? → `run_report.total_in_playlist` matches fetch.
4. Did the opening summary show the correct number of new videos found? → `run_report.new_found`.
5. Did the opening summary show the correct number of videos analyzed this run? → `run_report.analyzed`.
6. Did all six data tabs run without stopping early? → all six core data files updated this cycle (skills, tools, models, tips, news, connectors).
7. Did Tab 1 correctly identify and skip already-seen videos? → `skills.json.videos_seen` vs `data/processed/`.
8. Did Tab 1 fetch transcripts before falling back to descriptions? → per-record `source_type` (transcript|description|title).
9. Did Tab 1 use the transcript text exactly as YouTube provided without changes? → no rewriting of source transcript (English-output is generated separately).
10. Did Tab 1 extract a specific model version name and not a vague name for every skill? → **+routing:** versions present AND techniques vs tools routed correctly.
11. Did Tab 1 assign a category to every skill from the approved category list? → every record's `category` ∈ `config.categories`.
12. Did Tab 1 extract at least one tip for every relevant skill? → tips present per relevant record.
13. Did Tab 1 extract at least one slash command for every relevant skill **that has one**? → real `/command` only (strict filter; absence is OK if none exist).
14. Did Tab 1 correctly skip videos marked as not relevant? → relevance gate applied (`processed/` non-relevant flagged).
15. Did Tab 1 never overwrite a higher-scoring skill with a lower-scoring one? → `merge_log.json` shows score-aware merges only.
16. Did Tab 1 write a SKILL.md file for every new or updated skill (technique)? → `skills/<slug>/SKILL.md` exists per technique.
17. Did Tab 2 update the models ranking after Tab 1 completed? → `models.json` refreshed this cycle.
18. Did Tab 2 display a podium for every category that has at least one model? → dashboard podium per non-empty category.
19. Did Tab 2 sort models by score descending within each category? → ordering check in `models.json`.
20. Did Tab 2 never duplicate a model entry? → unique by exact name+version.
21. Did Tab 3 scan all existing skills for overlaps after Tab 1 completed? → improve audit recorded a dedup pass.
22. Did Tab 3 save every deleted skill to deleted_skills.json before removing it? → `deleted_skills.json` has the pre-delete snapshot.
23. Did Tab 3 write a merge reason for every merge action to merge_log.json? → every merge entry has `reason` + both scores.
24. Did Tab 4 add new tips without duplicating existing ones? → `tips.json.by_tool` dedup.
25. Did Tab 4 add new slash commands without duplicating existing ones? → `commands.json` dedup.
26. Did Tab 4 update the master commands.json file? → `commands.json` refreshed.
27. Did Tab 4 correctly assign general tips to the right topic? → `tips.json.general` topics ∈ `config.general_tip_topics`.
28. Did Tab 5 use the exact current run timestamp as the date reference? → news files' `ran_at` header.
29. Did Tab 5 correctly classify videos into daily, weekly, or monthly buckets? → bucket boundaries 24h/7d/30d.
30. Did Tab 5 exclude videos older than 30 days from all news files? → no >30 d entries.
31. Did Tab 5 sort news entries from newest to oldest? → ordering check.
32. Did Tab 5 show the correct date range header in each news file? → `covers` header present.
33. Did Tab 6 extract connector information from every relevant video? → connectors captured where mentioned (MCP hunt signals).
34. Did Tab 6 never duplicate a connector entry? → unique by exact name.
35. Did Tab 6 display the connection instructions at the end of the connectors list? → dashboard renders the How-To-Connect block.
36. Did Tab 6 correctly identify whether each connector works in Claude chat, Claude Code, or both? → `works_in` field set.
37. Did Tab 7 (→ dynamic tabs) detect off-tab information clusters? → `tab_candidates.json` captured this cycle.
38. Did the dynamic-tab stage correctly promote a cluster to a new tab when evidence ≥ threshold? → `extra_tabs.json` vs `dynamic_tabs.min_evidence_videos`.
39. Did new dynamic tabs carry a NEW badge + topic description for the badge window? → `extra_tabs[].created_at` + `description`; badge ≤ `new_badge_days`.
40. Did expired NEW badges get removed after the window? → no badge older than `new_badge_days`.
41. Did the routine respect the rate limit between videos to avoid 429s? → `config.rate_limit_seconds`; no rate-limit errors in `feeds_health.json`/run logs.
42. Did the routine retry automatically when a run failed or the connection was unavailable? → next scheduled tick recovered; `status.analyze_ok`.
43. Did the routine correctly save the run timestamp after completing? → `status.json` timestamps updated.
44. Did the routine avoid writing any API key to any log or output file? → no secrets in `data/`, `docs/`, or logs.
45. Did the routine keep up (no unbounded backlog / partial work never lost)? → `_pending` count not growing; per-video commits present.
46. Were zero duplicate entries written to any JSON file during this run? → dedup holds across skills/tools/models/connectors/commands.
47. Did every SKILL.md file contain all required fields with no empty values? → schema check across `skills/*/SKILL.md`.
48. Did the routine handle videos with no transcript and no description without crashing? → title-only fallback path worked; no crash records.
49. Did the self-check questions all receive a yes/no answer and get saved to self_check.json? → `self_check.json` complete (50 answers).
50. Did the routine identify at least one improvement task and log it to improvement_tasks.json? → `improvement_tasks.json` non-empty when score < 50.

**Scoring:** count yes/no, write totals to `self_check.json`, surface
`Self-check score: X/50 — Y improvements logged` on the dashboard, and queue
every **no** into `improvement_tasks.json` for auto-fix next run.
