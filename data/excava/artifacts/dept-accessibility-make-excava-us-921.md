# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-921` (dept) · 2026-07-14T22:52:46.905986+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a hidden skip link that appears only on keyboard focus.

**Plan:**
1. Add a hidden skip link at the top of every page with CSS `position: absolute; left: -9999px; top: 0;` and `opacity: 0;`.
2. Use `:focus-visible` to show the link only when keyboard-focused (no hover or mouse focus).
3. Ensure the link targets the main content via `href="#main"` and includes `aria-label="Skip to main content"`.
4. Test keyboard-only navigation with JavaScript disabled to confirm functionality.
5. Add a fallback hash link (`<a href="#main">Skip to main content</a>`) as a server-side fallback.
6. Document the skip link in the accessibility statement and code comments.

**What changed:**
Replaced persistent/server-side skip links with a hidden, keyboard-triggered skip link for universal accessibility.
