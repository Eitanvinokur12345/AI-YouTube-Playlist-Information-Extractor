# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-462` (dept) · 2026-07-15T10:56:07.854077+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid server-side skip link that is hidden by default and revealed through client-side JavaScript.

**Plan:**
1. Develop a server-side skip link included in every page rendering.
2. Ensure the skip link is hidden by default using CSS.
3. Create client-side JavaScript functionality to reveal the skip link when keyboard focus reaches specified page elements, like the footer.
4. Test the implementation with and without JavaScript enabled to ensure functionality for all users.
5. Engage the accessibility team for full oversight and support in the implementation and testing phases.

**What changed:** The decision to use a hybrid approach allows for reliable accessibility while maintaining visual integrity.
