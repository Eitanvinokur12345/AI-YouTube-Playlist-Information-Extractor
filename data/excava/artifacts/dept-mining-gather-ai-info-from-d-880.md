# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-880` (dept) · 2026-07-31T04:44:18.985661+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a broad sweep across GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-related channels) for posts from the last 7 days.
2. Extract raw data: links, titles, timestamps, platform, and engagement metrics (stars, upvotes, comments).
3. Deduplicate entries by URL and normalize metadata (e.g., platform-specific tags).
4. Filter for AI relevance using a lightweight keyword set (e.g., "LLM", "neural", "diffusion", "transformer").
5. Output a GitHub markdown table with columns: Platform | Title | URL | Date | Engagement | Tags.
6. Store the dataset in a new repo under `/data/raw_ai_sweep_YYYYMMDD.md`.

**What changed:** Focused on breadth-first data collection with minimal filtering upfront, deferring deeper analysis to post-processing.
