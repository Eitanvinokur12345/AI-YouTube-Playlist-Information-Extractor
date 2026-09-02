# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-431` (dept) · 2026-09-02T18:26:54.774802+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px focus ring at 7:1 contrast with a 0.5px inset shadow for all interactive elements.

**Plan:**
1. Update all interactive elements (buttons, links, form controls) to use a 3px focus ring with 7:1 contrast.
2. Add a 0.5px inset shadow at 7:1 contrast to ensure visibility in reduced motion and high contrast modes.
3. Test focus indicators in both light/dark themes and across reduced motion/high contrast modes.
4. Document the focus ring specifications in the design system (colors, dimensions, states).
5. Implement the changes in the component library and verify WCAG AAA compliance.
6. Conduct user testing with keyboard-only and screen reader users to confirm usability.

**What changed:**
Focus ring upgraded to 3px at 7:1 contrast with 0.5px inset shadow for cross-mode compatibility.
