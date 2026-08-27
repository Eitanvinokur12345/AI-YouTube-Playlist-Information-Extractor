# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-852` (dept) · 2026-08-27T15:27:48.071726+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract raw data: product names, launch dates, upvotes, and maker details.
3. Cross-reference maker details with GitHub/HN/Reddit/Telegram/social for additional context.
4. Filter and deduplicate results to ensure diversity of sources.
5. Compile findings into a structured dataset for further analysis.
6. Output final report in GitHub markdown format.

**What changed:** Focus narrowed to Product Hunt API as primary source for AI product data.
