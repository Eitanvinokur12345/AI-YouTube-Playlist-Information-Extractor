# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-535` (dept) · 2026-07-11T15:33:02.059374+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a **subtle focus ring (2px solid, high-contrast color)** by default for all interactive elements.
2. Add a **user toggle** (e.g., in settings or via keyboard shortcut) to switch to a **bold focus ring (3px dashed, animated)**.
3. Conduct A/B testing with real keyboard users to compare task completion speed and clarity between the two focus ring styles.
4. Analyze test results by **[date]** and select the better-performing focus ring style.
5. Document the chosen focus ring style and toggle functionality in EXCAVA’s accessibility guidelines.
6. Ensure the focus ring styles meet WCAG 2.2 AA contrast requirements.

**What changed:** Added configurable focus ring options (subtle default + bold toggle) with user-tested optimization.
