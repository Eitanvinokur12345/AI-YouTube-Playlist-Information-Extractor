# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-396` (group) · 2026-08-21T03:32:23.728641+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a **real-time, Legal-flagged triage queue** for top 3 harm-severity false negatives, with Engineering pre-building a "slur mutation tracker" to flag emerging patterns.

**Plan:**
1. **Legal** designates top 3 harm-severity false negatives within 5 minutes of detection, triggering immediate classifier updates.
2. **Engineering** pre-builds a "slur mutation tracker" to proactively flag new slur patterns before they propagate.
3. **Legal** reviews only the worst systemic harms from the tracker, while Engineering validates patterns and prevents noise drowning.
4. **Engineering** owns the retrain threshold (precision <90%) and implements automated daily triage of top 10 unique false negatives as backup.
5. **Scope** and **Reel** co-own the real-time queue implementation, with **Chisel** and **Sift** providing feedback on systemic misses.

**What changed:**
Combined real-time Legal triage with Engineering’s proactive mutation tracking to balance speed and systemic insight.
