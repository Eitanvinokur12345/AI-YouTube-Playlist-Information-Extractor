# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-216` (dept) · 2026-07-27T20:14:20.494006+00:00
> Decision artifact · room `dept-mining-gather-ai-info-from-d-216` (dept) · 2026-07-27T20:11:35.385154+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days.
2. Filter and rank results by upvotes to identify the top 10 most engaging threads.
3. Extract titles, upvotes, and direct links for each thread.
4. Compile the results into a GitHub markdown table with columns: Title, Upvotes, Link.
5. Save the table as `trending_ai_reddit_7d.md` in the `/data` directory.
6. Notify the team via Slack with the file path and a brief summary of findings.

**What changed:** Focus shifted from broad multi-source scraping to a targeted Reddit-first approach to quickly gather trending AI discussions.
2. Extract the top 10 most engaging threads (titles, upvotes, direct links).
3. Compile the results into a structured GitHub markdown table.
4. Store the raw feed in a designated repository for further mining.
5. Share the output with the team for validation and prioritization.
6. Integrate insights into the broader AI information pipeline.

**What changed:** Focus shifted from broad social mining to a targeted Reddit-first approach to gather high-engagement AI discussions efficiently.
