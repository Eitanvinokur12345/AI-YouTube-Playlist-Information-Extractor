# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-940` (dept) · 2026-07-31T01:44:07.664674+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a **3px solid focus ring in #000000 at 90% opacity with 3px outer offset** for dark themes and a **4px solid focus ring in #0078D4 with 1px outer offset** for light themes.
**Plan:**
1. Update the design system with CSS variables for a 3px solid focus ring in #000000 at 90% opacity with 3px outer offset for dark themes.
2. Update the design system with CSS variables for a 4px solid focus ring in #0078D4 with 1px outer offset for light themes.
3. Implement the new focus ring styles for all interactive elements across the application.
4. Conduct a thorough QA to ensure the new focus ring styles meet accessibility standards, including contrast and zoom requirements.
5. Verify that the new focus ring styles do not shrink touch targets or clutter small screens.
**What changed:** Focus ring size and color changed to ensure 4.5:1 contrast on both dark and light backgrounds while preserving touch targets and visual prominence.
