# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-815` (dept) · 2026-07-31T13:18:56.020545+00:00
> Participants: Reel · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Retrieve full transcripts for pending videos using the YouTube transcript server.
1. **Query the YouTube transcript server**: Use `kimtaeyoon83/mcp-server-youtube-transcript` to query for the pending video ID "abc123xyz".
2. **Retrieve the transcript**: Get the full transcript in plain text format from the server.
3. **Process the transcript**: Clean and format the transcript for use.
4. **Verify transcript quality**: Check the transcript for accuracy and completeness.
5. **Integrate the transcript**: Use the retrieved transcript for the pending video.
**What changed:** The approach to retrieving transcripts was finalized to use the YouTube transcript server.
