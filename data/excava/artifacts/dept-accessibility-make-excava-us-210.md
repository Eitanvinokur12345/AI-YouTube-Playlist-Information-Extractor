# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-210` (dept) · 2026-08-15T07:10:17.071027+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 2px solid #005fcc focus ring with a 2px #fff outer stroke at 80% opacity for all interactive elements.

**Plan:**
1. Update focus ring styles in the design system to use `2px solid #005fcc` with `2px #fff` outer stroke at 80% opacity.
2. Test WCAG 2.2 AA compliance in Windows High Contrast Mode and iOS VoiceOver.
3. Validate visibility on mobile/touch targets (e.g., buttons under 32px) and adjust stroke opacity if needed.
4. Document the focus ring spec in the accessibility guidelines for EXCAVA.
5. Implement the change across all interactive components (buttons, links, form fields).
6. Conduct cross-browser testing to ensure consistent rendering.

**What changed:** Focus ring updated to 2px #005fcc + 2px #fff at 80% opacity for universal visibility.
