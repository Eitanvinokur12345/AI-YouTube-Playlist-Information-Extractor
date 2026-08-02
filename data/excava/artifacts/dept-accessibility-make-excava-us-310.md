# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-310` (dept) · 2026-08-02T04:03:20.842747+00:00
> Participants: Access, Ramp, Reader · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px #000 outer ring with a 1px white inner ring for focus indicators.

**Plan:**
1. Implement the 2px #000 outer ring with a 1px white inner ring as the default focus indicator.
2. Test visibility on light, dark, and high-contrast patterned backgrounds to ensure WCAG 2.1 AA compliance.
3. Verify keyboard navigation usability across all interactive elements.
4. Confirm touch target adequacy for mobile/touch users.
5. Document the focus ring style in the design system for consistency.
6. Gather user feedback post-implementation to address any edge cases.

**What changed:**
Focus indicator updated to 2px #000 outer ring with 1px white inner ring for broader accessibility compliance.
