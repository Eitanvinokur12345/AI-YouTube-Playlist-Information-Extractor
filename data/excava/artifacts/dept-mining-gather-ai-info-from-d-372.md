# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-372` (dept) · 2026-08-26T14:50:09.809426+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for AI posts in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a registered developer token.
2. Fetch all posts tagged "AI" published in the last 30 days via the `/posts` endpoint with filters.
3. Extract and clean raw data: titles, descriptions, upvotes, launch dates, and URLs.
4. Store results in a structured format (e.g., JSON/CSV) for downstream analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit) to deduplicate and enrich metadata.
6. Output a consolidated dataset for AI trend analysis.

**What changed:**
Focused on Product Hunt as a high-signal source for AI product launches, prioritizing recency and diversity over exhaustive scraping.
