# Claude Code Analysis Instructions

This file is read by the Claude Code GitHub Action to perform the **analysis stage** of
the YouTube Skills Tracker pipeline. The fetch stage (`src/fetch.py`) has already run and
written raw video records to `data/_pending/<video_id>.json`. Your job is to analyze each
pending file and populate **all SIX tracker tabs**, then commit the results.

---

## Golden rules (read first)

1. **Process ONE video at a time, fully (all tabs), then COMMIT AND PUSH before moving to
   the next video.** This is mandatory. The run may be interrupted or time out at any moment
   — committing after every video guarantees no work is ever lost and the next run resumes
   cleanly from whatever is left in `data/_pending/`.
2. **Batch limit:** process at most `analyze_batch_size` (50) pending files per run. Leave
   the rest in `data/_pending/` — the next scheduled run (every few hours) picks them up.
3. **Output language is English only** (`output_language` in config.json). Every summary,
   SKILL.md, tip, description, and JSON value you WRITE must be English.
4. **Transcripts may be English OR Hebrew** (or a description/title fallback). Read and
   understand the source text *as provided* — but never edit, translate, or rephrase the
   SOURCE inside any record. Your *generated* output (summaries, skills, tips) is English.
   A Hebrew transcript is fine: comprehend it, then write English output.
5. **Never print or commit secret values** (API keys, tokens). They live only in GitHub
   Actions secrets / local environment variables.
6. **Preserve existing data.** Always read an existing JSON file before writing it; append
   or update records — never blindly overwrite a populated file.
7. All JSON must be valid, pretty-printed (2-space indent), UTF-8.
8. **Never touch a FROZEN (starred) record.** A skill or connector is frozen if its `slug`
   appears in `data/stars.json` **or** the record has `"starred": true` / `"locked": true`.
   Frozen = "proven excellent, keep in its original form forever." You must NOT overwrite,
   merge away, rescore, recategorize, or delete a frozen record — not even with a
   higher-scored new version. If a new video would normally supersede a frozen skill, keep
   the frozen one as-is and instead record the new variant under a different slug. Before any
   compare-and-keep-best (Step 3) or merge (Step 5), check this rule first.

---

## Step 1 — Pick up the pending batch

List `data/_pending/*.json` and take up to 50 files (oldest `fetched_at` first). Each file
contains:

| field               | meaning                                                      |
|---------------------|--------------------------------------------------------------|
| `video_id`          | YouTube video ID                                             |
| `title`             | video title                                                  |
| `description`       | video description                                            |
| `publishedAt`       | ISO-8601 publish timestamp                                   |
| `channel_name`      | YouTube channel name                                         |
| `transcript`        | transcript (first 8000 chars), or description, or title      |
| `transcript_lang`   | `"en"` / `"he"` / `""` (empty = a description/title fallback)|
| `transcript_source` | `"transcript"` \| `"description"` \| `"title"`               |
| `fetched_at`        | when the record was created                                  |

If `data/_pending/` is empty, there is nothing to analyze — jump straight to **Step 9**
(update the run report) and finish.

---

## Step 2 — Relevance gate (per video)

Decide whether the video is relevant to **AI tools, skills, models, techniques, connectors,
or AI news**. If it is clearly NOT relevant (off-topic, spam, non-AI content):

- Do **not** extract anything.
- Move its pending file to `data/processed/<video_id>.json`.
- Increment `run_report.skipped_not_relevant` in `data/status.json`.
- Commit and move to the next video.

Otherwise, continue with Steps 3–8 for this video.

> The video is already recorded in `videos_seen` (by the fetch stage), so a skipped video
> will never be re-fetched.

---

## Step 2b — Video quality review (per video)

Before extracting anything, rate the **source video's quality** so weak videos don't inject
bad information into the library. Configured by the `video_quality` block in `config.json`
(`enabled`, `low_quality_threshold`, `signals`, `recency_penalty_points`). If
`video_quality.enabled` is false, skip this step and treat every video as normal quality.

