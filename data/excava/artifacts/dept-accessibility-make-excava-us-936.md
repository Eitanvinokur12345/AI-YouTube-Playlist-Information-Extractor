# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-936` (dept) · 2026-08-03T02:21:59.259748+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px #ffffff inner ring with a 2px #000000 outer ring for focus indicators.

**Plan:**
1. Update EXCAVA’s focus indicator to a 2px solid white inner ring with a 2px solid black outer ring.
2. Test visibility on light, dark, and patterned backgrounds to ensure WCAG 2.2 3:1 contrast compliance.
3. Validate keyboard navigation and reduced-motion compatibility with the new focus ring.
4. Update the design artifact (EXCAVA) to reflect the new focus indicator style.
5. Document the change in the project’s accessibility guidelines.

**What changed:**
Focus indicator updated to 2px white inner ring + 2px black outer ring.
