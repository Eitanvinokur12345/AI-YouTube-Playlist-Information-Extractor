# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-725` (dept) · 2026-08-27T15:05:07.190386+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" from the last 7 days.
2. Parse raw JSON response to extract post titles, URLs, votes, and comments.
3. Cross-reference top-voted posts with GitHub repos (via search API) for code links.
4. Supplement with HN/Reddit/Telegram searches for additional AI tools/discussions.
5. Compile findings into a structured dataset (CSV/JSON) for triage.
6. Share raw data with the team for prioritization.

**What changed:** Focused on Product Hunt as a primary source while integrating GitHub/HN/Reddit/Telegram for diversity.
