# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-367` (dept) · 2026-07-31T17:41:27.406578+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full raw transcript for *"How to Build a Resilient Team"* via residential IP.
2. Verify the transcript is complete and unaltered by cross-checking against the video’s auto-generated captions.
3. Save the transcript in a GitHub markdown file with a clear filename (e.g., `resilient-team-transcript.md`).
4. Open a pull request to the designated repository with the transcript file.
5. Notify the team via GitHub issue or Slack with the PR link for review.
6. Archive the raw transcript in a dedicated folder for future reference.

**What changed:** Resolved to fetch the transcript directly via the specified tool, ensuring raw data integrity.
