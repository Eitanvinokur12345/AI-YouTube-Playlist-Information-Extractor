# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-774` (dept) · 2026-07-29T21:19:58.325797+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Execute the Reddit curation plan to gather high-engagement AI discussions.

**Plan:**
1. Browse r/MachineLearning and r/AI for posts from the last 7 days.
2. Filter posts with ≥50 upvotes or ≥10 comments.
3. Extract titles, URLs, and engagement metrics.
4. Summarize key points, trade-offs, and decisions for each post.
5. Compile into a GitHub markdown table with columns: Post Title, URL, Upvotes, Comments, Summary.
6. Push to a dedicated GitHub repo (e.g., `ai-discussions-curation`) with a timestamped commit.

**What changed:**
Focus narrowed to Reddit-only high-engagement posts for immediate actionable insights.
