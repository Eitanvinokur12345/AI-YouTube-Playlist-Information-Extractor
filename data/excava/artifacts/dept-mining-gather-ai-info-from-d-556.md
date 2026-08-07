# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-556` (dept) · 2026-08-07T01:27:28.438299+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data (product names, descriptions, upvotes, launch dates) into a structured format.
3. Cross-reference results with GitHub’s API to identify open-source AI projects linked in Product Hunt posts.
4. Manually review top 10% upvoted products for additional insights (e.g., tech stacks, team size).
5. Compile a filtered list of high-potential AI sources (GitHub repos, product pages) for further analysis.
6. Store results in a structured database (e.g., JSON/CSV) for downstream processing.

**What changed:** Focused on Product Hunt as a primary data source while integrating GitHub for validation.
