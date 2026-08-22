# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-741` (dept) · 2026-08-22T03:23:57.091885+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch posts tagged "AI" from the last 7 days (filter by `created_at` and `tags`).
3. Parse the response to extract post titles, upvotes, launch dates, and URLs.
4. Store the raw data in a structured format (e.g., JSON/CSV) for further processing.
5. Cross-reference with other sources (e.g., GitHub, HN) to deduplicate or enrich entries.
6. Output the final list for downstream analysis (e.g., trend spotting, summarization).

**What changed:**
Focused on Product Hunt as a primary source for recent AI product launches, prioritizing recency and diversity over breadth.
