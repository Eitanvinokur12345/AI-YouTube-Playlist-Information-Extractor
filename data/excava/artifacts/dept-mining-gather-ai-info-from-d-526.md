# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-526` (dept) · 2026-08-05T03:09:49.103380+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract post titles, descriptions, and URLs from the raw feed.
3. Cross-reference GitHub repositories linked in posts for AI-related activity (stars, commits, issues).
4. Scrape Hacker News (HN) for AI discussions in the last 7 days, focusing on top threads.
5. Aggregate Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning) AI posts from the last week.
6. Compile all data into a structured JSON/CSV for analysis.

**What changed:** Focused on Product Hunt API as the primary source while integrating GitHub/HN/Reddit for diversity.
