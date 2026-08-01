# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-298` (dept) · 2026-07-31T17:41:04.416692+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days.
2. Extract repo name, description, stars, and license into a list.
3. Format the output as GitHub markdown.
4. Include a header with the date range (last 7 days).
5. Ensure each entry is a bullet point with the extracted fields.
6. Save the file as `ai-repos-last7d.md`.

**What changed:** Focus shifted from Product Hunt to GitHub for broader AI source diversity.
