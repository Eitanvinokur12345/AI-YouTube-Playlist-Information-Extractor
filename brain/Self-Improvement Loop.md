---
tags: [system, self-improvement, overview]
aliases: [Self-Improvement Loop, Self-Improvement]
---

# Self-Improvement Loop

How Excavatortron gets better on its own, safely, with **no babysitting and no new cost**.
This note ties the pieces together; the mechanics live in [[Pipeline - Improve]],
[[Reference Self-Check]], [[Three-Agent Review]], [[Dynamic Tabs]], and [[Stars and Freezing]].

## The cycle (each deep pass)
```
analyze (ingest) ──► improve (curate + self-check) ──► review (3 agents) ──► dashboard
        ▲                       │  writes improvement_tasks.json                 │
        └───────────────────────┴── next run applies safe fixes (Step 1b) ◄──────┘
```
1. **Curate** what analyze produced (dedup, repair, calibrate) — safe ops auto, risky ops →
   `improvement_suggestions.json` for the user to approve.
2. **Return to the reference format** — the 50-question [[Reference Self-Check]] →
   `self_check.json` + `improvement_tasks.json`. Runs **every** pass.
3. **Learn from the skills folders** — read `./skills` + `./other-skills` to lift extraction +
   design quality (Step 6b), and re-read the [[Reference Spec]].
4. **Verify with a different engine** — the [[Three-Agent Review]] (usability, cut-the-bullshit,
   deep code bugs); Claude first, then external Gemini + CodeQL.
5. **Auto-fix next run** — Step 1b applies the safe fix tasks; the loop closes.

## Higher iteration in week one
`config.cadence.first_week` + `config.review.first_week_intensive` make improve **and** review
run **nightly** for the first 7 days (anchored in `data/review_state.json.first_run_at`), then
fall back to the weekly deep pass at night Israel time. See [[Cadence]].

## External / cloud agents (reinforcement)
Beyond the built-in three, you can point an additional **cloud or GitHub code agent** at the
repo (e.g. one discovered from the playlist videos) as an extra independent reviewer. Keep it
free-tier + graceful-skip, consistent with the [[Standing Constraints]].

## Autonomy & safety
- `safe_auto` operations apply automatically; `suggest_only` ones wait for approval
  (`data/approvals.json`).
- **Caps** bound changes per run; **token budget** keeps cost down.
- [[Stars and Freezing|Frozen]] records are never touched.

## Current snapshot
Self-check **45/50**, 5 open tasks (see [[Reference Self-Check]]). The improve deep pass had
not completed a scheduled run yet (Q21) — fixed so the self-check runs every pass; next
weekly run refreshes it.
