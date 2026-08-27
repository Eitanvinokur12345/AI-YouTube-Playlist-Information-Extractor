# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-156` (dept) · 2026-08-27T15:17:19.125640+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data (product names, upvotes, discussion links, tags).
3. Filter results to exclude duplicates or irrelevant entries (e.g., non-English, spam).
4. Cross-reference filtered results with GitHub/HN/Reddit/Telegram/social for additional context.
5. Compile a consolidated list of diverse AI sources with metadata (date, platform, engagement metrics).
6. Store the final dataset in a structured format (CSV/JSON) for downstream analysis.

**What changed:** Focused on Product Hunt as a primary source while ensuring integration with other platforms for diversity.
