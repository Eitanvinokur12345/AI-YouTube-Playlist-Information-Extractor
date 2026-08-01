# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-497` (dept) · 2026-07-31T15:39:48.064941+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Apply a 2px solid `#005FCC` focus ring with a 1px outer glow to all interactive elements.
2. Ensure the focus ring meets WCAG 2.2 AA contrast requirements.
3. Test on a 320px viewport at 150% zoom to verify visibility and touch target integrity.
4. Confirm that the 44px minimum touch target is preserved without overlap.
5. Document the focus ring style in the project’s design system or CSS guidelines.
6. Assign Ramp as the owner for implementation and testing.

**What changed:** Reduced focus ring to 2px solid + 1px glow to balance keyboard visibility and mobile touch targets.
