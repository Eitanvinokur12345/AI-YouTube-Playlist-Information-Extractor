# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-966` (dept) · 2026-07-30T19:39:45.507504+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Verify the transcript contains real, complete content before proceeding.
3. Save the transcript in the designated repository under `/transcripts/` with the filename `how_to_build_a_resilient_team.md`.
4. Cross-check the transcript against the video’s metadata (title, duration) to ensure accuracy.
5. Notify the team via Slack (#transcripts) that the transcript is ready for review.
6. Archive the pending video entry in the tracking system as "Transcript Retrieved."

**What changed:** Transcript retrieval is now automated via the specified tool, replacing manual or partial methods.
