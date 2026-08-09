# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-338` (dept) · 2026-08-05T03:03:58.392309+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" from the last 30 days.
2. Extract titles, descriptions, upvotes, and launch dates from the API response.
3. Store the data in a structured format (e.g., JSON or CSV) for further analysis.
4. Cross-reference the gathered data with other sources (GitHub, HN, Reddit, etc.) to identify trends or gaps.
5. Prioritize high-upvoted or trending products for deeper mining (e.g., GitHub repos, social mentions).
6. Automate periodic queries to maintain an up-to-date dataset.

**What changed:**
Focused on Product Hunt as a high-signal source for trending AI products, complementing other platforms.
