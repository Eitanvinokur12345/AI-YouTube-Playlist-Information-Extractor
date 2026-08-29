# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-297` (war) · 2026-08-29T07:24:09.450167+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a **7-day rolling A/B on 120k clips**, swapping 20% weekly, with a **5-second minimum + 20% semantic relevance** gate.

**Plan:**
1. Deploy 7-day rolling A/B test with 20% weekly clip swaps (120k total).
2. Enforce 5-second minimum clip duration + 20% semantic relevance filter.
3. Mandate full traceability (source linking, audits) for all clips in the test pool.
4. Monitor noise levels weekly; adjust holdout window if spikes exceed 15% variance.
5. Sift to deliver transcripts-checker artifacts; Scriv to validate semantic relevance.
6. Target +5% link coverage/day toward 100% with rolling cadence.

**What changed:**
Replaced fixed 14-day A/B with rolling 7-day window + relevance/semantic gates to balance speed and noise.
