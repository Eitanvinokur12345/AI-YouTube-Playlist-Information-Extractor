# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-724` (dept) · 2026-08-24T09:18:28.644461+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API endpoint `/v2/posts` with query parameters:
   - `tag=ai`
   - `created_after=2024-05-24T00:00:00Z` (30 days prior)
2. Parse the response to extract `id`, `name`, `tagline`, `votes_count`, and `created_at` for each post.
3. Store raw data in a structured format (e.g., JSON/CSV) for deduplication and analysis.
4. Cross-reference with other sources (GitHub/HN/Reddit) to validate uniqueness and avoid duplicates.
5. Enrich entries with metadata (e.g., upvote trends, launch dates) for prioritization.
6. Output a consolidated list of diverse AI products for further mining.

**What changed:**
Focused on Product Hunt’s API as a high-signal source for recent AI product launches, balancing breadth and recency.
