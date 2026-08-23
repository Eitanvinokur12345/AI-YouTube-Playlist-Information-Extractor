# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-284` (dept) · 2026-08-23T18:49:37.863710+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 2px solid focus ring at 6:1 contrast, no glow, static design.

**Plan:**
1. Implement a 2px solid focus ring with 6:1 contrast ratio.
2. Remove all glow/flicker effects from the focus ring.
3. Ensure the ring remains static (no animations) across all states.
4. Test the focus ring with users who rely on high contrast and reduced motion.
5. Document the decision in the project’s accessibility guidelines.
6. Update design tokens and component libraries to reflect the new focus ring.

**What changed:** Focus ring adjusted from 4.5:1 glow to 6:1 solid, no glow.
