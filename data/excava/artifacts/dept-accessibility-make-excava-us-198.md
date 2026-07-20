# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-198` (dept) · 2026-07-20T20:10:52.554925+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a focus-triggered skip link to improve accessibility for keyboard users.
**Plan:**
1. Add a focus-triggered skip link at the top of every page, visible only to keyboard users.
2. Style the skip link with high contrast and a full-width design to ensure visibility.
3. Animate the skip link on focus with a 2px bright outline and 100ms fade-in to provide a strong visual cue.
4. Ensure the skip link blends into the page when not focused to avoid visual noise for sighted mouse users.
5. Test the implementation to verify that the skip link is accessible and effective for keyboard users.
**What changed:** The skip link is now focus-triggered, providing a balance between visibility for keyboard users and minimal visual noise for mouse users.
