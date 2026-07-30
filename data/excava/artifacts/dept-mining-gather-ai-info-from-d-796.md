# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-796` (dept) · 2026-07-30T23:58:18.419840+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for AI repos with 100+ stars created in the last 30 days, extracting READMEs, star counts, and creation dates.
2. Sweep Reddit’s r/MachineLearning and r/ArtificialIntelligence for AI posts with 50+ upvotes in the last 7 days, extracting titles, links, and key claims.
3. Rank GitHub repos by star velocity (stars/day) and Reddit threads by engagement score (upvotes + comments).
4. Cross-reference top GitHub repos with Reddit discussions to identify overlapping or trending projects.
5. Compile a unified markdown list of high-potential AI projects with sources, metrics, and key claims.
6. Deliver the ranked list to the user for further analysis.

**What changed:** Combined GitHub and Reddit sweeps for broader coverage while prioritizing high-engagement and high-star projects.
