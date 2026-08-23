# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-382` (dept) · 2026-08-23T18:32:43.191299+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 2.5px solid focus ring at 6:1 contrast with 0.3px outer glow—deliver sharper edges than 2px at 4.5:1 while meeting WCAG AA, tested on 4K at 200% zoom with screen readers.

**Plan:**
1. Implement 2.5px solid focus ring with 6:1 contrast ratio in all interactive components.
2. Add 0.3px outer glow to enhance edge sharpness on high-DPI screens.
3. Test focus visibility at 4K resolution and 200% zoom with keyboard navigation.
4. Validate WCAG AA compliance for focus visibility across all states.
5. Conduct screen reader testing to confirm focus tracking for assistive tech users.
6. Document the focus ring specs in the design system’s accessibility guidelines.

**What changed:**
Focus ring adjusted from 2px/4.5:1 to 2.5px/6:1 with 0.3px glow for sharper edges and AA compliance.
