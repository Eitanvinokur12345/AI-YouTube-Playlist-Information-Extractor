# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-563` (dept) · 2026-09-03T03:14:14.872022+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Execute a query filtering posts by the "AI" tag and date range (last 30 days).
3. Parse the JSON response to extract post titles, descriptions, and URLs.
4. Store the results in a structured format (e.g., CSV or database).
5. Cross-reference with other sources (e.g., GitHub, Reddit) to validate trends.
6. Generate a summary report of key AI products/products discussed.

**What changed:**
Focused on Product Hunt’s API as a primary source for recent AI product launches.
