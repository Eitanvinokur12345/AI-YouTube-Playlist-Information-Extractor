# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-610` (dept) · 2026-08-09T22:18:39.493905+00:00
> Participants: Pick · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Query Product Hunt's API for AI-related posts and supplement with data from other sources
**Plan:**
1. Query Product Hunt's API for all posts tagged "AI" published in the last 7 days to gather a raw list of AI-related products.
2. Utilize GitHub's API to find open-source AI projects and repositories, focusing on recently updated projects.
3. Extract AI-related discussions and posts from Reddit's r/MachineLearning and r/AI, and Telegram groups dedicated to AI.
4. Scan Hacker News for AI-related stories and comments.
5. Filter and combine the data from all sources, removing duplicates and irrelevant information.
6. Organize the collected data into a structured format for further analysis.
**What changed:** The scope of data collection expanded to include multiple sources beyond Product Hunt.
