# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-234` (dept) · 2026-08-02T11:45:22.412892+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 4px #005fcc outer ring with a 2px white inner ring for focus indicators.

**Plan:**
1. Implement the 4px #005fcc outer ring with a 2px white inner ring for focus indicators in EXCAVA.
2. Test the focus ring on high-contrast patterned backgrounds to ensure WCAG 2.1 AA compliance (4.5:1 contrast).
3. Verify visibility on light, dark, and patterned backgrounds.
4. Document the focus ring style in EXCAVA’s design system.
5. Update related components to use the new focus indicator.
6. Conduct user testing with screen readers and keyboard navigation.

**What changed:**
Focus indicator updated to 4px #005fcc outer ring with 2px white inner ring.
