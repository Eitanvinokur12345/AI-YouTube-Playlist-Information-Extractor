# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-132` (dept) · 2026-07-31T22:04:04.719935+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Run Playwright MCP nightly against Chrome and Firefox only, logging cross-engine deltas to catch real breakage without wasting cycles on WebKit.

**Plan:**
1. Configure Playwright MCP to execute nightly against Chrome and Firefox engines.
2. Automate EXCAVA interface rendering tests for key visualization components.
3. Log and compare visual deltas between Chrome and Firefox outputs.
4. Generate a concise nightly report highlighting discrepancies for the visualization team.
5. Prioritize fixes based on impact to EXCAVA’s visibility, liveliness, and clarity.
6. Rotate secondary engine focus (e.g., Firefox) every quarter to catch emerging quirks.

**What changed:**
Switched from Chrome-only to Chrome + Firefox nightly testing with delta logging.
