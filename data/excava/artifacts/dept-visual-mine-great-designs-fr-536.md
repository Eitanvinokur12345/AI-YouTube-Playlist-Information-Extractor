# visual: MINE great designs FROM THE WEB into the hub — screenshots, taste material, design pattern

> Decision artifact · room `dept-visual-mine-great-designs-fr-536` (dept) · 2026-07-31T09:28:38.366192+00:00
> Participants: Easel, Chroma · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Twitter API (or scrape top tweets) for design systems tagged with #designsystem, #ui, or #ux.
2. Rank results by engagement (likes/retweets) and select top 3.
3. Use Playwright MCP to screenshot the landing pages of each selected design system.
4. Upload screenshots to the hub with filenames: `design-system-{rank}-{source}.png`.
5. Add metadata tags: `source:twitter`, `type:screenshot`, `trend:top-tweeted`.
6. Notify the hub via webhook/API that new taste material is available.

**What changed:** Switched from Dribbble (Chroma’s suggestion) to Twitter (Easel’s suggestion) for sourcing top-tweeted design systems.