Compute one **`video_quality_score` (integer 1–10)** from two signals:

1. **AI content review (primary).** Judge the transcript/content for substance: does it
   *actually demonstrate* the tools with specifics, or is it shallow hype/clickbait? Is it
   coherent, credible, and technically accurate? Rate 1–10:
   - 9–10 deep, specific, clearly credible · 7–8 solid · 5–6 useful but thin ·
     3–4 vague / hypey / weak demo · 1–2 noise.
   - If `transcript_source` is `"title"` (no real transcript or description), you have almost
     nothing to judge → cap the content rating at 3.
2. **Recency adjustment.** Compute the video's age from `publishedAt` → `fetched_at` and
   subtract `recency_penalty_points` (AI moves fast; stale how-tos mislead):
   - ≤ 6 months: −0 · ≤ 12 months: −1 · ≤ 2 years: −2 · older than 2 years: −3.

`video_quality_score = clamp(content_rating − recency_penalty, 1, 10)`. Write a one-line
`video_quality_reason` (e.g. "Specific live demo, but ~2.5 yrs old → −3.").

A video is **LOW QUALITY** if `video_quality_score < low_quality_threshold` (default 5).

**When the video is LOW QUALITY** (`low_quality_action: "downweight_and_flag"`), then for
*every* skill, connector, and news entry you extract from it in Steps 3–8:
- set **`low_quality_source: true`**, and
- **cap** its `quality_score` at `video_quality_score`
  (`quality_score = min(your_rating, video_quality_score)`).

When the video is normal/high quality, set `low_quality_source: false` and apply no cap.
Always carry `video_quality_score` onto each record so the dashboard can show a quality badge.
This never *drops* a video — it only down-weights and visibly flags weak sources.

---

## Step 3 — Tab 1: Skills Library

Extract ALL AI tools, models, skills, or techniques demonstrated in the video. For each one
build a skill record:

- `skill_name` — exact name incl. version (e.g. "Claude Sonnet 4.6", "Cursor", "n8n")
- `slug` — unique kebab-case id (see slug rules below)
- `category` — one of: design, code, automation, agents, image creation, video creation,
  writing, marketing, social, music, integration, research, productivity, other
- `description` — 2 sentences on what it does
- `use_case` — primary use case as shown in the video
- `output` — what the tool produces
- `quality_score` — integer **1–10** (rubric below)
- `model_version` — version string, or null
- `company` — company / creator
- `country` — company country of origin (e.g. "USA", "China"), or null
- `open_source` — true/false
- `target_tool` — which ecosystem this packaged skill belongs to: `"claude"` (default),
  or `"gemini"`, `"chatgpt"`, `"perplexity"`, etc. (see routing below)
- `is_claude_skill` — true if it is a Claude/Anthropic product or a Claude Code skill
- `source_type` — "youtube"
- `source_url` — `https://www.youtube.com/watch?v=<video_id>`
- `source_video_id` — `<video_id>`
- `tips` — up to 3 practical tips from the video
- `slash_commands` — list of slash commands mentioned (e.g. "/review"), else `[]`
- `general_tips` — list of general (not tool-specific) tips
- `relevance` — 1 sentence: why this matters to AI practitioners
- `popularity_signals` — list of explicit adoption/popularity claims made IN the video
  (e.g. "120k GitHub stars", "most downloaded MCP", "used by millions", "#1 on the
  leaderboard"). Quote them briefly and verbatim. Empty list if none are stated. (The
  self-improvement stage uses this to decide which rare skills to *propose* freezing.)
- `endorsement_video_ids` — list of video IDs that have featured/endorsed this skill.
  Initialize to `["<video_id>"]`. When the same skill reappears in a later video, ADD that
  video's id (see compare-and-keep-best). Its length = how many videos independently
  endorsed the skill.
- `video_quality_score` — the source video's 1–10 quality from Step 2b, copied onto the skill.
- `low_quality_source` — boolean from Step 2b. If `true`, this skill's `quality_score` was
  capped at `video_quality_score` and the dashboard badges it as coming from a weak video.

