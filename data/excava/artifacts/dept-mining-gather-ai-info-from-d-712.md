# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-712` (dept) · 2026-07-28T23:06:13.347596+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Browse Reddit’s r/MachineLearning and r/AI to extract the top 10 trending AI topics with links and brief summaries.

**Plan:**
1. Open r/MachineLearning and r/AI in separate browser tabs.
2. Sort posts by "Top" (past 24 hours) in each subreddit.
3. Select the top 10 posts (5 from each) based on upvotes and engagement.
4. Extract titles, links, and a 1-2 sentence summary for each post.
5. Format results into a GitHub markdown table with columns: Rank, Topic, Link, Summary.
6. Save as `trending_ai_reddit.md` in the mining directory.

**What changed:**
Focus narrowed to Reddit’s r/MachineLearning and r/AI for high-signal AI trend extraction.
