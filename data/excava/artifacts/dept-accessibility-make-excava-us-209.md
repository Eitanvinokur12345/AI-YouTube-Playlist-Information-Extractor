# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-209` (dept) · 2026-07-27T06:50:27.854374+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a single high-contrast "Skip to main content" link at the top of every page, paired with ARIA landmarks (`main`, `navigation`, `complementary`, etc.) for section navigation.

**Plan:**
1. Add a single high-contrast "Skip to main content" link at the very top of every page.
2. Implement ARIA landmarks (`main`, `navigation`, `complementary`, etc.) to enable screen-reader navigation between sections.
3. Ensure the skip link is keyboard-focusable and visible on focus.
4. Test with screen readers (NVDA, VoiceOver) and keyboard-only navigation to verify accessibility.
5. Confirm the skip link does not introduce excessive tab stops for sighted keyboard users.
6. Document the skip link and ARIA landmarks in the accessibility guidelines for future development.

**What changed:**
Added a single high-contrast skip link + ARIA landmarks for section navigation.
