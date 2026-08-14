# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-124` (dept) · 2026-08-14T20:59:35.054867+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract raw data (product names, votes, discussions, links).
3. Filter for high-vote posts (>50 upvotes) and active comment threads (>10 comments).
4. Cross-reference filtered results with GitHub/HN/Reddit/Telegram for duplicate or complementary insights.
5. Compile a curated list of unique AI products with engagement metrics and source links.
6. Export as GitHub-flavored markdown for further analysis.

**What changed:** Focused on Product Hunt’s API as a primary source for recent AI product launches, prioritizing high-engagement posts for quality signals.
