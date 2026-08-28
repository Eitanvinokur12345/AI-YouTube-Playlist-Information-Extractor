# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-508` (dept) · 2026-08-28T00:37:42.275312+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" from the last 30 days, including titles, descriptions, upvotes, and launch dates.
3. Parse the API response into a structured format (e.g., JSON/CSV) for further analysis.
4. Store the raw dataset in a local or cloud-based database for accessibility.
5. Cross-reference the Product Hunt data with other sources (GitHub/HN/Reddit/Telegram) to identify overlaps or gaps.
6. Generate a summary report highlighting trending AI products and their metadata.

**What changed:**
Focused on Product Hunt’s API as a primary source for AI product launches, prioritizing diversity in sources while maintaining actionable data collection.
