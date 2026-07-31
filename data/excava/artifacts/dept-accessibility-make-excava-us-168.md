# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-168` (dept) · 2026-07-31T18:08:56.873939+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px solid #005FCC focus ring at 4.5:1 contrast with a 1px inner shadow at 30% opacity (#005FCC) on all focusable elements.

**Plan:**
1. Apply the 2px solid #005FCC focus ring (4.5:1 contrast) to all focusable elements.
2. Add a 1px inner shadow at 30% opacity (#005FCC) to soften edges.
3. Ensure the focus ring remains visible on busy backgrounds.
4. Test contrast ratios to confirm WCAG 2.2 AA compliance.
5. Document the focus style in the design system.
6. Validate with keyboard navigation testing.

**What changed:**
Focus indicator updated to 2px solid ring + 1px inner shadow for visibility and WCAG compliance.
