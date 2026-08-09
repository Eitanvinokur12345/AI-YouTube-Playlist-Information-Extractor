# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-836` (dept) · 2026-08-05T17:45:58.934949+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for AI posts from the last 7 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" published in the last 7 days.
2. Extract post titles, descriptions, and links for analysis.
3. Cross-reference with GitHub’s API to identify related repositories.
4. Manually review Reddit/HN threads for additional context or discussions.
5. Compile findings into a structured dataset for further processing.

**What changed:** Focus narrowed to Product Hunt API as the primary initial source.
