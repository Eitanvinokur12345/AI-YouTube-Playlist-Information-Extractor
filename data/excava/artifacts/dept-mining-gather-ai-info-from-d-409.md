# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-409` (dept) · 2026-07-31T18:23:56.857212+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub for AI-related repos created in the last 7 days, ranked by stars and forks (top 20).
2. Extract trending AI posts from Hacker News (last 7 days), prioritizing engagement (comments, upvotes).
3. Cross-reference GitHub and HN results to identify overlapping trends (e.g., repos discussed on HN).
4. Query Product Hunt’s AI category (last 7 days) for trending launches, filtering by upvotes and maker activity.
5. Scan Reddit’s r/MachineLearning, r/artificial, and r/learnmachinelearning for AI discussions with high engagement (comments, awards).
6. Compile all findings into a unified markdown report with sources, metrics, and relevance scores.

**What changed:** Focus shifted from Telegram/social to GitHub/HN/Product Hunt/Reddit as primary sources, with cross-referencing for validation.
