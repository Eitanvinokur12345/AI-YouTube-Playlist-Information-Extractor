# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-711` (dept) · 2026-08-14T17:33:14.899074+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Cross-reference the Product Hunt data with GitHub, Hacker News, Reddit, Telegram, and social media for additional insights.
4. Compile a consolidated dataset of AI-related launches from diverse sources.
5. Analyze trends (e.g., upvotes, engagement) to identify high-potential AI tools or discussions.
6. Store the final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt’s API as the primary source for AI launches, then expanded to other platforms for validation and depth.
