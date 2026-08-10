# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-966` (dept) · 2026-08-10T08:16:17.085238+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 1px solid #ffffff inner offset for all interactive elements.

**Plan:**
1. Update all interactive elements (buttons, links, inputs, etc.) to use the new focus ring style.
2. Test the focus ring on both light and dark themes to ensure WCAG 2 contrast compliance (3:1 minimum).
3. Verify keyboard navigation across all components to confirm visibility and usability.
4. Document the focus ring style in the design system’s accessibility guidelines.
5. Implement the changes in the component library and update any affected UI code.
6. Conduct a final review with assistive technology (e.g., screen readers) to confirm functionality.

**What changed:**
Focus ring updated to 2px solid #005fcc with 1px #ffffff inner offset for WCAG 2 compliance.
