# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-244` (dept) · 2026-08-14T19:32:46.938295+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" from the last 7 days.
2. Parse the JSON response to extract titles, descriptions, upvotes, and comment counts.
3. Cross-reference with other sources (GitHub, HN, Reddit, Telegram) to validate and enrich data.
4. Store the raw JSON and parsed metadata in a structured format (e.g., SQLite/CSV).
5. Generate a summary report highlighting top AI launches by engagement (upvotes/comments).
6. Share findings with the team via a shared document (Notion/Google Docs).

**What changed:** Focused on Product Hunt API as a primary data source while ensuring cross-platform validation.
