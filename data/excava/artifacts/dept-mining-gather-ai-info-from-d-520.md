# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-520` (dept) · 2026-07-18T10:00:08.594883+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research," outputting a ranked list of 10 with names, star counts, and brief descriptions.
2. Cross-reference the GitHub results with Product Hunt’s top 10 AI products launched in the last 7 days, extracting names, descriptions, and upvotes.
3. Compile a combined dataset of 20 diverse AI tools (10 GitHub, 10 Product Hunt).
4. Enrich entries with metadata (e.g., tags, launch dates) from each source.
5. Export the dataset in a structured format (CSV/JSON) for further analysis.

**What changed:** Shifted from exclusive Product Hunt focus to a dual-source approach (GitHub + Product Hunt) for broader diversity.
