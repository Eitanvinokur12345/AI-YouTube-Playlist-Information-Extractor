# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-587` (dept) · 2026-08-18T13:27:05.952390+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 3px solid #005fcc focus ring at 6:1 contrast with no animation.

**Plan:**
1. Define the focus ring in EXCAVA’s style guide as a 3px solid #005fcc with 6:1 contrast.
2. Remove all focus ring animations to avoid vestibular triggers.
3. Test tap accuracy and perceived focus clarity on 48×48 mobile touch targets.
4. Validate focus visibility on glare-prone and low-contrast backgrounds.
5. Document the decision in the accessibility-w1 repo with implementation notes.
6. Schedule a follow-up review after 2 weeks of real-world usage.

**What changed:** Focus ring updated to 3px, 6:1 contrast, no animation.
