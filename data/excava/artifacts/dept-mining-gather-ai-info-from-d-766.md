# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-766` (dept) · 2026-08-09T19:14:27.739804+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" from the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts into a structured dataset.
3. Cross-reference with GitHub’s API to identify repositories linked in posts.
4. Scrape Hacker News (HN) for AI-related discussions using keyword filters.
5. Parse Reddit’s r/artificial and r/MachineLearning for trending AI posts.
6. Compile all data into a unified CSV for analysis.

**What changed:** Focused on Product Hunt API first, then expanded to GitHub/HN/Reddit for diversity.
