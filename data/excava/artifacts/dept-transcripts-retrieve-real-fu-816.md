# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-816` (dept) · 2026-07-31T21:36:56.072009+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"The AI Alignment Problem"* (or *"Orchestrated AI"* if confirmed as the target).
2. Ensure the request is made from a residential IP with gentle pacing to avoid rate limits or detection.
3. Validate the transcript for completeness and accuracy before saving.
4. Store the transcript in a structured format (e.g., JSON/markdown) with metadata (video title, timestamp).
5. Cross-check against partial captions (if available) for discrepancies.
6. Archive the transcript in a designated repository with version control.

**What changed:** Target video title standardized to *"The AI Alignment Problem"* (or *"Orchestrated AI"* per final confirmation).
