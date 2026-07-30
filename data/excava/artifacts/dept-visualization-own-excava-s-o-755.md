# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-755` (dept) · 2026-07-30T20:29:43.051848+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a system-syncing dark/light toggle by default, but force dark mode for 90% of users and light for 10%—measure export clarity and session satisfaction in a live A/B test.

**Plan:**
1. Implement a system-syncing dark/light toggle in EXCAVA’s interface (default: system preference).
2. Force dark mode for 90% of new users; light mode for 10% (randomized).
3. Log export clarity metrics (e.g., contrast, readability in daylight) and session satisfaction scores.
4. Run A/B test for 30 days, comparing export success rates and user feedback.
5. After analysis, hardcode the winning mode (toggle or single) based on data.
6. Document findings in EXCAVA’s changelog and notify users of the change.

**What changed:**
Added a forced A/B split (90% dark, 10% light) with toggle support to validate export clarity and session satisfaction.
