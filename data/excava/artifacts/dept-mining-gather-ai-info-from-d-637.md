# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-637` (dept) · 2026-07-31T13:01:08.546735+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 48-hour automated sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram for AI-related posts from the last 7 days.
2. Extract links, titles, and brief summaries for each post.
3. Curate and deduplicate the results into a structured list.
4. Format the output as a GitHub markdown table with columns: *Source*, *Title*, *Link*, *Summary*.
5. Deliver the curated list to the lead for review.
6. Iterate based on lead feedback (e.g., refine search terms or sources).

**What changed:** Extended sweep duration from "live" to 48 hours for broader coverage.
