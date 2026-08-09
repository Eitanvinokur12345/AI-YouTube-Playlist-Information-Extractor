# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-228` (dept) · 2026-08-09T05:30:51.900838+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 2px solid #005fcc focus ring with no inner ring for focus indicators.

**Plan:**
1. Implement the 2px solid #005fcc focus ring globally in the EXCAVA stylesheet.
2. Remove all instances of the 4px outer ring with 2px white inner ring.
3. Test the focus ring on high-contrast patterned backgrounds (e.g., zebra-striped).
4. Verify WCAG 2.2 AA compliance for focus visibility across all backgrounds.
5. Document the decision in the accessibility guidelines for EXCAVA.
6. Deploy the change in the next scheduled release.

**What changed:** Focus ring reduced to 2px solid #005fcc with no inner ring.
