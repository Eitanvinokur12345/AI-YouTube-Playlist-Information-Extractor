# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-327` (dept) · 2026-07-27T05:40:13.249369+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Add a **bold, full-width skip bar** at the top and bottom of every page.
2. Place **one skip link per distinct navigation block** (header, sidebar, footer, in-page nav).
3. Ensure skip links are **visible only when focused** to avoid visual clutter.
4. Implement **keyboard navigation** to jump between skip bars and navigation blocks in one tab stop.
5. Test with screen readers and keyboard-only users to verify bypass functionality.
6. Document the skip link system in the project’s accessibility guidelines.

**What changed:** Added multiple skip links (top/bottom bars + per-block links) for full keyboard bypass.
