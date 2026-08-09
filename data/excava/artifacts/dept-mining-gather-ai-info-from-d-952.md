# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-952` (dept) · 2026-08-09T22:05:28.345720+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid developer token.
2. Construct a query to fetch all posts tagged "AI" from the last 30 days.
3. Extract key fields: post title, description, upvotes, comments, tags, and launch date.
4. Store the raw dataset in a structured format (e.g., JSON/CSV) for downstream analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit) to validate trends.
6. Preprocess data (clean, deduplicate, and normalize) for AI-focused analysis.

**What changed:**
Prioritized Product Hunt as a primary source for AI product launches and engagement metrics.
