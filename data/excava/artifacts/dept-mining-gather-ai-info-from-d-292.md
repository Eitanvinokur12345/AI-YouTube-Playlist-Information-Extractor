# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-292` (dept) · 2026-08-27T15:11:29.984233+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" from the last 7 days.
3. Parse the raw JSON response to extract post titles, URLs, and descriptions.
4. Store the results in a structured format (e.g., CSV/JSON) for review.
5. Manually filter for diverse sources (e.g., startups, tools, research) to ensure breadth.
6. Cross-reference with other platforms (GitHub/HN/Reddit) to validate trends.

**What changed:**
Focused on Product Hunt as a high-signal source for recent AI launches, prioritizing diversity over exhaustive scraping.
