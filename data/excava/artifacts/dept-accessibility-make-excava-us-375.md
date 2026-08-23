# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-375` (dept) · 2026-08-23T20:52:37.078678+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 2px solid focus ring at 7:1 contrast, switching to 1px at 4.5:1 when reduced motion is enabled; owner: Ramp.

**Plan:**
1. Implement CSS for a 2px solid focus ring with 7:1 contrast by default.
2. Add media query `@media (prefers-reduced-motion: reduce)` to switch to 1px ring at 4.5:1 contrast.
3. Ensure the focus ring meets WCAG AA for reduced motion and WCAG AAA for standard mode.
4. Document the focus ring styles in EXCAVA’s design system.
5. Test keyboard navigation, touch targets, and reduced-motion scenarios.
6. Deploy changes via EXCAVA’s design system pipeline.

**What changed:**
Focus ring now defaults to 2px at 7:1 contrast, switching to 1px at 4.5:1 in reduced-motion mode.
