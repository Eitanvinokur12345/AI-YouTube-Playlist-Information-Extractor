# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-725` (dept) · 2026-07-09T15:20:03.667249+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit *both* static and dynamic accessibility in a cohesive report.

**Plan:**  
1. Set up a local dev environment and clone the repository.  
2. Run `npm install`, followed by `npm run build` to prepare the application.  
3. Execute `npm run test:accessibility` to evaluate static accessibility, focusing on contrast ratios and ARIA compliance.  
4. Conduct a live audit using Playwright’s accessibility checker on the staging branch with `npx playwright test --project=chromium --grep-invert="@skip"`.  
5. Stress-test the application with actual user flows to identify dynamic accessibility issues and race conditions.  
6. Compile findings from both audits into a single markdown report, including contrast ratios, ARIA compliance, and documented reproduction steps for identified issues.

**What changed:** Enhanced the accessibility audit scope to include both static and dynamic environments while integrating real user scenarios.
