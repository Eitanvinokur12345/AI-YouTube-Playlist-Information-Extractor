# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-984` (dept) · 2026-07-30T20:29:27.139928+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a 3px outset focus ring with 4.5:1 contrast and 2px spacing, tested across light/dark modes, mobile, and keyboard navigation.

**Plan:**
1. Implement a 3px focus ring with 2px spacing for all interactive elements.
2. Use #005FCC on light backgrounds and #00BFFF on dark backgrounds to ensure visibility.
3. Add a 1px white outline to the ring for low-contrast dark backgrounds.
4. Test across light/dark modes, mobile/touch, and keyboard navigation.
5. Verify WCAG 2.2 AA contrast compliance for the focus ring.
6. Document the focus ring styles in the design system.

**What changed:**
Added a 3px focus ring with 2px spacing, high-contrast colors, and a white outline for low-contrast dark backgrounds.
