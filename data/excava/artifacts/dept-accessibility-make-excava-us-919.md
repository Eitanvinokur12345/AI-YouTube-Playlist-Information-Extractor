# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-919` (dept) · 2026-07-28T17:46:51.094569+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a subtle, persistent high-contrast focus ring with a 50ms flash only on first focus per page/section.

**Plan:**
1. Implement a subtle, persistent high-contrast focus ring (e.g., 2px solid outline) for all interactive elements.
2. Add a 50ms flash animation only on the first focus event per page/section load.
3. Ensure the focus ring respects reduced-motion preferences (no flash if `prefers-reduced-motion` is enabled).
4. Test keyboard navigation at 125ms tab intervals to confirm the ring persists.
5. Document the behavior in EXCAVA’s accessibility guidelines.
6. Owner: `accessibility-w1` delivers implementation by 2024-06-15.

**What changed:** Focus ring now subtly persists with a brief flash only on first focus, reducing visual noise while ensuring visibility.
