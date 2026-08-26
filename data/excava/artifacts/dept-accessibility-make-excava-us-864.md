# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-864` (dept) · 2026-08-26T09:37:26.229839+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 5px solid focus ring at 7:1 contrast for EXCAVA.

**Plan:**
1. Implement 5px solid focus ring with 7:1 contrast ratio across all interactive elements.
2. Validate visibility on high-contrast and busy mobile backgrounds.
3. Test touch target precision on small interactive elements for motor-impaired users.
4. Ensure compliance with WCAG 2.2 AA for both desktop and mobile contexts.
5. Document the design spec in the accessibility-w1 repository artifact.
6. Conduct cross-device testing (touch, keyboard, reduced-motion) before release.

**What changed:** Focus ring updated from 4px/6:1 to 5px/7:1 for universal clarity.
