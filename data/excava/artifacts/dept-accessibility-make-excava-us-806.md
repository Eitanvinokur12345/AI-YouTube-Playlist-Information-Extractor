# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-806` (dept) · 2026-08-16T14:18:06.542181+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 2.5px solid #005fcc focus ring with a 0.75px white stroke at 60% opacity.

**Plan:**
1. Update EXCAVA’s CSS to set `outline: 2.5px solid #005fcc` with `outline-offset: 2px` and `box-shadow: 0 0 0 0.75px rgba(255,255,255,0.6)` for focus states.
2. Verify WCAG 2.2 AA contrast ratios against #ffffff (4.6:1) and #f5f5f5 (4.5:1) using automated and manual testing.
3. Test the ring’s visibility in dense interfaces (e.g., tables, grids) to confirm it remains unobtrusive.
4. Add the focus ring style to EXCAVA’s design system documentation and component examples.
5. Include the change in the next EXCAVA release notes under "Accessibility Improvements."
6. Monitor user feedback post-release for any reported issues with the new focus ring.

**What changed:** Focus ring updated to 2.5px #005fcc with 0.75px white stroke at 60% opacity for balanced WCAG compliance and subtlety.
