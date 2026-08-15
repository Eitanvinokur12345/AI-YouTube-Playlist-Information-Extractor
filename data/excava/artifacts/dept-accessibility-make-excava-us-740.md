# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-740` (dept) · 2026-08-15T05:00:14.768997+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 4px solid #005fcc focus ring with a 1px #fff outer stroke at 80% opacity.

**Plan:**
1. Implement the 4px #005fcc focus ring with 1px #fff outer stroke at 80% opacity globally.
2. Test WCAG 2.2 AA compliance for focus visibility on light/dark backgrounds.
3. Validate keyboard navigation across all interactive elements.
4. Ensure mobile/touch devices display focus indicators clearly.
5. Document the focus ring style in the design system’s accessibility guidelines.
6. Assign `accessibility-w1` as the owner for implementation and updates.

**What changed:**
Focus ring thickness increased to 4px with 1px #fff outer stroke at 80% opacity for WCAG 2.2 AA compliance across all themes and devices.
