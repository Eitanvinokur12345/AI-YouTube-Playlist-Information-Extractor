# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-980` (dept) · 2026-07-31T23:11:48.890893+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Hacker News’ "AI" posts from the last 7 days via API, rank by comment count, and extract top 10 threads.

**Plan:**
1. Query HN’s API for posts tagged "AI" from the last 7 days.
2. Filter results to include only threads with ≥50 comments.
3. Sort threads by comment count (descending).
4. Extract titles, URLs, and comment counts for the top 10.
5. Output as a GitHub-flavored markdown table (columns: Rank, Title, URL, Comments).
6. Store results in a new branch `hn-ai-sweep-<date>` with a commit message referencing this decision.

**What changed:**
Focus narrowed from "diverse sources" to HN-only for immediate high-signal AI mining.
