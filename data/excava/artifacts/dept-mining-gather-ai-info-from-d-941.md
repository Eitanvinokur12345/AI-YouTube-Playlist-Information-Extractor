# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-941` (dept) · 2026-07-29T20:59:13.090255+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Browse r/MachineLearning and r/AI for posts from the last 7 days.
2. Sort by engagement (upvotes + comments) and select the top 10.
3. Extract titles, links, and one-sentence summaries of core claims/findings.
4. Rank the list by engagement (highest to lowest).
5. Format as a GitHub markdown table with columns: Rank, Title, Link, Summary.
6. Output only the ranked list with no preamble.

**What changed:** Focus narrowed to Reddit-only extraction with ranked, concise summaries.
