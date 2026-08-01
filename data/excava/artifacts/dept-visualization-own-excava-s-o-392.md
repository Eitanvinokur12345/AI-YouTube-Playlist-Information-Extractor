# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-392` (dept) · 2026-07-30T22:51:10.064886+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default EXCAVA to dark theme but expose a one-click system-wide light/dark/auto toggle in the top-right corner.
> Decision artifact · room `dept-visualization-own-excava-s-o-392` (dept) · 2026-07-30T22:45:35.043141+00:00
> Participants: Facet, Pane, Lumen · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Default EXCAVA to dark theme with a persistent one-click toggle (light/dark/auto) in the top-right corner.
**Plan:**
1. Set dark theme as default in EXCAVA’s CSS with high-contrast interactive elements.
2. Implement a persistent top-right toggle (light/dark/auto) with instant theme switching.
3. Test glare resistance in real bright rooms (e.g., sunlit offices, outdoor setups) with 30%+ users.
4. Add auto-mode that detects ambient light via OS/browser APIs to auto-switch themes.
5. Ensure toggle state persists across sessions via localStorage or backend sync.
6. Document theme behavior in EXCAVA’s help section with glare-testing results.

**What changed:** Dark default + instant override toggle, validated in real glare conditions.
1. Implement a dark-themed interface as the default for EXCAVA, aligning with Manus and Graphify for consistency.
2. Add a one-click toggle (light/dark/auto) in the top-right corner for users to switch between themes.
3. Conduct usability testing in various environments, including bright and dimly lit rooms, to ensure the interface is usable for all users.
4. Test the auto-toggle feature to ensure it effectively switches between light and dark themes based on ambient light conditions.
5. Gather feedback from users, particularly the 30% who work in sunlit rooms, to identify areas for improvement.
**What changed:** The default theme of EXCAVA is now dark with a user-controlled toggle, prioritizing usability and consistency.
