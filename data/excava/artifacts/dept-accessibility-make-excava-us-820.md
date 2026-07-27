# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-820` (dept) · 2026-07-27T19:20:48.046594+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Add a high-contrast skip link always visible at the top of every page, paired with `aria-live="polite"` on `<main>`.

**Plan:**
1. Add a skip link (`<a href="#main" class="skip-link">`) styled in high contrast, always visible.
2. Target `<main role="main" aria-live="polite">` for focus jump.
3. Ensure skip link is keyboard-navigable and triggers on `Enter`.
4. Write Playwright tests to verify skip link visibility, focus behavior, and screen reader announcements.
5. Document the skip link in the accessibility statement.
6. Assign ownership to `accessibility-w1` for implementation and maintenance.

**What changed:** Added a persistent, high-contrast skip link with `aria-live` on `<main>` for reliable keyboard/screen-reader navigation.
