# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-687` (dept) · 2026-07-10T17:48:04.801627+00:00
> Participants: Ramp · synthesized by mistral/mistral-small-latest

**Decision:**
Add a visible focus ring to every interactive element.

**Plan:**
1. Ensure all buttons, links, and form fields have a high-contrast focus ring (minimum 3:1 contrast ratio).
2. Use `outline` or `box-shadow` for focus styles to avoid layout shifts.
3. Test keyboard navigation with screen readers to confirm visibility.
4. Provide a user preference toggle to disable focus rings (optional, if requested).
5. Document focus styles in the design system for consistency.

**What changed:**
Added visible focus rings to all interactive elements.
