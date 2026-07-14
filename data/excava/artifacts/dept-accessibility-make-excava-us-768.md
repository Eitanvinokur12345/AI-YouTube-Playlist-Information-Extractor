# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-768` (dept) · 2026-07-14T06:36:45.909850+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a visible skip link that collapses to a small icon on focus loss, tested with keyboard-only users to ensure discoverability without clutter.

**Plan:**
1. Add a skip link at the top of every page with text "Skip to main content" and a small collapse-to-icon behavior.
2. Style the skip link to match the page’s theme but ensure high-contrast focus ring when visible.
3. Implement JavaScript to hide the skip link text and show a small icon (e.g., chevron or skip symbol) when focus is lost.
4. Ensure the skip link is the first focusable element in the DOM to work with keyboard navigation.
5. Test with keyboard-only users to verify discoverability and usability.
6. Add a fallback for browsers without JavaScript to ensure the skip link remains visible.

**What changed:** Added a visible skip link that collapses to an icon on focus loss, improving keyboard navigation without clutter.
