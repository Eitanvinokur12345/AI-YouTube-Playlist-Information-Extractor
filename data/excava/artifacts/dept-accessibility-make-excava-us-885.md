# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-885` (dept) · 2026-08-16T10:52:01.321976+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 2px #fff outer stroke at 100% opacity for keyboard navigation.

**Plan:**
1. Update the focus ring style in the global CSS to use `2px solid #005fcc` with `2px #fff` outer stroke at 100% opacity.
2. Test the focus ring on light, dark, and high-contrast backgrounds to ensure WCAG 2.2 AA compliance.
3. Verify keyboard navigation visibility in all interactive components (buttons, links, form fields).
4. Document the focus ring style in the accessibility guidelines for future reference.
5. Deploy changes to staging and conduct user testing with screen reader and keyboard-only users.
6. Monitor feedback and adjust opacity or stroke width if any visibility issues arise.

**What changed:**
Focus ring updated to 2px #005fcc with 2px #fff outer stroke at 100% opacity for WCAG 2.2 AA compliance.
