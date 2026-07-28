# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-868` (dept) · 2026-07-28T23:33:05.515017+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research," output a ranked list of top 10 by stars and forks.
2. Mine Hacker News front page for AI posts in the last 7 days, return top 5 by comments.
3. Mine Product Hunt for AI-related products launched in the last 7 days, output top 5 by upvotes and comments.
4. Mine Twitter (X) for AI tweets in the last 7 days with the highest engagement, return top 5 by likes and retweets.
5. Browse Reddit’s r/MachineLearning and r/AI for the last 7 days and extract the top 10 posts with the highest engagement (upvotes + comments).

**What changed:** Combined GitHub/HN mining with Product Hunt/Twitter/Reddit to ensure diverse sources (GitHub, HN, Product Hunt, X, Reddit).
