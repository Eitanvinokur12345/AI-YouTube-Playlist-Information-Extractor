# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-195` (dept) · 2026-08-09T22:05:18.166826+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid `#005fcc` focus ring with a 1px inner `#ffffff` offset (total 4px) for interactive elements.

**Plan:**
1. Update the focus ring style in the design system to `3px solid #005fcc` with `1px inner white offset`.
2. Test the focus ring at 200% zoom on a Retina display to ensure crisp visibility.
3. Verify no collisions occur in dense UIs at 125% zoom on low-DPI screens.
4. Document the focus ring specs in the accessibility guidelines.
5. Implement the change in the component library and update affected UI patterns.
6. Conduct a regression test to confirm keyboard navigation remains clear.

**What changed:**
Focus ring updated to 3px solid `#005fcc` with 1px inner offset (total 4px).
