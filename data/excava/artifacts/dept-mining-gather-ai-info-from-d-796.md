# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-796` (dept) · 2026-08-01T23:31:44.015393+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize GitHub and Reddit sweeps for high-potential AI projects, then supplement with Product Hunt and Telegram.

**Plan:**
1. Sweep GitHub for AI repos with 100+ stars created in the last 30 days, extracting READMEs, star counts, and creation dates.
2. Sweep Reddit’s r/MachineLearning and r/ArtificialIntelligence for AI posts with 50+ upvotes in the last 7 days, extracting titles, links, and key claims (top 3 bullet points per post).
3. Sweep Product Hunt’s "AI" posts from the last 7 days via API, extracting titles, upvotes, makers, and key claims.
4. Sweep Telegram’s AI-related channels for posts with 50+ reactions in the last 7 days, extracting titles, links, and key claims.
5. Rank all results by engagement (stars/upvotes/reactions) and deliver a consolidated list of high-traction AI projects.
6. Cross-reference duplicates across sources to ensure diversity.

**What changed:** Added Reddit’s structured extraction method and consolidated all sources into a ranked pipeline.
