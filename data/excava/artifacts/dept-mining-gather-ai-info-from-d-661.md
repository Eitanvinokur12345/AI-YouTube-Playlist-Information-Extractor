# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-661` (dept) · 2026-07-31T03:23:05.757354+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a live sweep of GitHub’s trending AI repositories from the last 7 days with >50 stars, extracting core claims, tech stacks, and repo links.
2. Sweep Reddit’s AI subreddits (r/MachineLearning, r/artificial, r/learnmachinelearning) for posts in the last 7 days, extracting claims, tech stacks, and links.
3. Merge the two datasets into a single raw dataset of 40-80 high-signal items.
4. Apply a unified filtering step to remove duplicates, low-signal entries, and non-AI content.
5. Standardize the output format (claims, tech stack, link) for downstream analysis.
6. Output the final dataset in GitHub markdown format.

**What changed:** Combined GitHub and Reddit sweeps to ensure broader coverage while maintaining high signal.
