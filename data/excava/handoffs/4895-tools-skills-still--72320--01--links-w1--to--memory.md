# Hand-off — 4895 tools/skills still have no real link (55.0%)

| | |
|---|---|
| task | `4895-tools-skills-still--72320` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-10-04T00:05:21.490824+00:00 |

## What was done
Link-coverage pass assessed: **5572/10766 linked (51.76%)**, moving -0.12%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
5194 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
