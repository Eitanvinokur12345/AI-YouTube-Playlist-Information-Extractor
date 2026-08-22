# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-846` (dept) · 2026-08-22T07:13:57.155509+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvote counts from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts for additional AI-related code/data.
4. Supplement with top AI discussions from Hacker News (HN) and Reddit (r/MachineLearning, r/artificial).
5. Curate Telegram channels focused on AI tools/updates and scrape relevant messages.
6. Aggregate all findings into a structured dataset for further analysis.

**What changed:** Shifted from broad social scraping to targeted API queries and curated sources for higher-quality AI data.
