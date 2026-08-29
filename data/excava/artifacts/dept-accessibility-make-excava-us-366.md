# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-366` (dept) · 2026-08-29T03:25:12.836268+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast with 1px solid fallback on high-DPI screens.

**Plan:**
1. Implement 3px focus ring with 7:1 contrast ratio across all interactive elements.
2. Add 1px solid fallback for high-DPI screens to maintain crisp edges.
3. Test layout shift impact on dynamic content with keyboard navigation.
4. Validate with 3 real screen-reader users for usability feedback.
5. Document the decision in the design system with usage guidelines.
6. Monitor real-world usage metrics for focus ring effectiveness.

**What changed:** Focus ring reduced from 4px to 3px at 7:1 contrast with high-DPI fallback.
