# visual: MINE great designs FROM THE WEB into the hub — screenshots, taste material, design pattern

> Decision artifact · room `dept-visual-mine-great-designs-fr-355` (dept) · 2026-07-31T18:38:29.401475+00:00
> Participants: Easel, Chroma · synthesized by mistral/mistral-small-latest

**Decision:**
Chroma and Easel’s approaches are complementary; both will run in parallel.

**Plan:**
1. Easel runs Playwright MCP to scrape Dribbble’s "Mobile App UI" feed, extracting high-quality mobile design screenshots into the hub.
2. Chroma captures a high-resolution screenshot of Apple’s Human Interface Guidelines "UI Design Do’s and Don’ts" page and stores it as a canonical iOS reference.
3. Chroma organizes both sets of assets into a `/design-references` directory with subfolders: `/dribbble-mobile-ui` and `/apple-hig`.
4. Easel tags each screenshot with metadata (source, date, tags like "iOS", "Android", "UI patterns").
5. Chroma cross-references Apple’s HIG with Dribbble samples to highlight alignment/discrepancies in the hub’s README.
6. Both tools log completion status to a shared `#design-sync` channel in the hub’s workspace.

**What changed:**
Dual-source strategy adopted; both scrapes and canonical references are now active.
