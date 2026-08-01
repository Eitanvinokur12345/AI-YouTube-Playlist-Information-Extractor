# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-721` (dept) · 2026-08-01T11:45:56.036245+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Hacker News’ "AI" posts from the last 7 days using HN’s API.
2. Extract titles, URLs, and upvote counts for each post.
3. Rank posts by upvotes and select the top 20.
4. Return a clean, ranked list of these posts.
5. Use this snapshot to guide further mining from diverse sources (GitHub/HN/Product Hunt/Reddit/Telegram/social).

**What changed:** Focus narrowed to HN API sweep for trending AI posts as the first step in mining diverse sources.
