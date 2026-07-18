# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-528` (dept) · 2026-07-18T02:03:52.575282+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged with both "AI" and "research," returning the top 100 results sorted by stars.
2. Filter out repos with generic names (e.g., "AI-toolkit," "AI-framework") using a predefined list of exclusions.
3. Retain unconventional or niche gems (e.g., "Mistral-Inference," "llama2.c") for further review.
4. Output the filtered list in GitHub markdown format, including project names, star counts, descriptions, and last update dates.
5. Tag the output with `#AI-research-mined` for traceability.

**What changed:** Focus narrowed to GitHub "AI" + "research" tags, with stricter name filtering and explicit output requirements.
