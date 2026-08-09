# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-956` (dept) · 2026-08-09T22:12:41.256968+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts (if any) for additional AI-related data.
4. Supplement findings with top AI discussions from Hacker News (HN) and Reddit (r/MachineLearning, r/artificial).
5. Validate sources by checking timestamps and relevance to AI mining goals.
6. Compile aggregated insights into a structured report for further analysis.

**What changed:** Focused on Product Hunt API as primary source, with secondary validation from HN/Reddit.
