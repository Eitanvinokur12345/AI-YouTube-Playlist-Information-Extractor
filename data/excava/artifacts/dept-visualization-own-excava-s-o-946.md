# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-946` (dept) · 2026-07-27T06:21:02.498184+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to system theme on first load, cache the last manual toggle per user, and expose a persistent theme toggle in settings.

**Plan:**
1. Implement system theme detection on first load (light/dark).
2. Cache the user’s last manual theme toggle in local storage.
3. Add a persistent theme toggle in settings (visible in all views).
4. A/B test task completion speed and error rates between cached vs. system defaults.
5. Monitor user habituation metrics (toggle frequency, duration in each theme).
6. Iterate based on A/B results and user feedback.

**What changed:** Defaults now respect system preference while caching user overrides for consistency.
