# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-316` (dept) · 2026-08-19T20:58:11.206991+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API (`/v2/posts`) with filters: `tag="AI"`, `created_at` within last 30 days.
2. Extract raw data: post titles, descriptions, upvotes, comments, and launch dates.
3. Filter for quality signals: posts with ≥50 upvotes or ≥10 comments.
4. Cross-reference with GitHub/HN/Reddit/Telegram for duplicate or related discussions.
5. Compile a curated list of top AI products/launch trends.
6. Output results in a structured JSON/CSV format for further analysis.

**What changed:**
Focused on Product Hunt’s API as a high-signal source for recent AI product launches, prioritizing upvotes/comments to filter quality.
