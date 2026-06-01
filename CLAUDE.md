# Claude Code Analysis Instructions

This file is read by the Claude Code GitHub Action to perform the analysis stage of the YouTube Skills Tracker pipeline.

## Overview

The fetch stage (src/fetch.py) has already run and written raw video records to `data/_pending/<video_id>.json`. Your job is to analyze each pending file and populate all five tracker tabs, then commit the results.

---

## Step 1 — Read pending files

Read every file matching `data/_pending/*.json`. Each file contains:
- `video_id` — YouTube video ID
- `title` — video title
- `description` — video description
- `publishedAt` — ISO-8601 publish timestamp
- `channel_name` — YouTube channel name
- `transcript` — English transcript (first 8000 chars), or description, or title
- `fetched_at` — ISO-8601 timestamp when the record was created

If there are no files in `data/_pending/`, there is nothing to do — skip to Step 7.

---

## Step 2 — Tab 1: Skills Library

For each pending video, analyze the transcript/content and extract ALL AI tools, models, skills, or techniques mentioned. For each extracted skill:

**Extract:**
- `skill_name` — exact tool/skill name including version if mentioned (e.g. "Claude Sonnet 3.7", "Cursor AI", "n8n")
- `category` — one of: design, code, automation, agents, image creation, video creation, writing, marketing, social, music, integration, research, productivity, other
- `description` — 2-sentence description of what it does
- `use_case` — primary use case as demonstrated in the video
- `output` — what the tool outputs/produces
- `quality_score` — integer 1–10 based on demonstrated capability, usefulness, and production-readiness
- `model_version` — model/version string if known, else null
- `company` — company or creator name
- `country` — company country of origin (e.g. "USA", "UK", "China")
- `open_source` — true/false
- `source_type` — "youtube"
- `source_url` — `https://www.youtube.com/watch?v=<video_id>`
- `is_claude_skill` — true if the skill is a Claude/Anthropic product, else false
- `tips` — list of 3 practical tips extracted from the video
- `slash_commands` — list of slash commands mentioned (e.g. "/review", "/test"), empty list if none
- `general_tips` — list of general tips not specific to one tool
- `relevance` — 1-sentence statement of why this skill is relevant to AI practitioners

**Compare with existing skills in data/skills.json:**
- If a skill with the same slug already exists: keep the higher quality_score version; merge tips lists (deduplicate); log the discarded version to `data/deleted_skills.json` with reason "superseded by higher quality record".
- If the skill is new: append it.

**Write a SKILL.md file** at `skills/<skill-slug>/SKILL.md` using this template:

```markdown
---
name: <skill-slug-in-kebab-case>
description: "<One sentence describing when Claude should use this skill. Start with an action verb.>"
---

# <skill_name>

## Overview
<Brief explanation of what this skill covers — 2 sentences.>

## Key Techniques
- <Technique 1>
- <Technique 2>
- <Technique 3>

## How to Apply
<Step-by-step guidance on using this skill.>

## Examples
<Concrete examples from the source video.>

## Source
Extracted from: [<title>](https://www.youtube.com/watch?v=<video_id>)
Channel: <channel_name>
```

**Skills folder structure is FLAT — no category subfolders:**
```
skills/
  prompt-chaining/SKILL.md
  cursor-ai/SKILL.md
  n8n-automation/SKILL.md
  ...
```

**Slug rules:**
- Must be unique, kebab-case, and descriptive
- Lowercase, spaces replaced with hyphens, special characters removed
- Include a distinguishing suffix if the tool name is too generic (e.g. `claude-code-review` not just `review`)

**The `description` frontmatter field is the most important field** — it is what Claude reads to decide whether to activate this skill. Make it specific, actionable, and start with a verb (e.g. "Use when reviewing pull requests with Claude Code", not "A skill about code review").

**Update data/skills.json** — append new/updated skill records to the `skills` array. The skills array stores objects with `slug` and `source_video_id` only (no `category` field needed):

```json
{
  "videos_seen": ["<video_id>", ...],
  "skills": [
    {"slug": "cursor-ai", "source_video_id": "<video_id>"},
    {"slug": "n8n-automation", "source_video_id": "<video_id>"}
  ]
}
```

---

