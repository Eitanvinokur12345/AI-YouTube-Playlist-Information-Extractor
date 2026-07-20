# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-497` (dept) · 2026-07-20T17:44:15.785863+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a focus-triggered skip link on every page.

**Plan:**
1. Add a high-contrast, full-width skip link (`<a href="#main">Skip to content</a>`) at the top of every page.
2. Style it with `position: absolute; left: -9999px; top: 0;` (off-screen) and `focus` styles to reveal it when focused.
3. Ensure the link targets the main content container (`id="main"`) to bypass repetitive blocks.
4. Test keyboard navigation to confirm it works without disrupting mouse/sighted users.
5. Document the skip link in the accessibility statement.

**What changed:** Added a focus-triggered skip link to bypass repetitive blocks for keyboard users.
