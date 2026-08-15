# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-771` (dept) · 2026-08-15T00:54:48.657279+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" with a publication date within the last 7 days.
3. Parse the response to extract post titles, launch dates, upvotes, and maker details.
4. Store the results in a structured format (e.g., JSON or CSV) for further analysis.
5. Cross-reference the gathered data with other sources (GitHub, HN, Reddit, etc.) to validate trends.
6. Schedule automated runs of this query to maintain a live dataset of trending AI tools.

**What changed:**
Focused on Product Hunt as a high-signal source for trending AI tools, complementing other platforms.
