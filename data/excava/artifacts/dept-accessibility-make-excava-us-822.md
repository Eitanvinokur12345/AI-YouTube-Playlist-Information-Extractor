# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-822` (dept) · 2026-09-02T16:47:30.249029+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 4px focus ring at 7:1 contrast with `prefers-reduced-motion: no-preference` and a 3px focus ring at 4.5:1 only when `forced-colors: active`.

**Plan:**
1. Set default focus ring to 4px at 7:1 contrast.
2. Apply `prefers-reduced-motion: no-preference` to maintain the 4px ring.
3. Override to 3px at 4.5:1 contrast when `forced-colors: active` is detected.
4. Test keyboard navigation on high-contrast and reduced-motion systems.
5. Validate WCAG 2.2 compliance for focus visibility.
6. Document the decision in the project’s accessibility guidelines.

**What changed:**
Focus ring adapts to `forced-colors` mode while defaulting to high-contrast for all other cases.
