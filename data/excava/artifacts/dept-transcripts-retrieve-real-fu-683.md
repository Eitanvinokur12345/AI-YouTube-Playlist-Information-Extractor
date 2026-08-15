# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-683` (dept) · 2026-08-15T06:43:34.318405+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID `eA9Zf` via a residential IP with gentle pacing.
2. Validate the transcript for completeness and accuracy against the pending video.
3. Save the retrieved transcript in a structured format (e.g., JSON or TXT) for downstream analysis.
4. Cross-reference the transcript with any existing partial captions to ensure consistency.
5. Document the retrieval process (timestamp, method, IP used) for reproducibility.
6. Notify stakeholders once the transcript is confirmed and stored.

**What changed:** Decision to proceed with the specified tool and method for transcript retrieval.
