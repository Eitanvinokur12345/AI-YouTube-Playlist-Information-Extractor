# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-950` (dept) · 2026-07-31T21:42:56.162070+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Drive EXCAVA’s interface live in Chrome only via Playwright MCP for screencasts.

**Plan:**
1. Configure Playwright MCP to launch EXCAVA in a single Chrome instance for all screencasts.
2. Ensure Playwright’s viewport settings match EXCAVA’s default dimensions for consistency.
3. Implement error handling to detect and log Chrome-specific failures (e.g., timeouts, element visibility).
4. Generate screencasts directly from the live Chrome session with minimal post-processing.
5. Document Chrome-only limitations in the screencast metadata (e.g., "Tested on Chrome 120+").
6. Validate screencast quality by comparing against a reference Chrome session before deployment.

**What changed:** Chrome-only automation adopted to prioritize speed and consistency over cross-browser coverage.
