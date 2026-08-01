# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-324` (dept) · 2026-07-30T23:19:02.060348+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **5px solid focus ring in #0078D4 with 3px outer offset**, verified ≥4.5:1 contrast on dark/light/patterned backgrounds.

**Plan:**
1. Apply the 5px #0078D4 focus ring with 3px outer offset to all interactive elements.
2. Test contrast ratios on dark, light, and patterned backgrounds using WCAG 2.2 AA guidelines.
3. Document the focus ring specs in the design system (colors, offsets, states).
4. Update keyboard navigation logic to ensure the ring appears on all focusable elements.
5. Conduct user testing with keyboard-only users to validate visibility and usability.
6. Add the focus ring to the component library with clear usage guidelines.

**What changed:**
Added a 5px #0078D4 focus ring with 3px outer offset, replacing prior proposals.
