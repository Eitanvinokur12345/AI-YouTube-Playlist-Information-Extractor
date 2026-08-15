# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-680` (dept) · 2026-08-15T06:38:04.733786+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching full transcripts using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**
1. Re-run kimtaeyoon83/mcp-server-youtube-transcript on pending videos.
2. Output full transcripts/captions to Scriv for format confirmation.
3. Verify output matches department’s "real full transcripts/captions" requirements.
4. If format is correct, proceed with processing; if not, adjust tool settings.
5. Confirm completion with Scriv before finalizing.
6. Archive raw outputs for audit.

**What changed:** Re-ran tool and routed outputs to Scriv for validation.
