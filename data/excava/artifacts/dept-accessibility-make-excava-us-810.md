# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-810` (dept) · 2026-07-20T18:02:20.720612+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a focus-triggered skip link to enhance accessibility in EXCAVA's UI.
**Plan:**
1. Design a high-contrast, full-width skip link that appears on the first tab press.
2. Develop a fade-out effect that hides the skip link after navigation, with a 1-second delay.
3. Integrate the skip link component into EXCAVA's UI library for consistency across the platform.
4. Test the skip link for usability and accessibility, ensuring it meets the needs of keyboard users.
5. Refine the visual design of the skip link to be visually subdued until focus is applied, then enhance its contrast and visibility.
**What changed:** EXCAVA will now include a focus-triggered skip link to improve accessibility for keyboard users.
