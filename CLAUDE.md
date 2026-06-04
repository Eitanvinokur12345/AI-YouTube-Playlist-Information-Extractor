# Claude Code Analysis Instructions

This file is read by the Claude Code GitHub Action to perform the **analysis stage** of
the YouTube Skills Tracker pipeline. The fetch stage (`src/fetch.py`) has already run and
written raw video records to `data/_pending/<video_id>.json`. Your job is to analyze each
pending file and populate the dashboard's data tabs, then commit the results.

**The data tabs you fill:**
1. **Skills Library** — `data/skills.json` — *reusable techniques & workflows only* (methods
   you apply: agent loops, prompt patterns, context engineering, a packaged image workflow…).
2. **Tools** — `data/tools.json` — *the products, models, apps and services themselves*
   (Gemini 2.5 Pro, Cursor, Midjourney, n8n, DeepSeek…). Tools and techniques are SEPARATE
   tabs — never put a bare product/model name in `skills.json` (see Step 3 vs Step 3b).
3. **Models Ranking** — `data/models.json` — every model, ranked per category with a podium.
4. **Tips & Commands** — `data/tips.json`, `data/commands.json`.
5. **News Feed** — `data/daily_news.json` / `weekly_news.json` / `monthly_news.json`.
6. **Connectors** — `data/connectors.json` — Claude connectors & MCP servers.
Plus **auto-discovered tabs**: when material keeps appearing that fits none of the tabs above,
log it as a *tab candidate* (Step 8b); the self-improvement stage may spin it into a new tab.

**Two principles that override convenience:**
- **Extract everything the video AND its surroundings offer.** Each video is a dense source —
  mine the transcript, the description, and every AI-relevant link (Step 2c) for *all* tools,
  techniques, models, tips, commands, connectors, news angles and notable claims. Missing a
  tool or a connector that was clearly shown is the main failure mode; be exhaustive.
- **Work at batch speed.** A run may need to clear ~50–100 videos. Be thorough but economical
  per video: capture every material item, but don't over-write prose. Commit after each video.

---

## Golden rules (read first)

1. **Process ONE video at a time, fully (all tabs), then COMMIT AND PUSH before moving to
   the next video.** This is mandatory. The run may be interrupted or time out at any moment
   — committing after every video guarantees no work is ever lost and the next run resumes
   cleanly from whatever is left in `data/_pending/`.
2. **Batch limit & order:** the analyze workflow tells you, in its prompt, **how many** videos
   to process this run and in **what order** (`newest_first` or `oldest_first`). Honor those
   exactly. Normally it is `analyze_batch_size` (50), oldest first. During **catch-up mode**
   (a massive addition of videos — see `data/catch_up.json` / the `catch_up` block in
   `config.json`) it is a large batch, **newest published first**, so the freshest knowledge
   lands first. Either way, leave any remainder in `data/_pending/` for the next run, and keep
   committing after every single video.
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
9. **Techniques vs. tools — route every extraction to the right tab.** A *technique/skill*
   (Step 3 → `skills.json`) is a reusable METHOD or workflow you apply. A *tool* (Step 3b →
   `tools.json`) is a product, model, app or service. The same video usually yields BOTH: put
   the product in `tools.json` and the specific way-of-using-it in `skills.json`. Never let a
   bare tool/model name become a "skill". This split is the #1 quality rule.
