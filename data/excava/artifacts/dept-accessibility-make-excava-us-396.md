# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-396` (dept) · 2026-07-31T15:17:44.469719+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005FCC focus ring (WCAG 2.1 AA contrast) with no glow for all interactive elements.

**Plan:**
1. Implement CSS rule for `*:focus-visible { outline: 2px solid #005FCC; outline-offset: 0; }` targeting buttons, links, form fields, and custom widgets.
2. Remove all existing focus styles (e.g., `outline: 3px`) to avoid conflicts.
3. Test with a low-vision keyboard user on EXCAVA to confirm visibility and usability.
4. Document the change in the accessibility audit log with WCAG 2.1 AA contrast ratio verification.
5. Assign `accessibility-w1` to deliver the CSS rule and validate via user testing by [date].
6. Add the rule to the shared component library for consistency across projects.

**What changed:**
Replaced 3px focus ring with 2px solid #005FCC (no glow) for all interactive elements.
