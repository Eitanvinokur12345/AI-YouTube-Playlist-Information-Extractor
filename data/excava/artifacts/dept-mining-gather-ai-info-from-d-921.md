# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-921` (dept) · 2026-09-01T02:48:06.103651+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid token.
2. Construct a query to fetch posts tagged "AI" with a publication date within the last 7 days.
3. Parse the response to extract titles, descriptions, upvotes, and launch dates.
4. Store the extracted data in a structured format (e.g., JSON or CSV).
5. Cross-reference the results with other sources (GitHub/HN/Reddit/Telegram) for validation.
6. Output the final dataset for further analysis.

**What changed:**
Focused on Product Hunt’s API as a primary source for recent AI products, aligning with the goal of gathering diverse, current data.
