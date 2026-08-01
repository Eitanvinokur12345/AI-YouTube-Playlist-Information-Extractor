# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-610` (dept) · 2026-07-31T16:52:32.921910+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching the full YouTube transcript for *"How to Build a Resilient Team"* using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**
1. Reel executes the tool call to retrieve the raw, timestamped transcript.
2. Reel delivers the full transcript to the lead for review.
3. Lead reviews the transcript for accuracy and completeness.
4. If gaps or errors are found, Reel re-runs the tool with adjusted parameters (e.g., language, segment length).
5. Final transcript is saved in the designated repository with metadata (video title, URL, fetch timestamp).
6. Notify the team via Slack/email once the transcript is validated and stored.

**What changed:**
No changes—proceeding with the original plan.
