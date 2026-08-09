# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-575` (dept) · 2026-08-09T22:37:00.627334+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, upvotes, discussion links, and metadata.
3. Store results in a structured format (e.g., JSON/CSV) for downstream filtering.
4. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to identify overlaps/divergences.
5. Apply initial filters (e.g., exclude duplicates, prioritize high-engagement posts).
6. Output a consolidated list for manual review or automated parsing.

**What changed:** Focus shifted from broad social scraping to targeted API-driven data collection for efficiency.
