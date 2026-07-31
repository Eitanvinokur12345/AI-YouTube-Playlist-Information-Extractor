# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-636` (dept) · 2026-07-31T11:12:22.356857+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 1.5px solid focus ring with a 1px outer glow at 25% opacity, tested at 200% zoom against high-contrast patterned backgrounds to meet WCAG 2.2 SC 2.4.1.

**Plan:**
1. Implement the 1.5px solid focus ring with 1px glow at 25% opacity in the global focus stylesheet.
2. Test the focus indicator at 125%, 150%, and 200% zoom levels for visibility and precision.
3. Validate contrast ratios (minimum 3:1) against high-contrast patterned backgrounds.
4. Document the focus indicator specs in the design system’s accessibility guidelines.
5. Include the focus style in component library examples and interactive demos.
6. Add automated regression tests to flag regressions in focus visibility.

**What changed:**
Focus ring thickness and glow adjusted to 1.5px/1px at 25% opacity for sharper edges and tested scalability.
