# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-571` (dept) · 2026-07-28T21:42:46.639089+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Browse r/MachineLearning and r/AI to extract top 10 trending AI topics by upvotes and comment volume from the last 7 days.
2. Rank topics by engagement metrics (upvotes + comment volume) to prioritize relevance.
3. For each topic, write a 1-2 sentence plain-language summary explaining its significance.
4. Compile results into a GitHub markdown table with columns: Rank, Topic, Upvotes, Comments, Summary.
5. Push the markdown file to a GitHub repo named `ai-trends-mining`.
6. Share the repo link with the team for validation and iteration.

**What changed:** Focus narrowed to Reddit-only scraping for trending AI topics, replacing broader social media sources.
