# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-450` (dept) · 2026-08-21T01:32:13.236700+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px solid #005fcc focus ring at 8:1 contrast with no glow.

**Plan:**
1. Implement a 4px solid focus ring with #005fcc (8:1 contrast) for all interactive elements.
2. Remove glow/inner shadow effects to ensure visibility on patterned backgrounds.
3. Test focus ring visibility on 10 real patterned backgrounds and high-DPI screens.
4. Validate WCAG 2.2 AA compliance for keyboard navigation across devices.
5. Document focus ring specs in EXCAVA’s design system.
6. Update codebase with the new focus ring style and remove legacy glow/shadow logic.

**What changed:**
Focus ring thickness increased to 4px at 8:1 contrast (no glow) for universal visibility.
