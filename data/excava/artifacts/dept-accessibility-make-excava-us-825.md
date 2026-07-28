# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-825` (dept) · 2026-07-28T23:18:58.194252+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a high-contrast focus ring that appears instantly on focus.
2. Fade the ring to subtle after 125ms to reduce cognitive noise.
3. Ensure the ring follows tab order without exceptions for keyboard users.
4. Conduct user testing to measure task completion time and error rates for sighted keyboard users and screen-reader users.
5. Adjust timing or contrast based on test results to balance clarity and cognitive load.
6. Document the focus ring behavior in the accessibility guidelines for EXCAVA.

**What changed:** Focus ring now appears instantly then fades to subtle after 125ms, balancing clarity and cognitive noise.
