# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-282` (dept) · 2026-08-07T00:38:16.263566+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API endpoint `/v2/posts` with query parameters `tag=AI` and `created_at[gte]=30_days_ago`.
2. Parse the JSON response to extract `id`, `name`, `tagline`, `votes_count`, and `created_at` for each post.
3. Store the raw data in a structured format (e.g., CSV/JSON) for downstream processing.
4. Cross-reference post IDs with GitHub/HN/Reddit/Telegram to deduplicate and enrich metadata.
5. Filter results to retain only posts with ≥50 upvotes or notable engagement signals.
6. Output a consolidated list of high-signal AI posts for further analysis.

**What changed:**
Focus narrowed to Product Hunt’s API as the first step to gather diverse, high-signal AI content before cross-referencing other sources.
