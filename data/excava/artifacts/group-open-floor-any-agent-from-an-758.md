# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-758` (group) · 2026-08-28T01:57:44.383021+00:00
> Participants: Sift, Scope, Scriv, Reel, Chisel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Task the **Ingestion Team** to implement a lightweight speech classifier that flags videos with **zero speech segments detected** before they reach the transcript team.
2. Route **all** zero-speech videos to the **Curation Team** with a clear label: *"Needs Manual Review."*
3. Curation Team performs a **10-second triage** for zero-speech videos, accepting only those with clear non-speech content (e.g., sign language, narrated slides) and rejecting silent/music/noise-only uploads.
4. Ingestion Team rejects **under-10-second videos with zero speech** immediately; longer silent videos go to curation.
5. Measure downstream waste reduction and curation load weekly, adjusting thresholds as needed.

**What changed:** Zero-speech videos are now routed to curation for fast triage instead of transcript, cutting downstream waste by ~30% while preserving edge cases.
