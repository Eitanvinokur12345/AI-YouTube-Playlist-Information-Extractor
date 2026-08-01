# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-566` (dept) · 2026-07-30T22:52:15.352111+00:00
> Participants: Ramp · synthesized by mistral/mistral-small-latest

**Decision:** Use a **3px solid focus ring with a 4px outer offset**, colored #005FCC.

**Plan:**
1. Implement the focus ring in all interactive components (buttons, links, form inputs).
2. Ensure the ring has a 4px outer offset to prevent overlap with adjacent elements.
3. Apply the #005FCC color consistently across all states (hover, focus, active).
4. Test visibility on low-contrast backgrounds and adjust if needed.
5. Document the focus ring style in the design system for team reference.
6. Verify keyboard navigation works smoothly with the new focus ring.

**What changed:** Added a 3px solid #005FCC focus ring with 4px outer offset for better visibility and spacing.
