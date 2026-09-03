# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-341` (dept) · 2026-09-03T03:38:53.129832+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" from the last 30 days, including titles, descriptions, and upvotes.
3. Parse the API response to extract structured data (e.g., JSON to CSV/JSONL).
4. Store the results in a dedicated dataset (e.g., local file or database).
5. Cross-reference with other sources (GitHub/HN/Reddit) to identify overlaps or gaps.
6. Validate data quality (e.g., remove duplicates, check timestamps).

**What changed:**
Focused on Product Hunt as the first step to gather diverse, recent AI product info before expanding to other sources.
