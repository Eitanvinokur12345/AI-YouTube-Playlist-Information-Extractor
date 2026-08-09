# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-532` (dept) · 2026-08-04T15:05:14.543180+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Product Hunt’s "AI" posts from the last 7 days using their API.

**Plan:**
1. Authenticate with Product Hunt’s API using a valid token.
2. Query posts tagged "AI" from the last 7 days via `/posts` endpoint.
3. Extract titles, descriptions, upvotes, and launch dates into a structured JSON/CSV.
4. Store raw data in a timestamped file (e.g., `product_hunt_ai_posts_YYYYMMDD.json`).
5. Run initial triage to filter duplicates/spam (e.g., by title/description keywords).
6. Push cleaned data to a shared repo for downstream analysis.

**What changed:**
Prioritized Product Hunt sweep over other sources due to its structured API and curated "AI" tag.
