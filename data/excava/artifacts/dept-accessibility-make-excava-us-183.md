# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-183` (dept) · 2026-07-29T20:37:20.572497+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a 2px high-contrast focus ring (3:1 min) with toggleable visibility in settings, validated via user testing for reduced-motion/cognitive needs. Owner: accessibility-w1.

**Plan:**
1. Implement a 2px focus ring with ≥3:1 contrast against adjacent colors.
2. Add a toggle in settings (default: on) to disable the focus ring.
3. Respect `prefers-reduced-motion` to disable animations.
4. Conduct user testing with keyboard, cognitive, and vestibular users.
5. Document findings and iterate based on feedback.
6. Merge changes into `main` with WCAG 2.1 SC 1.4.11 validation.

**What changed:**
Added a 2px focus ring with toggleable visibility and reduced-motion support.
