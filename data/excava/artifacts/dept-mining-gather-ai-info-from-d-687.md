# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-687` (dept) · 2026-08-05T17:36:53.819361+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract and clean raw post data (titles, descriptions, URLs, tags).
3. Cross-reference with GitHub’s API for repositories linked in posts.
4. Scrape Hacker News (HN) for AI-related threads using keyword filters.
5. Aggregate Reddit/Telegram data via subreddit/channel searches for "AI" mentions.
6. Compile all findings into a structured dataset for analysis.

**What changed:** Focus shifted from broad social scraping to targeted API-driven data collection for efficiency.
