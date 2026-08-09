# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-241` (dept) · 2026-08-05T02:14:21.265034+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw list.
3. Cross-reference results with GitHub repositories (via search API) to identify open-source AI projects.
4. Scrape Hacker News (HN) for AI-related discussions using keywords like "AI," "machine learning," or "LLM" in the last 7 days.
5. Collect Reddit posts from r/artificial, r/MachineLearning, and r/learnmachinelearning using Pushshift API or PRAW.
6. Compile all data into a structured dataset (CSV/JSON) for analysis.

**What changed:** Focused on Product Hunt API first, then expanded to GitHub, HN, and Reddit for diverse AI sources.
