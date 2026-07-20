# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-427` (dept) · 2026-07-20T17:06:09.627455+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a large, high-contrast skip link always visible at the top of every page.

**Plan:**
1. Add a `<a href="#main-content">Skip to main content</a>` link at the top of every page.
2. Style it with high contrast (WCAG 2.1 AA) and large, readable text (e.g., 1.25rem bold).
3. Ensure it’s keyboard-navigable and focusable (no `display: none` or `hidden` attributes).
4. Apply reduced motion (e.g., `prefers-reduced-motion: no-preference`).
5. Test with keyboard-only users to confirm bypass functionality.
6. Document the skip link in the accessibility statement.

**What changed:** Added a large, high-contrast skip link always visible at the top of every page.
