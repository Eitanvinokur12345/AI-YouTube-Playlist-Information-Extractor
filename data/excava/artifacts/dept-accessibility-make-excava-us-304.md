# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-304` (dept) · 2026-07-31T07:20:52.073045+00:00
> Participants: Ramp, Reader, Access · synthesized by sambanova/Meta-Llama-3.3-70B-Instruct

**Decision:** Ship a 3px solid focus ring in the brand color with a 1px inner shadow at 50% opacity.
**Plan:**
1. Implement a 3px solid focus ring in the brand color for keyboard navigation.
2. Add a 1px inner shadow at 50% opacity to the focus ring for depth.
3. Conduct live contrast tests against busy backgrounds at 125% zoom to ensure visibility.
4. Verify that the focus indicator does not bleed into adjacent elements.
5. Update the design documentation to reflect the new focus indicator style.
**What changed:** Dropped the outer glow in favor of a 1px inner shadow to reduce bleed and improve contrast.
