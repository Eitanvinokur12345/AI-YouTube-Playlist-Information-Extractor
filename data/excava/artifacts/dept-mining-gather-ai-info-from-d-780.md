# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-780` (dept) · 2026-07-28T12:21:10.051593+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for repos tagged "AI" and "research" (Python, Jupyter Notebook, or Markdown).
2. Rank repos by stars (descending), then by last commit activity (descending).
3. Output top 10 repos with name, stars, last commit date, and direct GitHub link.
4. Cross-reference top 3 repos with Reddit’s r/MachineLearning and r/AI for community engagement.
5. Compile final list of 10 repos (GitHub + Reddit overlap) with engagement metrics.

**What changed:** Focused on GitHub-first synthesis with Reddit validation, prioritizing star activity and recency.
