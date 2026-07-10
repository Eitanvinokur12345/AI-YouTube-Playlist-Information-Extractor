# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-813` (dept) · 2026-07-10T23:32:05.646689+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Add a user-controlled "High Contrast Focus Mode" toggle with a 4.5:1 focus ring (visible only when enabled), default off.

**Plan:**
1. Implement a persistent toggle (e.g., in settings or keyboard shortcut) labeled "High Contrast Focus Mode."
2. Apply a 4.5:1 contrast focus ring to all interactive elements *only* when the toggle is on.
3. Ensure the focus ring respects brand colors/themes when the toggle is off.
4. Test keyboard navigation to confirm the ring is visible and functional in all states.
5. Document the toggle’s behavior in accessibility guidelines for users.
6. Default the toggle to "off" to avoid visual disruption for sighted users.

**What changed:** Added user-controlled high-contrast focus ring (4.5:1) with default off.
