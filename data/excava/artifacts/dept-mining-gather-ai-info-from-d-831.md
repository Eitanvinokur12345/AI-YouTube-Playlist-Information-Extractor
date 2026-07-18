# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-831` (dept) · 2026-07-18T15:31:22.661052+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" in the last 7 days.
2. Rank results by stars (descending) and filter for relevance (e.g., README clarity, recent commits).
3. Select top 10 repositories with brief reasons (e.g., "10k stars, active research in LLMs").
4. Output as a GitHub-flavored markdown list with links, stars, and tags.
5. Cross-check for diversity (avoid duplicate authors/projects).
6. Export results to a structured JSON file for further processing.

**What changed:** Shifted from Reddit to GitHub to prioritize code-based AI research sources.
