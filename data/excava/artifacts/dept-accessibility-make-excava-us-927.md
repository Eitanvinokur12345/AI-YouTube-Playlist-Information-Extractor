# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-927` (dept) · 2026-07-28T03:49:03.209043+00:00
> Participants: Access, Ramp, Reader · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Ship a high-contrast, moving focus ring that announces the focused element to screen readers, ensuring clarity for keyboard users with low vision and screen reader users.
**Plan:**
1. Implement a single, high-contrast focus ring that moves with tab order to minimize visual clutter.
2. Test the moving focus ring with screen-reader users to validate its effectiveness.
3. Combine the moving focus ring with a clear, screen-reader-friendly announcement of the focused element.
4. Ensure the focus ring is visible and accessible on both desktop and mobile devices.
5. Verify that the solution works seamlessly with keyboard navigation and reduces visual noise.
**What changed:** Added screen-reader-friendly announcement of the focused element to the moving focus ring solution.
