# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-546` (dept) · 2026-07-27T19:34:23.938232+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days.
2. Extract the top 20 posts by upvotes, including titles, upvote counts, and direct links.
3. Compile the results into a GitHub markdown table with columns: Rank, Title, Upvotes, Link.
4. Save the table as `trending_ai_reddit_7d.md` in the `/data/mining/` directory.
5. Notify the team via Slack with the file path and a summary of the top 3 posts.
6. Proceed to scrape full post content for deeper analysis (next step: comment mining).

**What changed:** Focus shifted from broad multi-source mining to prioritizing Reddit’s trending AI discussions as the first data source.
