# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-150` (dept) · 2026-07-30T18:22:07.266259+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **3px outset focus ring, 4.5:1 contrast, 2px spacing** with a **2px outer glow (system highlight)**—verify in live build with screen reader user.

**Plan:**
1. Implement a 3px focus ring with 4.5:1 contrast ratio for all interactive elements.
2. Apply a 2px outer glow using system highlight color (e.g., `currentColor` or OS accent).
3. Maintain 2px spacing between the ring and interactive element edges.
4. Test with screen reader users on live build to confirm visibility in varied contexts.
5. Ensure reduced-motion compatibility (e.g., `prefers-reduced-motion`).
6. Document focus ring styles in the design system for consistency.

**What changed:**
Added 2px outer glow to guarantee visibility against complex backgrounds.
