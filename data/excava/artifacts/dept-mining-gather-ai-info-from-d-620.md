# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-620` (dept) · 2026-08-28T00:02:23.394781+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results to ensure diversity (exclude duplicates, low-quality entries).
4. Cross-reference with GitHub/HN/Reddit/Telegram/social for additional context (e.g., GitHub stars, HN discussions).
5. Compile a consolidated list with sources and metadata.
6. Output a structured dataset (CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt as a primary source while ensuring cross-platform validation.
