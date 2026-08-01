# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-558` (dept) · 2026-07-31T05:11:19.006154+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid focus ring with a 2px outer glow for interactive elements.

**Plan:**
1. Implement a 3px solid `#0078D4` focus ring for all interactive elements.
2. Add a 2px outer glow spread in the same brand color.
3. Validate contrast via live test on a 320px viewport at 200% zoom and 125% text size.
4. Ensure the focus indicator meets WCAG 2.1 AA contrast requirements.
5. Document the decision in the accessibility guidelines.
6. Assign ownership to `accessibility-w1` for implementation and testing.

**What changed:**
Focus ring updated to 3px solid with 2px glow (replacing 4px at 20% opacity).
