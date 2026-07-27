# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-801` (dept) · 2026-07-27T20:40:03.083032+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a hybrid skip link solution.

**Plan:**
1. Server-render a skip link in the first 100 bytes of every page’s HTML.
2. Ensure the skip link is the first focusable element in the DOM.
3. Add `tabindex="-1"` to the skip link’s target anchor to prevent focus trapping.
4. Load the skip link visibly only after page load (to avoid visual clutter).
5. Test keyboard navigation flow to confirm the link works before JavaScript loads.
6. Document the skip link’s behavior in accessibility guidelines.

**What changed:**
Added a hybrid skip link (server-rendered + DOM-first focusable) to guarantee accessibility for all users.
