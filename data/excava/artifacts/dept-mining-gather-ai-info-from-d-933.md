# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-933` (dept) · 2026-07-18T02:10:22.557639+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research," ranked by stars and forks.
2. Filter results for "odd gems" (low stars but high signal: unique approaches, recent activity, or niche relevance).
3. Cross-reference top 10 high-impact projects with other sources (HN/Reddit/Telegram) for validation.
4. Extract key metadata (description, stars, forks, last commit, license) for each candidate.
5. Compile a curated list of 10 high-impact + 5 odd-gem projects with brief justifications.
6. Output as a GitHub-flavored markdown table with columns: Rank, Project, Stars, Forks, Signal Score, Source.

**What changed:** Expanded scope to include "odd gems" and multi-source validation.
