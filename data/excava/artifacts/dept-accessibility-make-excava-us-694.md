# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-694` (dept) · 2026-07-23T17:57:21.494038+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a time-limited skip link triggered by keyboard focus.

**Plan:**
1. Add a single high-contrast skip link at the top of every page, hidden by default.
2. Show the skip link only when keyboard focus arrives (via `focus` or `keydown` events).
3. Auto-fade the skip link after 2 seconds of inactivity or once focus moves away.
4. Ensure the skip link remains keyboard-navigable and screen-reader-announced.
5. Test keyboard navigation in EXCAVA to confirm bypass works without overlap.
6. Verify mobile/touch behavior doesn’t interfere with skip link functionality.

**What changed:** Added a time-limited, focus-triggered skip link with high contrast and auto-fade.
