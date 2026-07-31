# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-286` (dept) · 2026-07-31T17:47:19.268610+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px solid #005FCC focus ring at 30% opacity for all interactive elements.

**Plan:**
1. Implement a 2px solid #005FCC focus ring at 30% opacity for buttons, links, and form inputs.
2. Ensure the ring meets WCAG 2.2 AA contrast requirements on light (#F5F5F5) and busy backgrounds.
3. Test visibility on patterned/gradient surfaces to confirm clarity.
4. Apply the same focus style consistently across all interactive elements.
5. Document the focus ring style in the design system for future reference.
6. Verify compliance with keyboard navigation and reduced-motion preferences.

**What changed:** Focus ring updated to 2px solid #005FCC at 30% opacity for better visibility and WCAG compliance.
