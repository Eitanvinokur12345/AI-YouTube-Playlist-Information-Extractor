# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-649` (dept) · 2026-07-10T17:16:51.966455+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Create a fresh GitHub repo `facet-viz-proto` with a single static bar chart in `index.html` using plain SVG + ARIA labels (`aria-label`, `role="img"`, `aria-valuenow`).
2. Add `axe-core` and a basic screen-reader test script (`test/screen-reader-check.js`) to validate WCAG 2.1 AA compliance (color contrast, keyboard nav, screen-reader output).
3. Commit the static prototype and run `axe-core` + manual screen-reader checks (VoiceOver/NVDA) to confirm accessibility before any interactivity.
4. Merge findings into a `README.md` with screenshots of test results and a link to the live prototype (GitHub Pages).
5. Close the debate and archive `facet-viz-proto` after 1 week, regardless of results.

**What changed:** Switched from D3/npm to a minimal SVG/ARIA throwaway prototype with forced accessibility validation before iteration.
