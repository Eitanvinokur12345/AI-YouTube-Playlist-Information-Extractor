# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-768` (dept) · 2026-08-09T22:24:43.831076+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the API response.
3. Cross-reference the Product Hunt data with GitHub repositories tagged "AI" (using GitHub’s search API).
4. Supplement with top AI-related discussions from Hacker News (via Algolia API) and Reddit (via Pushshift or PRAW).
5. Compile all data into a structured dataset (CSV/JSON) for analysis.
6. Prioritize sources with the highest engagement (upvotes/comments) for deeper mining.

**What changed:** Focused on Product Hunt as a primary source while integrating GitHub, HN, and Reddit for diversity.
