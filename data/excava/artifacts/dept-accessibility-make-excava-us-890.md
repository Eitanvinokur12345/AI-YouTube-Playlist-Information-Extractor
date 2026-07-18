# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-890` (dept) · 2026-07-18T03:04:02.853184+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, zero-opacity skip link that becomes visible on keyboard focus and is announced by screen readers.

**Plan:**
1. Add a `<a>` skip link at the top of every page with `href="#main-content"` (or equivalent target).
2. Style it with `opacity: 0` by default, transitioning to `opacity: 1` when focused.
3. Apply `aria-hidden="false"` to ensure screen readers announce it.
4. Position it off-screen (e.g., `top: -40px`) to avoid layout shifts.
5. Ensure the target (`#main-content`) is a landmark region (e.g., `<main id="main-content">`).
6. Test with keyboard navigation and screen readers to verify behavior.

**What changed:** Added a persistent, zero-opacity skip link that appears on focus and is screen-reader-announced.
