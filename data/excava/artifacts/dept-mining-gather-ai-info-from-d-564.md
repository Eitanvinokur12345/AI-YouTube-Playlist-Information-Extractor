# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-564` (dept) · 2026-08-15T01:24:02.103726+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and creator details from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts to gather additional AI-related code/data.
4. Supplement with HN/Reddit/Telegram discussions referencing Product Hunt AI posts for deeper context.
5. Compile findings into a structured dataset (e.g., CSV/JSON) with source attribution.
6. Validate data diversity by ensuring coverage across at least 3 of the 5 specified platforms.

**What changed:** Focused on Product Hunt API as primary source, with cross-platform validation.
