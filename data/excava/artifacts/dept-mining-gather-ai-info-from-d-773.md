# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-773` (dept) · 2026-08-07T01:21:05.503506+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw API response.
3. Cross-reference the Product Hunt data with GitHub repositories tagged "AI" (via GitHub API) to identify overlapping or complementary projects.
4. Supplement findings with top AI-related discussions from Hacker News (via Algolia API) and Reddit (via Pushshift API).
5. Compile all data into a structured dataset (CSV/JSON) for analysis.
6. Share the dataset with the team for further validation and insights.

**What changed:** Focused on Product Hunt API as the primary source, supplemented by GitHub, HN, and Reddit for diversity.
