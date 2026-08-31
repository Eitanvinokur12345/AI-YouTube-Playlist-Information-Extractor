# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-695` (war) · 2026-08-31T16:01:27.724138+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 48-hour parallel A/B test on 10k clips comparing Whisper batch vs. Deepgram real-time.
2. Measure transcript quality (error rate) and cost per minute for both tools.
3. Scriv owns the test setup and delivers results by EOD Friday.
4. If Deepgram meets quality and cost targets, adopt it for real-time transcription.
5. If Whisper batch meets targets, proceed with batch processing for the A/B test.
6. Proceed with the winning tool to push link coverage toward 100% at +5%/day.

**What changed:** Switched from a 14-day fixed A/B test to a 48-hour parallel test to balance speed and tool lock-in risk.
