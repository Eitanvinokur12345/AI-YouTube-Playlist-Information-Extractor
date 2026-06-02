# Self-Improvement Protocol (every few days)

This file is read by the Claude Code GitHub Action in the **improvement stage**
(`.github/workflows/improve.yml`, runs every few days — cadence set by `self_improvement.cadence`). It is separate from the analysis stage
(`CLAUDE.md`). Where analysis *adds* new knowledge from videos, this stage *curates* what is
already there: it deduplicates, repairs, calibrates ratings, protects the best skills with a
**star (freeze)**, reviews the dashboard, optimizes for tokens, and writes a health report.

The behavior is configured by the `self_improvement` block in `config.json`. Read that block
first and obey it. If `self_improvement.enabled` is `false`, do nothing and exit.

---

## Golden rules (read first)

1. **NEVER modify, merge, rescore, recategorize, or delete a FROZEN record.** A record is
   frozen if its `slug` appears in `data/stars.json` **or** the record itself has
   `"starred": true` or `"locked": true`. Starred = "proven excellent, keep in its original
   form forever." This rule overrides every module below. The only thing you may do to a
   frozen record is *read* it and stamp it `"starred": true` for consistency (Module 4).
2. **Autonomy is split** (`self_improvement.autonomy: "safe_auto_suggest_risky"`):
   - Operations listed in `self_improvement.safe_auto` you may **perform automatically**.
   - Operations listed in `self_improvement.suggest_only` you must **NOT perform**. Instead
     write a *proposal* to `data/improvement_suggestions.json` for the user to approve later.
   - The ONE exception: a suggestion the user has already approved (its id is in
     `data/approvals.json` → `approved_ids`) — you apply it this run (see Step 1).
3. **Respect the caps** in `self_improvement.caps` (max merges / deletes / rescores per run,
   max UI changes per week). Stop an operation type once its cap is reached; defer the rest.
4. **Never auto-star and never auto-unstar.** Stars are the user's call. You may *propose*
   `star_suggestions`, but only the user (via the dashboard / MCP) adds to `stars.json`.
5. **Token discipline.** Stay under `self_improvement.token_budget_per_run`. Work
   incrementally: prefer reading `data/index.json` over every file; only deep-read records
   changed since `status.last_improved_at`. If you approach the budget, finish the current
   safe operation, write the audit + health report, and stop cleanly.
6. **Preserve data & never lose work.** Always read a JSON file before writing it. Back up
   anything you remove to `data/deleted_skills.json`. All JSON: valid, 2-space indent, UTF-8.
7. **Never print or commit secrets.**
8. **Commit after each module** (Step 10 commit recipe) so a timeout never loses progress.

---

## Step 0 — Load state

Read, creating sane defaults if missing:
- `config.json` → the `self_improvement` block (enabled, autonomy, modules, safe_auto,
  suggest_only, caps, token_budget_per_run, ux_review_min_interval_days) **and** the
  `catch_up` block (`enabled`, `curation`).
- `data/catch_up.json` → `{ "active": bool, "mode": ... }` (default `{"active": false}`).
- `data/status.json` → note `last_improved_at`, `last_ux_review` (may be absent on first run).
- `data/stars.json` → `{ "starred": [ {slug, reason, starred_at} ] }` (default `{"starred":[]}`).
- `data/approvals.json` → `{ "approved_ids": [], "dismissed_ids": [] }` (default both empty).
- `data/improvement_suggestions.json` → `{ "suggestions": [] }`.
- `data/improvement_audit.json` → `{ "runs": [] }`.

Build the frozen-slug set = every slug in `stars.json.starred[*].slug` ∪ every skill/connector
with `starred==true` or `locked==true`. Keep this set in mind for ALL later steps.

**Catch-up light mode.** If `catch_up.active` is true **and** `config.catch_up.curation ==
"light_until_caught_up"`, the library is still mid-ingest, so do **not** curate half-finished
data. This run, perform ONLY the cheap, safe modules — **Step 2 (data hygiene / exact-dup /
consistency), Step 8 (health report), and Step 9 (audit)** — and **SKIP** Steps 3–7b
(near-duplicate, ratings calibration, stars, UX self-review, trend/new-tab detection,
feed-health proposals). Still apply already-approved suggestions (Step 1). Record
`"mode": "light (catch-up)"` in the audit and set `health.json.note` to say curation is paused
until the backlog clears. Full curation resumes automatically on the next run after catch-up ends.

