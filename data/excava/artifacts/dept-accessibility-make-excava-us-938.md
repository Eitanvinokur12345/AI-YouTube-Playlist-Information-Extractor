# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-938` (dept) · 2026-07-31T06:41:59.536142+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #0078D4 focus ring with 1px outer glow at 0s opacity, validated by live contrast tests at 125% zoom against brand palette.

**Plan:**
1. Implement the 2px solid #0078D4 focus ring with 1px outer glow (0s opacity) for all interactive elements.
2. Conduct live contrast tests at 125% zoom to ensure WCAG 2.2 Level AA compliance against the brand palette.
3. Document the focus ring specifications in the design system’s accessibility guidelines.
4. Update component libraries (React, Figma, Storybook) with the new focus ring style.
5. Test keyboard navigation across all major browsers and screen readers.
6. Monitor user feedback post-launch and iterate if issues arise.

**What changed:**
Focus ring updated to 2px solid #0078D4 with 1px outer glow (0s opacity) for better accessibility compliance.
