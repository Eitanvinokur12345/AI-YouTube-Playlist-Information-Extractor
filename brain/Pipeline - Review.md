---
tags: [pipeline, engine, review, quality]
aliases: [Review, Review Stage]
---

# Pipeline — Review

The **quality gate**. Spec: **`REVIEW.md`** (see [[Engines]]); workflow
`.github/workflows/review.yml`. It runs ~3h after [[Pipeline - Improve]] so it critiques fresh
data, weekly at night Israel time + first-week nightly intensive. Full detail in
[[Three-Agent Review]].

## The three agents (three lenses)
1. **Usability / UX** — benchmarked against competitors (`config.review.usability.competitors`:
   Future Tools, There's An AI For That, Toolify, Product Hunt AI). What do they do better,
   what do we do better, what to borrow next.
2. **"Cut the bullshit"** — strip filler, hype, vague claims, duplication, dead UI.
3. **Deep code-bug researcher** — hunt real bugs/edge cases in `src/`, the workflows, and the
   dashboard JS.

## Claude first, then a different engine
Claude reviews first (`claude_first_then_external: true`), then an **external second opinion**
verifies — Gemini free tier via `EXTERNAL_REVIEW_API_KEY` (`src/external_review.py`,
**graceful-skip** if the key is absent). Plus **CodeQL** (`codeql.yml`) as the automated
static-analysis arm. Three independent checks under different conditions — the owner's
requirement (see [[Self-Improvement Loop]] §"external agents").

## Output
`data/review_findings.json`: `scores` (usability / cut_the_bullshit / deep_code_bugs /
overall), `benchmark`, `findings[]`, `top_actions[]`, `history[]`. Review is **read-only on
content**; it may write `ui_change` / `skills_folder_learning` suggestions for the user to
approve. Surfaced on the dashboard's Self-Improvement area (see [[Tabs]]).
