# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-707` (dept) · 2026-07-28T22:57:15.879222+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a high-contrast focus ring with a 125ms delay, toggleable via 'u'.

**Plan:**
1. Implement a high-contrast focus ring (WCAG 2.2 AA compliant).
2. Add a 125ms delay before the ring appears.
3. Include a toggle via the 'u' key to enable/disable the focus ring.
4. Add user preference persistence (localStorage).
5. Document keyboard navigation testing notes.
6. Assign Ramp as owner for implementation and maintenance.

**What changed:** Added toggleable high-contrast focus ring with 125ms delay.
