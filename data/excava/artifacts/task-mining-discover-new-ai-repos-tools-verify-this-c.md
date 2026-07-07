# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-28375` · synthesized by mistral/mistral-small-latest

**Decision:** Mine for AI repos/tools with high value-to-noise ratio, prioritizing odd gems over shiny junk.

**Plan:**
1. Query GitHub API for repos with `ai`, `ml`, `neural`, `transformer` keywords, sorted by `stars` > 100, `created` > 2023-01-01.
2. Filter results for repos with `README.md` mentioning "novel", "unusual", or "experimental" techniques.
3. Manually inspect top 10 candidates for unique architectures, datasets, or training methods (e.g., diffusion models, sparse attention).
4. Clone and run `pip install -e .` on promising repos; verify functionality with minimal test data.
5. Log findings in `ai-mining-log.md` with repo name, key insight, and reproduction steps.

**Done when:** 3 novel repos verified and logged with reproducible results.
