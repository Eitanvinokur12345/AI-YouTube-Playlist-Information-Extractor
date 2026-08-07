# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-200` (dept) · 2026-08-07T00:56:29.369027+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Query Telegram’s AI channels for posts with 50+ reactions, output a list of top posts with titles, links, and reaction counts for further mining.

**Plan:**
1. Identify and join relevant Telegram AI channels (e.g., AI-related groups, news channels).
2. Use Telegram API or a scraper to fetch posts with 50+ reactions from the last week.
3. Filter results to include only AI-tagged or AI-related content.
4. Extract post titles, links, and reaction counts into a structured list.
5. Output the list in GitHub markdown format for downstream mining.

**What changed:** Shifted from Product Hunt to Telegram due to broader, real-time AI discussions with high engagement.
