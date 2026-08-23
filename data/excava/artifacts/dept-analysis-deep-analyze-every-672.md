# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-672` (dept) · 2026-08-23T01:15:45.885414+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Chisel’s audio-based approach is infeasible; Marrow’s transcript-driven analysis is adopted.

**Plan:**
1. **Extract full transcript** from the earnings call source (audio/video file or raw text).
2. **Run BloodHound-MCP** on the transcript to:
   - Identify all speaker turns with timestamps.
   - Analyze sentiment shifts per segment.
   - Generate a structured report (JSON/CSV) with speaker labels, timestamps, and sentiment scores.
3. **Validate transcript accuracy** by cross-checking against the original audio (if available) for critical segments.
4. **Flag potential compliance issues** (e.g., loud segments, abrupt tone shifts) for human review.
5. **Deliver report** to downstream teams with clear action items (e.g., "Trim segment X at timestamp Y").
6. **Archive raw data** and report for auditability.

**What changed:** Switched from audio decibel analysis to transcript-based speaker/sentiment extraction due to BloodHound-MCP’s text-only limitation.
