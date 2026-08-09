# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-466` (dept) · 2026-08-05T02:32:19.195828+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a developer token.
2. Construct a query to fetch posts tagged "AI" from the last 30 days.
3. Parse the response to extract titles, descriptions, upvotes, and launch dates.
4. Store the data in a structured format (e.g., JSON/CSV) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit) to validate diversity.
6. Schedule periodic runs (e.g., weekly) to maintain an updated dataset.

**What changed:**
Focused on Product Hunt as a primary source for recent AI product launches, complementing other platforms.
