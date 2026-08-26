# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-374` (dept) · 2026-08-26T11:05:59.941282+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts for AI-related code.
4. Supplement with HN/Reddit/Telegram discussions on trending AI tools.
5. Compile findings into a structured dataset (CSV/JSON) for analysis.
6. Validate sources for diversity (avoid over-reliance on a single platform).

**What changed:** Focused on Product Hunt API as primary source, expanded to GitHub/HN/Reddit/Telegram for validation.
