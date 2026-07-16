# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-815` (war) · 2026-07-16T03:39:16.882246+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use a 7-day rolling average capped at 95% link coverage as the breach threshold, updated daily, with Product Ops owning the threshold definition and the system enforcing it.

**Plan:**
1. Implement a daily update system for measuring link coverage based on a 7-day rolling average.
2. Set a hard floor at 95% coverage to ensure visibility into recent failures.
3. Allow Product Ops to define the threshold parameters while retaining authority to make adjustments as necessary.
4. Monitor and report link coverage metrics regularly to catch spikes in broken links promptly.
5. Conduct periodic reviews to adapt the threshold based on evolving circumstances and user feedback.

**What changed:** The decision incorporates real-time responsiveness to broken links while maintaining a clear accountability structure for threshold definitions.
