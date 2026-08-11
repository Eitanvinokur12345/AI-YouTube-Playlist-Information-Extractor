# Hand-off — Raise G3 Truth & access (51/100): 51.6% of tools/skills have a real link (target: ~100%)

| | |
|---|---|
| task | `raise-g3-truth-access-51-12150` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-08-11T01:35:53.449592+00:00 |

## What was done
Link-coverage pass assessed: **4878/8375 linked (58.24%)**, moving +0.15%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
3497 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
