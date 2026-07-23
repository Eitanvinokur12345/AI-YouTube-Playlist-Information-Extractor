# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-628` (dept) · 2026-07-23T23:30:39.402751+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" (last 30 days).
2. Rank by stars (descending) and filter for last commit within 90 days.
3. Output top 20 with stars, last commit date, and a one-line reason for inclusion.
4. Cross-check top 5 against Hacker News (last 7 days) for overlap/validation.
5. Append Reddit’s top 10 AI posts (last 7 days) to the dataset.
6. Merge and deduplicate, prioritizing GitHub > HN > Reddit.

**What changed:** Shifted from Reddit-only to GitHub-first, then layered HN/Reddit for diversity.
