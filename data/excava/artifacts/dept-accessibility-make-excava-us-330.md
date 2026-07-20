# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-330` (dept) · 2026-07-20T17:26:09.150955+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a focus-triggered skip link to enhance accessibility for keyboard users while maintaining a clean interface for mouse users.
**Plan:**
1. Add a high-contrast, full-width skip link that appears only when the Tab key is pressed.
2. Ensure the skip link collapses after it is used, removing it from view for mouse users.
3. Implement the skip link in the top position of the page to allow for easy bypassing of repetitive navigation blocks.
4. Test the implementation on various devices, including mobile, to guarantee responsiveness and accessibility.
5. Verify that the focus-triggered skip link is visible to all keyboard users, including those with visual impairments, while remaining invisible to mouse users.
**What changed:** The original proposal for a persistent or single high-contrast skip link was replaced with a focus-triggered skip link for better accessibility and UI clarity.
