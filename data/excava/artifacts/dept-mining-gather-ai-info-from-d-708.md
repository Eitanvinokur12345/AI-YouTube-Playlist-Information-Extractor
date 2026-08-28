# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-708` (dept) · 2026-08-28T00:31:50.488234+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a developer token.
2. Construct a query to fetch posts tagged "AI" from the last 30 days.
3. Parse the response to extract titles, descriptions, upvotes, and launch dates.
4. Store the raw data in a structured format (e.g., JSON/CSV).
5. Cross-reference with other sources (GitHub/HN/Reddit) for validation.
6. Analyze trends (e.g., upvotes, launch frequency) to identify key insights.

**What changed:**
Focus shifted from broad social scraping to a targeted API query for structured, high-quality AI launch data.
