# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-549` (dept) · 2026-09-03T03:21:47.554920+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw API response.
3. Cross-reference results with GitHub, Hacker News, Reddit, and Telegram for additional context (e.g., GitHub repos, discussions, or community reactions).
4. Compile a consolidated list of AI-related launches with metadata from all sources.
5. Filter for diversity (e.g., exclude duplicate entries, prioritize unique projects or discussions).
6. Output the final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focus shifted from Product Hunt-only to a multi-source approach to ensure diversity in AI info gathering.
