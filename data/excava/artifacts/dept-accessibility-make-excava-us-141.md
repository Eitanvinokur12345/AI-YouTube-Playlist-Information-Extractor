# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-141` (dept) · 2026-07-28T23:45:30.918664+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a high-contrast focus ring with a 125ms delay to improve accessibility for keyboard users.
1. **Add a high-contrast focus ring** to every interactive element, ensuring keyboard users can see where they are at a glance.
2. **Introduce a 125ms delay** before showing the focus ring to balance between providing feedback and avoiding cognitive noise.
3. **Make the focus ring toggleable** via a keyboard shortcut to accommodate different user preferences.
4. **Validate with Playwright tests** to ensure the implementation meets accessibility standards.
5. **Monitor user feedback** to assess the effectiveness of the focus ring and gather insights for future improvements.
**What changed:** The introduction of a delay and a toggle option for the high-contrast focus ring to address concerns about visual clutter and cognitive noise.
