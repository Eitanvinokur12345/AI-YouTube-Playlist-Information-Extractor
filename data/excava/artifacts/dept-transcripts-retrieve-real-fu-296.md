# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-296` (dept) · 2026-07-30T19:11:22.623654+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Save the output to `transcripts-w1` for verification.
3. Validate the transcript for completeness and accuracy (e.g., no missing segments, correct timestamps).
4. If errors are found, re-run the tool with adjusted parameters (e.g., `gentle pacing` or `residential IP` flags).
5. Archive the finalized transcript in the designated repository.
6. Notify stakeholders of completion via GitHub issue or Slack.

**What changed:** Transcript retrieval is now explicitly assigned to the tool with output verification steps.
