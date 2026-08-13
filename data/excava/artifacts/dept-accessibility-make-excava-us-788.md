# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-788` (dept) · 2026-08-13T14:01:28.117472+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 1px inner #fff cutout at 90% opacity for crisp, high-contrast visibility across all modes.

**Plan:**
1. Implement the 2px solid #005fcc focus ring with a 1px inner #fff cutout at 90% opacity.
2. Test WCAG 2.2 contrast (4.5:1 on light, 3:1 on dark/high-contrast) in all modes (light/dark/Windows high-contrast).
3. Validate crisp edges at 100%–400% zoom levels without blur or flicker.
4. Ensure compatibility with keyboard navigation and touch targets.
5. Document the decision in the accessibility guidelines.
6. Deploy and monitor user feedback for refinements.

**What changed:**
Focus ring refined to 2px solid #005fcc with 1px inner #fff cutout at 90% opacity for balanced crispness and contrast.
