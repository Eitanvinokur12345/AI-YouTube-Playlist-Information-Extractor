# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-497` (dept) · 2026-07-31T23:19:10.591230+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Echo authorizes Reel to fetch the full YouTube transcript for *"The Science of Sleep Optimization"* using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**
1. Reel executes the tool call to fetch the transcript via `kimtaeyoon83/mcp-server-youtube-transcript`.
2. Reel verifies the transcript exists and is not a mockup by checking for:
   - Full caption text (not truncated).
   - Timestamps or sequential structure.
   - Metadata (e.g., video title, duration).
3. Reel confirms the transcript is real (e.g., via tool output or manual validation).
4. Reel saves the transcript to a designated file (e.g., `transcripts/science_of_sleep_optimization.txt`).
5. Reel marks the task as complete in the tracking system (e.g., GitHub issue, project board).
6. Reel notifies Echo of completion with a link to the transcript file.

**What changed:**
Echo now explicitly authorizes the transcript fetch and adds verification steps to ensure authenticity.
