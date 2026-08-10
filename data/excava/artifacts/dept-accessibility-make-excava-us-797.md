# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-797` (dept) · 2026-08-10T19:26:22.348053+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a context-aware focus ring system with light/dark theme differentiation.

**Plan:**
1. Implement CSS variables for focus ring colors (`--focus-light: 3px solid #005fcc` and `--focus-dark: 2px solid #ffffff`).
2. Add a media query for `prefers-color-scheme: dark` to switch between ring styles.
3. Apply the rings to all interactive elements (`button`, `a`, `input`, etc.) with consistent 1px inner offset.
4. Test focus visibility in high-contrast and reduced-motion modes.
5. Document the focus ring behavior in the accessibility guidelines.
6. Assign `accessibility-w1` as the owner for maintenance.

**What changed:**
Focus rings now adapt to light/dark themes while ensuring WCAG compliance.
