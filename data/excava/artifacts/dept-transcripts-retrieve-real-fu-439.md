# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-439` (dept) · 2026-07-29T07:23:18.565788+00:00
> Participants: Reel · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Retrieve full transcripts for pending videos using the YouTube transcript server.
1. **Query the YouTube transcript server**: Use `kimtaeyoon83/mcp-server-youtube-transcript` to retrieve the transcript for video ID "abc123xyz".
2. **Retrieve the full transcript**: Obtain the full-text transcript from the server for review.
3. **Review the transcript**: Examine the transcript for accuracy and completeness.
4. **Process the transcript**: Clean and format the transcript for further use.
5. **Store the transcript**: Save the transcript for future reference and potential updates.
**What changed:** The approach to retrieving transcripts shifted to utilizing the YouTube transcript server for efficient data collection.
