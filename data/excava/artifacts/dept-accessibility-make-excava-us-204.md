# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-204` (dept) · 2026-07-27T05:03:10.373756+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a bold, full-width skip bar that bypasses navigation, always visible but only high-contrast on keyboard focus.

**Plan:**
1. Add a `<nav role="navigation" aria-label="Skip to main content">` skip bar at the top of every page, wrapping a link to `#main-content`.
2. Style the skip bar with `position: fixed; top: 0; left: 0; width: 100%;` and ensure it’s keyboard-focusable (`tabindex="0"`).
3. Default styling: subtle (e.g., low opacity, minimal height) to avoid visual clutter for mouse users.
4. On `:focus-visible` (or `:focus` with JS polyfill), apply high-contrast styling (e.g., `background: #000; color: #fff; padding: 1rem`).
5. Ensure the skip link targets `#main-content` (or equivalent landmark) and is announced by screen readers via `aria-label`.
6. Test with keyboard and screen reader users to validate bypass efficiency and discoverability.

**What changed:** Skip bar now always exists in DOM (visible to SRs) but only high-contrast on focus, balancing clutter and discoverability.
