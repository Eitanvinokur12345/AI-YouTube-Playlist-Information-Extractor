# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-747` (dept) · 2026-07-14T23:27:54.883674+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search (`created:>2024-05-20 topic:ai`) to scrape repositories tagged with "AI" created in the last 7 days.
2. Query Hacker News’ Algolia API (`https://hn.algolia.com/api/v1/search?query=AI&numericFilters=created_at_i>1716268800`) for AI-related posts from the last week.
3. Scrape Product Hunt’s API (`https://api.producthunt.com/v2/posts?search[query]=AI&search[created_at][gte]=2024-05-20`) for AI tools launched in the last 7 days.
4. Extract AI-related submissions from Reddit’s `/r/MachineLearning`, `/r/artificial`, and `/r/learnmachinelearning` using PRAW with `created_utc > 1716268800`.
5. Monitor Telegram AI channels (e.g., `@ai_news`, `@DeepLearningAI`) for recent AI tool announcements via their public post history.
6. Compile results into a single markdown table with columns: **Source**, **Project Name**, **Link**, **Description**, **Date**.

**What changed:** Consolidated multi-source mining into a structured, automated plan with time-bound queries.
