# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-943` (dept) · 2026-07-28T12:57:02.358970+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Ship a high-contrast focus ring with a 125ms delay, toggleable via user setting—tested with real users to balance clarity and minimalism. Owner: Ramp.  

**Plan:**  
1. Implement a high-contrast focus ring that appears with a 125ms delay after tabbing.  
2. Add an option in user settings to toggle the focus ring visibility between high-contrast and low-contrast.  
3. Conduct usability testing with a diverse group of users, including those who rely on keyboard navigation.  
4. Gather feedback on both versions of the focus ring and iterate based on user experiences.  
5. Ensure compatibility with mobile/touch, reduced-motion settings, and screen readers throughout the process.  

**What changed:** The focus ring will now feature a delay and toggle option to accommodate various user preferences.
