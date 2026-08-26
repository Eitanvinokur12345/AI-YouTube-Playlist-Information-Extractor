# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-342` (dept) · 2026-08-26T09:44:09.271691+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract and clean raw data (titles, descriptions, tags, upvotes, comments).
3. Filter for high-signal posts (e.g., upvotes > 50, engagement > 10 comments).
4. Cross-reference filtered posts with GitHub/HN/Reddit/Telegram for duplicate or complementary info.
5. Compile a curated dataset of diverse AI sources with metadata (source, date, engagement).
6. Output results in GitHub markdown format for downstream analysis.

**What changed:** Prioritized Product Hunt API query as the first step to gather recent, high-signal AI launches for cross-platform validation.
