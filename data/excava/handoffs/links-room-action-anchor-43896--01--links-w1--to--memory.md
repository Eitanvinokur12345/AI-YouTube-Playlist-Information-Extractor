# Hand-off — [links room action] Anchor delivers the prioritized report of broken/outdated links with recommendations to the links team by EOD.

| | |
|---|---|
| task | `links-room-action-anchor-43896` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-07-29T15:16:42.308914+00:00 |

## What was done
Link-coverage pass assessed: **4570/7666 linked (59.61%)**, moving -0.09%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
3096 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
