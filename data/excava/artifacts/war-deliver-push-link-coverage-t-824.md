# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-824` (war) · 2026-07-10T02:26:47.312591+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Replay risk-weighted traffic to identify real blast radius and target coverage gaps effectively.

**Plan:**
1. Capture a 24-hour traffic dump from the API gateway (`/var/log/nginx/access.log`).
2. Filter the dump to select high-complexity and high-impact endpoints using cyclomatic complexity metrics.
3. Implement a traffic replay script that tests these selected endpoints against staging environments.
4. Inject poison-pill scenarios during the replay to reveal hidden failures and weaknesses.
5. Analyze the results to identify coverage gaps in the relevant code paths.
6. Prioritize testing and increasing coverage specifically for those identified gaps to ensure safety.

**What changed:** The focus shifted from optimizing based on static metrics to prioritizing risk during the coverage enhancement process.
