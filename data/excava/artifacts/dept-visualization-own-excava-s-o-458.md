# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-458` (dept) · 2026-07-28T17:54:04.780017+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with system-preference-based theme by default, with a pre-set fixed theme option at install.

**Plan:**
1. Implement theme detection on first load to match system preference (dark/light).
2. Add an install-time prompt: "Use system theme or set a fixed theme?" with options.
3. Store user choice in local storage/config file for persistence.
4. Remove manual toggle UI post-install to simplify UX.
5. Track telemetry on theme changes (if any) to validate adoption.
6. Optimize first-load delay for auto-switching to under 100ms.

**What changed:**
Default theme now follows system preference with a one-time install choice override.
