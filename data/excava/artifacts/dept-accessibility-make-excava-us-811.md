# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-811` (dept) · 2026-09-03T03:27:20.568290+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 2px focus ring with a 2px outer stroke at 7:1 contrast, no glow.

**Plan:**
1. Implement a reusable focus ring component with 2px ring + 2px outer stroke at 7:1 contrast ratio.
2. Add test cases for patterned backgrounds (e.g., checkerboard at 50% zoom) and mobile viewport simulations.
3. Validate contrast compliance using automated tools (e.g., axe-core, WebAIM Contrast Checker).
4. Document the component’s usage in the design system’s accessibility guidelines.
5. Assign ownership to `accessibility-w1` for maintenance and updates.
6. Conduct user testing with participants who have low vision or cognitive disabilities.

**What changed:** Focus ring now uses a 2px outer stroke (no glow) at 7:1 contrast for guaranteed visibility across all backgrounds.
