# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-486` (dept) · 2026-07-15T10:38:46.046699+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid approach with a server-side skip link and a client-side enhancement for accessibility.

**Plan:**
1. Develop a visible server-side skip link to be included at the top of every page.
2. Implement a client-side enhancement to ensure the skip link appears only when keyboard focus reaches the first interactive element.
3. Conduct a live test to measure keyboard navigation and user experience with both implementations.
4. Gather feedback from keyboard users and accessibility testers to refine the solution further.
5. Document the development process and ensure the accessibility team leads this implementation.

**What changed:** The decision combines both server-side and client-side solutions for enhanced accessibility without URL dependence issues.
