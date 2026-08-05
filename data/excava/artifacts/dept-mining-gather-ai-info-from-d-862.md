# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-862` (dept) · 2026-08-05T01:42:55.142517+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Product Hunt’s "AI" posts from the last 7 days using their API to gather diverse AI info sources.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Query the API for posts tagged "AI" from the last 7 days, retrieving titles, descriptions, upvotes, and creator details.
3. Store raw post data in a structured format (e.g., JSON/CSV) for filtering.
4. Filter results to exclude low-quality or irrelevant posts (e.g., upvotes < 5 or generic titles).
5. Extract unique URLs, GitHub links, and creator handles for further analysis.
6. Output the filtered list for integration into the broader mining pipeline.

**What changed:** Focused on Product Hunt as a high-signal source for AI tools/products, prioritizing diversity over volume.
