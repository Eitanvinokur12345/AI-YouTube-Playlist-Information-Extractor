# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-905` (dept) · 2026-08-28T00:20:00.666096+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid API key.
2. Construct a query to fetch all posts tagged "AI" from the last 30 days.
3. Parse the response to extract titles, descriptions, upvotes, and launch dates.
4. Store the raw data in a structured format (e.g., JSON or CSV).
5. Cross-reference the results with other sources (GitHub/HN/Reddit/Telegram) for diversity.
6. Validate the data for completeness and relevance before further processing.

**What changed:**
Focused on Product Hunt as a primary source for AI product launches, ensuring diversity in data collection.
