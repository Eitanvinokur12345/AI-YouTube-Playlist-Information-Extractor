# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-972` (dept) · 2026-07-31T20:32:11.148764+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days, filtering by stars, forks, and recent activity.
2. Output a list of 10-15 high-signal items with plain-language summaries of their purpose and novelty.
3. Exclude repos with <10 stars or no README to ensure quality.
4. Prioritize repos with recent commits (last 3 days) or active discussions (issues/PRs).
5. Format output as a GitHub-flavored markdown list with bolded names, links, and summaries.

**What changed:** Focus narrowed to GitHub-only, last 7 days, high-signal repos.
