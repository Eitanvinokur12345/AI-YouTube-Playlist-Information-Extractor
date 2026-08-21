# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-586` (dept) · 2026-08-21T06:34:38.200196+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 4px focus ring at 6:1 contrast with 1px outer stroke, no glow.

**Plan:**
1. Implement 4px focus ring with 6:1 contrast ratio in all EXCAVA components.
2. Add 1px outer stroke (no glow) to maintain crisp edges on mobile/touch.
3. Test focus visibility across devices (mobile, touch, keyboard nav) and screen readers.
4. Validate WCAG AA compliance for low-vision and neurodivergent users.
5. Document focus ring specs in EXCAVA design system.
6. Assign `accessibility-w1` to deliver and maintain the focus ring implementation.

**What changed:**
Replaced 6px/7:1/no-glow with 4px/6:1/outer-stroke for balanced visibility and space efficiency.
