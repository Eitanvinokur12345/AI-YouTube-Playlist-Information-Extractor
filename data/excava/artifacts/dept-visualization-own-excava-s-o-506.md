# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-506` (dept) · 2026-07-31T20:59:50.026502+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use Playwright MCP to drive EXCAVA’s interface live for real-time, interactive visualization.

**Plan:**
1. Integrate Playwright MCP with EXCAVA’s interface to enable live interaction.
2. Define stable, testable UI elements in EXCAVA for Playwright to target.
3. Implement real-time state synchronization between EXCAVA and the screencast.
4. Add error handling for silent failures (e.g., logging, fallback static overlays).
5. Validate live screencast stability via automated regression tests.
6. Document EXCAVA’s UI contract for Playwright to prevent silent breakage.

**What changed:** Switched from pre-recorded screencast + highlights to live Playwright-driven interaction.
