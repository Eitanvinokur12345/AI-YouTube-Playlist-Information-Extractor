# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-204` (dept) · 2026-08-10T20:41:47.511239+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring at 90% opacity with a 1px inner #ffffff offset.

**Plan:**
1. Implement the 3px #005fcc focus ring at 90% opacity with a 1px inner #ffffff offset across all interactive elements.
2. Test WCAG 2.1 AA contrast ratios on dark backgrounds (minimum 4.5:1).
3. Validate keyboard navigation and screen reader compatibility in high-contrast and reduced-motion modes.
4. Audit mobile/touch interfaces to ensure the focus ring remains visible but unobtrusive.
5. Document the focus ring style in the design system and share with the development team.
6. Schedule a review after 2 weeks of real-world usage to address edge cases.

**What changed:**
Focus ring opacity increased from 80% to 90% to meet WCAG 2.1 AA on dark backgrounds.
