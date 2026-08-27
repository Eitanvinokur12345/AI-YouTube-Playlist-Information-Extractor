# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-943` (dept) · 2026-08-27T15:23:18.942017+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data (titles, descriptions, upvotes, launch dates).
3. Cross-reference with GitHub repositories linked in Product Hunt posts.
4. Supplement with HN/Reddit/Telegram/social media mentions of the same products.
5. Compile a unified dataset of AI-related products and their metadata.
6. Export results in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt as a primary source, then expanded to other platforms for diversity.
