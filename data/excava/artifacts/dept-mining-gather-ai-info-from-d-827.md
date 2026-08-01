# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-827` (dept) · 2026-07-31T04:58:12.043509+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a broad sweep across GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-related channels) for AI-related posts from the last 7 days.
2. Use relevance scoring (e.g., GitHub stars, HN upvotes, engagement metrics) to curate a list of trending AI projects, discussions, and tools.
3. Extract key metadata (title, URL, description, engagement metrics) for each item.
4. Deduplicate and normalize entries (e.g., merge GitHub repos with HN discussions).
5. Output a GitHub-flavored markdown table with columns: **Source**, **Title**, **URL**, **Relevance Score**, **Brief Description**.
6. Save the file as `ai-trends-YYYYMMDD.md` in a dedicated repo.

**What changed:** Expanded scope to include Telegram and stricter deduplication.
