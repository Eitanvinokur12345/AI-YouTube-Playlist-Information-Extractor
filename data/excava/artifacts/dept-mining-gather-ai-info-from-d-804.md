# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-804` (dept) · 2026-07-31T18:45:10.067920+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper (e.g., Scrapy/Apify) to fetch AI-related posts from GitHub (trending repos), Hacker News (front page + "Show HN"), Product Hunt (daily top AI products), Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-focused channels).
2. Filter results using keywords ("AI", "LLM", "neural", "transformer", "diffusion", "agent") and exclude duplicates/junk (e.g., spam, old posts).
3. For each source, extract: title, URL, summary (3-5 words), source, and timestamp.
4. Deduplicate and rank by recency (prioritize last 24h) and engagement (GitHub stars, HN upvotes, etc.).
5. Export as a GitHub-flavored markdown table with columns: **#**, **Source**, **Title**, **Summary**, **Link**, **Timestamp**.
6. Push to a dedicated repo (e.g., `ai-trends-daily`) with a `README.md` auto-updating the table via GitHub Actions.

**What changed:** Switched from a manual "curated list" to an automated, real-time sweep with structured output.
