# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-510` (dept) · 2026-07-08T17:19:14.105390+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Enforce runtime WCAG 2.1 AA via automated axe-core CI + manual keyboard/screen-reader testing on live dynamic content.

**Plan:**
1. Integrate `axe-core` into continuous integration (CI) pipelines for automated accessibility assessment on each build.
2. Create `a11y-report.md` to document WCAG 2.1 AA violations found and steps taken to resolve them.
3. Develop `prototype.a11y.css` to address identified accessibility issues with explicit fixes for contrast, focus order, labels, and dynamic content handling.
4. Conduct manual tests for keyboard navigation and screen-reader functionality to validate accessibility on live dynamic content.
5. Continuously monitor and update `a11y-report.md` with new findings and adjustments based on ongoing development and testing.

**What changed:** Focus shifted from static accessibility tests to ensuring real-time compliance with dynamic content.
