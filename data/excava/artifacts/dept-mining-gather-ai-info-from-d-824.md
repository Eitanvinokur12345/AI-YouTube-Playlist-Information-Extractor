# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-824` (dept) · 2026-08-17T03:30:04.488469+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and creator details from the raw list.
3. Cross-reference GitHub repositories linked in posts for additional AI-related code/data.
4. Scrape Hacker News (HN) for AI-related discussions in the last 7 days, focusing on comments and links.
5. Compile Reddit threads (r/artificial, r/MachineLearning) from the last 7 days, prioritizing high-engagement posts.
6. Log sources, timestamps, and relevance scores for each entry.

**What changed:** Shifted from a single-source Product Hunt query to a multi-platform AI data gathering strategy.
