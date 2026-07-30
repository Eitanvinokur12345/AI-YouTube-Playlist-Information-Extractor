# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-392` (dept) · 2026-07-30T22:51:10.064886+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default EXCAVA to dark theme but expose a one-click system-wide light/dark/auto toggle in the top-right corner.

**Plan:**
1. Set dark theme as default in EXCAVA’s CSS with high-contrast interactive elements.
2. Implement a persistent top-right toggle (light/dark/auto) with instant theme switching.
3. Test glare resistance in real bright rooms (e.g., sunlit offices, outdoor setups) with 30%+ users.
4. Add auto-mode that detects ambient light via OS/browser APIs to auto-switch themes.
5. Ensure toggle state persists across sessions via localStorage or backend sync.
6. Document theme behavior in EXCAVA’s help section with glare-testing results.

**What changed:** Dark default + instant override toggle, validated in real glare conditions.
