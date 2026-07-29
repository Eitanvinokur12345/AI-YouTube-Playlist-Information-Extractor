# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-290` (dept) · 2026-07-29T15:29:17.027251+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Ship a high-contrast focus ring (immediate, static) + subtle secondary outline (thin, always present).  

**Plan:**  
1. Implement a high-contrast focus ring that appears immediately during keyboard navigation.  
2. Design a subtle secondary outline that is always present around interactive elements.  
3. Test the new focus indicators to ensure they meet WCAG 2.2 SC 2.4.7 compliance.  
4. Gather feedback from users, particularly keyboard navigation users, to assess usability.  
5. Iterate on design based on user feedback to balance focus visibility and visual harmony.  

**What changed:** The decision combines immediate visibility for keyboard users with a reduced visual overload through a dual-focus indicator system.
