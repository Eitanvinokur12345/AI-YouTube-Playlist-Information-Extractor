# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-274` (dept) · 2026-08-03T02:02:54.482443+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 4px #005fcc outer ring with 2px white inner ring for focus indicators.

**Plan:**
1. Update focus indicator styles in the component library to use `4px #005fcc` outer ring with `2px white` inset.
2. Verify WCAG 2.2 contrast ratios (4.5:1+) on light/dark patterned backgrounds via automated and manual testing.
3. Document the focus ring design in the accessibility guidelines for EXCAVA.
4. Replace existing focus indicators in all interactive components (buttons, links, form elements).
5. Conduct a cross-browser/device audit to ensure consistency.
6. Add a design token (`focus-ring-primary`) for maintainability.

**What changed:** Focus indicators now use a 4px #005fcc outer ring with 2px white inset.
