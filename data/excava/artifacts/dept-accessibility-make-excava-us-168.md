# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-168` (dept) · 2026-07-31T18:06:31.564500+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px solid #005FCC focus ring at 4.5:1 contrast with a 1px inner shadow at 30% opacity (#005FCC) on all focusable elements.

**Plan:**
1. Update EXCAVA’s CSS to apply the 2px solid #005FCC focus ring (4.5:1 contrast) to all focusable elements.
2. Add a 1px inner shadow at 30% opacity (#005FCC) to soften edges without reducing contrast.
3. Implement live contrast checks in the CSS to ensure WCAG 2.2 AA compliance across all backgrounds.
4. Test the focus style on busy backgrounds to confirm visibility.
5. Assign ownership to `accessibility-w1` for maintenance and updates.
6. Document the change in EXCAVA’s accessibility changelog.

**What changed:**
Added a 2px solid #005FCC focus ring with a 1px inner shadow at 30% opacity for WCAG 2.2 AA compliance.
