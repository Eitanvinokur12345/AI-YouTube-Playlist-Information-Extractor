# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-627` (dept) · 2026-07-27T20:50:31.380924+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search for AI-related repositories created/updated in the last 7 days, filtering by stars, forks, or recent activity.
2. Scrape Hacker News front page and "Show HN" posts for AI-related submissions in the last 7 days, extracting titles, links, and key claims.
3. Query Product Hunt API for AI-related products launched in the last 7 days, prioritizing upvoted or trending entries.
4. Search Reddit via Pushshift API (or manual scraping) for AI-related posts in r/MachineLearning, r/artificial, r/learnmachinelearning, etc., from the last 7 days.
5. Manually scan Telegram channels (e.g., AI-related groups, news bots) for recent AI posts, extracting links and summaries.
6. Compile results into a GitHub markdown table with columns: **Source**, **Link**, **Title/Summary**, **Key Claim/Tool**.

**What changed:** Switched from "broad sweep" to structured API/scraping plan with prioritized sources and output format.
