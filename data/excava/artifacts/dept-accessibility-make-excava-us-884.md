# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-884` (dept) · 2026-08-18T14:30:21.459379+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 6px solid #005fcc focus ring at 7:1 contrast with no animation or glow.

**Plan:**
1. Set focus ring width to 6px with solid stroke.
2. Ensure ring color has 7:1 contrast against all backgrounds.
3. Remove animations (e.g., glow, transitions) from focus states.
4. Test focus visibility on glare-prone mobile screens and small touch targets.
5. Validate WCAG 2.1 AA compliance for focus visibility.
6. Document the ring specs in the design system.

**What changed:** Focus ring increased to 6px at 7:1 contrast, no glow/animation.
