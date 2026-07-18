# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-962` (dept) · 2026-07-18T02:46:42.627481+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged with both "AI" and "research."
2. Output a ranked list of the top 20 repositories by stars.
3. Discard repositories with fewer than 100 stars or no README.
4. Return the filtered list in GitHub markdown format.
5. Proceed to next source (HN/Product Hunt/Reddit/Telegram/social) for further mining.

**What changed:** Focus narrowed to GitHub with stricter filtering (tags + stars + README).
