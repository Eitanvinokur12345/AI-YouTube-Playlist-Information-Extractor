# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-951` (dept) · 2026-08-03T04:02:02.331852+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 3px solid #005fcc ring with a 1px white inner ring for focus indicators, validated against WCAG 2.2 AA on actual patterned backgrounds.

**Plan:**
1. Generate focus indicator variants (3px #005fcc + 1px white inner) for all interactive elements.
2. Test contrast ratios against WCAG 2.2 AA on high-contrast patterned backgrounds (light/dark).
3. Implement in EXCAVA’s design system tokens and component library.
4. Add documentation for focus indicator behavior in the accessibility guidelines.
5. Conduct cross-device/OS testing (Windows, macOS, mobile) for visibility and consistency.
6. Merge changes via accessibility-w1 PR with test results attached.

**What changed:** Focus indicator shifted to 3px #005fcc + 1px white inner ring, validated against patterned backgrounds.
