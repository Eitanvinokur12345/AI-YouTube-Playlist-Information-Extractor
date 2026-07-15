# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-657` (dept) · 2026-07-15T10:01:26.884851+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid approach with a server-side skip link hidden by default, activated via client-side JavaScript.

**Plan:**
1. Develop a server-side skip link that is present in the HTML but visually hidden by default.
2. Create client-side JavaScript that activates the skip link when keyboard focus reaches the first interactive element after the navigation block.
3. Ensure the skip link is accessible for keyboard users without disrupting the experience for mouse or touch users.
4. Conduct testing with JavaScript disabled to validate accessibility and functionality for keyboard users.
5. Gather feedback from users to refine the implementation and address any additional accessibility concerns.

**What changed:** A balanced approach was adopted to ensure all users can access the skip link effectively, enhancing overall usability.
