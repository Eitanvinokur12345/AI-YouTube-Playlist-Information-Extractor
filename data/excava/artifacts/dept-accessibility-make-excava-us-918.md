# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-918` (dept) · 2026-08-05T20:11:15.549283+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 4px outer ring in #005fcc with a 2px white inner ring for focus indicators.

**Plan:**
1. Implement the 4px outer ring with 2px white inner ring in #005fcc for focus indicators in EXCAVA’s CSS.
2. Conduct live testing on patterned backgrounds by the accessibility team by EOD Friday.
3. Document test results, including edge cases where focus visibility may still be compromised.
4. Iterate on the design if testing reveals unresolved visibility issues.
5. Ensure the focus indicator meets WCAG 2.2 AA for contrast and visibility across all backgrounds.
6. Merge changes into the main branch after validation.

**What changed:** Focus indicator style updated to 4px #005fcc outer ring with 2px white inner ring.
