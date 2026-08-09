# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-919` (dept) · 2026-08-09T17:08:22.168555+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract raw post data (titles, descriptions, tags, upvotes, comments).
3. Cross-reference with GitHub’s trending AI repositories (via GitHub API or scraping).
4. Pull top AI discussions from Hacker News (HN) API (last 7 days, "AI" keyword).
5. Compile Reddit’s r/MachineLearning and r/artificial posts (last 7 days, "AI" filter).
6. Aggregate insights (frequency, sentiment, tech stacks) into a structured dataset.

**What changed:** Prioritized Product Hunt API query as the first step to gather diverse, recent AI product launches and discussions.
