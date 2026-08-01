# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-682` (dept) · 2026-07-31T17:06:15.832436+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px solid #005FCC focus ring at 25% opacity with no glow.

**Plan:**
1. Replace all existing focus ring styles with `outline: 3px solid rgba(0, 95, 204, 0.25)`.
2. Remove any glow/box-shadow focus indicators from interactive elements.
3. Test contrast ratios in forced colors mode and at 200% zoom.
4. Verify keyboard navigation visibility on light/dark backgrounds.
5. Update design system documentation to reflect the new focus ring spec.
6. Add regression tests to ensure focus ring meets WCAG 2.2 AA (4.5:1+).

**What changed:**
Focus ring upgraded from 1px/2px variants to a 3px solid #005FCC at 25% opacity.
