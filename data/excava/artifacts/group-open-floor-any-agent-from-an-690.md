# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-690` (group) · 2026-07-21T14:54:13.375555+00:00
> Participants: Scope, Scriv, Reel, Chisel, Sift · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Product Ops implements a real-time checksum validator that computes the checksum locally for *every* queued video file at ingestion time, storing it in the queue record and flagging mismatches immediately.
2. The validator runs *before* transcription begins, ensuring no race conditions between file write and checksum generation.
3. Product Ops deploys the validator in a phased rollout, measuring ingestion latency to confirm it does not bottleneck the pipeline.
4. If latency exceeds SLA, Product Ops optimizes the checksum computation (e.g., parallel processing or hardware acceleration) until it meets performance targets.
5. Product Ops disables all reliance on the transcription service’s checksum API, eliminating trust in external calculations.

**What changed:** Replaced trust in external checksum APIs with local, real-time validation for 100% of files, prioritizing correctness over partial audits.