### Quality score rubric (1–10)
- **9–10** — production-ready, widely useful, clearly demonstrated, strong results.
- **7–8** — solid and useful, minor caveats or narrower scope.
- **5–6** — useful but niche, early-stage, or lightly demonstrated.
- **3–4** — experimental, weak demo, or limited applicability.
- **1–2** — barely relevant, hype with little substance.

### Compare-and-keep-best (dedup by slug)
Read `data/skills.json`. **First check Golden rule #8:** if the existing skill is frozen
(slug in `data/stars.json`, or `starred`/`locked` true), leave it untouched — do not replace,
rescore, or merge it; if your new record is genuinely different, give it a distinct slug.
Otherwise, if a skill with the same `slug` already exists:
- **Keep the higher `quality_score`** version (the "keeper"); on a tie, prefer the one with
  the higher `video_quality_score` (better source). The keeper carries its own source video's
  `video_quality_score` and `low_quality_source`.
- **Merge** `tips`, `slash_commands`, and `general_tips` from both into the keeper
  (deduplicate, case-insensitive).
- **Union** `endorsement_video_ids` (add the new video's id — this grows the multi-video
  endorsement count) and `popularity_signals` (dedup) into the keeper.
- **Back up the discarded** version to `data/deleted_skills.json` (append to the array)
  with `reason: "superseded by higher quality record"` and a timestamp.
If the slug is new, append the record.

### Write a SKILL.md package
Only create a SKILL.md package for skills that are genuinely **reusable and useful
(`quality_score >= 5`)**. (Lower-scored skills still live in `skills.json` and the rankings,
just without a package folder, to keep the skill folders clean.)

**Routing — which folder the package goes in:**
- `target_tool == "claude"` (default) → **`skills/<slug>/SKILL.md`** (FLAT — no category
  subfolders). These sync to the user's `claude skills of eitan` folder.
- Any other `target_tool` (a packaged skill for another ecosystem — a Gemini Gem, a ChatGPT
  Custom GPT, etc.) → **`other-skills/<target_tool>/<slug>/SKILL.md`**. These sync to a
  per-tool folder named `<target_tool> skills of eitan`.

```
skills/                         other-skills/
  prompt-chaining/SKILL.md        gemini/
  cursor-ai/SKILL.md                deep-research-gem/SKILL.md
  n8n-automation/SKILL.md         chatgpt/
  ...                               coding-mentor-gpt/SKILL.md
```

**SKILL.md template:**
```markdown
---
name: <slug-in-kebab-case>
description: "<One sentence: when should this skill be used. Start with an action verb.>"
---

# <skill_name>

## Overview
<What this skill covers — 2 sentences.>

## Key Techniques
- <Technique 1>
- <Technique 2>
- <Technique 3>

## How to Apply
<Step-by-step guidance.>

## Examples
<Concrete examples from the source video.>

## Source
Extracted from: [<title>](https://www.youtube.com/watch?v=<video_id>)
Channel: <channel_name>
```

