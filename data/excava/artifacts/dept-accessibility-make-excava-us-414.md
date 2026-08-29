# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-414` (dept) · 2026-08-29T04:14:10.154762+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 7px focus ring at 6:1 contrast with `prefers-reduced-motion: no-preference` override.

**Plan:**
1. Implement 7px focus ring with 6:1 contrast ratio.
2. Add `prefers-reduced-motion: no-preference` override to ensure visibility.
3. Conduct user testing on high-contrast, low-motion devices.
4. Document contrast and motion preferences in design system.
5. Update accessibility guidelines to reflect final focus ring specifications.
6. Deploy changes and monitor feedback for adjustments.

**What changed:** Focus ring increased to 7px at 6:1 contrast with reduced-motion override.
