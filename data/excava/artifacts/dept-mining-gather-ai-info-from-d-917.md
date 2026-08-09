# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-917` (dept) · 2026-08-05T02:44:26.849726+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract post titles, descriptions, upvotes, and launch dates into a structured dataset.
3. Cross-reference GitHub repositories linked in Product Hunt posts to gather additional AI-related code/data.
4. Supplement with top AI discussions from Hacker News (via Algolia API) and Reddit (r/MachineLearning, r/artificial).
5. Validate sources by checking timestamps and relevance to AI/ML.
6. Compile findings into a unified markdown report with source attribution.

**What changed:** Focused on Product Hunt API first, then expanded to GitHub/HN/Reddit for diversity.
