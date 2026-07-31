# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-182` (dept) · 2026-07-31T21:20:54.489088+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use Playwright MCP to drive EXCAVA’s interface live in Chrome for the screencast.

**Plan:**
1. Configure Playwright MCP to automate EXCAVA’s interface in Chrome.
2. Record the screencast live, ensuring visibility, liveliness, and speed.
3. Validate the screencast’s clarity by reviewing the recorded output for immediate feedback.
4. Document the Chrome-only dependency in the demo setup instructions.
5. Add a note in the project’s README about potential subtle rendering differences in other browsers.
6. Deploy the screencast as the primary visualization tool for EXCAVA’s interface.

**What changed:** Chrome-only Playwright MCP automation replaces multi-engine CI checks for the live screencast.
