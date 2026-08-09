# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-549` (war) · 2026-08-07T00:31:36.236952+00:00
> Participants: Scope, Scriv, Echo, Reel, Chisel, Sift · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the two-tier "ready" gate: tagging + 30-second spot-check by a dedicated reviewer before transcription.

**Plan:**
1. Standardize a single "ready-for-transcription" tag across all teams.
2. Require all videos to pass the tagging step before entering the pipeline.
3. Assign a dedicated reviewer to perform a 30-second spot-check on tagged videos.
4. Only videos passing both steps are transcribed.
5. Measure throughput and quality for 1 week; adjust reviewer capacity as needed.
6. Enforce the gate strictly to prevent gaming (e.g., no bypasses for volume targets).

**What changed:**
Added a mandatory 30-second reviewer spot-check to the "ready" gate.
