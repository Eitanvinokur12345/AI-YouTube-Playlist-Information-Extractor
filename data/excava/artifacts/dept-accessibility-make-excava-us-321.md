# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-321` (dept) · 2026-07-15T10:19:46.871386+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid skip link that is server-rendered, hidden by default, and revealed on focus via CSS.

**Plan:**
1. Design and implement a server-rendered skip link at the top of every page that is initially hidden using CSS.
2. Create a CSS rule to reveal the skip link when it receives keyboard focus.
3. Test the implementation for functionality with and without JavaScript enabled.
4. Ensure the skip link works smoothly across different devices and screen sizes to maintain usability.
5. Document the implementation in the accessibility guidelines for future reference and maintenance.

**What changed:** A balanced approach was chosen to provide both accessibility and visual consistency.
