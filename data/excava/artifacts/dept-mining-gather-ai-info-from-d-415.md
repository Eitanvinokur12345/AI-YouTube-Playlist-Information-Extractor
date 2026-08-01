# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-415` (dept) · 2026-07-30T18:22:57.651389+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for trending AI repos this week using Python filter, sorted by stars (top 20-30).
2. Extract key details: repo name, star count, last commit date, primary use case.
3. Sweep Product Hunt for AI products launched in last 7 days, ranked by upvotes (top 10-15).
4. Extract key details: product name, tagline, upvotes, launch date.
5. Cross-reference findings to identify overlapping or complementary AI projects.
6. Compile results into a unified markdown table for analysis.

**What changed:** Added Product Hunt sweep to diversify sources beyond GitHub.
