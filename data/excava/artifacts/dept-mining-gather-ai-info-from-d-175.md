# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-175` (dept) · 2026-07-31T23:29:18.344939+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use HN’s API to fetch all posts tagged "AI" from the last 7 days.
2. Extract titles, URLs, and upvote counts for each post.
3. Filter and sort posts by upvotes to identify the top 10.
4. Summarize key themes for each of the top 10 posts.
5. Return a concise GitHub-flavored markdown list with titles, URLs, upvotes, and themes.
6. Store the output in a structured format (e.g., JSON or table) for further analysis.

**What changed:** Focused on HN’s API for a prioritized snapshot of AI community trends, excluding other sources for now.
