# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-257` (dept) · 2026-08-05T07:17:52.852280+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, upvotes, and launch dates from the API response.
3. Store the raw data in a structured format (e.g., JSON/CSV) for further processing.
4. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate and diversify AI-related info.
5. Filter for unique or high-signal entries based on upvotes/engagement.
6. Output the synthesized list for downstream analysis.

**What changed:** Focused on Product Hunt as a primary source while ensuring integration with other platforms for diversity.
