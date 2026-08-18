# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-778` (dept) · 2026-08-18T15:05:26.963621+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 5px solid #005fcc focus ring at 6:1 contrast with no animation; deliver a tested, glare-resistant focus style for mobile and screen-reader users; Reader owns the artifact.

**Plan:**
1. Implement a 5px solid focus ring with #005fcc color across all interactive elements.
2. Ensure 6:1 contrast ratio against all backgrounds (light/dark/patterned).
3. Remove glow/animation from focus states for predictability.
4. Test focus visibility with real screen-reader users on mobile and glare-heavy backgrounds.
5. Document the artifact (CSS/design tokens) in Reader’s repo.
6. Validate WCAG 2.1 AA compliance for focus visibility.

**What changed:**
Focus ring adjusted to 5px at 6:1 contrast (#005fcc) from prior proposals.
