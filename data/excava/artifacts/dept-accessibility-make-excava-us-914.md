# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-914` (dept) · 2026-07-31T06:03:44.086743+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a 2px solid focus ring in #0078D4 with 1px outer glow at 0s to ensure sufficient contrast and visibility for keyboard navigation.
**Plan:**
1. Implement a 2px solid focus ring in #0078D4 for interactive elements to provide clear focus indication.
2. Add a 1px outer glow at 0s to enhance visibility without introducing excessive visual noise.
3. Conduct testing with a 10-person keyboard-only user group to validate the effectiveness of the chosen design.
4. Verify that the implemented focus ring design meets WCAG 2.1 AA contrast requirements on various brand backgrounds.
5. Refine the design as needed based on user testing feedback and accessibility compliance checks.
**What changed:** The focus ring design was adjusted to balance visibility, contrast, and minimal visual noise, ensuring accessibility for keyboard navigation.