## Step 3 — Tab 2: Models Ranking

Read `data/models.json` (create if missing: `{}`).

For every AI model found across all pending videos:
- Record its name, version, category, company, quality score (from skill records).
- Match by exact name+version — never create duplicates.
- Update the score if a higher score is found for the same model.

Structure of `data/models.json`:
```json
{
  "<category>": {
    "podium": [
      {"rank": 1, "name": "...", "version": "...", "company": "...", "score": 9},
      {"rank": 2, ...},
      {"rank": 3, ...}
    ],
    "full_ranking": [
      {"rank": 1, "name": "...", "version": "...", "company": "...", "score": 9, "open_source": false},
      ...
    ]
  }
}
```

- `podium` = top 3 models per category (or fewer if less than 3 exist).
- `full_ranking` = ALL models in that category sorted by score descending, re-ranked from 1.
- Rank EVERY model found — do not limit to top 10 or any other cutoff.

---

## Step 4 — Tab 3: Skills Improvement

Scan all skills in `data/skills.json`. For any two skills whose slugs overlap significantly (same tool, slight wording variation, or one is clearly a subset of another):
1. Keep the stronger one (higher quality_score; if equal, keep the one with more tips).
2. Merge tips, slash_commands, and general_tips from both into the keeper (deduplicate).
3. Back up the deleted skill to `data/deleted_skills.json` (append to array with reason "merged into <keeper_slug>").
4. Log the merge action to `data/merge_log.json` (append to array):

```json
{
  "timestamp": "<ISO-8601>",
  "merged_from": "<deleted skill slug>",
  "merged_into": "<keeper skill slug>",
  "reason": "overlapping skills"
}
```

---

## Step 5 — Tab 4: Tips & Commands

**data/tips.json** structure:
```json
{
  "by_tool": {
    "<tool_name>": ["tip 1", "tip 2", ...]
  },
  "general": {
    "prompt engineering": ["tip 1", ...],
    "automation": [...],
    "agents": [...],
    "code": [...],
    "parallel tasks": [...],
    "self-improving systems": [...],
    "harness code": [...]
  }
}
```

- Append new tips extracted from each pending video to the appropriate tool or general topic.
- No duplicates (compare case-insensitively).
- Read existing `data/tips.json` first; merge without overwriting.

**data/commands.json** structure:
```json
{
  "commands": [
    {"command": "/review", "description": "...", "tool": "...", "source_video": "<video_id>"}
  ]
}
```

- Append new slash commands found across all pending videos.
- No duplicates (match on `command` field).
- Read existing `data/commands.json` first; merge without overwriting.

---

## Step 6 — Tab 5: News summaries

For each entry in `data/daily_news.json`, `data/weekly_news.json`, `data/monthly_news.json` where `summary` is empty or missing:
- Find the corresponding pending file in `data/_pending/<video_id>.json`.
- Write a **two-sentence summary** of the video based on the transcript/content.
- Fill in the `summary` field for that entry.

Re-save all three news JSON files with the filled summaries.

---

## Step 7 — Move processed files

After successfully processing all pending files:
- Move each file from `data/_pending/<video_id>.json` to `data/processed/<video_id>.json`.
- Ensure `data/_pending/` is empty when done.

---

## Step 8 — Commit and push

```bash
git config user.name "skills-tracker-bot"
git config user.email "actions@users.noreply.github.com"
git add data/ skills/
git commit -m "analysis: update tabs from $(ls data/processed/*.json 2>/dev/null | wc -l) new videos"
git push
```

If there is nothing to commit (no pending files were processed), skip the commit.

---

## Important rules

- **Output language:** English only for all text, summaries, SKILL.md files, tips, and JSON values.
- **Never print or commit secret values** (API keys, tokens, etc.).
- **Preserve existing data** — always read existing JSON files before writing; append/update, never overwrite blindly.
- **Follow PIPELINE.md** for any details not covered here.
- **All JSON files** must be valid, pretty-printed (2-space indent), UTF-8.
- **Skills folder is FLAT** — `skills/<slug>/SKILL.md`, never `skills/<category>/<slug>/SKILL.md`.
- **skill slug in paths** must be filesystem-safe: lowercase, spaces replaced with hyphens, special chars removed.
