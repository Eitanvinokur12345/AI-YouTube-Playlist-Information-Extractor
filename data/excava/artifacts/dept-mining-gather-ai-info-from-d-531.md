# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-531` (dept) · 2026-08-05T02:02:07.215951+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Cross-reference GitHub repositories linked in the posts to gather additional AI-related code/data.
4. Supplement with HN/Reddit/Telegram discussions referencing the Product Hunt posts.
5. Compile a consolidated dataset of AI info from diverse sources.
6. Validate and deduplicate entries for quality control.

**What changed:** Focused on Product Hunt as a primary source, then expanded to GitHub/HN/Reddit/Telegram for corroboration.
