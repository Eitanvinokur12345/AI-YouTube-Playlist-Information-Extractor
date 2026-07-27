# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-797` (dept) · 2026-07-27T18:26:59.025207+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days, sorted by "Top" (all time) and filtered by "Past 7 days."
2. Extract the top 20 threads by upvotes + comments (engagement metric).
3. For each thread, record: title, URL, upvotes, and comment count.
4. Export results as a GitHub-flavored markdown table with columns: Rank, Title, URL, Upvotes, Comments.
5. Save the file as `ai_reddit_top_20_7d.md` in the `/data/mining/` directory.
6. Notify the team via Slack with the file path and a brief summary of findings.

**What changed:** Prioritized Reddit mining over other sources due to high engagement potential for AI discussions.
