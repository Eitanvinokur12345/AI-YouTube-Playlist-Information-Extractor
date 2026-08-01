# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-439` (dept) · 2026-07-31T11:57:04.315251+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3-pixel solid focus ring with a 1-pixel inner glow at 10% opacity.

**Plan:**
1. Implement the 3-pixel solid focus ring with 1-pixel inner glow (10% opacity) in EXCAVA’s CSS.
2. Test focus visibility at 125% zoom across all interactive elements (buttons, inputs, links).
3. Validate keyboard navigation (tab order, focus traps) in high-contrast and reduced-motion modes.
4. Audit low-vision modes (e.g., Windows HC, macOS contrast) to ensure the glow remains visible.
5. Document the focus ring specs in the design system’s accessibility guidelines.
6. Add automated regression tests for focus ring rendering at 125% zoom.

**What changed:**
Focus indicator upgraded from 2-pixel dashed/glow to 3-pixel solid with inner glow.
