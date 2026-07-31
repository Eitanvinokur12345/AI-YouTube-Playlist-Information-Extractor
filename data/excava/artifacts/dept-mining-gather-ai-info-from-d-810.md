# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-810` (dept) · 2026-07-31T05:05:12.259452+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a targeted GitHub search for AI repositories created in the last 7 days with stars >100 and topics "llm," "agent," or "rag."
2. Extract key details (name, description, stars, last commit date) for each repository.
3. Curate the results into a list of 20-50 high-potential repositories.
4. Output the final list in GitHub markdown format.
5. Validate the list for duplicates, outdated info, and relevance.
6. Finalize and present the curated list.

**What changed:** Focus narrowed to GitHub-only, high-signal repositories with strict recency and engagement filters.
