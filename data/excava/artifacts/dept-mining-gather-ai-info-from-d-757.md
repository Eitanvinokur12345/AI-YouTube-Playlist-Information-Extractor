# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-757` (dept) · 2026-07-31T21:21:33.957583+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper (e.g., Python + `requests`/`BeautifulSoup`/`selenium`) to query GitHub, HN, Product Hunt, Reddit (r/MachineLearning, r/artificial), and Telegram (AI-focused channels) for AI-related activity in the last 24 hours.
2. Filter results by relevance (keywords: "AI", "ML", "LLM", "neural", "transformer", etc.) and exclude duplicates.
3. Extract key details (title, link, summary, engagement metrics like stars/upvotes/comments) and format as a markdown table.
4. Prioritize high-engagement items (top 10% by metrics) and tag sources (GitHub, HN, etc.).
5. Output a single GitHub-flavored markdown file with sections for each source, sorted by recency.
6. Schedule automated daily runs (e.g., via GitHub Actions) and store historical logs.

**What changed:** Shifted from manual curation to automated, real-time aggregation across diverse sources.
