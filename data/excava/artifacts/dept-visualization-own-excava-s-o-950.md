# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

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
