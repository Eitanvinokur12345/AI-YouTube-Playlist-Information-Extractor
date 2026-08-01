# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-143` (dept) · 2026-07-31T20:38:25.202498+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use Playwright MCP to drive EXCAVA’s interface directly.

**Plan:**
1. Integrate Playwright MCP into EXCAVA’s visualization layer to enable real-time updates.
2. Implement robust error handling in the MCP server to mitigate single-point-of-failure risks.
3. Add logging for interface state snapshots to Redis as a fallback for debugging.
4. Assign the visualization-w1 lead to own and maintain the interface integration.
5. Document the coupling risks and recovery procedures for the MCP server.
6. Conduct stress tests to validate real-time performance under load.

**What changed:** Playwright MCP now drives the interface directly, prioritizing liveliness over decoupling.
