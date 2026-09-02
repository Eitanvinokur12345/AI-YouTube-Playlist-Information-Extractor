# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-470` (dept) · 2026-09-02T18:10:27.167074+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px focus ring at 7:1 contrast by default, with a 0.5px inset shadow at 4.5:1 for reduced-motion users.

**Plan:**
1. Implement the 3px focus ring at 7:1 contrast in EXCAVA’s style system as the default.
2. Add a conditional 0.5px inset shadow at 4.5:1 contrast for users who enable reduced motion.
3. Document the focus ring styles in the design system with usage guidelines.
4. Conduct live testing with 5 users toggling both reduced motion and high contrast to verify visibility.
5. Publish the tested focus ring styles in the EXCAVA component library.
6. Monitor user feedback and adjust if issues arise in production.

**What changed:**
Default focus ring increased to 3px at 7:1 contrast with reduced-motion fallback.
