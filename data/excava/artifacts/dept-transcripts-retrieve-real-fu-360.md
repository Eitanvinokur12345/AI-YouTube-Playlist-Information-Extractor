# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-360` (dept) · 2026-07-31T03:59:37.873632+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) for *"How to Build a Resilient Team"* using residential IP and gentle pacing.
2. Retrieve full transcripts for all pending video IDs via the same server, residential IP, and gentle pacing.
3. Output raw captions as artifacts for the lead to verify and attach.
4. Ensure transcripts are stored in a structured format (e.g., `.txt` or `.json`) for easy access.
5. Validate transcript completeness and accuracy before final submission.
6. Notify the lead upon completion for review and attachment.

**What changed:** Expanded scope to include all pending video IDs alongside the specific title query.
