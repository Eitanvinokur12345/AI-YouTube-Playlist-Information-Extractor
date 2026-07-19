# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-193` (dept) · 2026-07-19T15:32:39.129986+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a persistent, 1px tall skip link underline that matches the page's contrast and layout to ensure visibility for sighted keyboard users.
**Plan:**
1. Add a persistent skip link at the top of every page, styled to match the page's contrast and layout.
2. Use CSS to create a 1px tall skip link underline, allowing it to be visible yet unobtrusive for sighted users.
3. Ensure the skip link is visible to screen reader users and keyboard navigators, providing an efficient way to bypass repetitive content.
4. Test the implementation for both screen reader and keyboard users to verify its effectiveness.
5. Verify the solution works across different devices and browsers to guarantee accessibility.
**What changed:** The approach shifted from a purely visually hidden or only-on-focus skip link to a subtle, persistent skip link underline.
