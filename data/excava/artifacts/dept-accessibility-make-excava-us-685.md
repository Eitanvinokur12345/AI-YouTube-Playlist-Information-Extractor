# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-685` (dept) · 2026-08-26T09:15:38.597384+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 5px solid focus ring at 5:1 contrast, static design, validated with 10 low-vision users across light/dark/mobile contexts.

**Plan:**
1. Implement 5px solid focus ring with 5:1 contrast ratio in all interactive elements.
2. Ensure static (non-animated) focus ring to avoid motion sensitivity issues.
3. Conduct user testing with 10 low-vision participants across light/dark/mobile scenarios.
4. Document focus ring specs in design system (color tokens, spacing rules).
5. Add fallback focus styles for legacy browsers if needed.
6. Monitor real-world usage data post-launch for adjustments.

**What changed:**
Focus ring increased from 3px/4px to 5px at 5:1 contrast for broader accessibility coverage.
