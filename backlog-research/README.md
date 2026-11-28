# Frozen research ledger

Membership is pinned to commit `2ce91d7becac95063a9842fd01cf0998b1ae16ea`. Each line in `scope.jsonl.gz` is a JSON pair of stable subject ID and occurrence locators. Read with Python's gzip module or zcat. Counts are in scope-summary.json. These are independently reviewable subjects, including configured sources, archived rows and discovery queries, not a count of unique products. An element and a video about it require different evidence. A single publisher review can support multiple records when identity is established.

Locators resolve within the frozen tree: e.g. `social_intake/items/8` means array index 8 in data/social_intake.json, `processed/ID.json` is under data, and `../config` means root config.json. The same ID retains its acquisition lanes. YouTube IDs, GitHub owner/repo and arXiv work IDs normalize across supported URL variants. Other URLs are preserved conservatively. Case, aliases, embedded links, overlapping descriptions and non-identical mirrors can require manual reconciliation. A shared slug can have several source rows: inspect all before closing it. Frozen source bytes remain in Git.

Each batch contains closed research IDs and their findings. For the current balance, take the union of batch IDs, intersect with scope, then subtract from the frozen IDs. Read exceptions separately; these remain open. Existing catalog stage, verified links and mining flags are leads to prior evidence, not a research completion mark. Check the frozen catalog and original_sources matches before repeating work. Preserve archive status. Group later discoveries in subsequent.json, which records the exact main revision last compared. Never grow scope with later arrivals. Use a separate evidence reference to update the status of a previously unreadable item.

Batch 001 reviews 11 video transcripts, 11 publisher documents and 17 extracted prompt records. Prompt bodies stay in the frozen prompts.json at the supplied offsets. Video interpretations do not imply that linked templates were recovered. Publisher review covers identity, practical use, runtime, data handling and static indicators on named files. Package-wide antivirus clearance is outstanding. Read the two skill documents via raw URLs and fetch their companion folders at the same revision when needed. No upstream code was executed.

Resume with unconfirmed videos that have actual text and intake URLs absent from mined_state. For short caption-only or intro-only clips, try existing visual/acquisition lanes. For exceptions with no direct record, inspect the listed occurrences for alternate evidence. Verify a saved finding on main before counting it. Final reconciliation also requires verifying scope coverage against remaining historical stores and checking unresolved identity/scan exceptions.

### Checkpoint after batch 003

At source snapshot `090788071c8f316db9a57448f9e5d50a67191b6b`, the 1,762 post-freeze IDs matched the key set already in subsequent.json. Its occurrence offsets still refer to its own compared_main revision.

The union of batches 001–003 contains 134 distinct frozen IDs (42,146 open). Batch 003 adds 30 prompt records, six transcript interpretations, one publisher problem statement and 14 publisher-linked IDs. Those 14 represent eight original reviews: five skill packages and three connector repositories. Alias rows link to the full review. Stored prompt bodies remain in the frozen prompts file. Descriptions of missing prompt originals and assistant output are classified as extracted records only.

The Manim connector review includes a source-level finding about directory cleanup and concurrent renders. Each of the five skill documents matched its frozen SHA-256. Package checks record scoped static indicators; signature results from the frozen catalog apply only to the named skill documents. The recovered introduction for video 7qjpP7nDc0c is tracked in exceptions.json; only its linked publisher problem was closed.


### Checkpoint after batch 004

The frozen ledger contains 180 reviewed IDs and 42,100 open IDs. This batch covers 20 publisher feeds, 19 versioned author abstracts, five transcripts and two catalog IDs sharing one Bilibili connector review. Feed evidence describes the observed endpoint and sample entries. It does not close the linked articles. Paper findings are explicitly limited to the abstract. Two unreadable feed endpoints remain in exceptions.json. No fetched connector code was executed. The subsequent queue holds 1,764 IDs as of its recorded comparison revision.
