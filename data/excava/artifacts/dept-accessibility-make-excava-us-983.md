# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-983` (dept) · 2026-07-18T09:59:48.862434+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Add a persistent skip link styled as a thin, subtle underline at the top of every page.
2. Ensure the underline thickens and contrasts on keyboard focus (e.g., 2px solid, high-contrast color).
3. Test that the skip link appears instantly when focus reaches the top, without layout shift.
4. Verify sighted keyboard users see the visual cue immediately, while mouse/touch users remain unaffected.
5. Confirm the skip link bypasses repetitive navigation blocks with a single tab stop.
6. Document the behavior in the accessibility audit and update the design system.

**What changed:** Added a persistent, subtle skip link with focus-triggered high contrast.
