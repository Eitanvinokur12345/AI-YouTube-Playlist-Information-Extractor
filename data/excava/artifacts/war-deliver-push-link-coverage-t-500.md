# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-500` (war) · 2026-08-08T21:02:16.300473+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Use the kimtaeyoon83/mcp-server-youtube-transcript tool now for pending videos, then switch to YouTube’s official API only if the wrapper fails.

**Plan:**
1. Deploy the kimtaeyoon83/mcp-server-youtube-transcript tool to extract transcripts from all pending video links immediately.
2. Monitor tool reliability and coverage rate daily to ensure +5%/day progress toward 100%.
3. If the wrapper fails (e.g., breaks or misses targets for 48+ hours), escalate to YouTube’s official API with quota management.
4. Set up API keys and quota tracking for the official YouTube API as a fallback pipeline.
5. Document tool failures and API setup steps in the project’s runbook for future reference.
6. Re-evaluate wrapper performance weekly; if stable, continue using it as the primary method.

**What changed:** Prioritized immediate transcript extraction via community wrapper, with official API as a contingency.
