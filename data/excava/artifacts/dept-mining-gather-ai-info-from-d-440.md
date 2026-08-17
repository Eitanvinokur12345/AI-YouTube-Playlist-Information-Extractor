# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-440` (dept) · 2026-08-17T05:14:38.915691+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Call Product Hunt’s API endpoint `/posts` with query parameters: `tags=AI`, `created_after=[7 days ago]`, and `order_by=popularity`.
2. Parse the JSON response to extract `id`, `name`, `tagline`, `votes_count`, and `user` details for each post.
3. Store results in a structured format (e.g., CSV/JSON) with a timestamp for tracking.
4. Cross-reference top posts with GitHub/HN/Reddit to validate relevance and avoid duplicates.
5. Output a filtered list of unique, high-engagement AI launches for further analysis.

**What changed:**
Focus narrowed to Product Hunt’s API as the primary source for recent AI launches, replacing broader social media scraping.
