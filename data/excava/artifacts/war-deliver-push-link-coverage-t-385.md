# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-385` (war) · 2026-08-09T11:34:40.420666+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Pre-filter pending videos to maximize coverage growth while respecting quota limits.

**Plan:**
1. Pre-filter pending videos: skip those with existing transcripts or low engagement (e.g., <100 views).
2. Run `kimtaeyoon83/mcp-server-youtube-transcript` only on the filtered set to avoid quota waste.
3. Batch submissions to stay under Luma’s 100 pulls/day cap.
4. Prioritize high-impact videos (e.g., top 20% by engagement) for transcript generation.
5. Log skipped videos for manual review if coverage stalls.
6. Monitor daily coverage growth and adjust filtering thresholds weekly.

**What changed:** Switched from bulk raw transcripts to pre-filtered, quota-aware execution.
