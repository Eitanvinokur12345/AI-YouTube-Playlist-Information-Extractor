# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-806` (dept) · 2026-07-30T23:50:33.939492+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for fresh AI repos with >50 stars in the last 7 days, returning raw links, titles, star counts, and one-sentence summaries.
2. Sweep Product Hunt for AI products launched in the last 7 days, outputting top 10 with links, titles, and one-sentence summaries.
3. Sweep Reddit’s r/MachineLearning and r/ArtificialIntelligence for AI posts from the last 7 days, listing top 10 with links, titles, and one-sentence summaries.
4. Aggregate all outputs into a single, unfiltered list of leads by source.
5. Assign a relevance score (0-10) to each lead based on recency, star count, and community engagement.
6. Export the final list as a raw markdown table with columns: Source, Link, Title, Summary, Relevance Score.

**What changed:** Combined GitHub, Product Hunt, and Reddit sweeps into a single, unfiltered multi-source lead list with relevance scoring.
