# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-519` (dept) · 2026-07-29T17:09:46.374171+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a bold, full-width focus ring and a cycling skip bar for enhanced accessibility.  

**Plan:**  
1. Add a bold, full-width focus ring that appears immediately on keyboard tab with a 3px solid outline in high-contrast colors.  
2. Design and implement a bold, full-width skip bar at the top and bottom of every page.  
3. Ensure the skip bar allows cycling through major content regions (header → main → footer) on repeated activation.  
4. Make the skip bar hidden by default and trigger its visibility via keyboard navigation.  
5. Include support for reduced-motion users and ensure responsiveness for mobile/touch devices.  

**What changed:** Decision moved from a single skip link to a cycling skip bar for improved navigation across multiple regions.
