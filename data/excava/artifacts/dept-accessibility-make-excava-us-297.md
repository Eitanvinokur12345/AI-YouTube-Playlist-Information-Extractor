# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-297` (dept) · 2026-09-02T17:21:03.698696+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use 4px focus ring at 10:1 contrast for all interactive elements.

**Plan:**
1. Set 4px focus ring with 10:1 contrast for all interactive elements by default.
2. Remove any media-query adjustments for `prefers-reduced-motion`.
3. Test focus visibility with screen readers and keyboard-only users.
4. Validate WCAG 2.2 AA compliance for contrast and focus indicators.
5. Document the decision in the accessibility guidelines.
6. Implement the change in the next design system release.

**What changed:**
Focus ring contrast increased to 10:1 for all states, removing motion-based contrast toggles.
