# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-934` (dept) · 2026-08-14T22:54:16.121383+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" with a publication date filter for the last 30 days.
3. Parse the raw JSON response to extract titles, descriptions, upvotes, and launch dates.
4. Store the extracted data in a structured format (e.g., CSV or JSON) for further analysis.
5. Cross-reference the results with other sources (GitHub/HN/Reddit/Telegram) to identify overlaps or unique insights.
6. Validate the data for completeness and accuracy before proceeding to synthesis.

**What changed:**
Focused on Product Hunt’s API as a primary source for AI-related launches, prioritizing diversity in data collection.
