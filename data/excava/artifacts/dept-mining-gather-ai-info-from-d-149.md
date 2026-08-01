# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-149` (dept) · 2026-07-31T22:57:59.489216+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a real-time sweep across GitHub, Hacker News, Product Hunt, and Reddit for AI-related posts from the last 24 hours.
2. Compile a curated list with direct links and one-sentence summaries of emerging AI tools, discussions, and trends.
3. Sweep Hacker News’ "AI" posts from the last 7 days and extract the top 10 most discussed or upvoted threads.
4. Compile these threads with direct links and one-sentence summaries of their core claims or debates.
5. Merge both datasets into a single prioritized list, ranked by recency (24h) and engagement (7d HN).
6. Export the final list as a GitHub markdown table with columns: Source, Title, Link, Summary, Timestamp.

**What changed:** Combined real-time diversity (24h) with HN’s top engagement (7d) for a balanced, prioritized snapshot.
