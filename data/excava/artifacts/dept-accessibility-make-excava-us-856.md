# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-856` (dept) · 2026-08-17T09:12:09.791881+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid focus ring combining crisp visibility and touch safety.

**Plan:**
1. Implement a **2.5px solid #005fcc** focus ring as the base.
2. Add a **15% opacity glow** with a **2px outer spread** for high-contrast/patterned backgrounds.
3. Test visibility on:
   - Busy patterned backgrounds (e.g., grid/textures).
   - High-contrast modes (inversion/Windows HC).
   - Mobile touch targets (fat-finger safety).
   - 200% zoom (WCAG 1.4.4).
4. Ensure the glow does not overlap adjacent interactive elements.
5. Document the ring specs in the design system’s `focus-states.md`.
6. Assign `accessibility-w1` as owner for iterative testing.

**What changed:**
Hybrid 2.5px solid + 15% glow focus ring replaces prior 3px/2px proposals.
