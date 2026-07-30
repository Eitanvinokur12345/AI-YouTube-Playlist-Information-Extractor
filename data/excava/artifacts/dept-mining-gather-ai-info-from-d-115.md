# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-115` (dept) · 2026-07-30T20:30:20.974680+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Product Hunt for AI products launched in the last 7 days.
2. Extract top 20 results with name, tagline, launch date, upvotes, and direct link.
3. Output results in GitHub markdown format (one entry per line, pipe-separated).
4. Store raw dataset in a structured file (e.g., `ai_products_phunt_7d.md`).
5. Proceed to next source (GitHub/HN/Reddit/Telegram) after validation.

**What changed:** Focus narrowed to Product Hunt first, per Boulder’s directive.
