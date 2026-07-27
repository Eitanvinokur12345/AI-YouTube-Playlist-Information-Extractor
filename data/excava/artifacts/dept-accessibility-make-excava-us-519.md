# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-519` (dept) · 2026-07-27T05:57:52.999970+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a **bold, full-width skip bar** at the top and bottom of every page.
2. Cycle through regions (header → main → footer) on repeated activation (keyboard-triggered).
3. Hide the skip bar by default and only show it when keyboard navigation is detected.
4. Add **reduced-motion support** (e.g., instant transitions, no animations).
5. Ensure **mobile/touch compatibility** (e.g., tap-to-activate, visible focus states).
6. Test with screen readers and keyboard users to validate navigation flow.

**What changed:** Added a cycling skip bar at top/bottom with keyboard-triggered visibility and reduced-motion support.
