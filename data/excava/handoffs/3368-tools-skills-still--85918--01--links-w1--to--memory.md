# Hand-off — 3368 tools/skills still have no real link (48.3%)

| | |
|---|---|
| task | `3368-tools-skills-still--85918` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-08-16T13:12:01.535898+00:00 |

## What was done
Link-coverage pass assessed: **4968/8518 linked (58.32%)**, moving -0.08%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
3550 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
