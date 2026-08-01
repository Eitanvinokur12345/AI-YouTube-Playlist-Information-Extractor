# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-661` (dept) · 2026-07-31T16:02:56.215484+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Run a multi-source sweep combining GitHub, Reddit, and Product Hunt for AI trends, prioritizing GitHub’s depth and Reddit’s community insights.

**Plan:**
1. **GitHub Sweep:** Scrape trending AI repos from the last 7 days with >50 stars, extracting claims, tech stacks, and links (target: 20-40 repos).
2. **Reddit Sweep:** Parse AI subreddits (r/MachineLearning, r/artificial, r/learnmachinelearning) for posts in the last 7 days, extracting claims, tech stacks, and links (target: 20-40 items).
3. **Product Hunt Sweep:** Collect AI launches from the last 7 days, extracting claims, tech stacks, and product links (target: 10-20 items).
4. **Merge & Deduplicate:** Combine datasets, remove duplicates, and standardize fields (claims, tech stacks, links).
5. **Filter for High-Signal:** Apply criteria (e.g., novelty, technical depth, engagement) to reduce to 30-50 items for downstream analysis.
6. **Export:** Save as a structured markdown table for further processing.

**What changed:**
Telegram sweep dropped in favor of GitHub/Reddit/Product Hunt to balance depth, community insights, and launch trends.
