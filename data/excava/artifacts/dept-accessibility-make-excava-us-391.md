# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-391` (dept) · 2026-07-31T19:19:39.602014+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Use a 2px solid #005FCC focus ring with a 1px inset shadow (darker than the ring) at 30% opacity.
**Plan:**
1. Implement a 2px solid #005FCC focus ring with a 1px inset shadow in EXCAVA to ensure high contrast for keyboard users.
2. Test the focus ring with Playwright MCP on iOS Safari at 400% zoom to verify compliance with WCAG 2.1 touch size and contrast requirements.
3. Verify the focus ring does not crowd small touch targets on mobile devices and passes WCAG 2.1 on all tested color schemes.
4. Conduct user testing to ensure the focus ring is visible and usable for users with visual impairments.
5. Refine the focus ring's design and implementation as needed based on user testing and accessibility feedback.
**What changed:** The focus ring design was updated to balance contrast, touch target size, and visual clarity, ensuring EXCAVA is usable by everyone.
