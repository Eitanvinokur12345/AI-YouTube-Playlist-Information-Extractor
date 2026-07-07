# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-35271` · synthesized by mistral/mistral-small-latest

**Decision:** Mine for AI repos/tools with high novelty-to-noise ratio, prioritizing odd gems over shiny junk.

**Plan:**
1. Query GitHub API for repos tagged `ai`, `machine-learning`, or `deep-learning` created in last 30 days, sorted by stars descending.
2. Filter results by `size:<20` (small repos) and `language:python` (prioritize tooling).
3. Manually inspect top 20 results: discard repos with >50% boilerplate (e.g., tutorials, forks of popular libs).
4. Clone and run `pip install -e .` in each remaining repo; check for functional README/demo.
5. Log repos with unique architectures (e.g., novel attention mechanisms, unconventional training loops) in `mined_repos.md`.

**Done when:** 3 novel, functional AI repos/tools are verified and documented in `mined_repos.md`.
