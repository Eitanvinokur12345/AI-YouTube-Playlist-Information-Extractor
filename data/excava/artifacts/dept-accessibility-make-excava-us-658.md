# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-658` (dept) · 2026-08-28T11:35:48.012378+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px solid focus ring at 7:1 contrast with 48px minimum touch target, static design, validated across monochrome/inversion modes; owner: accessibility-w1 delivers artifact by EOD.

**Plan:**
1. Implement 3px solid focus ring with 7:1 contrast ratio in all interactive components.
2. Enforce 48px minimum touch target size for all focusable elements.
3. Test focus ring visibility in monochrome, high-contrast, and color-inversion modes.
4. Validate reduced-motion compliance by ensuring focus ring remains static.
5. Document focus ring specifications in the design system.
6. Deliver finalized artifact (e.g., Figma/Storybook) to accessibility-w1 by EOD.

**What changed:**
Adopted 3px ring at 7:1 contrast with 48px touch targets, replacing prior 6:1/2px proposals.
