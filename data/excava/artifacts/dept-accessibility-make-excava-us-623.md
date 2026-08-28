# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-623` (dept) · 2026-08-28T14:19:39.996600+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7.5:1 contrast with 0.5px static inner shadow—deliver CSS spec to UI lead by EOD; Ramp owns.

**Plan:**
1. Generate CSS spec for `3px` focus ring with `7.5:1` contrast and `0.5px static inner shadow`.
2. Test on high-DPI screens to verify visibility without pixel blurring.
3. Validate reduced-motion compliance (static shadow only).
4. Measure task completion time for screen-reader users post-implementation.
5. Document trade-offs (e.g., slight visibility reduction for severe low vision) in accessibility notes.
6. Submit spec to UI lead by EOD with Ramp as owner.

**What changed:**
Focus ring adjusted to 3px at 7.5:1 contrast with static inner shadow, replacing prior 2px/4px proposals.
