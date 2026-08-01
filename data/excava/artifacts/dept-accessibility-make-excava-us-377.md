# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-377` (dept) · 2026-08-01T04:03:32.813758+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid focus indicator combining a 3px solid ring for clarity and a 2px offset shadow for adaptability.

**Plan:**
1. Implement a **3px solid #005fcc focus ring** with **2px padding** as the default for all interactive elements.
2. Add a **2px offset shadow (#005fcc, 0 0 2px)** to the focus ring for cases where content overlap is a risk (e.g., dense layouts).
3. Ensure the focus indicator **does not overlap adjacent content** at breakpoints 320px and 1920px.
4. Test contrast ratios with a live checker to confirm WCAG 2.2 AA compliance.
5. Conduct user testing with keyboard navigators and low-vision users to validate visibility.
6. Document the focus indicator styles in the design system under `accessibility-w1`.

**What changed:**
Replaced the double-ring proposal with a hybrid 3px solid ring + 2px shadow to balance clarity and adaptability.
