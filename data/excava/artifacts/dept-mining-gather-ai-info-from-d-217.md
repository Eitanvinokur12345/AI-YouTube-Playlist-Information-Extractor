# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-217` (dept) · 2026-08-02T07:10:06.576132+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Product Hunt’s "AI" posts from the last 7 days using their API.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Query the API for posts tagged "AI" from the last 7 days, fetching titles, descriptions, upvotes, and creator handles.
3. Store the raw JSON response in a structured format (e.g., JSON file or database).
4. Parse the data into a CSV/TSV for quick triage (e.g., sorting by upvotes).
5. Flag posts with duplicate titles/descriptions to avoid redundancy.
6. Share the processed list with the team for further analysis.

**What changed:**
Prioritized Product Hunt API sweep over other sources due to its structured data and ease of integration.
