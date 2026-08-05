# Hand-off — [links room action] Anchor publishes the verified, updated link inventory for the Mission Control Dashboard, listing all external links with

| | |
|---|---|
| task | `links-room-action-anchor-95298` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-08-05T21:49:49.690277+00:00 |

## What was done
Link-coverage pass assessed: **4794/8230 linked (58.25%)**, moving -0.19%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
3436 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
