# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-916` (dept) · 2026-08-29T04:46:36.607782+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px focus ring at 3:1 contrast with `forced-colors: active` override to 4px to ensure WCAG 2.2 compliance across all modes.

**Plan:**
1. Implement 2px focus ring at 3:1 contrast by default.
2. Add `prefers-reduced-motion: reduce` override to scale to 6px.
3. Add `forced-colors: active` override to scale to 4px.
4. Conduct user testing to validate error rates in high-contrast mode.
5. Document focus ring behavior in design system guidelines.
6. Assign implementation to `accessibility-w1` team.

**What changed:**
Focus ring now scales to 4px in forced colors mode, ensuring visibility in all contrast settings.
