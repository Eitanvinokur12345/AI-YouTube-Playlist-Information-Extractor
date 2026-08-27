# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-178` (dept) · 2026-08-27T14:39:04.542801+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API to fetch all posts tagged "AI" from the last 30 days.
2. Extract raw data including product names, descriptions, votes, comments, and launch dates.
3. Filter results for quality signals (e.g., high upvotes, engagement, or trending tags).
4. Cross-reference with GitHub/HN/Reddit/Telegram/social for additional context or validation.
5. Compile a curated list of high-potential AI products for deeper analysis.
6. Store the dataset locally for iterative refinement.

**What changed:**
Focused on Product Hunt as a primary source for AI product launches, prioritizing recent and diverse data.
