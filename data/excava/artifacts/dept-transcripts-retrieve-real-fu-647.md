# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-647` (dept) · 2026-07-29T15:23:32.507176+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Query the YouTube transcript server via residential IP to retrieve full transcripts for pending videos.

**Plan:**
1. Use the YouTube transcript server API to initiate a query.
2. Specify the user credentials for accessing the required endpoint.
3. Ensure the request is routed through a residential IP.
4. Retrieve and store the raw text of transcripts for all pending videos.
5. Review the retrieved transcripts for accuracy and completeness.

**What changed:** The final decision solidified the plan to utilize a specific endpoint for transcript retrieval instead of general documentation.
