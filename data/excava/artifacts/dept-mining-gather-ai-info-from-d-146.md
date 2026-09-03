# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-146` (dept) · 2026-09-03T03:55:55.025706+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, launch dates, upvotes, and maker details.
3. Filter results for diversity of sources (exclude duplicates or rebranded products).
4. Cross-reference with GitHub/HN/Reddit/Telegram to validate novelty and relevance.
5. Compile a curated list of unique AI products with metadata for further analysis.
6. Store the final dataset in a structured format (e.g., JSON/CSV) for downstream tasks.

**What changed:** Prioritized Product Hunt API as the first step to efficiently gather diverse, recent AI product launches for synthesis.
