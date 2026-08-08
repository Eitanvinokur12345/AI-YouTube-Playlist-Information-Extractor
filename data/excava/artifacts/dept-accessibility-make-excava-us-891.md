# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-891` (dept) · 2026-08-08T11:03:56.081990+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 1px #ffffff outer ring (total 5px).

**Plan:**
1. Update focus indicator styles to use `3px solid #005fcc` with `1px #ffffff` outer ring.
2. Test on high-contrast patterned backgrounds (e.g., zebra-striped) to verify WCAG 2.1 AA compliance.
3. Ensure the ring remains visible on all backgrounds, including dark pages with busy textures.
4. Document the focus ring specs in the design system’s accessibility guidelines.
5. Implement the change in the EXCAVA codebase and verify via automated and manual testing.
6. Add the focus ring to all interactive elements (buttons, links, inputs, etc.).

**What changed:**
Focus ring updated to 3px #005fcc with 1px #ffffff outer ring for WCAG 2.1 AA compliance.
