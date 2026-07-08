# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-851` (dept) · 2026-07-08T01:38:29.929243+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Mine GitHub’s "Trending AI" (this week) + top 100 starred AI repos, plus HN/Product Hunt/Reddit/Telegram threads, scanning README/CHANGELOG/docs for keywords; output CSV with repo/thread name, source, AI keywords, and relevance score.

**Plan:**
1. Access GitHub’s "Trending AI" page for the current week.
2. Clone the top 50 trending AI repos using `gh repo clone <url>`.
3. Clone the top 100 starred AI repos using `gh repo list --topic ai --sort stars --order desc --limit 100`.
4. Scan `README.md`, `CHANGELOG.md`, and `docs/` for AI-specific keywords (e.g., LLM, transformer, diffusion).
5. Gather data from HN, Product Hunt, Reddit, and Telegram threads relevant to AI.
6. Compile the output into a CSV with repo/thread name, source, AI keywords, and a relevance score.

**What changed:** Expanded the mining scope to include both trending and top starred repos while integrating diverse external sources.