**Idle early-exit (token-saver).** If catch-up is *not* active and **nothing has changed**
since `status.last_improved_at` — no ids in `approvals.approved_ids`; `data/processed/` has not
grown since the count recorded in the last `improvement_audit.json` run; no news feed has
crossed the fail-streak threshold since the last run; and the previous health report listed no
open schema / orphan / exact-duplicate issues — then this is a quiet run. Do ONLY `build_index`
(Step 2's index), the health report (Step 8) and the audit (Step 9); tag the audit
`"mode": "idle (no changes)"`; commit and stop. Skip Steps 1 and 3–7b. This keeps a no-work
day nearly free of tokens.

---

## Step 1 — Apply already-approved suggestions (do this FIRST)

For each suggestion in `improvement_suggestions.json` whose `id` is in
`approvals.json.approved_ids` and whose `status` is still `"pending"`:
- Apply its `proposed_change` **unless** it touches a frozen record (then skip it and set the
  suggestion `status:"skipped_frozen"`).
- Honor the relevant cap (e.g. an approved merge still counts against `max_merges_per_run`).
- Set the suggestion `status:"applied"`, add `applied_at` (ISO-8601).
- If the change deleted/merged a skill, back it up to `deleted_skills.json` and log to
  `merge_log.json` exactly as the analysis stage does.
Then remove those ids from `approved_ids` (they are done). Record each applied id in the audit.

---

## Step 2 — Module 1: Data hygiene, dedup & consistency  (SAFE-AUTO)

Only if `modules.data_hygiene` is true. These are all in `safe_auto`, so perform them:

- **`build_index`** → write `data/index.json`: a compact array of every skill
  `{slug, skill_name, category, quality_score, target_tool, source_video_id, starred}` plus
  top-level counts. This is the cheap file every later step (and the MCP/dashboard) reads
  first to avoid loading all heavy records.
- **`schema_repair`** → fix malformed records in place: missing `slug` (derive kebab-case
  from name), missing `category` (set `"other"`), `quality_score` out of 1–10 (clamp),
  missing `target_tool` (default `"claude"`), non-array `tips`/`slash_commands` (coerce to
  `[]`). For skills missing the cross-tool fields, backfill **safely without inventing**: if
  `compatibility` is absent/empty, set it to a single entry from `target_tool`
  (`[{ "tool": "<Target>", "up_to_version": "any" }]`, capitalized); then set `multi_tool` to
  `len(compatibility) > 1`. Never add tools the record doesn't already evidence — only the
  default-from-`target_tool` is allowed here; richer cross-tool data comes from the analyze
  stage. Do not invent scores or descriptions.
- **`orphan_cleanup`** → reconcile folders ↔ `skills.json`:
  - A `skills/<slug>/SKILL.md` (or `other-skills/<tool>/<slug>/`) with **no** matching skill
    record → record it as an orphan; if clearly stale (slug not anywhere in skills.json),
    move the folder away is *risky* → instead **suggest** `orphan_folder` removal. (Do not
    auto-delete skill folders.)
  - A skill record with `quality_score>=5` but **no** package folder → recreate the missing
    `SKILL.md` from the record (safe; restores expected output).
- **`exact_duplicate_merge`** → only EXACT duplicates (identical `slug`, or identical
  normalized `skill_name`+`company`). Keep the higher `quality_score`, merge
  tips/slash_commands/general_tips, back up the loser to `deleted_skills.json`, log to
  `merge_log.json`, delete the loser's folder. **Skip if either side is frozen.** Counts
  against `max_merges_per_run`.
- **`fill_missing_summaries`** → for news entries (`daily/weekly/monthly_news.json`) whose
  `summary` is empty but whose source video is already in `data/processed/`, write the
  two-sentence English summary from the processed record. Do not refetch anything.
- **`cross_tab_consistency`** → make tabs agree: every model in `models.json` should trace to
  a skill; `status.total_skills` should equal the real count; a starred slug should be
  stamped `"starred": true` on its skill record (see Module 4); commands in `commands.json`
  should reference a known tool. Fix counts and flags; *suggest* anything ambiguous.

---

## Step 3 — Module 1b: Near-duplicates  (SUGGEST-ONLY)

`fuzzy_duplicate_merge` is in `suggest_only`. Detect skills that are *probably* the same tool
(very similar names, one a subset of the other, same company + overlapping use-case) but are
not exact matches. For each candidate pair (neither side frozen), write a suggestion:

```json
{ "id": "<stable-hash>", "type": "fuzzy_duplicate_merge",
  "detail": "‘claude-code-reviewer’ and ‘claude-pr-review’ look like the same skill.",
  "proposed_change": { "action": "merge", "merge_from": "claude-pr-review",
                       "merge_into": "claude-code-reviewer" },
  "created_at": "<ISO-8601>", "status": "pending" }
```
Do **not** merge them now. Cap the number of new suggestions sensibly; do not re-propose a
pair that already has a pending/dismissed suggestion (match on the stable `id`).

---

## Step 4 — Module 2: Ratings calibration & category hygiene  (SUGGEST-ONLY)

Only if `modules.ratings_and_locking` is true. `rescore_outliers` and `recategorize` are
suggest-only. Using `index.json`:
- **Rescore outliers** — flag scores that look miscalibrated against the rubric in CLAUDE.md
  (e.g. a barely-demonstrated tool scored 9, or a clearly production-grade tool scored 3),
  and scores far from the median of their category. Propose a new score with a one-line
  reason. Never rescore a frozen record.
- **Recategorize** — flag skills whose `category` clearly mismatches their description.
  Propose the better category (must be one of `config.categories`).
Write these as `rescore_outliers` / `recategorize` suggestions (same shape as Step 3). Respect
`max_rescores_per_run` for how many you bother to propose. Apply none of them now.

---

## Step 5 — Module 3: Stars (freeze best-in-class)

Only if `modules.ratings_and_locking` is true.
- **Apply stars (SAFE):** for every slug in `stars.json`, ensure its skill/connector record
  has `"starred": true` and `"locked": true`, and ensure it is sorted/marked so the dashboard
  shows it first. This is the consistency stamp; it is the only write Module 4 makes.
- **Propose stars (SUGGEST, very rare):** `star_suggestions` is suggest-only — NEVER auto-add
  to `stars.json`. Stars are reserved for an exceptional handful. Obey the
  `self_improvement.stars` config exactly:
  - **Quota cap:** if `len(stars.json.starred) >= stars.max_total` (default 10), propose
    nothing — the freeze quota is full.
  - **Per-run cap:** propose at most `stars.max_suggestions_per_run` (default 1).
  - **ALL of `stars.proposal_criteria` must hold for a candidate:**
    1. `quality_score >= min_quality_score` (default 9.5 — in practice a 10/10),
    2. `require_cited_popularity`: the skill's `popularity_signals` is **non-empty** (the
       videos cited real adoption — downloads, GitHub stars, "most used", etc.),
    3. `require_multi_video_endorsement`: `len(endorsement_video_ids) >= min_endorsing_videos`
       (default 2 — independently endorsed across multiple videos).
  - Skip any skill already starred, or that already has a pending/dismissed star_suggestion.
  - Put the evidence in `detail` so the user can decide in seconds. Write a `star_suggestion`:
