---
name: claude-academic-peer-review-skill
description: "Use when you need to validate an academic or research write-up for accuracy and check for fabricated citations before trusting or publishing it."
---

# Claude Academic Research Peer-Review Skill

## Overview
A Claude research skill that runs multiple agent "peer reviews" over a piece of academic
writing to check accuracy and catch fabricated (hallucinated) citations.

## Key Techniques
- Run several independent agent reviewers over the same draft.
- Have each reviewer specifically check citations against real sources.
- Aggregate reviewer findings to flag accuracy issues before the draft is trusted.

## How to Apply
1. Produce or gather the research draft/citations to be checked.
2. Run the multi-agent peer-review pass over it.
3. Treat any citation flagged as unverifiable/fake as a hard blocker before publishing.

## Examples
Described in the source video as "academic research skills with multiple agent peer reviews
to ensure accuracy and catch fake citations."

## Source
Extracted from: [Claude skills drive faster AI workflows with search, design](https://www.youtube.com/watch?v=qcmSxb__Mj8)
Channel: Alice Reed | Crypto Day & Night
