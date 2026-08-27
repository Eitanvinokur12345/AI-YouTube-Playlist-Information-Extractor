# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-296` (dept) · 2026-08-27T03:32:18.793996+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" from the last 7 days.
2. Extract post titles, descriptions, and URLs for further analysis.
3. Cross-reference with GitHub, HN, Reddit, and Telegram for additional context.
4. Compile a structured dataset of AI-related products and discussions.
5. Filter for diversity in sources and topics to ensure broad coverage.
6. Store results in a searchable format (e.g., JSON/CSV) for downstream analysis.

**What changed:**
Focused initial data collection on Product Hunt’s AI-tagged posts to seed a broader multi-source mining strategy.
