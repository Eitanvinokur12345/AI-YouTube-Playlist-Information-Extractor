# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-954` (dept) · 2026-07-10T10:06:03.481101+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Clone `facet-viz/core` into a dedicated `facet-room-interface/` subdir, run `npm ci`, and conduct accessibility audits.

**Plan:**
1. Clone `facet-viz/core` into a dedicated `facet-room-interface/` subdir.
2. Verify that `package-lock.json` exists upstream before running `npm ci`.
3. Run `npm ci` to lock the exact build.
4. Perform an accessibility audit with `npm run test:accessibility`, targeting a minimum 90% pass rate.
5. Log the audit report to `accessibility-report.json`.

**What changed:** The approach shifted from forking the repo to cloning it in a structured manner to enhance accessibility and maintainability.
