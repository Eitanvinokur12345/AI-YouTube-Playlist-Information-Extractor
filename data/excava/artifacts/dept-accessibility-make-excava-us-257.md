# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-257` (dept) · 2026-07-20T18:21:32.454684+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a focus-triggered skip link.

**Plan:**
1. Add a high-contrast, full-width skip link at the top of every page, hidden by default.
2. Make the skip link visible only after the first tab press, then hide it until the next page load.
3. Include the skip link in the codebase with Playwright test coverage.
4. Assign ownership to `accessibility-w1`.
5. Conduct testing with 3 keyboard users to validate discoverability.

**What changed:** Added a focus-triggered skip link.
