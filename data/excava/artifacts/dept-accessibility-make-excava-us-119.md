# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-119` (dept) · 2026-07-31T22:36:16.659436+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px #005fcc focus ring with a 1px white inset shadow on all focusable elements.

**Plan:**
1. Update EXCAVA’s CSS system to define the focus ring style as `3px #005fcc ring with 1px white inset shadow` for all interactive elements.
2. Ensure the style meets WCAG 2.2 AA contrast requirements across light, dark, and patterned backgrounds.
3. Replace any existing focus ring styles (e.g., two-layer rings or box-shadow blurs) with the new 3px/1px inset shadow variant.
4. Test keyboard navigation across browsers/devices to verify crisp focus indicators on high-contrast and patterned surfaces.
5. Document the change in the EXCAVA design system with visual examples and contrast ratios.
6. Assign ownership of the CSS system to Ramp for future maintenance.

**What changed:** Focus ring style updated to 3px #005fcc with 1px white inset shadow for WCAG 2.2 AA compliance.
