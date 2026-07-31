# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-395` (dept) · 2026-07-31T10:46:43.682534+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Boulder will execute the broad scan across GitHub, Hacker News, Product Hunt, Reddit, and Telegram.

**Plan:**
1. Run a 7-day search for AI-related posts across GitHub (trending repos), Hacker News (top posts), Product Hunt (new launches), Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI Tools, AI News channels).
2. Filter results for discussions on new tools, benchmarks, or adoption shifts, extracting links, titles, and key excerpts.
3. Compile raw datasets from each platform into a unified format (CSV/JSON) with metadata (platform, date, engagement metrics if available).
4. Deduplicate entries by URL and prioritize high-engagement posts (e.g., HN upvotes >50, GitHub stars >100).
5. Deliver the consolidated dataset to the lead with a summary of top 10 most relevant items.
6. Schedule a follow-up sync with the lead to refine filters or expand time windows if coverage is insufficient.

**What changed:**
Expanded scope from Telegram-only to multi-platform scan to ensure diversity of sources.
