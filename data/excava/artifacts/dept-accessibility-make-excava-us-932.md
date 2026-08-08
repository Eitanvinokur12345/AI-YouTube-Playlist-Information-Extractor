# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-932` (dept) · 2026-08-08T21:02:21.717736+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 1px #ffffff outer ring for universal accessibility.

**Plan:**
1. Implement the 3px solid #005fcc focus ring with a 1px #ffffff outer ring across all interactive elements.
2. Test WCAG 2.1 AA compliance for solid backgrounds and WCAG 2.1 AAA for patterned backgrounds.
3. Ensure the ring remains compact enough for small touch targets (minimum 44x44px interactive areas).
4. Document the focus indicator style in the design system with usage guidelines.
5. Assign Ramp as the owner for maintenance and updates.
6. Deploy the component by [date] with rollback plans if issues arise.

**What changed:**
Focus indicator updated from 4px/2px to 3px/1px ring configuration.
