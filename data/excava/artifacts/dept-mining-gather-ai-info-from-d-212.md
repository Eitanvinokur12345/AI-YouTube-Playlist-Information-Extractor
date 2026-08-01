# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-212` (dept) · 2026-07-31T21:43:35.004013+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a real-time sweep on Hacker News for AI stories posted in the last 7 days using a script/tool (e.g., `hn` CLI, `praw`, or `scrapy`).
2. Extract titles, URLs, submission times, and upvote counts for each story.
3. Filter results to exclude job postings, low-effort content, and non-AI topics.
4. Generate a curated Markdown list with links, summaries (3-5 sentences), and metadata (source, date, engagement).
5. Store the output in a structured GitHub repo (e.g., `/data/hn_ai_sweep_YYYYMMDD.md`).
6. Schedule daily/weekly automated runs with GitHub Actions for incremental updates.

**What changed:** Focus narrowed to Hacker News as the primary real-time source for AI trends, replacing broader (and less actionable) multi-platform sweeps.
