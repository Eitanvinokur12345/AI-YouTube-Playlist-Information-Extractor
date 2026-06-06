---
tags: [pipeline, engine, improve, self-improvement]
aliases: [Improve, Deep Pass, Curation Stage]
---

# Pipeline — Improve (the deep pass)

Where [[Pipeline - Analyze]] *adds* knowledge, the **improve** stage *curates* it. Spec:
**`IMPROVE.md`** (see [[Engines]]); workflow `.github/workflows/improve.yml`. It is the
**weekly deep pass at night Israel time** plus a **first-week nightly intensive** (see
[[Cadence]] and [[Self-Improvement Loop]]).

## Steps (IMPROVE.md)
- **0 — Load state** + build the frozen-slug set ([[Stars and Freezing]]). Decide run mode:
  **catch-up light** (mid-ingest → only hygiene + self-check + health + audit),
  **idle early-exit** (nothing changed → index + self-check + health + audit), or **full**.
- **1 / 1b — Apply** already-approved suggestions, then last run's self-check fix tasks.
- **2 — Data hygiene** (SAFE-AUTO): schema repair, orphan cleanup, exact-dup merge,
  cross-tab consistency, rebuild `index.json`.
- **3 — Near-duplicates** (SUGGEST-ONLY) → `improvement_suggestions.json`.
- **4 — Ratings calibration & category hygiene** (SUGGEST-ONLY).
- **5 — Stars** — *propose only*; the user freezes ([[Stars and Freezing]]).
- **6 — Dashboard / UX self-review** (SUGGEST-ONLY, rate-limited).
- **6b — Skills-folder learning** — read `./skills` + `./other-skills` to lift extraction +
  design quality → suggestions.
- **7 — [[Dynamic Tabs]]** — cluster `tab_candidates.json` → `extra_tabs.json` when evidence
  ≥ threshold; NEW badge auto-expires.
- **7b — News-feed health** — propose dropping dead feeds.
- **7c — [[Reference Self-Check]]** — answer the 50 questions → `self_check.json` +
  `improvement_tasks.json`. **Runs on EVERY invocation** (light + idle too).
- **8 — Health report** + cadence advice → `health.json`.
- **9 — Audit** → `improvement_audit.json`.
- **10 — Commit** after each module (crash-safe).

## Autonomy (safe vs suggest)
`safe_auto` ops are applied automatically; `suggest_only` ops are written as proposals the
user approves via the [[Operations and Setup|MCP server]] / dashboard. Caps limit how much
changes per run. Frozen records are never touched. See [[Self-Improvement Loop]].
