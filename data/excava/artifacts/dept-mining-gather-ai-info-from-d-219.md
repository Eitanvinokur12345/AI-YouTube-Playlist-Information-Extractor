# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-219` (dept) · 2026-08-01T10:19:49.913816+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Hacker News’ "AI" posts from the last 7 days via API for raw data, then filter for quality and relevance.

**Plan:**
1. Use HN’s API to fetch all posts tagged "AI" from the last 7 days, extracting titles, URLs, and submission times.
2. Store results in a structured format (e.g., JSON/CSV) for downstream filtering.
3. Apply initial relevance filters (e.g., exclude job posts, low-engagement links) to reduce noise.
4. Cross-reference filtered links with GitHub/HN/Product Hunt/Reddit/Telegram/social for diversity validation.
5. Prioritize posts with high engagement (comments/upvotes) or unique contributors for deeper mining.
6. Schedule weekly repeats to maintain a dynamic dataset.

**What changed:**
Focus shifted from broad social scraping to targeted HN API mining as the first step, balancing efficiency and diversity.
