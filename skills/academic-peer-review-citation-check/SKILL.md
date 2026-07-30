---
name: academic-peer-review-citation-check
description: "Use when producing academic or research writeups that need their citations and factual claims cross-checked by independent reviewer passes before being trusted."
---

# Academic Research Peer-Review (Multi-Agent Citation Check)

## Overview
Runs a research draft through additional agent passes that act as independent peer reviewers,
specifically hunting for fabricated or unverifiable citations and unsupported claims.

## Key Techniques
- Separate the drafting pass from the review pass so the reviewer isn't anchored to the writer's framing.
- Have the reviewer check every citation against a real, findable source before it is trusted.
- Flag (don't silently fix) anything that can't be verified, so a human makes the final call.

## How to Apply
1. Produce the research draft as normal.
2. Run a second, independent pass whose only job is peer review: verify each citation resolves to a real source and each claim is supported.
3. Collect flagged citations/claims and resolve or remove them before publishing.

## Examples
Used to add credibility to AI-assisted research and academic writing by catching fake citations
before a document is shared or submitted.

## Source
Extracted from: [Claude skills drive faster AI workflows with search, design](https://www.youtube.com/watch?v=qcmSxb__Mj8)
Channel: Alice Reed | Crypto Day & Night
