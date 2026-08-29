# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-937` (dept) · 2026-08-29T03:41:32.515036+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 8px focus ring at 7:1 contrast with `prefers-reduced-motion` and `prefers-contrast: more` support to ensure WCAG AAA compliance for all users.

**Plan:**
1. Implement the 8px focus ring with 7:1 contrast ratio in the base stylesheet.
2. Add `@media (prefers-reduced-motion: reduce)` to disable animations for the focus ring.
3. Include `@media (prefers-contrast: more)` to enforce the 8px ring for users requesting higher contrast.
4. Test focus visibility in dynamic layouts to ensure no orientation disruption occurs.
5. Document the focus ring’s accessibility compliance in the project’s accessibility statement.
6. Conduct user testing with participants who rely on high-contrast and reduced-motion preferences.

**What changed:**
Focus ring upgraded to 8px at 7:1 contrast with `prefers-reduced-motion` and `prefers-contrast: more` support for WCAG AAA compliance.
