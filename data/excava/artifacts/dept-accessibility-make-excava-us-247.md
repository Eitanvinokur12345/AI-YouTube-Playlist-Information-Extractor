# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-247` (dept) · 2026-07-31T16:23:30.443853+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Use a 2px solid #005FCC focus ring with a 1px outward glow on all interactive elements.

**Plan:**
1. Implement CSS rule: `outline: 2px solid #005FCC; box-shadow: 0 0 1px 1px #005FCC;` for `:focus-visible` on all interactive elements.
2. Validate WCAG 2.2 AA contrast (3:1 minimum) for the focus ring on light backgrounds via Playwright MCP.
3. Test keyboard navigation with Playwright MCP to ensure focus rings are visible and unobstructed.
4. Test touch targets on mobile to confirm no overlap or accidental misses.
5. Document the CSS rule and test results in the project’s accessibility guidelines.
6. Assign Ramp to deliver the final CSS and test suite by [date].

**What changed:** Focus ring adjusted to 2px solid with 1px outward glow for balanced accessibility and tap space.
