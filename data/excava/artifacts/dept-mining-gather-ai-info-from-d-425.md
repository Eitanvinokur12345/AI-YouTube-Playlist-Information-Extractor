# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-425` (dept) · 2026-07-31T07:39:16.202632+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Reddit’s AI-related subreddits for fresh posts linking to GitHub repos, papers, or tools.

**Plan:**
1. Target r/MachineLearning, r/artificial, and r/learnmachinelearning for posts in the last 7 days.
2. Extract links to GitHub repos, papers (arXiv/PDF), or tools (Hugging Face, Papers with Code).
3. Filter for posts with ≥5 upvotes to prioritize quality.
4. Compile results into a raw list with post title, URL, and subreddit.
5. Export as a GitHub markdown table (columns: Title | URL | Subreddit | Upvotes).
6. Schedule a follow-up pass every 48 hours to maintain freshness.

**What changed:** Focus shifted from broad social mining to targeted Reddit sweeps for high-signal AI sources.
