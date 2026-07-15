# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-888` (dept) · 2026-07-15T09:21:51.902047+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid approach with a server-side skip link using `display: none` that toggles visibility via client-side JavaScript when it receives keyboard focus.

**Plan:**
1. Develop a server-side skip link that is accessible on every page load but remains hidden using `display: none`.
2. Write client-side JavaScript to toggle the skip link's visibility when keyboard focus reaches the first interactive element on the page.
3. Conduct performance testing to ensure that the hybrid approach does not adversely affect load times.
4. Implement the feature across all pages of EXCAVA and ensure compliance with accessibility standards.
5. Create documentation detailing how the skip link works and its benefits for both keyboard and sighted users. 

**What changed:** A hybrid solution was chosen to balance accessibility needs with performance concerns.
