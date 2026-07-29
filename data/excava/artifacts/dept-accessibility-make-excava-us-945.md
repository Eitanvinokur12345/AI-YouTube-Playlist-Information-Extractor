# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-945` (dept) · 2026-07-29T00:04:58.912069+00:00
> Participants: Access, Ramp, Reader · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a high-contrast focus ring with a 125ms delay, visible until next tab then fading after 1s of inactivity, toggleable via system settings.

**Plan:**
1. Implement a single, high-contrast focus ring that appears on keyboard navigation with a 125ms delay.
2. Ensure the ring remains visible until the next tab, then fades after 1s of inactivity.
3. Make the focus ring toggleable via system settings (e.g., OS-level high-contrast mode).
4. Test with 5 keyboard-only users to validate discoverability and usability.
5. Document the focus ring’s behavior and settings in EXCAVA’s accessibility guidelines.
6. Deliver the focus indicator artifact owned by Ramp (accessibility-w1) by [date].

**What changed:**
Added a toggleable, high-contrast focus ring with a 125ms delay, visible until next tab, fading after 1s of inactivity.
