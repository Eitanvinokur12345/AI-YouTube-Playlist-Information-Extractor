# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-388` (dept) · 2026-08-28T00:25:53.018073+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvotes from the raw list.
3. Cross-reference results with GitHub, Hacker News, Reddit, and Telegram for additional context.
4. Aggregate and deduplicate findings into a structured dataset.
5. Output the refined list in GitHub markdown format.
6. Schedule a follow-up query for broader timeframes if initial results are insufficient.

**What changed:** Focused on Product Hunt API as the primary source, with secondary cross-referencing.
