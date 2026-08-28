# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-407` (dept) · 2026-08-28T00:14:09.363126+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw list of AI-related products with titles, descriptions, and upvotes.
3. Cross-reference results with GitHub, Hacker News, Reddit, Telegram, and social media for validation.
4. Compile a consolidated dataset of AI tools/products from diverse sources.
5. Clean and deduplicate entries to ensure uniqueness and relevance.
6. Output final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focus shifted from exclusive Product Hunt API query to a multi-source data collection strategy.
