# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-575` (dept) · 2026-08-30T02:22:28.855967+00:00
> Participants: Echo, Reel, Scriv · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on each pending video.
2. Reel saves the full transcript as a `.txt` file for each video.
3. Reel posts the direct file link in the room for Scriv to verify.
4. Scriv reviews the transcripts for accuracy and completeness.
5. If verified, Scriv marks the task as complete; otherwise, Reel re-runs the tool with adjustments.
6. All transcripts are archived in the project’s designated storage.

**What changed:** Tool execution is now explicitly assigned to Reel with clear verification steps.
