# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-579` (dept) · 2026-07-31T19:48:53.133901+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to a **dynamic theme** that auto-switches between light (white base with dark text/accents) and dark (dark base with high-contrast accents) based on ambient light, with a fallback to dark if detection fails.

**Plan:**
1. Implement ambient light detection (e.g., via OS API or browser sensor) to trigger theme switching.
2. Design two base themes:
   - **Light mode**: White background with dark text/accents (high readability in bright light).
   - **Dark mode**: Dark background with high-contrast accents (reduces glare in low light).
3. Ensure fallback to dark mode if detection fails or is unsupported.
4. Test rendering consistency across devices and screencast tools (e.g., OBS, Manus).
5. Document presenter lighting protocol (e.g., avoid direct glare sources) for controlled recordings.
6. Align dark mode accents with Manus’s color scheme for consistency.

**What changed:**
Dynamic theme replaces fixed dark/light themes, prioritizing readability across lighting conditions.
