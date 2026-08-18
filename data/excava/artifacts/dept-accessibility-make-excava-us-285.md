# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-285` (dept) · 2026-08-18T03:42:21.786522+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 1px inner shadow (no glow/animation) at 6:1 contrast for EXCAVA.

**Plan:**
1. Set all interactive elements’ `:focus-visible` state to `3px solid #005fcc` with `1px inner shadow`.
2. Ensure 6:1 contrast ratio against all backgrounds via automated testing (e.g., Stark/axe).
3. Validate in screen-reader sessions (NVDA/JAWS) for clear announcement and no flicker.
4. Test in reduced-motion OS/browser settings to confirm no animation triggers.
5. Audit toolbar buttons and small elements for spacing conflicts; adjust padding/margins if needed.
6. Document the focus style in EXCAVA’s design system with code snippets and contrast specs.

**What changed:** Replaced 2px ring + 4px glow with 3px solid ring + 1px inner shadow at 6:1 contrast.
