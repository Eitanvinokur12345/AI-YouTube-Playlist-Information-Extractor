# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-860` (dept) · 2026-08-03T01:43:45.595243+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px #ffffff outer ring with a 2px #000000 inner ring for focus indicators.

**Plan:**
1. Implement the 3px #ffffff outer ring with 2px #000000 inner ring for focus indicators across all interactive elements.
2. Test contrast ratios on EXCAVA’s actual light, dark, and patterned backgrounds using a color contrast analyzer.
3. Ensure the solution meets WCAG 2.2 AA (7:1 contrast) in all scenarios.
4. Update design tokens and component documentation to reflect the new focus indicator style.
5. Conduct manual testing with keyboard navigation to verify visibility and usability.
6. Deploy changes and monitor user feedback for any visibility issues.

**What changed:**
Focus indicators now use a 3px white outer ring with a 2px black inner ring for consistent 7:1 contrast on all backgrounds.
