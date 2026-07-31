# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-967` (dept) · 2026-07-31T18:52:17.548268+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper (e.g., Scrapy/Playwright) to fetch AI-related posts from GitHub (repos with "AI", "LLM", "transformer"), Hacker News (front page + "Show HN"), Product Hunt (AI category), and Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning).
2. Filter posts from the last 7 days using date metadata (GitHub "created_at", HN "time", etc.).
3. Extract titles, URLs, and 1-2 sentence summaries (prioritizing open-source models/tools/trends).
4. Deduplicate by URL and rank by engagement (GitHub stars, HN upvotes, Reddit upvotes).
5. Output as a GitHub-flavored markdown table with columns: **Source**, **Title**, **URL**, **Summary**, **Engagement Metric**.
6. Store results in a new repo branch (`ai-sweep-<date>`) with a README linking to the raw data.

**What changed:** Focus shifted from broad "AI info" to **actionable open-source mining** with strict recency and engagement filters.
