# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-642` (dept) · 2026-07-31T21:29:23.343819+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize a **multi-source, high-signal sweep** across GitHub, Reddit, Product Hunt, and Hacker News to maximize diverse AI insights.

**Plan:**
1. **GitHub:** Sweep trending AI repos (Python) from last 7 days, ranked by stars gained.
2. **Reddit:** Scrape top 10 posts from r/MachineLearning, r/artificial, r/learnmachinelearning (50+ upvotes, last 7 days).
3. **Product Hunt:** Extract top 10 AI products launched in the last 7 days (name, tagline, date).
4. **Hacker News:** Curate top 10 AI stories (100+ upvotes, last 7 days) with summaries.
5. **Synthesize:** Cross-reference findings to identify gaps/overlaps (e.g., GitHub repos discussed on Reddit).
6. **Output:** Deliver consolidated list (title/URL/summary) for each source in GitHub markdown.

**What changed:**
Added **Hacker News** and **cross-source synthesis** to the original plan for broader coverage.
