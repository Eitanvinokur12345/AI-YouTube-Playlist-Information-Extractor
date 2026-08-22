# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-996` (dept) · 2026-08-22T02:01:45.083717+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw list.
3. Cross-reference the Product Hunt data with GitHub repositories tagged "AI" (via GitHub API or search).
4. Supplement with top AI-related discussions from Hacker News (via Algolia API) and Reddit (via Pushshift or PRAW).
5. Validate and deduplicate entries across sources to ensure diversity.
6. Compile the synthesized AI info into a structured dataset (CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt as a primary source while integrating GitHub, HN, and Reddit for diversity.
