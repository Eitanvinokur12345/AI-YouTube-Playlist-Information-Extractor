# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-781` (dept) · 2026-08-26T09:37:56.885271+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract raw data (product names, upvotes, maker details, URLs).
3. Cross-reference with GitHub’s API for repos linked in posts or maker profiles.
4. Scrape Hacker News (HN) for AI-related discussions in the last 7 days.
5. Manually check Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning) for AI posts.
6. Compile all data into a structured dataset (CSV/JSON) for analysis.

**What changed:** Focused on Product Hunt API first, then expanded to GitHub/HN/Reddit for diversity.
