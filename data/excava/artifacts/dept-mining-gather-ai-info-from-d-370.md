# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-370` (dept) · 2026-07-17T17:40:49.995308+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged with both "AI" and "research," ranking results by stars.
2. Extract the top 50 projects, including their names, star counts, last update dates, and a one-line justification for inclusion.
3. Filter for projects with recent activity (last update within the past 12 months).
4. Prioritize repositories with clear research focus or novel approaches (e.g., papers, benchmarks, or unique architectures).
5. Export results in a structured GitHub markdown table format.
6. Cross-reference with other sources (HN/Reddit) to validate trending status.

**What changed:** Focus narrowed to "AI" + "research" tags, reducing scope to 50 high-signal projects with stricter recency and novelty criteria.
