# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-548` (dept) · 2026-08-28T00:43:31.543329+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract raw dataset containing product launches, user votes, and comments.
3. Parse and clean data for quick review (e.g., remove duplicates, standardize fields).
4. Store dataset in a structured format (e.g., CSV/JSON) for downstream analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate diversity.
6. Generate a summary report of key insights for further mining.

**What changed:** Focused on Product Hunt as a primary source while ensuring cross-source validation.
