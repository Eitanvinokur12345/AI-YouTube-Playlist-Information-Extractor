# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-924` (dept) · 2026-07-31T18:30:22.678378+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a light theme with a dark accent for EXCAVA’s interface, validated by glare testing.

**Plan:**
1. Implement a light theme with WCAG 2.1 AA contrast ratios (min 4.5:1 for text, 3:1 for interactive elements).
2. Add a dark accent for interactive charts/nodes (e.g., deep blue or graphite) to mirror Manus’s polish.
3. Include a brightness slider (0-100%) for manual adjustment under glare conditions.
4. Conduct glare testing in bright rooms with 5+ users, measuring squinting/readability.
5. If glare impairs visibility, auto-adjust contrast or prompt theme toggle.
6. Document contrast ratios and test results in `/docs/theme-validation.md`.

**What changed:** Switched from dark theme to light theme with dark accent + brightness slider.
