# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-504` (dept) · 2026-08-10T19:51:15.076988+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring at 90% opacity with a 1px inner #ffffff offset.

**Plan:**
1. Implement the 2px #005fcc focus ring at 90% opacity with a 1px inner #ffffff offset.
2. Validate WCAG 2.1 AA contrast (4.5:1) on both light/dark themes and busy backgrounds.
3. Test on Samsung Galaxy A51 (touch) at 100% zoom to ensure visibility.
4. Add reduced-motion media query to disable animations for users who prefer it.
5. Document the focus ring style in the design system for consistency.
6. Assign Ramp as owner for implementation and future updates.

**What changed:**
Focus ring updated to 2px #005fcc at 90% opacity with 1px inner offset for WCAG compliance and touch visibility.
