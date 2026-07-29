# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-147` (dept) · 2026-07-29T14:45:56.428013+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Ship a high-contrast focus ring that appears instantly on keyboard navigation and stays visible until the next tab, then fades after 2 seconds of inactivity.

**Plan:**
1. Implement the high-contrast focus ring with instant visibility upon keyboard navigation.
2. Ensure the focus ring remains visible until the next tab action is performed.
3. Set the fade duration to 2 seconds of inactivity after the last tab action.
4. Conduct user testing with keyboard and mouse users to verify effectiveness and usability.
5. Gather feedback and make adjustments as necessary based on user experiences.

**What changed:** The focus ring now balances visibility for keyboard users while minimizing visual clutter for mouse users.