The **`description` frontmatter is the most important field** — Claude reads it to decide
whether to activate the skill. Make it specific and start with a verb (e.g. "Use when
reviewing pull requests with Claude Code", not "A skill about code review").

**Slug rules:** unique, kebab-case, lowercase, spaces→hyphens, special chars removed; add a
distinguishing prefix/suffix if the bare name is too generic (`claude-code-review`, not
`review`).

### Update data/skills.json
```json
{
  "videos_seen": ["<video_id>", "..."],
  "skills": [
    {"slug": "cursor-ai", "category": "code", "target_tool": "claude",
     "quality_score": 8, "source_video_id": "<video_id>"}
  ]
}
```
Keep the full per-skill records (with all fields above) in the `skills` array — the table
columns shown here are the minimum. Do not remove `videos_seen` entries.

---

## Step 4 — Tab 2: Models Ranking (rank ALL models)

Read `data/models.json` (create as `{}` if missing). For every AI **model** referenced
(across the skills you extracted), record name, version, category, company, country,
`open_source`, and its best `quality_score`. Match by exact name+version — never duplicate;
if a higher score appears for the same model, update it.

For **each category**, store both a podium and the complete ranking, plus a ready-to-display
ASCII podium string:

```json
{
  "code": {
    "podium": [
      {"rank": 1, "name": "Claude Sonnet", "version": "4.6", "company": "Anthropic", "score": 9.5},
      {"rank": 2, "name": "GPT-5", "version": "", "company": "OpenAI", "score": 9.2},
      {"rank": 3, "name": "Gemini", "version": "2.5 Pro", "company": "Google", "score": 9.0}
    ],
    "full_ranking": [
      {"rank": 1, "name": "Claude Sonnet", "version": "4.6", "company": "Anthropic",
       "score": 9.5, "open_source": false},
      {"rank": 2, "...": "..."}
    ],
    "ascii_podium": "<see format below>"
  }
}
```

- `podium` = top 3 (or fewer) by score.
- `full_ranking` = **ALL** models in the category, sorted by score desc, re-ranked from 1.
  Never cap the list — rank every model found.
- `ascii_podium` = a pure-ASCII (no emoji) podium for the dashboard / MCP, e.g.:

```
                CODE
               +------+
               |  #1  |
               | 9.5  |
        +------+------+------+
        |  #2  |Claude|  #3  |
        | 9.2  |Sonnet| 9.0  |
        |GPT-5 |      |Gemini|
        +------+------+------+
```
Fill rank/score/short-name cells; truncate names to fit the cell width and keep the box
aligned in a monospace font.

---

## Step 5 — Tab 3: Skills Improvement (merge overlaps)

Scan `data/skills.json`. For any two skills whose slugs clearly describe the **same tool**
(wording variant, or one is a subset of the other). **Skip the pair if either skill is frozen**
(Golden rule #8) — never merge a starred skill away. Otherwise:
1. Keep the stronger one (higher `quality_score`; tie → more tips).
2. Merge `tips`, `slash_commands`, `general_tips` into the keeper (dedup).
3. Append the deleted skill to `data/deleted_skills.json` with `reason: "merged into <keeper_slug>"` and a timestamp.
4. Append a record to `data/merge_log.json`:
```json
{"timestamp": "<ISO-8601>", "merged_from": "<slug>", "merged_into": "<keeper_slug>", "reason": "overlapping skills"}
```
5. Delete the now-redundant `skills/<slug>/SKILL.md` (or `other-skills/.../<slug>/SKILL.md`) folder of the merged-away skill.

---

## Step 6 — Tab 4: Tips & Commands

**data/tips.json**
```json
{
  "by_tool": { "<tool_name>": ["tip 1", "tip 2"] },
  "general": {
    "prompt engineering": [], "automation": [], "agents": [], "code": [],
    "parallel tasks": [], "self-improving systems": [], "harness code": []
  }
}
```
Append new tips to the right tool / general topic. No duplicates (case-insensitive). Read
the existing file first and merge.

**data/commands.json**
```json
{ "commands": [ {"command": "/review", "description": "...", "tool": "...", "source_video": "<video_id>"} ] }
```
Append new slash commands. No duplicates (match on `command`). Read existing first; merge.

---

## Step 7 — Tab 5: News summaries

The fetch stage already classified videos into `data/daily_news.json`,
`data/weekly_news.json`, `data/monthly_news.json` (newest→oldest, US-Eastern headers). For
each entry whose `summary` is empty/missing and whose `video_id` is in the current batch:
- Write a **two-sentence English summary** from the transcript/content.
- Fill the `summary` field.
- Also set `low_quality_source` and `video_quality_score` on the entry to match the video's
  Step 2b rating, so the News tab can badge low-quality items.

Re-save the three news files with the filled summaries. Do not reorder or change headers.

> The News tab ALSO merges official-site headlines (`data/daily_web_news.json` etc., produced
> by `src/news.py`) at display time, so the feed refreshes every day even when no new videos
> appeared. You never edit those web files here — only the video news files above.

---

## Step 8 — Tab 6: Connectors

Track **Claude connectors and MCP servers** mentioned in the video → `data/connectors.json`
(create as `{"connectors": []}` if missing).

For each connector / MCP server:
```json
{
  "name": "Filesystem MCP",
  "type": "mcp_server",                      // "mcp_server" | "connector"
  "provider": "Anthropic",
  "category": "integration",
  "what_it_does": "Two-sentence description.",
  "install_or_source": "npx / URL / repo if mentioned, else null",
  "official": true,
  "quality_score": 8,
  "source_video": "<video_id>",
  "source_url": "https://www.youtube.com/watch?v=<video_id>",
  "video_quality_score": 8,
  "low_quality_source": false
}
```
Dedup by `name` (case-insensitive); keep the higher `quality_score` and merge details. Read
the existing file first; append/update, never overwrite. Apply the Step 2b cap/flag here too:
if the source video is low quality, set `low_quality_source: true` and cap `quality_score` at
`video_quality_score`.

---

## Step 9 — Update the Run Report in status.json

Read `data/status.json` (the fetch stage initialized `run_report`). After processing the
batch, update — do not reset — these fields:

- `run_report.analyzed_this_run` += number of videos you fully analyzed this run
- `run_report.skipped_not_relevant` += videos skipped by the relevance gate
- `run_report.errors` += videos that errored (record briefly; keep going)
- `run_report.pending_to_analyze` = remaining count of `data/_pending/*.json`
- `total_videos_analyzed` (top-level, **cumulative all-time**) += videos analyzed this run
- `last_analyze` = current ISO-8601 timestamp
- `run_report.no_transcript` — leave as set by fetch (videos with no real transcript track,
  analyzed via description/title fallback).

Also write a ready-to-display ASCII run report into `run_report.ascii`:

```
+======================================================+
|            YOUTUBE SKILLS TRACKER  —  RUN            |
+======================================================+
| Run time (ET) ........ 2026-06-02 06:00              |
| Total in playlist .... 912                           |
| Already seen ......... 860                           |
| New found ............ 52                            |
| Analyzed this run .... 50                            |
| Skipped (not rel.) ... 1                             |
| Skipped (no transc.) . 1                             |
| Errors ............... 0                             |
| Pending remaining .... 2                             |
| Total analyzed (all) . 910                           |
+======================================================+
```

---

## Step 10 — Move processed files & commit (PER VIDEO)

This is not a final step — do it **for each video as you finish it** (Golden rule #1):

```bash
git config user.name "skills-tracker-bot"
git config user.email "actions@users.noreply.github.com"
git add data/ skills/ other-skills/
git commit -m "analyze: <video_id> — <short title>"
git push
```

Before committing each video, move its file
`data/_pending/<video_id>.json` → `data/processed/<video_id>.json` so it is never
re-analyzed. When the batch is done, `data/_pending/` holds only the videos left for the
next run. If a video produced no commit-worthy change, still move it to `processed/` and
commit (so it is not retried forever).

**If `git push` is rejected** ("non-fast-forward" / remote moved because the fetch stage
pushed): run `git pull --rebase --autostash` then `git push` again, and continue.

---

## Quick checklist per video
1. Relevance gate (Step 2) — skip if off-topic.
2. Rate video quality; flag + cap scores if low quality (Step 2b).
3. Extract skills + write/route SKILL.md packages (Step 3).
4. Update models ranking (Step 4).
5. Merge overlapping skills (Step 5).
6. Tips & commands (Step 6).
7. News summary + carry quality flag (Step 7).
8. Connectors (Step 8).
9. Update run report + cumulative count (Step 9).
10. Move pending→processed, commit & push (Step 10).
11. Stop after 50 videos; leave the rest for the next run.
