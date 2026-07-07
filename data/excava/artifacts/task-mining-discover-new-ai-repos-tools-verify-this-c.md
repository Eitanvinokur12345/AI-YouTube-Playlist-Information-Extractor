# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-38138` · synthesized by mistral/mistral-small-latest

**Decision:** Keep only repos with novel architectures or niche optimizations; discard flashy demos.

**Plan:**
1. Query GitHub API for `ai tools` with `stars:>1000 pushed:>2023-01-01` (filter out tutorials/books).
2. Manually inspect top 50 results: prioritize repos with `README.md` describing unconventional methods (e.g., "neural ODEs", "diffusion on graphs").
3. Clone and run `main.py` or `demo.py`—discard if setup fails or output is trivial (e.g., MNIST accuracy >98%).
4. Check commit activity: keep if active in last 3 months *and* has <5 contributors (signals niche focus).
5. Log kept repos in `~/prospecting/ai_repos_YYYY-MM.txt` with 1-line justification (e.g., "Diffusion on graphs for molecule generation").

**Done when:** 3 novel repos added to prospecting log with verified functionality.
