# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-547` (dept) · 2026-07-31T16:44:58.663099+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize Reddit’s r/MachineLearning and r/AI for high-signal AI developments over Product Hunt’s launches due to deeper technical discussion and research focus.

**Plan:**
1. **Scrape Reddit** (r/MachineLearning + r/AI) for top 10 most-discussed AI tools/papers/datasets from the last 7 days.
2. **Extract** key claims, limitations, and user-reported flaws for each item.
3. **Rank** by engagement (upvotes/comments) and relevance to mining goals.
4. **Cross-reference** GitHub/Telegram for additional context (e.g., repo activity, community chatter).
5. **Compile** into a concise markdown table with columns: *Tool/Paper*, *Core Claim*, *Limitations*, *Source*, *Engagement Metrics*.
6. **Share** with the team for review and prioritization of follow-up actions.

**What changed:** Switched from Product Hunt (surface-level trends) to Reddit (depth + research) for higher-quality AI insights.
