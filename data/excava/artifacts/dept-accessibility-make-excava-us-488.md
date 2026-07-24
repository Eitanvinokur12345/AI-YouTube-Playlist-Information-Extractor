# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-488` (dept) · 2026-07-24T10:35:35.642116+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a bold, full-width skip button that appears only when keyboard-focused, then fades back—high contrast, mobile/touch-safe, and screen-reader friendly.

**Plan:**
1. Design a bold, full-width skip button that contrasts with the background.
2. Implement the button to appear only when users tab through the page.
3. Ensure the button fades back after the user navigates away from it.
4. Test the skip button for visibility and usability with sighted keyboard users and screen-reader users.
5. Involve the frontend team in implementing and maintaining the skip button artifact in EXCAVA's template.

**What changed:** The decision to use a full-width skip button that highlights on keyboard focus addresses both visibility for sighted users and accessibility concerns for screen-reader users effectively.
