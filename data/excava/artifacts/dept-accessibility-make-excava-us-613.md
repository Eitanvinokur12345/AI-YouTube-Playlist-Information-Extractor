# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-613` (dept) · 2026-07-18T01:46:25.587608+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a compact, high-contrast skip link always visible above primary navigation.

**Plan:**
1. Add a skip link (`<a href="#main">Skip to content</a>`) positioned absolutely above primary navigation with `top: 0; left: 0;`.
2. Style with high contrast (WCAG 2.1 AA) and reduced motion (`prefers-reduced-motion`).
3. Ensure skip link is keyboard-focusable and programmatically associated with `#main` content landmark.
4. Test with Playwright MCP for keyboard navigation success (time-to-main-content < 2s).
5. Validate with axe-core and WAVE for compliance.
6. Document in `README.md` under "Accessibility" with usage notes.

**What changed:**
Added a compact, always-visible high-contrast skip link above primary navigation.
