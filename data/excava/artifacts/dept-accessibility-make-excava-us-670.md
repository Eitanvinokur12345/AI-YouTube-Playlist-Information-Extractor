# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-670` (dept) · 2026-07-29T15:47:47.929113+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Ship a high-contrast focus ring (immediate, static) + subtle reduced-motion variant (toggle via user motion preference).  

**Plan:**  
1. Implement a high-contrast focus ring that is immediately visible on keyboard navigation.  
2. Develop a subtle focus ring variant that adapts to user motion preferences, fading out for reduced-motion users.  
3. Ensure both focus styles meet WCAG 2.2 Level AA compliance.  
4. Create CSS and JavaScript to manage the implementation of both focus styles.  
5. Develop Playwright MCP tests to validate the functionality of the focus indicators in both states.  
6. Assign ownership of the task to the accessibility-w1 team for oversight and execution.  

**What changed:** A balance was reached between visibility for keyboard users and cognitive comfort for others by offering two variants of the focus ring.
