---
tags: [system, review, quality, agents]
aliases: [Three-Agent Review, 3-Agent Review, External Agents]
---

# Three-Agent Review

The owner's rule: after each self-improvement pass, **at least three different agents check the
work under different conditions** — and Claude's own work is verified by a *different* engine,
not just itself (a [[Locked Decisions|locked decision]]). Spec: `REVIEW.md`; stage:
[[Pipeline - Review]].

## The three lenses
| Agent | Question it asks | Config dimension |
|---|---|---|
| **Usability / UX** | Is this easier + better than competitors? | `usability` (benchmarked) |
| **"Cut the bullshit"** | What's filler, hype, vague, or dead? | `cut_the_bullshit` |
| **Deep code-bug researcher** | What real bug/edge case is hiding in the code? | `deep_code_bugs` |

## Independent verification (different engines)
- **Claude first** (`REVIEW.md`) produces findings + scores.
- **External second opinion** — Gemini free tier (`src/external_review.py`, stdlib-only),
  keyed by `EXTERNAL_REVIEW_API_KEY`, **graceful-skip** if absent. A *different* engine, so
  the check isn't Claude grading itself.
- **CodeQL** (`codeql.yml`) — free static analysis = the automated deep-code arm.

That's three independent conditions. You can also point a **cloud/GitHub code agent** at the
repo as a fourth (e.g. one discovered from the playlist) — see [[Self-Improvement Loop]].

## First-week intensive
`config.review.first_week_intensive: true` → nightly during week one (anchored in
`data/review_state.json.first_run_at`, **shared** with [[Pipeline - Improve]]), then back to
weekly. Output: `data/review_findings.json` (see [[Data Files]]).