```json
{ "id": "<stable-hash>", "type": "star_suggestion",
  "detail": "claude-artifact-ui - 10/10, video cited '180k GitHub stars', endorsed in 4 videos.",
  "proposed_change": { "action": "star", "slug": "claude-artifact-ui",
                       "reason": "Top score + cited popularity + multi-video endorsement." },
  "evidence": { "quality_score": 10, "popularity_signals": ["180k GitHub stars"], "endorsing_videos": 4 },
  "created_at": "<ISO-8601>", "status": "pending" }
```
The user stars/unstars via the dashboard's MCP tools (`star_skill` / `unstar_skill`), which
edit `stars.json` (enforcing `max_total`). You only ever *read* `stars.json` and stamp the flag.

---

## Step 6 — Module 4: Dashboard / UX self-review  (SUGGEST-ONLY, rate-limited)

Only if `modules.ux_self_review` is true **and** at least `ux_review_min_interval_days` days
have passed since `status.last_ux_review` (else skip this module). `ui_changes` is suggest-only
and capped by `caps.max_ui_changes_per_week`.

Review `docs/index.html` + `docs/dashboard.js` as a critical user would: clarity of the six
(now seven) tabs, whether counters surface the right numbers, empty-state messaging, mobile/PWA
layout, contrast/readability, whether starred skills are visually obvious, whether the
token-renewal warning is prominent. Write at most one or two concrete `ui_change` suggestions:
```json
{ "id": "<stable-hash>", "type": "ui_change",
  "detail": "Starred skills aren’t visually distinct enough on mobile.",
  "proposed_change": { "file": "docs/dashboard.js",
                       "change": "Add a gold ★ badge and a subtle border to starred cards." },
  "created_at": "<ISO-8601>", "status": "pending" }
```
Do not edit `docs/` in this module — only propose. (Approved `ui_change`s are applied in Step 1
on a later run, and count against `max_ui_changes_per_week`.) Set
`status.last_ux_review` to now whenever this module runs.

