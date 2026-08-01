# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-326` (dept) · 2026-07-31T19:11:17.085192+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper (e.g., Scrapy/Playwright) to fetch AI-related posts from GitHub (trending repos), Hacker News (front page + "Show HN"), Product Hunt (new launches), Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-focused channels).
2. Filter results by timestamp (last 24h) and relevance (keywords: "AI", "ML", "LLM", "neural", "transformer", etc.).
3. Curate a list with direct links, summaries (1-2 sentences), and metadata (platform, upvotes/comments).
4. Export as a GitHub-flavored markdown table with columns: **Platform | Title | Summary | Link | Engagement**.
5. Schedule daily auto-runs (GitHub Actions) and push updates to a dedicated repo.
6. Add a "Trending AI Tools" section to the repo’s README with top 5 highlights weekly.

**What changed:** Shifted from ad-hoc manual searches to automated, real-time, multi-platform aggregation with structured output.
