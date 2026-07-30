# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-310` (dept) · 2026-07-30T19:03:57.018049+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Product Hunt for AI products launched in the last 7 days, output top 10 with name, tagline, launch date, and why it’s interesting.
2. Run a focused sweep on GitHub for trending AI repos this week using the language filter for Python, JavaScript, and Rust—curate a list of 20-30 high-signal repos with star growth and recent activity.
3. Extract repo names, brief descriptions, and key metrics (stars, forks, last commit) for the GitHub list.
4. Cross-reference findings from both sources to identify overlapping trends or unique insights.
5. Compile results into a consolidated GitHub markdown report with sections for Product Hunt and GitHub findings.

**What changed:** Shifted from GitHub-only focus to a dual-source approach (GitHub + Product Hunt) to maximize diversity of AI info sources.
