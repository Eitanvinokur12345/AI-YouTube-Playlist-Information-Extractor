# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-567` (dept) · 2026-08-16T16:54:00.117223+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 2px solid #005fcc focus ring with a 2px inner glow at 30% opacity.

**Plan:**
1. Implement the 2px solid #005fcc focus ring with a 2px inner glow at 30% opacity for all interactive elements.
2. Ensure the glow is visible on all backgrounds, including dark mode and high-contrast themes.
3. Test on a 320px viewport with 44px buttons to confirm mobile/touch usability.
4. Validate keyboard navigation visibility in reduced-motion and low-contrast scenarios.
5. Document the focus ring style in the design system for consistency.
6. Gather user feedback post-implementation to refine if needed.

**What changed:** Focus ring updated from 3px ring with white stroke to 2px ring with inner glow for better accessibility across contexts.
