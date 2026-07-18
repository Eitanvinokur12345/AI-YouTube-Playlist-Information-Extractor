# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-905` (dept) · 2026-07-18T02:10:07.612092+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a persistent, high-contrast skip link to ensure accessibility for keyboard users.
1. **Add a persistent skip link**: Create a high-contrast skip link at the top of every page.
2. **Style with reduced visual weight**: Use a thin underline or similar styling to minimize visual footprint.
3. **Ensure immediate visibility**: Make the skip link appear immediately when the page loads and remain fixed at the top.
4. **Test with keyboard users**: Validate the solution with real keyboard users to ensure it meets their needs.
5. **Monitor and adjust**: Continuously monitor user feedback and adjust the implementation as needed.
**What changed:** The decision moved from a hidden or focus-based skip link to a always-visible, high-contrast link with reduced visual weight.
