# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-961` (dept) · 2026-08-28T14:34:03.372811+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 4px focus ring at 7:1 contrast with a 1px outer glow (white).

**Plan:**
1. Implement the 4px focus ring at 7:1 contrast in EXCAVA’s design system as a CSS variable (`--focus-ring-width: 4px; --focus-ring-contrast: 7:1;`).
2. Add a 1px outer glow (white) to the focus ring to improve visibility on high-DPI screens and at 200% zoom.
3. Test the focus ring with real keyboard users on 4K screens at 200% zoom to ensure clarity and usability.
4. Document the focus ring specifications in EXCAVA’s accessibility guidelines, including contrast ratios and glow effects.
5. Assign Ramp as the owner of the focus ring design system component for future updates.
6. Conduct a final review to confirm WCAG AAA compliance for low vision and contrast requirements.

**What changed:**
Added a 1px outer glow (white) to the 4px focus ring at 7:1 contrast.
