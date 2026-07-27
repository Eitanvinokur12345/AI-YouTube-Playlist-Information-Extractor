# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-132` (dept) · 2026-07-27T07:07:51.914233+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Use one high-contrast "Skip to main content" link at the top of every page.

**Plan:**
1. Implement a single "Skip to main content" link at the top of every page, styled with high contrast.
2. Ensure the link jumps directly to the main content area (`<main>` or equivalent landmark).
3. Test with keyboard-only users and screen readers on pages with varied layouts (simple, complex, multi-section).
4. Confirm the skip link does not create confusion or redundancy in navigation.
5. Document the implementation in the accessibility guidelines for consistency.
6. Assign ownership to `accessibility-w1` for maintenance and updates.

**What changed:** Added a single high-contrast "Skip to main content" link to all pages.
