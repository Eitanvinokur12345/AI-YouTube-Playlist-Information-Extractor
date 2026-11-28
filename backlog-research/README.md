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


### Checkpoint after batch 005

237 distinct frozen IDs reviewed and 42,043 open. The batch contains 40 spoken transcript interpretations and 17 publisher-linked IDs across five distinct upstream repositories. The Council guide resolves to a single Markdown skill with inline advisor roles. Three conflicting GitHub attributions remain in exceptions.json. The two skill packages have pinned raw originals, companion package links and document hashes. Prompt templates remain in the original documents, separate from the research findings. Package checks are static and do not certify runtime behavior or binary releases.

The comparison against main at 61fc8bba2e73579fb2b0eb9f48b4da71eef04394 found 1,781 distinct post-freeze IDs. Occurrence offsets in subsequent.json resolve at its own comparison revision.


### Checkpoint after batch 006

293 frozen IDs reviewed; 41,987 open. This batch reconciles host commands with publisher references, including changed command names and session/cloud differences. Eleven natural-language prompt shortcuts are assessed separately, with pointers to their stored text. Their status as executable commands is unverified. The gstack entries share one pinned package review; raw skill documents, invocation names and document digests are recorded separately. The two completed videos each have substantive speech. An unrelated title-only record stays open.

At source comparison c5123745a07c0eff5a08c8e6a2ccb8893cfe9474, the current inventory contains 1,781 post-freeze IDs. See subsequent.json for their occurrence revision.


### Checkpoint after batch 007

61 newly reviewed IDs: 42 frozen format descriptions, 17 versioned author abstracts and two extracted tool records traced from those papers to pinned publisher repositories. The format reviews use the stored descriptions and rebuild hints. They do not certify the original videos or count them as reviewed. Publisher reviews name runtime, data, integrity hashes and static-check limits. The PuMVR review independently checks row identifiers, image existence and gold answer positions across scripts.

The reviewed-ID union is 354 of 42,280, leaving 41,926 open. Main at 2c7c7eeb75b1ad9d434adee652bea07de7ac1fc4 is the verified batch 006 publication. The source inventory did not change since that comparison; subsequent.json retains 1,781 later IDs with locators at its recorded revision.

### Checkpoint after batch 008

Compared 712 quarantine entries with 672 deletion entries. The index identifies 670 exact one-to-one content matches at the freeze. Reviewed 75 distinct archived entries, including 12 prompt or interface text findings stored separately, and linked their 75 duplicate IDs. The remaining 595 pairs receive no completion credit from this mapping. Archive dispositions are preserved. Six publisher-linked IDs were reviewed across two pinned projects, including their source hashes, OS/runtime and data boundaries, and static-check limits.

The reviewed-ID union is 510 of 42,280, leaving 41,770 open. At fe7425da12e8718e346446b5e3af84c2ace941d8, the current inventory contains 1,842 subsequent IDs. No video was credited for reviewing extracted records.

### Checkpoint after batch 009

Read and analyzed 10 previously open video transcripts. Reviewed 43 distinct archived entries, including 30 prompt/text entries stored separately; 42 exact archival duplicates link to those findings. Four publisher IDs resolve to two pinned originals. Astral's original and license files contradict the ownership and licensing flags in the frozen uv tool row. The historical row is preserved.

Union of completed frozen IDs: 609 of 42,280, leaving 41,671 open. Title-only video cases remain separately recorded in exceptions.json. The intervening main commit changed only the ledger; subsequent.json retains 1,842 later IDs with their occurrence revision. No reviewed archive command was executed.

### Checkpoint after batch 010

Reviewed four spoken transcripts, 50 distinct archived entries and two publisher-linked Kronos IDs. Fifty exact archive duplicates point to the individual assessments. Prompt text has its own batch. The pinned inference example and predictor signature expose a reversed history slice and incompatible keywords in the extracted walkthrough. Publisher archive contents also distinguish a referenced CSV from a bundled dataset. Source and model code were inspected without execution.

The union contains 715 of 42,280 frozen IDs, with 41,565 open. Compared source inventory at 3d3261c6560c9cd53f42f48e4e184496ed9bc5f5; 1,867 later IDs currently present. Occurrence offsets in subsequent.json always resolve at its own comparison revision.
