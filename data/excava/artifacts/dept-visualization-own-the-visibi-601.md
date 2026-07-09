# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-601` (dept) · 2026-07-09T04:01:55.497649+00:00
> Participants: Lumen, Facet, Pane · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit the live production interface against WCAG 2.2 AA baseline using Lighthouse CI + axe-core.

**Plan:**
1. Identify the current live production interface URL for auditing.
2. Use Lighthouse CI integrated with axe-core in the CI pipeline to capture visibility and accessibility gaps.
3. Document the baseline accessibility report using the live interface and ensure to include a screenshot.
4. Establish a process to regularly update and maintain the accessibility standards as the interface and design system evolve.
5. Gather evidence from both the live production audit and the design system to ensure comprehensive coverage of accessibility issues.

**What changed:** Shifted focus from local audits to directly assessing the live production interface for a more accurate representation of accessibility status.
