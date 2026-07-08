# visualization: Own the visibility of the WHOLE interface: more liveliness, better info access, user enjoy

> Decision artifact · room `dept-visualization-own-the-visibi-431` (dept) · 2026-07-08T12:09:15.664259+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Lumen locks the living style guide to **5 core components** (buttons, cards, typography, inputs, nav) with **3 color variants** (light, dark, brand), **2 state variants** (default/hover), and **3 breakpoints** (mobile/tablet/desktop), all demoed in `/src/demo/`—no more.

**Plan:**
1. Document 5 core components with detailed specifications in `/docs/living-style-guide.md`.
2. Create interactive previews for these components in `/src/demo/`.
3. Establish 3 color variants (light, dark, brand) and ensure they are reflected in the examples.
4. Implement 2 state variants (default/hover) for all components in the demos.
5. Design the components to be responsive across 3 breakpoints (mobile/tablet/desktop).

**What changed:** The living style guide is structured to ensure maintainability while providing a robust foundation for the interface.
