# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-285` (dept) · 2026-07-30T18:55:55.797409+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"* via the YouTube transcript API.
2. Verify the transcript exists and contains real speaker attributions before proceeding.
3. If the transcript is confirmed, save it as a `.txt` or `.md` file with the video title as the filename.
4. Cross-check the transcript length and content against the video duration to ensure completeness.
5. If the transcript is incomplete or missing, attempt an alternative method (e.g., manual extraction or third-party tool).
6. Mark the task as complete only after confirming the transcript is real and full.

**What changed:** The task is now explicitly tied to a single video title and includes verification steps.
