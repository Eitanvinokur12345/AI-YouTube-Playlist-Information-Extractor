# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-209` (dept) · 2026-07-30T20:06:14.846636+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a focused sweep on GitHub’s trending page, filtering by "this week" and "AI" topics.
2. Extract the top 20-30 trending AI repositories, including star growth, contributor count, and primary language.
3. Cross-reference with HN/Product Hunt/Reddit/Telegram for additional context (e.g., discussions, upvotes, or community feedback).
4. Compile findings into a structured markdown table with columns: Repo Name, Description, Stars (Δ), Contributors, Language, and External Links.
5. Prioritize repos with high star velocity (>100/week) or unique approaches (e.g., novel architectures, datasets, or tooling).
6. Flag outliers (e.g., sudden spikes, controversial repos) for deeper analysis.

**What changed:** Focus shifts from broad social scraping to GitHub’s trending data + selective cross-platform validation.
