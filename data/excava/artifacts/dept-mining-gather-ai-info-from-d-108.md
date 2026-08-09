# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-108` (dept) · 2026-08-05T02:38:41.364542+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch all posts tagged "AI" with a publication date within the last 30 days.
3. Retrieve and parse the response to extract product names, upvotes, launch dates, and URLs.
4. Store the results in a structured format (e.g., JSON/CSV) for immediate review.
5. Cross-reference the results with other sources (GitHub/HN/Reddit) to identify overlaps or gaps.
6. Generate a summary report highlighting trending AI products and their engagement metrics.

**What changed:**
Focused on Product Hunt’s API as the first step to gather trending AI product data efficiently.
