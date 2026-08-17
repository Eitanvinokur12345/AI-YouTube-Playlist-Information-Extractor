# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-325` (dept) · 2026-08-17T01:21:59.137129+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with 30% inner glow at 4px spread for EXCAVA.

**Plan:**
1. Implement focus ring style: `2px solid #005fcc` with `box-shadow: 0 0 4px rgba(0, 95, 204, 0.3)`.
2. Test on patterned backgrounds and OS/browser focus overrides to verify WCAG 2.1 AA compliance.
3. Validate mobile/touch target spacing to ensure no accidental activation during quick tabbing.
4. Document focus ring specs in EXCAVA’s design system for consistency.
5. Assign `accessibility-w1` as owner for ongoing maintenance and testing.
6. Add focus ring to all interactive elements (buttons, links, form inputs).

**What changed:**
Focus indicator updated to 2px ring with 4px glow for universal visibility and WCAG compliance.
