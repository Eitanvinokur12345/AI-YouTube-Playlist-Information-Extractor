# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-756` (dept) · 2026-07-24T23:35:11.580276+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a persistent, high-contrast skip link at the top of every page, tested with keyboard users to ensure visibility without visual clutter.

**Plan:**
1. Add a full-width skip bar at the top of every page, styled with high contrast (e.g., dark background with light text).
2. Ensure the skip bar only appears when keyboard-focused (no hover/focus tricks).
3. Test with keyboard users to confirm visibility and usability.
4. Document the skip bar’s behavior in the accessibility guidelines.
5. Include the skip bar in all page templates and components.
6. Monitor feedback and adjust contrast or positioning as needed.

**What changed:** Added a persistent, high-contrast skip bar for keyboard navigation.
