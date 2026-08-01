# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-236` (dept) · 2026-07-31T21:00:53.045944+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for *"Orchestrated AI"*.
2. Reel verifies the transcript file exists and matches the expected format (e.g., `.txt` or `.json`).
3. Reel marks the task as complete in the pending video queue.
4. Reel logs the transcript retrieval in the project tracking system.
5. Reel notifies the team via Slack/email with the transcript file link.
6. Reel archives the raw transcript in the designated storage (e.g., Google Drive or GitHub).

**What changed:** The full, unaltered transcript for *"Orchestrated AI"* is now retrieved and verified.
