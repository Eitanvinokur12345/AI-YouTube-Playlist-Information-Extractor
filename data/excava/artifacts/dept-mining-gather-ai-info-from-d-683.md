# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-683` (dept) · 2026-07-31T01:16:32.407110+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for trending AI repos in the last 7 days, filtering for star delta >50, output ranked list with name, star delta, language, and one-line summary.
2. Sweep Reddit’s r/MachineLearning and r/artificial for posts in the last 7 days, filtering for >50 upvotes and fresh comments, output ranked list with title, upvotes, subreddit, and one-line summary.
3. Sweep Product Hunt for AI products launched in the last 7 days, output ranked list with name, upvotes, category, and one-line description.
4. Sweep Telegram’s AI channels for fresh posts in the last 7 days, output ranked list with title, channel, engagement delta, and one-line summary.
5. Deduplicate and merge all ranked lists into a single consolidated output, prioritizing unique sources and high-engagement items.
6. Export final ranked list as GitHub markdown table with columns: Source, Title/Name, Metric (stars/upvotes/engagement), Language/Category, and Summary.

**What changed:** Consolidated all proposed actions into a structured, multi-source mining plan with deduplication.