---

## Step 7 — Module 6: Trend detection & new dashboard tabs  (AUTO-CREATE, announced & capped)

Only if `modules.trend_tabs` is true and `dynamic_tabs.enabled` is true. This is the one place
you may add to the dashboard automatically — the user explicitly delegated tab creation to you
— but it is tightly governed by `self_improvement.dynamic_tabs`, and every creation is announced.

**Goal:** spot a recurring, important theme across the videos that does NOT fit any existing
tab, and give it its own tab so the user *sees* the trend.

**Detect.** Using `index.json`, `data/processed/*`, skills, news, and connectors, look for a
coherent theme (a topic, a recurring workflow, a class of tool/news) that:
- appears across **>= `dynamic_tabs.min_evidence_videos`** distinct videos (default 5), AND
- does **not** belong to any existing tab purpose — not one of `dynamic_tabs.reserved_tab_ids`
  (skills, models, improvement, tips, news, connectors, selfimprove) and not an already-active
  dynamic tab, AND
- is genuinely useful to surface on its own (not a rephrasing of an existing tab).

**Guards — create nothing if any fails:**
- Active tabs in `data/extra_tabs.json` (status `active`) already `>= dynamic_tabs.max_total_active`
  (default 6).
- A tab was already created within the last 7 days (`caps.max_new_tabs_per_week`, default 1).
- The `trend_key` was previously **dismissed** by the user (status `dismissed`) — never recreate it.
- Create **at most one** new tab per run.

**Create.** Append a spec to `data/extra_tabs.json` (`{ "tabs": [...] }`, create if missing).
The dashboard renders any active tab here generically — **no code change needed**:
```json
{ "id": "ai-safety-policy", "title": "AI Safety & Policy",
  "trend_key": "ai-safety-policy",
  "description": "A recurring theme across recent videos that did not fit the other tabs.",
  "created_at": "<ISO-8601>", "status": "active",
  "evidence_video_ids": ["<id1>", "<id2>", "<id3>", "<id4>", "<id5>"],
  "items": [
    { "title": "<headline>", "sub": "<source / channel / date>",
      "body": "<2-sentence English summary>", "url": "https://www.youtube.com/watch?v=<id>" }
  ] }
```
- `id` / `trend_key`: kebab-case, unique, never one of `reserved_tab_ids`.
- Populate `items` from the evidence (newest first), factual English summaries.

**Announce (required — "I want to know it").** Whenever you create a tab:
- Add a `created_tab` entry to this run's audit record (Step 9: id, title, evidence count).
- Set `data/health.json` → `new_tab_announcement` to a one-line note (the dashboard shows a
  "NEW TAB" highlight).
- Set `status.last_tab_created` = now.
The user can dismiss a tab via the MCP tool `dismiss_dynamic_tab(id)` (sets status `dismissed`);
after that you must never recreate that `trend_key`.

---

## Step 7b — Module 7: News-feed health  (SUGGEST-ONLY)

