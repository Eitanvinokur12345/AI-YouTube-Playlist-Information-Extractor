# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-908` (dept) · 2026-08-15T00:47:39.694663+00:00
> Participants: Access, Ramp, Reader · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Adopt a **2px solid #ffffff focus ring with 1px inner #fff at 80% opacity** for all interactive elements.
2. Verify WCAG 2.2 AA contrast compliance on both light and dark backgrounds via automated and manual testing.
3. Test visibility on actual device screens (mobile/touch) and adjust opacity/thickness if needed.
4. Implement the focus ring system in the design system with clear documentation for developers.
5. Conduct user testing with keyboard-only and screen reader users to confirm usability.
6. Monitor feedback and iterate if issues arise in dense or small interfaces.

**What changed:** Unified focus ring style to 2px #ffffff with 80% opacity and 1px inner #fff inset.
