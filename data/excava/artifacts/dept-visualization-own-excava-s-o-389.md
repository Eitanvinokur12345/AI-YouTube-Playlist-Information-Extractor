# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-389` (dept) · 2026-07-27T01:38:51.470663+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. On first load, detect and apply the user’s OS theme preference as the default.
2. Trigger a one-time modal prompt: *“High contrast improves readability. Enable now?”* with “Yes” and “No” buttons.
3. If accepted, set high-contrast mode and store the choice; if declined or ignored, retain the OS theme.
4. Do not persist a theme toggle in the interface—only the one-time prompt appears.
5. Ensure high-contrast mode meets WCAG AA standards and respects system color schemes.
6. Log the user’s choice for analytics (optional) but never re-prompt unless reset.

**What changed:** Defaults to system theme with a one-time high-contrast override prompt; no persistent toggle.
