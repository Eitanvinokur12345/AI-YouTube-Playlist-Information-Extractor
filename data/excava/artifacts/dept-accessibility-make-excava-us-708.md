# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-708` (dept) · 2026-07-15T11:48:20.216964+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hidden skip link that appears when focused via keyboard, ensuring WCAG compliance and improved keyboard navigation.

**Plan:**
1. Develop a hidden skip link that activates on keyboard focus, adhering to accessibility guidelines.
2. Conduct user testing to evaluate the effectiveness and placement of the skip link, assessing user experience for both keyboard and sighted users.
3. Optimize the position of the skip link based on testing feedback, considering placements like top-right, fixed position, or directly after the header.
4. Document findings from user testing and adjustments made to inform future accessibility enhancements.
5. Ensure ongoing maintenance and updates to the skip link feature based on user feedback and emerging accessibility standards.

**What changed:** Focus on user testing led to a decision to implement a hidden skip link instead of a visible one.
