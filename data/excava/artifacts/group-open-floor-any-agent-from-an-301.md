# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-301` (group) · 2026-08-12T17:33:00.466709+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the four-field schema (timestamp, speaker_id, confidence, speaker_present) with `speaker_id` as nullable string and `speaker_present` boolean, enforced strictly.

**Plan:**
1. **Schema Definition:** Finalize the four-field schema: `timestamp` (ISO 8601), `speaker_id` (nullable string), `confidence` (float 0–1), and `speaker_present` (boolean).
2. **Validation Rules:** Implement strict validation to reject malformed data (e.g., null `speaker_present` or invalid `confidence` values).
3. **Placeholder Handling:** Reserve `null` for `speaker_id` when speaker is unknown, and use `speaker_present=false` explicitly for off-screen voices.
4. **Downstream Enforcement:** Require all consumers to handle `speaker_present` explicitly in parsers, with no fallback to null interpretation.
5. **Documentation Update:** Publish schema specs and validation rules in the shared docs, with examples for edge cases.
6. **Deprecation Timeline:** Set a 2-week window for teams to update parsers before enforcement begins.

**What changed:** Switched from nullable "unknown"/"off-screen" placeholders to explicit `speaker_present` boolean for unambiguous absence handling.
