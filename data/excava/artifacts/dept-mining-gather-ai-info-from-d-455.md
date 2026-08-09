# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-455` (dept) · 2026-08-05T03:22:10.382576+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvotes from the raw list.
3. Cross-reference GitHub repositories mentioned in Product Hunt posts with GitHub’s API to gather metadata (stars, forks, contributors).
4. Scrape Hacker News (HN) for AI-related posts in the last 7 days, capturing titles, URLs, and comment counts.
5. Compile Reddit’s r/MachineLearning and r/artificial posts from the last 7 days, including upvotes and discussion threads.
6. Aggregate all data into a structured dataset for analysis.

**What changed:** Focused on Product Hunt as the primary source while integrating GitHub, HN, and Reddit for broader AI info gathering.
