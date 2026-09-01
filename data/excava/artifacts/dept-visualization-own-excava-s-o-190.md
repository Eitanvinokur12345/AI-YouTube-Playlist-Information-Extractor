# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-190` (dept) · 2026-09-01T03:37:13.947396+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend as a thin, persistent top strip that collapses to a slim tab when unused.

**Plan:**
1. Implement a sticky top strip (12px height) for the legend, matching Manus’ dark theme.
2. Add a collapse toggle (slim tab) that expands to full height (48px) on hover/click.
3. Ensure the strip stays fixed at the top, never scrolling out of view.
4. Reserve the left sidebar for primary controls/context, keeping the graph’s horizontal space intact.
5. Test liveliness by animating the strip’s expansion/collapse (e.g., 150ms fade).
6. Validate clarity by ensuring the legend remains high-contrast (e.g., white text on dark bg).

**What changed:**
Replaced the debated sidebar/banner with a minimalist, always-accessible top strip for the legend.
