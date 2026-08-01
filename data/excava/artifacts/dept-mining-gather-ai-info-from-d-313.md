# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-313` (dept) · 2026-07-31T22:51:18.991602+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Hacker News’ "AI" posts from the last 7 days using a script (e.g., `hn_api` or `praw`).
2. Extract engagement metrics (upvotes, comments, shares) for each post.
3. Rank posts by engagement and select the top 10 most discussed.
4. Compile links, titles, and metrics into a GitHub markdown table.
5. Store the output in a dedicated repo (e.g., `ai-trending-discussions`).
6. Schedule daily automation (GitHub Actions) for future sweeps.

**What changed:** Focus shifted from multi-platform scraping to prioritizing Hacker News’ high-signal AI discussions.