10. **Slash commands must be REAL commands.** Only record a `/command` that is an actual
    invocable command in a specific tool (a Claude Code command, a CLI/bot command), each with
    a clear "what it does". Reject prose, hashtags, file paths, "and/or" slashes, or generic
    words (see Step 6's filter). A wrong command is worse than a missing one.
11. **Hunt connectors & MCP servers actively.** These videos are full of MCP servers; they are
    high-value and easy to miss. Treat every `npx …-mcp`, Smithery entry, `mcpServers` config,
    or "connect X to Claude" as a Connector (Step 8).
12. **Capture orphans as tab candidates, never as junk.** Important, recurring material that
    fits none of the existing tabs goes to `data/tab_candidates.json` (Step 8b) — not forced
    into a tab where it doesn't belong.

---

## Step 1 — Pick up the pending batch

List `data/_pending/*.json` and take up to the batch size the workflow gave you, in the order
it gave you: **`oldest_first`** → sort by `fetched_at` ascending (the normal default);
**`newest_first`** → sort by `publishedAt` descending (catch-up mode, so the most recent videos
are analyzed first). Each file contains:

| field               | meaning                                                      |
|---------------------|--------------------------------------------------------------|
| `video_id`          | YouTube video ID                                             |
| `title`             | video title                                                  |
| `description`       | video description                                            |
| `publishedAt`       | ISO-8601 publish timestamp                                   |
| `channel_name`      | YouTube channel name                                         |
| `transcript`        | transcript (first 80,000 chars), or description, or title    |
| `transcript_lang`   | `"en"` / `"he"` / `""` (empty = a description/title fallback)|
| `transcript_source` | `"transcript"` \| `"description"` \| `"title"`               |
| `links`             | up to N AI-resource candidate URLs from the description (deny-filtered, may be `[]`) |
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

## Step 2c — Linked resources (follow AI-relevant links in the description)

Videos often point to where the real material lives — a GitHub repo collecting dozens of
agents, an "awesome-MCP" list, a tool's docs, a launch blog post. The fetch stage already
pulled up to `link_following.max_links_per_video` candidate URLs into the pending record's
**`links`** array (social / store / donation domains are already removed by the denylist).
This step mines those resources so their skills/models/connectors land in the tabs too.

Governed by the `link_following` block in `config.json` (`enabled`, `max_links_per_video`,
`max_items_per_resource`, `follow_for_low_quality_videos`). If `enabled` is false or `links`
is empty, skip this step entirely.

1. **Pick the AI-relevant links.** From `links`, keep only those that clearly relate to AI
   tools / skills / models / agents / connectors (judge by the URL and the surrounding
   description text). Drop anything off-topic that slipped through (merch, newsletters,
   unrelated docs). Follow at most `max_links_per_video`. If the video is LOW QUALITY
   (Step 2b), only follow links when `follow_for_low_quality_videos` is true.
2. **Fetch each chosen link with `WebFetch`.** This is the only stage allowed to use the
   network (the analyze workflow allow-lists `WebFetch`). If a fetch fails or times out,
   skip it silently and continue — never fail a video over a bad link.
3. **Extract on the resource's own merits.** Treat the fetched page as a *source* and run the
   same extraction as Steps 3 / 4 / 6 / 8 (skills, models, tips/commands, connectors). A
   single "awesome list" or multi-agent repo can yield MANY items — cap what you take from
   one resource at `max_items_per_resource`, keeping the clearly-useful ones. Score each item
   on the resource's own evidence; the source video's quality cap from Step 2b does **not**
   apply here (a linked resource is an independent source). Set `low_quality_source: false`
   unless the resource itself is weak.
4. **Attribution — tag every link-derived record**, in addition to the normal fields:
   - `source_type: "linked_resource"`
   - `source_url`: the followed link (the resource URL, NOT the video)
   - `discovered_via: "video_description_link"`
   - `via_video_id`: the `<video_id>` whose description contained the link
   - `source_video_id`: keep `<video_id>` too, so it still ties back to the video
   (For connectors, likewise set `source_url` to the link and add `via_video_id`.)
5. **Dedup exactly like the video path.** Use the same compare-and-keep-best by `slug`
   (Step 3) / by `name` (Step 8). A linked-resource skill that collides with an existing one
   merges normally; add the resource's `via_video_id` to `endorsement_video_ids`. Always
   respect Golden rule #8 (never touch a frozen record).

Everything from this step is committed together with the video in Step 10.

---

## Step 3 — Tab: Skills Library  (TECHNIQUES & WORKFLOWS ONLY)

This tab holds **reusable techniques, workflows and packaged skills** — the *methods you
apply*, not the products you apply them with. What BELONGS here: "Claude agent loop",
"context-engineering for long tasks", "the nano-banana image pipeline", "multi-agent code
review", "3D website build workflow", a Claude Code SKILL you can install. What does NOT belong
here (these go to **Step 3b → `tools.json`**): "Gemini 2.5 Pro", "Cursor", "Midjourney", "n8n",
"DeepSeek", "ChatGPT" — those are *tools/models/products*.

**Routing test (apply to every candidate):** "Is this a *way of doing something* (technique)
or a *thing that does it* (tool)?" Technique → here. Tool/model/app/service → Step 3b. A
product that ships an applicable, repeatable workflow yields TWO records: the product in
`tools.json`, and the technique in `skills.json` with `target_tool` pointing at the product.
When in doubt and it's just a named product → `tools.json`, not here.

For each genuine **technique** build a skill record:

- `skill_name` — the technique's name (e.g. "Claude Agent Loop", "Context Engineering for
  Long Tasks", "Nano-Banana Image Pipeline"). NOT a bare product/model name — those are tools.
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
- `compatibility` — **which AI tools this skill/technique works with, and up to which
  version**. A list of objects: `[{ "tool": "Claude", "up_to_version": "Sonnet 4.6" },
  { "tool": "ChatGPT", "up_to_version": "GPT-5" }, { "tool": "Gemini", "up_to_version":
  "2.5 Pro" }]`. Decide the list with **reasonable inference, not only literal mentions**:
  - **Generic, tool-agnostic techniques** (prompting patterns, chain-of-thought, ReAct,
    agent/RAG designs, context engineering, multi-step workflows) → also list the mainstream
    tools they obviously apply to (typically **Claude, ChatGPT, Gemini**, plus any others the
    video centers on), even if only one was demonstrated. Use `"up_to_version": "any"` for an
    inferred entry (you don't know its version ceiling).
  - **Tool-specific features** (a Claude Code slash command, a Gemini Gem, a ChatGPT Custom
    GPT, an MCP-only integration, or a product like Cursor / n8n) → list ONLY the tool(s) they
    actually run on. Never infer cross-tool support that cannot exist.
  When the video explicitly shows a tool **and** version, use that exact version (e.g.
  "Sonnet 4.6") instead of "any". If there is genuinely no signal at all, default to a single
  entry from `target_tool` (e.g. `[{ "tool": "Claude", "up_to_version": "any" }]`). Capitalize
  tool names for display.
- `multi_tool` — boolean; `true` when `compatibility` lists **2+ distinct tools**. The
  dashboard badges these and offers a "multi-tool only" filter, so set it accurately.
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
**Token-saver — check the compact index first.** `data/skills.json` grows large, so don't
re-read the whole file for every skill. If **`data/index.json`** exists (a compact
`{slug: {score, video_quality_score, starred, target_tool}}` map the improve stage maintains),
look up your new skill's `slug` there first. **Absent → it's a new skill:** append the record
without deep-reading the existing ones. **Present → a collision:** read just what you need
from `data/skills.json` to run the merge below. If `data/index.json` is missing, fall back to
reading `data/skills.json` directly.

**Then check Golden rule #8:** if the existing skill is frozen
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
- **Union** `compatibility` into the keeper: dedup by `tool` (case-insensitive); when the same
  tool appears in both, keep the **higher** `up_to_version` (a later video may prove a newer
  version works). Then recompute `multi_tool` (`true` if 2+ tools remain).
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

## Step 3b — Tab: Tools  (PRODUCTS, MODELS, APPS & SERVICES)

Every named **tool, model, app, platform or service** the video (or a followed link) shows
goes here → `data/tools.json` (`{"tools":[...]}`, create if missing). This is the catalog of
*things*, ranked by how often the playlist mentions them. Be exhaustive: if it has a brand name
and you could go use it, it belongs here — even when it also produced a technique in Step 3.

Tool record:
- `name` — exact name incl. version where shown (e.g. "Gemini 2.5 Pro", not "Gemini").
- `slug` — kebab-case unique id (slug rules in Step 3).
- `category` — one of `config.categories`.
- `company`, `country` — maker and country of origin (or null).
- `open_source` — true/false.
- `description` — 1–2 factual sentences on what it is and does.
- `quality_score` — integer 1–10 (same rubric as skills); capped by Step 2b if the source video is low-quality.
- `model_version` — version string, or null.
- `target_tool` — ecosystem it belongs to/extends (`"claude"`, `"gemini"`, `"openai"`, …, or `"other"`).
- `endorsement_video_ids` — video ids that featured it; initialize `["<video_id>"]`.
- `mentions` — `len(endorsement_video_ids)` (how many playlist videos reference it).
- `source_video_id`, `source_url`, `video_quality_score`, `low_quality_source` — as elsewhere.

**Dedup by `slug` (and obvious name aliases).** If the tool already exists: union
`endorsement_video_ids` (recompute `mentions`), keep the higher `quality_score`, keep the
richer `description`, and fill any missing `model_version`/`company`/`country`. Never split one
product across two slugs — merge aliases (e.g. "perplexity-ai" → "perplexity").

After updating, **re-sort `tools.json` by `mentions` desc, then `quality_score` desc, then
`name`** so the catalog stays ranked. Tools do NOT get a SKILL.md folder (only techniques do).

> Models are a *subset* of tools: when a tool is an AI model, ALSO add/update it in
> `models.json` (Step 4). Tools = the full catalog; Models = the ranked-by-category view.

---

## Step 4 — Tab: Models Ranking (rank ALL models)

Read `data/models.json` (create as `{}` if missing). For every AI **model** referenced
(across the skills you extracted), record name, version, category, company, country,
`open_source`, and its best `quality_score`. Match by exact name+version — never duplicate;
if a higher score appears for the same model, update it.

**Use the right model categories — not just one or two.** Sort each model into the category
that fits its PURPOSE, and always maintain at least these when models exist for them: `code`,
`image creation`, `video creation`, `productivity` — plus any other of `config.categories`
that apply (`agents`, `design`, `research`, `writing`, `music`, …). A coding model → `code`;
an image model (Nano Banana, Midjourney, Flux) → `image creation`; a video model (Seedance,
Kling, Runway, Veo, Sora) → `video creation`; a general chat/assistant model → `productivity`.
Do NOT collapse everything into one bucket — the dashboard shows a medal podium per category,
so populate every category the videos actually cover.

For **each category**, store a podium and the complete ranking. **Do NOT generate an
`ascii_podium`** — the dashboard renders the podium as HTML and the MCP server renders ASCII
from these numbers at read-time, so writing an ASCII string here only burns tokens. Store the
data only:

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
    ]
  }
}
```

- `podium` = top 3 (or fewer) by score.
- `full_ranking` = **ALL** models in the category, sorted by score desc, re-ranked from 1.
  Never cap the list — rank every model found.
- If a file already contains an old `ascii_podium` field, just leave it (or drop it); never
  spend effort creating or refreshing one — the read side draws the podium from the data.

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
the existing file first and merge. Keep tips **tight and de-duplicated**: each tip is one
actionable sentence; merge near-duplicates into the single clearest version rather than listing
both; aim for the strongest ~8–12 tips per tool and per topic, not an exhaustive dump. Quality
over volume — the Tips tab must stay skimmable.

**data/commands.json** — REAL slash commands only.
```json
{ "commands": [ {"command": "/review", "description": "what it does", "tool": "Claude Code", "source_video": "<video_id>"} ] }
```
A record qualifies ONLY if ALL hold:
- it starts with `/` and is a single invocable token (`/review`, `/agents`, `/ultra-plan`) —
  letters/digits/hyphens only, no spaces inside the command itself;
- it is an ACTUAL command in a specific tool (Claude Code, a CLI, a chatbot) — name that tool in `tool`;
- you can state precisely what it does in `description`.
**Reject** (do NOT add): prose or a sentence after the slash, hashtags, URLs / file paths,
fractions or "and/or" slashes ("client/server", "24/7"), section numbers, and generic words
that aren't real commands. When unsure, leave it out. Dedup on `command` (case-insensitive);
read existing first and merge.

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

## Step 8 — Tab: Connectors  (HUNT FOR MCP SERVERS — high priority)

These videos are full of **Claude connectors and MCP servers**, and they are the single
easiest thing to under-extract. Actively scan every video and every followed link for them and
record each → `data/connectors.json` (create as `{"connectors": []}` if missing). Signals that
mean "connector/MCP, capture it": an `npx …-mcp` / `uvx` install line, a `mcpServers` JSON
block, a Smithery / mcp.so / "awesome-mcp" listing, a GitHub repo whose name ends in `-mcp`,
"connect <service> to Claude", a Claude.ai Connectors-page entry, or a Desktop/Code config
snippet. Err toward capturing — a real MCP server missed is a real loss for this tab.

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
  "source": "where it comes from / who makes it (e.g. 'Anthropic', 'community', 'Smithery')",
  "url": "homepage / repo / install URL if known, else null",
  "free": "yes",                             // "yes" | "no" | "freemium"
  "free_tokens": "free tier / quota if any (e.g. '500 calls/mo', 'unlimited'), else null",
  "paid_version": "paid plan name + price if any (e.g. 'Pro $20/mo'), else null",
  "works_in": "both",                        // "claude chat" | "claude code" | "both"
  "source_video": "<video_id>",
  "source_url": "https://www.youtube.com/watch?v=<video_id>",
  "video_quality_score": 8,
  "low_quality_source": false
}
```
The six fields **`source`, `url`, `free`, `free_tokens`, `paid_version`, `works_in`** are
required so the Connectors tab can show, at a glance, where each MCP/connector comes from,
whether it is free, what the free quota is, the paid upgrade, and which Claude surface it runs
in. Fill them from the video; use `null` only when the video genuinely gives no signal.
`free` is `"yes"` (fully free / open-source), `"no"` (paid only), or `"freemium"` (free tier +
paid plan). `works_in` is `"claude chat"`, `"claude code"`, or `"both"`.

