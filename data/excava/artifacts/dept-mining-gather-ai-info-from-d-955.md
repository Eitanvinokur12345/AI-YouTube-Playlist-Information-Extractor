# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-955` (dept) · 2026-08-27T23:55:43.127198+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract product names, descriptions, upvotes, and launch dates from the API response.
3. Filter results for diversity (e.g., exclude duplicates, prioritize unique sources).
4. Cross-reference top products with GitHub/HN/Reddit/Telegram for additional context.
5. Compile a curated list of AI tools with metadata for further analysis.
6. Store raw and processed data in a structured format (e.g., JSON/CSV).

**What changed:** Focused on Product Hunt as a primary source, then layered in cross-platform validation for diversity.
