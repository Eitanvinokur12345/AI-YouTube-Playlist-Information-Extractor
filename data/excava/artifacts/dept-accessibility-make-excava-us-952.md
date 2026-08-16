# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-952` (dept) · 2026-08-16T22:51:07.145001+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 4px solid #005fcc focus ring with a 2px outer glow at 20% opacity.

**Plan:**
1. Update EXCAVA’s focus ring style to `4px solid #005fcc` with `2px outer glow at 20% opacity`.
2. Test focus visibility on low-contrast backgrounds and patterned UI elements.
3. Validate WCAG 2.1 AA compliance for focus visibility (minimum 3:1 contrast ratio).
4. Conduct mobile/touch usability tests to ensure fat-finger targets are hit reliably.
5. Document the focus ring style in EXCAVA’s design system for consistency.
6. Deploy changes and monitor user feedback for adjustments.

**What changed:** Focus ring increased to 4px with 2px outer glow for better accessibility and touch usability.
