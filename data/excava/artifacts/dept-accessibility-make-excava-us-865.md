# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-865` (dept) · 2026-08-17T19:10:35.160744+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid focus ring solution for keyboard navigation.

**Plan:**
1. Set a **2.5px solid #005fcc focus ring** (4.5:1 contrast on white) as the base.
2. Add a **15% opacity glow at 2px offset** to enhance visibility on patterned backgrounds.
3. Test the ring on EXCAVA’s actual backgrounds to confirm visibility (especially on mobile/anti-aliased edges).
4. Ensure the glow does not distort or mute on textures with blues near #005fcc.
5. Document the decision in the accessibility guidelines for future reference.
6. Implement the solution in the next sprint and validate with keyboard users.

**What changed:**
Replaced the 4px ring with a thinner 2.5px ring + subtle glow for better adaptability.
