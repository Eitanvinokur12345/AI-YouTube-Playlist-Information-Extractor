# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-172` (dept) · 2026-07-31T21:41:28.129266+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a real-time sweep on Hacker News for AI stories posted in the last 7 days using a script/tool (e.g., `hn` CLI, `praw`, or a custom scraper).
2. Extract the top 10-20 posts by relevance (upvotes, comments, or keyword matching for "AI/ML/LLM").
3. Compile a markdown table with columns: **Title**, **URL**, **Poster**, **Upvotes**, **Relevance Notes** (e.g., "LLM benchmark tool," "AI startup funding").
4. Share the table with the team via GitHub/Gist or Slack for review.
5. Archive the sweep results in a dedicated GitHub repo (e.g., `ai-sweeps-hn`) with a timestamped commit.
6. Schedule recurring sweeps (e.g., weekly) and automate via GitHub Actions.

**What changed:** Focused on Hacker News as a high-signal source for AI trends, replacing broader (and lower-signal) social media scans.
