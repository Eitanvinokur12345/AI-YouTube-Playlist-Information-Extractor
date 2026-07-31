# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-572` (dept) · 2026-07-31T00:45:10.730544+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for fresh AI repos with >50 stars in the last 7 days.
2. Rank the top 10 by star velocity and recency.
3. Return a GitHub markdown table with repo names, star counts, and a one-line pitch for each.
4. Cross-reference with Reddit’s r/MachineLearning and r/ArtificialIntelligence for AI posts with >20 upvotes in the last 7 days.
5. Cross-reference with Product Hunt’s AI section for launches in the last 7 days with >50 upvotes.
6. Compile a final ranked list combining GitHub, Reddit, and Product Hunt data.

**What changed:** Prioritized GitHub sweep as primary source, integrated Reddit and Product Hunt for diversity.
