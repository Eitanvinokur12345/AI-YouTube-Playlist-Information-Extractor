# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-599` (dept) · 2026-07-27T05:09:16.789298+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to system theme on first load, with a one-time prompt offering a high-contrast theme if system contrast fails WCAG 2.1 AA.

**Plan:**
1. On first load, detect the system theme (light/dark) and apply it by default.
2. Run a contrast check against WCAG 2.1 AA standards for the detected theme.
3. If contrast fails, display a one-time prompt: *"High contrast improves readability. Enable now?"* with "Yes" and "No" options.
4. If "Yes" is selected, switch to a high-contrast theme and store the preference.
5. Provide a persistent toggle in settings to switch between system theme, high-contrast theme, and original theme.
6. Ensure all themes meet WCAG 2.1 AA contrast ratios for text and interactive elements.

**What changed:**
Defaulted to system theme with a one-time high-contrast fallback prompt for accessibility.
