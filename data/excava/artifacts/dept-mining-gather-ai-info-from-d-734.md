# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-734` (dept) · 2026-09-03T03:33:10.482840+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts to gather additional AI-related data.
4. Supplement with AI discussions from Hacker News (HN) and Reddit (r/MachineLearning, r/artificial) in the last 7 days.
5. Collect AI-related posts from Telegram channels (e.g., AI-focused groups) and social platforms (Twitter/X, LinkedIn) using relevant keywords.
6. Consolidate all gathered data into a structured format for analysis.

**What changed:** Focused on Product Hunt API as the primary source, expanded to include GitHub, HN, Reddit, Telegram, and social platforms for diverse AI data collection.
