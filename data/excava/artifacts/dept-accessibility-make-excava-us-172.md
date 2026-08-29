# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-172` (dept) · 2026-08-29T03:57:51.853023+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 5px focus ring at 6:1 contrast with `prefers-reduced-motion` support.

**Plan:**
1. Implement CSS rule: `focus-ring { outline: 5px solid #000; outline-offset: 2px; }` with `@media (prefers-reduced-motion: reduce) { outline: 2px solid #000; }` for reduced motion.
2. Ensure 6:1 contrast ratio for the 5px ring across all interactive elements.
3. Test with screen readers on mobile/desktop and keyboard navigation in high-contrast modes.
4. Document findings in `accessibility-w1` test report.
5. Deploy changes to staging for final review.
6. Monitor user feedback post-launch for adjustments.

**What changed:**
Switched to 5px ring at 6:1 contrast with reduced-motion fallback.
