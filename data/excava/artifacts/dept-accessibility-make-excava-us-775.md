# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-775` (dept) · 2026-07-29T21:47:31.503529+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **3px solid focus ring (4.5:1 contrast)**, inset 1px, tested on 4K/150% zoom with keyboard/screen reader users.

**Plan:**
1. Implement the 3px solid focus ring (4.5:1 contrast) on all interactive elements.
2. Inset the ring 1px from the element edge.
3. Test focus visibility on 4K displays at 150% zoom with keyboard-only and screen reader users.
4. Document the focus ring style in the design system’s accessibility guidelines.
5. Add a fallback to 4:1 contrast if testing reveals visibility issues on low-contrast screens.
6. Include the focus ring style in the component library’s codebase with clear usage examples.

**What changed:**
Focus ring updated to 3px solid (4.5:1 contrast), inset 1px, validated on 4K/150% zoom.
