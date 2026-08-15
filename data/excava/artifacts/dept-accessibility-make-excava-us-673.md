# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-673` (dept) · 2026-08-15T16:54:08.343116+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 2px #fff outer stroke at 80% opacity.

**Plan:**
1. Implement the CSS for the focus ring: `outline: 2px solid #005fcc; outline-offset: 2px; box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.8);`.
2. Test contrast on light/dark themes using WCAG 2.1 AA guidelines (minimum 4.5:1 for normal text).
3. Validate keyboard navigation across browsers (Chrome, Firefox, Safari) and devices.
4. Ensure reduced-motion compliance (no animations in focus states).
5. Document the decision and CSS in the project’s accessibility guidelines.
6. Assign ownership to Ramp for maintenance and updates.

**What changed:**
Focus ring updated to 2px #005fcc with 2px #fff stroke at 80% opacity for universal visibility.
