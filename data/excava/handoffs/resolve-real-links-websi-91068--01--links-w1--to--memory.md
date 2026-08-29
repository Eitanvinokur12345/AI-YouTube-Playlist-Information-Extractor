# Hand-off — Resolve real links (website/github/codespaces) for the next 200 unlinked elements

| | |
|---|---|
| task | `resolve-real-links-websi-91068` (step 1/8) |
| from | **links-w1** |
| to | **memory** department |
| at | 2026-08-29T08:11:11.935415+00:00 |

## What was done
Link-coverage pass assessed: **5076/8963 linked (56.63%)**, moving -0.10%/day against the +5.0%/day target (NOT on track — resolver budget is the lever). The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI.

## Artifacts (where the work lives)
- `data/coverage_log.json`
- `data/skills.json`
- `data/tools.json`

## What remains
3887 items still unlinked. After each resolver batch the semantic index must be re-embedded so EXCAVA's recall sees the NEW links, not last week's.

## Context the next agent needs
Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items.

## Done criteria (unchanged unless stated)
memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI
