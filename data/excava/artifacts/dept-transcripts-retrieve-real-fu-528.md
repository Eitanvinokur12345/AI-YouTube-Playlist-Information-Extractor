# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-528` (dept) · 2026-07-17T09:38:23.407724+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on video ID `dQw4w9WgXcQ` to fetch the full transcript.
2. Reel delivers the complete, timestamped transcript to Product Ops for review.
3. Product Ops validates the transcript for accuracy and completeness.
4. If approved, the transcript is archived in the pending videos database.
5. If rejected, Reel re-runs the tool with adjusted parameters (e.g., retry or alternative method).
6. Log the action and outcome in the project tracker for audit.

**What changed:** Tool execution and transcript delivery are now formally assigned to Reel with clear handoff to Product Ops.
