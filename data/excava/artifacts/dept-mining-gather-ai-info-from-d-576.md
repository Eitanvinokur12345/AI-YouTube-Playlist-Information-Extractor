# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-576` (dept) · 2026-08-07T00:44:12.537747+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results for diversity (exclude duplicates, verify non-job postings).
4. Cross-reference with GitHub/HN/Reddit/Telegram/social for additional context.
5. Compile findings into a structured dataset for further analysis.
6. Output final report in GitHub markdown format.

**What changed:** Focused on Product Hunt API as primary source, supplemented by cross-platform validation.
