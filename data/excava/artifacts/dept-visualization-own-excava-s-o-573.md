# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-573` (dept) · 2026-08-26T09:43:47.346449+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Implement a sticky sidebar legend anchored to the left edge of the graph by default.
2. Condense the legend into a thin vertical strip (e.g., 30px width) when users zoom into dense data.
3. Ensure the condensed strip remains sticky and reveals full legend content on hover or click.
4. Conduct usability tests to validate visibility, context retention, and data clarity at all zoom levels.
5. Iterate based on test feedback, adjusting strip width or interaction triggers (e.g., hover delay).
6. Document the behavior in the interface’s help/tooltip for discoverability.

**What changed:** Legend transitions from full sticky panel to condensed sticky strip during zoom.
