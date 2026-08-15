# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-442` (dept) · 2026-08-15T01:23:49.179754+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 4px solid #005fcc focus ring with a 1px #fff outer stroke at 70% opacity and add a 100ms fade-in animation.

**Plan:**
1. Implement the 4px solid #005fcc focus ring with a 1px #fff outer stroke.
2. Set opacity to 70% for the ring.
3. Add a 100ms fade-in animation to the focus ring.
4. Ensure the focus ring meets WCAG 2.2 AA contrast requirements on all backgrounds.
5. Test keyboard navigation to confirm visibility and usability.
6. Document the focus ring specifications in the design system.

**What changed:**
Focus ring increased to 4px with fade-in animation for better visibility and compliance.
