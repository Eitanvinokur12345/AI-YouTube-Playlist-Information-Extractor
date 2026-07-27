# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-276` (dept) · 2026-07-27T19:21:26.759499+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days using `site:reddit.com/r/ai OR site:reddit.com/r/MachineLearning OR site:reddit.com/r/artificial "AI"` with a time filter.
2. Sort results by "Top" (past week) and extract the top 10 threads with highest engagement (upvotes + comments).
3. For each thread, record: title, upvotes, direct link, and subreddit.
4. Export results as a GitHub markdown table with columns: #, Title, Upvotes, Link, Subreddit.
5. Store the table in a new repo branch (`data/raw/reddit_ai_trends_YYYYMMDD.md`).
6. Trigger a downstream script to scrape linked posts/comments for AI keywords (e.g., "LLM", "model", "dataset").

**What changed:** Prioritized Reddit as a high-signal source for trending AI discussions, replacing unfocused multi-platform scraping.
