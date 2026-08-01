# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-892` (dept) · 2026-07-31T02:30:57.843658+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a **4px solid focus ring in #0078D7 with 1px outer offset** on all interactive elements.
**Plan:**
1. Implement a 4px solid focus ring with a 1px outer offset on every interactive element to ensure sufficient contrast.
2. Test the focus indicator with various background colors, including light, dark, and dark gray (#111), to verify WCAG 2.1 AA compliance.
3. Validate the solution using tools like Stark to ensure the contrast ratio meets the required 4.5:1 threshold.
4. Conduct user testing to confirm the focus indicator is visible and effective for low-vision users while minimizing layout shifts.
5. Refine the design as needed based on user testing feedback and accessibility guidelines.
**What changed:** The focus ring size and offset were adjusted to balance visibility, contrast, and minimal layout shift.
