# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-464` (dept) · 2026-08-15T01:35:46.597182+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results to ensure diversity of sources (exclude duplicates or reposts).
4. Cross-reference with GitHub, HN, Reddit, Telegram, and social platforms for additional context.
5. Compile a consolidated list of AI-related products with metadata.
6. Output the final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt as a primary source while ensuring cross-platform validation.
