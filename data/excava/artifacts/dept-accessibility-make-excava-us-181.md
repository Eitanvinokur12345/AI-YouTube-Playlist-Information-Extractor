# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-181` (dept) · 2026-07-15T09:42:35.695571+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid skip link to enhance accessibility for all users.

**Plan:**  
1. Create a skip link that is always visible but positioned off-screen until focused by keyboard users.  
2. Ensure the skip link is coded to provide a fall-back server-side option for environments where JavaScript is disabled or slow-loading.  
3. Test the implementation across various devices and screen readers to ensure usability and visibility cues are effective.  
4. Gather user feedback specifically from screen reader and keyboard users to refine the solution if necessary.  
5. Document the implementation process and accessibility outcomes in the project repository for future reference.

**What changed:** A hybrid approach balances visibility for keyboard users while maintaining a clean interface for mouse users.
