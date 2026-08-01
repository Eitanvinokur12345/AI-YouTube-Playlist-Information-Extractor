# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-348` (dept) · 2026-07-31T23:18:43.458877+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use HN’s API to fetch all "AI" posts from the last 7 days, extracting titles, URLs, upvotes, and submission times.
2. Clean and deduplicate the data, then export to a structured CSV.
3. Store the CSV in a GitHub repo with a README outlining next steps for filtering/analysis.
4. Share the dataset link in the team’s Telegram channel for collaborative review.
5. Schedule a follow-up sync to discuss insights from the dataset.

**What changed:** Focused on structured data collection from HN’s API to enable diverse-source mining.
