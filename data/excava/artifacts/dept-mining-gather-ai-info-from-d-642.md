# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-642` (dept) · 2026-07-30T19:17:54.873581+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for trending AI repos in the last 7 days with Python filter.
2. Rank repositories by stars gained in the last 7 days.
3. Output top 10 results in GitHub markdown format (name, stars gained, URL).
4. Cross-verify top 3 repos with Product Hunt for additional validation.
5. Log all sources (GitHub API, Product Hunt scraping) for reproducibility.

**What changed:** Focused GitHub sweep prioritized over Product Hunt.
