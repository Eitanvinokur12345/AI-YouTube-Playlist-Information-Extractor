# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-101` (dept) · 2026-07-27T06:33:28.923816+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a single high-contrast "Skip to main content" link at the top of every page, reinforced by ARIA landmarks (`<main>`, `<aside>`) for screen readers.

**Plan:**
1. Implement a single high-contrast "Skip to main content" link at the very top of every page.
2. Add `<main>` and `<aside>` landmarks to all pages to support screen reader navigation.
3. Ensure the skip link is keyboard-focusable and visible when focused.
4. Test the skip link with keyboard-only and screen reader users to verify functionality.
5. Document the skip link component in EXCAVA’s accessibility guidelines.
6. Owner: accessibility-w1 to deliver and maintain the component.

**What changed:**
Added a single high-contrast "Skip to main content" link with ARIA landmarks.
