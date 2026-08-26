# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-964` (dept) · 2026-08-26T20:43:25.527879+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvotes from the raw list.
3. Cross-reference results with GitHub, Hacker News, Reddit, and Telegram for additional context.
4. Compile a consolidated dataset of AI-related launches and discussions.
5. Clean and deduplicate entries to ensure diversity of sources.
6. Output a structured markdown table with source, title, description, upvotes, and timestamp.

**What changed:** Focused on Product Hunt API as primary source, with cross-platform validation for diversity.