Only if `modules.health_and_cadence` is true (shares the health gate). The news stage
(`src/news.py`) writes `data/feeds_health.json` every run with a per-feed `fail_streak`
(consecutive runs that returned nothing). `drop_dead_feed` is in `suggest_only`, so **NEVER
edit `config.json` yourself here** — only propose. Read `data/feeds_health.json` (skip this
module if it's missing or empty). For each feed whose
`fail_streak >= self_improvement.feed_health.fail_streak_threshold` (default 5) — effectively a
dead feed — write one `drop_dead_feed` suggestion (do not re-propose a feed that already has a
pending/dismissed one, match on the stable `id`):

```json
{ "id": "<stable-hash>", "type": "drop_dead_feed",
  "detail": "'The Register AI/ML' has returned nothing for 11 runs straight (last error: fetch failed). Consider removing it from config.news_sources.",
  "proposed_change": { "action": "remove_news_source", "name": "The Register AI/ML",
                       "url": "https://www.theregister.com/software/ai_ml/headlines.atom" },
  "evidence": { "fail_streak": 11, "last_ok": "2026-05-01T00:00:00+00:00",
                "last_error": "fetch failed (network/HTTP)" },
  "created_at": "<ISO-8601>", "status": "pending" }
```

The user approves removals via the dashboard / MCP. An approved `drop_dead_feed` is applied in
Step 1 on a later run by removing that one entry from `config.news_sources` (this is the only
case where the improve stage edits `config.json`, and only because the user approved it). Count
proposals in the audit's `suggested.drop_dead_feed`.

---

## Step 8 — Module 5: Health report + cadence advice  (ADVISORY, SAFE to write)

Only if `modules.health_and_cadence` is true. `health_report` is safe-auto. Compute and write
`data/health.json`:

```json
{
  "generated_at": "<ISO-8601>",
  "score": 0-100,
  "metrics": {
    "total_skills": 0, "starred": 0, "missing_summaries": 0, "schema_issues": 0,
    "orphan_folders": 0, "exact_duplicates_open": 0, "fuzzy_dupe_suggestions": 0,
    "rescore_suggestions": 0, "pending_suggestions": 0, "pending_to_analyze": 0,
    "avg_quality_score": 0.0, "active_dynamic_tabs": 0, "unhealthy_feeds": []
  },
  "token_optimization": {
    "index_built": true, "biggest_files": [ {"file": "skills.json", "kb": 0} ],
    "advice": "One line on how to keep token use low next run."
  },
  "cadence_advice": "e.g. 'Backlog is 0 — fetch cadence of 48h is fine.' or 'Backlog growing — consider analyzing more often.'",
  "new_tab_announcement": "",
  "advice": [ "Top 1–3 plain-English recommendations for the user." ],
  "history": [ {"date": "<date>", "score": 0} ]
}
```
`score` is your honest 0–100 rating of data health (deduct for schema issues, orphans, open
exact duplicates, large unindexed files, big analyze backlog). Append today's `{date, score}`
to `history` (keep the last ~60). This module is advisory: it does not change skills.

Set `metrics.unhealthy_feeds` to the names of feeds in `data/feeds_health.json` whose
`fail_streak >= self_improvement.feed_health.fail_streak_threshold` (read-only here — proposing
their removal is Step 7b). Use `[]` if `feeds_health.json` is missing.

`token_optimization` also covers `self_improvement.token_budget_per_run`: note in `advice` if
this run came close to the budget and what to trim.

---

## Step 9 — Write the audit record

Append one run summary to `data/improvement_audit.json` → `runs` (keep the last ~60 runs):

```json
{ "run_at": "<ISO-8601>", "duration_note": "ok",
  "applied": { "approved_suggestions": [], "exact_merges": 0, "schema_fixes": 0,
               "summaries_filled": 0, "stars_stamped": 0, "index_built": true,
               "created_tabs": [] },
  "suggested": { "fuzzy_duplicate_merge": 0, "rescore_outliers": 0, "recategorize": 0,
                 "ui_change": 0, "star_suggestion": 0, "orphan_folder": 0, "drop_dead_feed": 0 },
  "skipped_frozen": 0, "caps_hit": [], "health_score": 0,
  "notes": "One or two sentences on what happened this run." }
```
`created_tabs` lists any tab created in Step 7, e.g. `[{"id":"ai-safety-policy","title":"AI Safety & Policy","evidence":5}]`.

Also update `data/status.json`:
- `last_improved_at` = now (ISO-8601).
- `last_ux_review` = now **only if** Module 4 actually ran this time.
- `last_tab_created` = now **only if** Step 7 created a tab this run.
- `total_skills` = the corrected count.
- Do **not** touch `run_report` counters owned by fetch/analyze.

---

## Step 10 — Commit (after each module, and at the end)

```bash
git config user.name "skills-tracker-bot"
git config user.email "actions@users.noreply.github.com"
git add data docs skills other-skills
git commit -m "improve: <module> — <one-line summary>" || echo "nothing to commit"
git pull --rebase --autostash origin main || true
git push || echo "push skipped"
```
If `git push` is rejected because the remote moved (fetch/analyze pushed meanwhile), run
`git pull --rebase --autostash origin main` and `git push` again, then continue.

---

## Quick checklist
1. Load config + state; build the frozen-slug set (Step 0).
2. Apply already-approved suggestions, skipping frozen (Step 1).
3. Data hygiene: index, schema, orphans, exact-dup merge, summaries, consistency (Step 2).
4. Suggest near-duplicate merges (Step 3).
5. Suggest rescores + recategorizations (Step 4).
6. Stamp stars; suggest new stars — never auto-star (Step 5).
7. UX self-review — suggest only, rate-limited (Step 6).
8. Detect trends; auto-create a new tab if warranted — announce it (Step 7).
9. Propose dropping dead news feeds — suggest only (Step 7b).
10. Write health.json incl. unhealthy feeds (Step 8).
11. Write audit + update status (Step 9). Commit throughout (Step 10).
12. Never modify a frozen record. Stay under the token budget and the caps.
