# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-961` (dept) · 2026-07-31T11:50:51.326395+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Run a live sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram for AI-related posts from the last 24 hours.

**Plan:**
1. Use a Python script with GitHub API, Hacker News API, Product Hunt API, Reddit API (PRAW), and Telegram API (telethon) to fetch posts.
2. Filter results for AI-related keywords (e.g., "AI", "LLM", "neural", "transformer") and last 24 hours.
3. Generate a curated list of 50–100 high-signal items with titles, sources, and one-line summaries.
4. Export the list as a GitHub markdown table for triage.
5. Share the table with the team for review and prioritization.
6. Archive the raw data for future reference.

**What changed:**
Expanded scope to include all five platforms (GitHub, HN, Product Hunt, Reddit, Telegram) within the last 24 hours instead of Telegram-only for 7 days.
