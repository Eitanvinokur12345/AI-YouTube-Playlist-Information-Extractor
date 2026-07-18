# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-171` (dept) · 2026-07-18T22:29:20.898017+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" from the last 7 days, ranked by stars.
2. Extract top 10 repositories with names, descriptions, stars, and direct links.
3. Cross-reference with Reddit’s top 10 AI posts (last 7 days) for diversity.
4. Compile combined results into a structured dataset (CSV/JSON).
5. Prioritize sources with high engagement (stars, upvotes) and recent activity.
6. Output final report with ranked lists and metadata.

**What changed:** Shifted from single-source (GitHub-only) to multi-source (GitHub + Reddit) for broader AI info gathering.
