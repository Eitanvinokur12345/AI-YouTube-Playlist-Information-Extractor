# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-43456` · synthesized by mistral/mistral-small-latest

**Decision:** Mine AI repos/tools with high novelty-to-noise ratio.

**Plan:**
1. Query GitHub API for repos with `ai`, `ml`, `llm`, or `transformers` in name/description, sorted by `pushed:>2023-11-01` and `stars:>50`.
2. Filter results for repos with `README.md` containing "novel", "research", or "experimental".
3. Clone top 10 candidates, run `pip install -e .` in a venv to check for installability.
4. Run `pytest` or `python -m unittest` if tests exist; otherwise, manually test core functionality.
5. Open issues/PRs for critical bugs or missing docs; discard if unmaintained (no commits >30 days).

**Done when:** 3 repos pass install/test and have unique value (e.g., new architecture, dataset, or tool).
