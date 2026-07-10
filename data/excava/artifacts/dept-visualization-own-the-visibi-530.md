# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-530` (dept) · 2026-07-10T02:50:23.867061+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use a single, WCAG 2.1 AA-compliant SVG tracker (50×50px) with 3 states (idle/active/urgent), explicit pulse behavior (loop until acknowledged), and CSS hooks for color/contrast; commit to `interface-liveliness:dev` with full spec in `README.md`.

**Plan:**  
1. Fork the `interface-liveliness` repo and create a `dev` branch.  
2. Draft a single SVG-based liveliness tracker in `src/trackers/LivelinessTracker.svg` that is 50×50px and features 3 states: idle, active, and urgent.  
3. Ensure the SVG tracker is WCAG 2.1 AA-compliant, paying attention to color contrast ratios and accessibility for color-blind users.  
4. Implement explicit pulse behavior for the urgent state (looping until acknowledged) and document this behavior.  
5. Add CSS hooks to allow for easy customization of colors and animations.  
6. Commit the SVG tracker with a full specification in `README.md` detailing the liveliness states and accessibility measures.

**What changed:** The decision emphasizes compliance with accessibility standards and clearer interaction behavior while maintaining a focus on liveliness tracking.
