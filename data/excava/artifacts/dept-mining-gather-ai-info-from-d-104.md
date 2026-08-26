# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-104` (dept) · 2026-08-26T18:21:10.456898+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for AI posts from the last 30 days.

**Plan:**
1. Use Product Hunt’s API endpoint (`/v2/posts`) with filters: `tag="AI"`, `created_at` within last 30 days.
2. Extract fields: `id`, `name`, `tagline`, `votes_count`, `created_at`, `discussion_url`.
3. Store raw JSON response in a structured format (e.g., `product_hunt_ai_posts.json`).
4. Deduplicate posts by `id` and validate timestamps.
5. Output a sanitized CSV/JSON file for downstream analysis.
6. Log API call metadata (rate limits, errors) for reproducibility.

**What changed:**
Focus narrowed to Product Hunt’s API for AI posts, excluding other sources temporarily.
