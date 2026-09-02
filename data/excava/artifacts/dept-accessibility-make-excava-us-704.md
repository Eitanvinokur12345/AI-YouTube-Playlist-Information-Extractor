# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-704` (dept) · 2026-09-02T21:33:04.858294+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px focus ring at 7:1 contrast with a 0.5px inset shadow for all interactive elements.

**Plan:**
1. Implement a 3px solid focus ring with 7:1 contrast for all interactive elements.
2. Add a 0.5px inset shadow to the focus ring to ensure visibility in high-contrast and reduced-motion modes.
3. Test focus visibility in normal, reduced-motion, and high-contrast modes across devices.
4. Validate WCAG 2.2 AA compliance for focus visibility in all tested modes.
5. Document the focus ring specifications in the design system for consistency.
6. Gather user feedback on focus ring usability and adjust if needed.

**What changed:**
Focus ring now uses 3px at 7:1 contrast with 0.5px inset shadow for cross-mode visibility.
