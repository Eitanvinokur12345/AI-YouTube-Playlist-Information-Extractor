# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-621` (dept) · 2026-08-01T17:34:35.781340+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Hacker News’ "AI" posts from the last 7 days via HN’s API, extracting post titles, URLs, and upvote counts.
2. Store raw data in a structured format (e.g., JSON/CSV) for triage.
3. Apply quality filters (e.g., upvote threshold, engagement metrics) to prioritize posts.
4. Cross-reference filtered posts with other sources (GitHub/HN/Product Hunt/Reddit/Telegram) for diversity.
5. Compile a curated list of high-signal AI resources for deeper mining.
6. Automate periodic sweeps (e.g., weekly) to maintain fresh data.

**What changed:** Focused on HN API sweep as the first step to gather diverse AI content efficiently.
