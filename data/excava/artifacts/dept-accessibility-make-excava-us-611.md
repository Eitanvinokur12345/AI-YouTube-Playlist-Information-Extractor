# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-611` (dept) · 2026-08-03T04:54:23.668370+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc ring with a 1px white inner ring for focus indicators.

**Plan:**
1. Implement a 3px #005fcc outer ring with a 1px white inner ring for focus indicators.
2. Test contrast on high-contrast patterned backgrounds.
3. If contrast fails WCAG 2.2 AA, add a 1px black outer outline.
4. Ensure touch-friendly sizing (minimum 2px touch target).
5. Validate keyboard navigation and reduced-motion compatibility.
6. Document the final focus style in the design system.

**What changed:** Switched from 4px ring to 3px ring with optional black outline for better pattern resilience.
