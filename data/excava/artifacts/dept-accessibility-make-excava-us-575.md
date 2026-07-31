# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-575` (dept) · 2026-07-31T21:40:40.151281+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px solid system accent ring (#007AFF/macOS, #0066CC/Windows) with 2px outer glow (#FFFFFF on light, #000000 on dark) for focus visibility.

**Plan:**
1. Implement a 3px solid focus ring using system accent colors (#007AFF for macOS, #0066CC for Windows).
2. Add a 2px outer glow—white (#FFFFFF) on light backgrounds, black (#000000) on dark backgrounds.
3. Test WCAG 2.1 contrast on light/dark backgrounds and patterned surfaces.
4. Apply consistently to all interactive elements (buttons, links, form inputs).
5. Document the focus ring style in the design system for future use.
6. Validate keyboard navigation flow with the new focus indicator.

**What changed:**
Focus ring upgraded to 3px solid system accent with 2px outer glow for cross-theme visibility.
