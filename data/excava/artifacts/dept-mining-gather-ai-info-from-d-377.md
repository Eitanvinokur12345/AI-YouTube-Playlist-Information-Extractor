# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-377` (dept) · 2026-08-19T19:07:58.218462+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvotes from the raw list.
3. Cross-reference with GitHub, Hacker News, Reddit, Telegram, and social platforms to validate and supplement data.
4. Filter for diversity of sources (avoid over-reliance on any single platform).
5. Compile a consolidated dataset of AI-related products and trends.
6. Store results in a structured format (e.g., JSON/CSV) for further analysis.

**What changed:** Focus shifted from exclusive Product Hunt mining to a multi-source approach for broader AI info gathering.
