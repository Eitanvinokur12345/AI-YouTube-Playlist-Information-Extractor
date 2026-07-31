# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-455` (dept) · 2026-07-31T07:57:30.610306+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a 1px solid #0078D4 focus ring with a 2px outer glow at 25% opacity.
**Plan:**
1. Implement a 1px solid focus ring with a 2px outer glow at 25% opacity for all interactive elements.
2. Test the focus indicator at 125% zoom on various backgrounds, including high-contrast and low-contrast themes.
3. Verify that the focus indicator remains visible and does not bleed or disappear on different backgrounds and zoom levels.
4. Conduct accessibility testing with keyboard navigation and screen readers to ensure the focus indicator is visible and usable.
5. Refine the design as needed based on testing results to ensure the focus indicator meets accessibility requirements.
**What changed:** The focus ring design was updated to a 1px solid ring with a 2px outer glow at 25% opacity to balance visibility and subtlety.
