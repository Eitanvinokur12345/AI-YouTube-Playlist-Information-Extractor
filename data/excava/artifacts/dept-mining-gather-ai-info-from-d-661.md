# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-661` (dept) · 2026-08-05T22:55:49.263463+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results to ensure diversity of sources (exclude duplicates or near-identical entries).
4. Store the curated list in a structured format (e.g., JSON/CSV) for further analysis.
5. Cross-reference with other platforms (GitHub/HN/Reddit/Telegram) to validate or supplement missing info.
6. Output the final dataset for downstream mining tasks.

**What changed:** Focused on Product Hunt API as a primary source while preserving flexibility for cross-platform validation.
