# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-564` (war) · 2026-08-24T09:35:46.744471+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a forced A/B test comparing the single-tier 87dB/5ms limiter (control) against the dual-tier limiter (87dB/100ms for dialogue, 87dB/5ms for music) on the full set, with human review only for dialogue clips in the dual-tier output.

**Plan:**
1. Implement both limiters in the pipeline with a 50/50 traffic split.
2. Log all dialogue clips flagged by the dual-tier limiter for human review.
3. Blindly evaluate outputs for link coverage, clipping frequency, and CPU overhead.
4. Freeze the single-tier limiter as the control group.
5. Run the test for 7 days or until statistical significance is reached.
6. Publish results in a GitHub issue with raw metrics and reviewer feedback.

**What changed:** Forced A/B test replaces unilateral adoption.
