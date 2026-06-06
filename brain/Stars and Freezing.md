---
tags: [system, stars, freezing, safety]
aliases: [Stars, Freezing, Frozen Records, Stars and Freezing]
---

# Stars and Freezing

A **star** marks a record as *proven excellent — keep it in its original form forever*. It is
the owner's hard guarantee that the curation engine can never quietly degrade the best skills.

## The rule (a [[Standing Constraints|standing constraint]])
- Max **10** starred records total (`config.self_improvement.stars.max_total`).
- A record is **FROZEN** if its `slug` is in `data/stars.json` **or** the record itself has
  `"starred": true` or `"locked": true`.
- A frozen record is **NEVER** modified, merged, rescored, recategorized, or deleted by
  [[Pipeline - Improve]] or [[Pipeline - Analyze]]. The only allowed write is stamping
  `"starred": true` for consistency.

## Who stars
**Only the user.** The engine never auto-stars or auto-unstars. It may *propose* a star
(`star_suggestions`, max 1/run) when a record clears strict criteria —
`min_quality_score` 9.5, cited popularity, and endorsement by ≥ 2 videos — but the actual
star is added by the user through the [[Operations and Setup|MCP server]] / dashboard.

## Why it matters
The whole system is built to run with **no babysitting**. Freezing is the safety valve that
lets it self-curate aggressively everywhere *except* the handful of things the owner has
declared sacred. See [[Self-Improvement Loop]].
