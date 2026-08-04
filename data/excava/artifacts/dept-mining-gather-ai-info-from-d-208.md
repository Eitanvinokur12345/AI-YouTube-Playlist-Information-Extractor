# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-208` (dept) · 2026-08-04T20:12:20.314189+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Product Hunt’s "AI" posts from the last 7 days using their API.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Query the API for posts tagged "AI" published in the last 7 days.
3. Extract structured data (titles, descriptions, upvotes, creator details) from the response.
4. Store the raw list in a JSON file for further processing.
5. Log the timestamp and query parameters for reproducibility.
6. Share the raw dataset with the team for downstream analysis.

**What changed:**
Focus shifted from broad social scraping to a targeted API-based sweep of Product Hunt’s AI posts.
