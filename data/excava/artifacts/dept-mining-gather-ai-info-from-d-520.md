# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-520` (dept) · 2026-07-31T22:22:02.742671+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Reddit’s AI subreddits (r/MachineLearning, r/artificial, r/learnmachinelearning) for top posts in the last 7 days.
2. Extract key details (title, URL, upvotes, summary) into a single list.
3. Cross-reference with GitHub’s trending AI repos (last 7 days) for additional sources.
4. Compile a raw but structured dataset of fresh AI activity in GitHub markdown format.
5. Include a brief note on inclusion criteria (e.g., relevance, recency).
6. Output the final list with clear headers for each source.

**What changed:** Focus narrowed to Reddit + GitHub only, excluding other platforms for brevity.
