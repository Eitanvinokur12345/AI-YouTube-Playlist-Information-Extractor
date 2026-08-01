# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-150` (dept) · 2026-07-30T21:34:58.539729+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Fetch the full transcript for *"How to Build a Resilient Team"* using the YouTube transcript tool.

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the raw transcript text for *"How to Build a Resilient Team"*.
2. Output the transcript in GitHub markdown format.
3. Verify the transcript is complete and matches the video's content.
4. Save the transcript as a `.md` file with the video title as the filename.
5. Confirm the transcript is accessible and properly formatted.

**What changed:**
The action shifted from fetching *"Orchestrated AI"* to *"How to Build a Resilient Team"* based on Echo's directive.
