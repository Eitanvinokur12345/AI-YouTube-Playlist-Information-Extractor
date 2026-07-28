# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-431` (dept) · 2026-07-28T13:05:07.805743+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Browse Reddit’s r/MachineLearning and r/AI to extract the top 10 trending posts by upvotes in the last 7 days.

**Plan:**
1. Use Reddit’s API or a scraping tool to fetch posts from r/MachineLearning and r/AI.
2. Filter posts published in the last 7 days.
3. Sort posts by upvotes (descending) and select the top 10.
4. Extract titles, URLs, upvote counts, and key themes (e.g., new models, benchmarks).
5. Compile results into a structured GitHub markdown table.
6. Share the output in the designated repository.

**What changed:**
Focus shifted from "diverse sources" to prioritizing Reddit’s AI communities for high-signal trending discussions.
