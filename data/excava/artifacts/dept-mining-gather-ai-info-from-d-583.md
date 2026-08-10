# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-583` (dept) · 2026-08-10T05:58:35.369876+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query filtering posts by the "AI" tag and date range (last 30 days).
3. Execute the API request and retrieve raw JSON data (titles, descriptions, upvotes, launch dates).
4. Parse the response to extract structured data (e.g., CSV/JSON format).
5. Store the results in a local database or file for further analysis.
6. Cross-reference with other sources (GitHub/HN/Reddit) to validate and enrich the dataset.

**What changed:**
Focused on Product Hunt as a primary source for AI product launches while acknowledging the need for broader cross-platform validation.
