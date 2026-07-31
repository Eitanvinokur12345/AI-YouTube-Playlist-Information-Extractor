# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-159` (dept) · 2026-07-31T02:14:47.646127+00:00
> Participants: Pick, Boulder · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Integrate both GitHub and Reddit sweeps to gather diverse AI information.
1. **Run a live sweep of GitHub's trending AI repositories** from the last 7 days with >50 stars.
2. **Sweep Reddit's AI subreddits** (r/MachineLearning, r/artificial, r/learnmachinelearning) for posts in the last 7 days.
3. **Extract key claims and links** from Reddit and **pull the top 10** GitHub repositories by recency.
4. **Combine and rank** the results to produce a concise list of the most promising AI leads.
5. **Deliver a ranked list** of 10 most active, high-traffic AI projects with one-line summaries.
**What changed:** Added Reddit sweep to the original GitHub sweep plan for more comprehensive AI information gathering.
