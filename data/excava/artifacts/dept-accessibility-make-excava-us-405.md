# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-405` (dept) · 2026-08-15T22:52:09.908408+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 2px #fff outer stroke at full opacity for keyboard navigation.

**Plan:**
1. Implement the 2px #005fcc focus ring with a 2px #fff outer stroke.
2. Ramp to verify WCAG 2.2 AA contrast on light, dark, and extreme backgrounds.
3. Test focus visibility in high-contrast mode and reduced-motion scenarios.
4. Ensure the focus ring meets 3:1 contrast ratio in all modes.
5. Document the focus ring style in the design system.
6. Add automated contrast checks to the CI pipeline.

**What changed:**
Focus ring style updated to 2px #005fcc with 2px #fff outer stroke for universal contrast.
