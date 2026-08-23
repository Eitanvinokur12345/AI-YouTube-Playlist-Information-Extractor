# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-165` (dept) · 2026-08-23T18:14:47.146794+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 1.5px solid focus ring at 5:1 contrast with 1px sharp outer stroke.

**Plan:**
1. Update EXCAVA’s design system repo with the approved focus ring CSS snippet.
2. Apply the new focus ring to all interactive elements (buttons, links, inputs).
3. Test visibility on high-DPI screens at 200% zoom with screen readers.
4. Verify WCAG AA compliance for focus visibility across all contrast modes.
5. Document the change in the design system’s accessibility guidelines.
6. Assign `accessibility-w1` as the owner for future focus ring refinements.

**What changed:**
Focus ring adjusted to 1.5px solid at 5:1 contrast with 1px sharp outer stroke for sharper visibility on high-DPI screens.
