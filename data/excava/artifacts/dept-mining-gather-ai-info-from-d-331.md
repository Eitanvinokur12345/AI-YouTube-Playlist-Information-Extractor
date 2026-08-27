# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-331` (dept) · 2026-08-27T14:45:57.909926+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Use Product Hunt’s API endpoint `/v2/posts` with query parameters `tag=ai` and `created_at[gte]=7_days_ago`.
2. Parse the JSON response to extract `id`, `name`, `tagline`, `votes_count`, and `created_at` for each post.
3. Store the raw data in a structured format (e.g., CSV/JSON) for further processing.
4. Cross-reference with other sources (GitHub/HN/Reddit) to deduplicate or enrich entries.
5. Output the filtered list of unique AI products for manual review or automated analysis.

**What changed:**
Focused on Product Hunt’s API as the primary source for recent AI product launches, prioritizing speed and diversity over other platforms.
