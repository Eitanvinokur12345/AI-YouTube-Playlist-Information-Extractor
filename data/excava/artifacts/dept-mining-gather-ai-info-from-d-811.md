# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-811` (dept) · 2026-08-05T02:07:54.408706+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data (titles, descriptions, upvotes, launch dates) into a structured format.
3. Cross-reference with GitHub’s API to identify repositories linked in Product Hunt posts.
4. Scrape Hacker News (HN) for AI-related discussions in the last 30 days, focusing on comments and links.
5. Aggregate Reddit’s top AI posts (last 30 days) from r/MachineLearning, r/artificial, and r/learnmachinelearning.
6. Compile all data into a unified dataset for AI info mining.

**What changed:** Focused on Product Hunt API as primary source, supplemented with GitHub, HN, and Reddit for diversity.
