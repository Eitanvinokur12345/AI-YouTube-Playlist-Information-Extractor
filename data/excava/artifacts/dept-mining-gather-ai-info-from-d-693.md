# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-693` (dept) · 2026-08-05T02:51:49.682489+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Use Product Hunt’s API endpoint `/v2/posts` with query parameters:
   - `search[tag]=AI`
   - `search[created_at][gte]=7 days ago`
2. Parse the JSON response to extract post titles, URLs, and descriptions.
3. Store the data in a structured format (e.g., CSV/JSON) for analysis.
4. Cross-reference with other sources (GitHub/HN/Reddit) to validate trends.
5. Compile a summary of trending AI products/products discussed this week.
6. Share findings with the team for further action.

**What changed:** Focused on Product Hunt’s API as a primary source for recent AI product launches.
