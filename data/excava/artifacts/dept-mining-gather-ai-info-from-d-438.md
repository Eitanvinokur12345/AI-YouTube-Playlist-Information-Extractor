# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-438` (dept) · 2026-08-05T01:55:42.518530+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" from the last 7 days.
2. Extract titles, descriptions, and engagement metrics (upvotes, comments) from the raw list.
3. Filter results to exclude duplicates or low-quality entries (e.g., <5 upvotes).
4. Cross-reference filtered posts with GitHub/HN/Reddit/Telegram/social for additional AI-related discussions.
5. Compile a consolidated list of diverse AI sources with metadata for further analysis.
6. Store the final dataset in a structured format (e.g., JSON/CSV) for downstream processing.

**What changed:** Prioritized Product Hunt API as a high-signal source for recent AI trends, integrating it with broader multi-platform mining.
