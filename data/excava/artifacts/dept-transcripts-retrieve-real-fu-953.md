# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-953` (dept) · 2026-07-14T23:06:13.808025+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool for video ID `"UC-9bX9X8X9X9X"` to fetch the full transcript.
2. If the transcript is missing or incomplete, re-check with the same ID `"UC-9bX9X8X9X9X"` to confirm availability.
3. If still missing, escalate to manual review or alternative methods (e.g., YouTube API fallback).
4. Validate the retrieved transcript for accuracy and completeness.
5. Store the verified transcript in the designated repository or system.
6. Log the outcome (success/failure) for tracking.

**What changed:** Tool query prioritized with ID `"UC-9bX9X8X9X9X"` and fallback checks added.
