# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-756` (dept) · 2026-07-28T12:35:33.968457+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a semi-transparent, high-contrast focus ring with adjustable opacity (default: 70%).
2. Dynamically scale ring opacity based on content density (e.g., reduce opacity to 30% on dense screens).
3. Ensure the ring follows tab order and is keyboard-only visible by default (no hover triggers).
4. Add a user preference to toggle focus ring visibility or adjust opacity levels (stored in localStorage).
5. Test with screen readers, keyboard navigation, and low-vision users to validate usability.
6. Document the feature in accessibility guidelines for developers.

**What changed:** Focus ring is now semi-transparent, scalable, and user-adjustable.