Dedup by `name` (case-insensitive); keep the higher `quality_score` and merge details. Read
the existing file first; append/update, never overwrite. Apply the Step 2b cap/flag here too:
if the source video is low quality, set `low_quality_source: true` and cap `quality_score` at
`video_quality_score`.

---

## Step 8b — Capture tab candidates (feeds auto-discovered tabs)

Sometimes a video keeps pushing material that is clearly important but fits **none** of the
tabs above (Skills techniques, Tools, Models, Tips, Commands, News, Connectors) — a whole theme
the tracker has no home for (e.g. "AI hardware devices", "AI regulation & policy", "AI voice
agents" as a distinct class). Do NOT force it into a wrong tab and do NOT drop it. Instead
append an **anecdote** to `data/tab_candidates.json` (`{"candidates":[...]}`, create if missing):

```json
{ "theme": "ai-voice-agents",
  "label": "AI Voice Agents",
  "note": "Video builds a phone agent with a realtime voice API — no skills/tools/news fit.",
  "video_id": "<video_id>", "source_url": "https://www.youtube.com/watch?v=<video_id>",
  "ts": "<ISO-8601>" }
```
Use a stable kebab `theme` so repeats across videos pile up under the same key — that recurrence
is exactly what later promotes a theme to a real tab. At most one or two candidates per video;
this is for genuine orphans, not for everything. The self-improvement stage clusters these and,
once a theme recurs across enough distinct videos, spins it into its own announced tab (with a
"NEW" badge for its first week).

---

## Step 9 — Update the Run Report in status.json

Read `data/status.json` (the fetch stage initialized `run_report`). After processing the
batch, update — do not reset — these fields:

- `run_report.analyzed_this_run` += number of videos you fully analyzed this run
- `run_report.skipped_not_relevant` += videos skipped by the relevance gate
- `run_report.errors` += videos that errored (record briefly; keep going)
- `run_report.pending_to_analyze` = remaining count of `data/_pending/*.json`
- `total_videos_analyzed` (top-level, **cumulative all-time**) += videos analyzed this run
- `total_tools` (top-level) = total entries in `data/tools.json`
- `run_report.tab_candidates_open` = total entries in `data/tab_candidates.json`
- `last_analyze` = current ISO-8601 timestamp
- `run_report.no_transcript` — leave as set by fetch (videos with no real transcript track,
  analyzed via description/title fallback).

**Do NOT write a `run_report.ascii` string** — the dashboard and the MCP server render the
run-report box from the numeric fields above at read-time, so generating ASCII here only
burns tokens. Just keep the numeric `run_report` fields accurate; leave any pre-existing
`run_report.ascii` value alone.

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
3. Follow AI-relevant description links; extract on their own merits + tag `linked_resource` (Step 2c).
4. Extract **techniques** → skills.json + route SKILL.md packages (Step 3) — index-first dedup.
5. Extract **tools / models / apps** → tools.json, ranked by mentions (Step 3b).
6. Update models ranking per category — data only, no ASCII (Step 4).
7. Merge overlapping skills/tools (Step 5).
8. Tips + REAL slash commands only (Step 6).
9. News summary + carry quality flag (Step 7).
10. Connectors / MCP servers — hunt hard (Step 8).
11. Capture genuine orphans as tab candidates (Step 8b).
12. Update run report + cumulative counts — data only, no ASCII (Step 9).
13. Move pending→processed, commit & push (Step 10).
14. Stop after the batch limit; leave the rest for the next run.
