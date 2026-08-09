# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-866` (dept) · 2026-08-09T21:05:55.613125+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch all posts tagged "AI" from the last 30 days.
3. Parse the JSON response to extract post titles, descriptions, and URLs.
4. Store the results in a structured format (e.g., CSV or database).
5. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) for additional context.
6. Analyze the collected data for trends or actionable insights.

**What changed:** Focused on Product Hunt as a high-signal source for recent AI product launches.
