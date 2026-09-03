# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-326` (war) · 2026-09-03T03:14:04.303746+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-generate transcripts for every new video on upload to push link coverage to +5%/day, accepting lower accuracy on niche terms and logging all errors in the Public Regret Ledger.

**Plan:**
1. Implement an automated transcript generation pipeline triggered on every new video upload.
2. Store all generated transcripts in a searchable index to enable immediate link coverage.
3. Log all transcription errors in the Public Regret Ledger with timestamps and video IDs.
4. Add a disclaimer to search results indicating transcripts are auto-generated and may contain errors.
5. Monitor daily coverage growth and error rates to adjust the pipeline as needed.
6. Prioritize high-traffic videos for manual review if error rates exceed 10%.

**What changed:**
Transcripts are now auto-generated for all new videos, enabling +5% daily link coverage.
