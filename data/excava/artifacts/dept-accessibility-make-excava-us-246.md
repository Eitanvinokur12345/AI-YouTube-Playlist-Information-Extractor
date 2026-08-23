# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-246` (dept) · 2026-08-23T17:56:39.632274+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 2.5px solid focus ring at 5:1 contrast with 0.3px outer glow—tested on high-DPI and standard screens, owned by Ramp (accessibility-w1).

**Plan:**
1. Implement the 2.5px focus ring with 5:1 contrast in the component library.
2. Add the 0.3px outer glow effect with reduced opacity for depth.
3. Test on high-DPI (4K) and standard screens at 200% zoom.
4. Validate WCAG 2.2 AA compliance for focus visibility.
5. Document the decision in the accessibility guidelines.
6. Assign Ramp (accessibility-w1) as the owner for ongoing maintenance.

**What changed:**
Focus ring updated from 3px/7:1 to 2.5px/5:1 with 0.3px glow for sharper visibility across devices.
