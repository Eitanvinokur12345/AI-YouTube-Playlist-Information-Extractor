# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-410` (dept) · 2026-07-31T16:02:21.317739+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 1.5px solid #005FCC focus ring with a 2px outer glow for all interactive elements.

**Plan:**
1. Update focus ring styles to `1.5px solid #005FCC` with `2px outer glow` across all interactive components.
2. Validate WCAG 2.2 AA contrast ratios for the focus ring on light/dark backgrounds via Playwright MCP.
3. Test touch target integrity (44px) and tap accuracy on iOS/Android at 200% zoom using Playwright MCP.
4. Document focus ring specs in the design system’s accessibility guidelines.
5. Implement changes in the next sprint, prioritizing high-traffic interactive elements.
6. Conduct user testing with keyboard and touch users to confirm usability.

**What changed:**
Focus ring width increased from 1px/2px to 1.5px with 2px glow for balanced accessibility.
