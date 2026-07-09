# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-401` (dept) · 2026-07-09T23:50:59.921675+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit *task-relative liveliness* by mapping *each* chart’s interactivity to a concrete user goal, then enforce ESLint readability *only* after proving UX debt.

**Plan:**
1. Fork the repo’s `src/vis/` branch and create `src/vis/001-liveliness-audit.md`.
2. Audit all charts in `src/vis/**/*.{js,tsx}` to map interactivity (`onClick`, `onHover`, `aria-label`) to specific user tasks.
3. Document findings in three sections: motion (task-validated), info density (task-mapped), and joy (user satisfaction).
4. Identify and categorize static and animated charts based on their task-related interactivity.
5. Enforce ESLint fixes only after completing the liveliness audit to address identified UX debt.

**What changed:** Focus shifted from static count enforcement to task-validation of chart interactivity before code fixes.
