# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-594` (dept) · 2026-08-28T14:03:17.928166+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white).

**Plan:**
1. Implement 3px focus ring with 7:1 contrast ratio in EXCAVA’s design tokens.
2. Add 1px white outer glow to the focus ring for high-DPI and mobile visibility.
3. Test focus ring in WCAG AAA compliance tools (e.g., axe, WAVE).
4. Validate touch accuracy and visibility in user tests with low-vision participants.
5. Ensure compatibility with system high-contrast modes.
6. Document the decision in EXCAVA’s accessibility guidelines.

**What changed:** Focus ring upgraded from 3px at 6:1 to 3px at 7:1 with white glow for AAA compliance and high-DPI visibility.
