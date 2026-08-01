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
> Decision artifact · room `dept-visualization-own-excava-s-o-950` (dept) · 2026-07-31T21:40:51.306479+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use Playwright MCP to drive EXCAVA live in Chrome only for screencasts, accepting Firefox/Safari blind spots since Chrome is the primary target.

**Plan:**
1. Configure Playwright MCP to exclusively use Chrome for automation.
2. Implement a single-browser screencast pipeline with Playwright’s Chrome engine.
3. Optimize EXCAVA’s interface for Chrome’s rendering quirks to ensure consistency.
4. Validate screencast output for speed, clarity, and reproducibility.
5. Document Chrome-only limitations in the project README.
6. Monitor for silent failures and log Chrome-specific edge cases.

**What changed:** Chrome-only automation adopted for screencasts, sacrificing Firefox/Safari compatibility.
