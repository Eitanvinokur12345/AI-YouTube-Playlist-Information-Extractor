---
name: research-skill
description: "Use when Claude Code needs to remember research findings across sessions on the same project instead of re-researching from scratch every time the context is wiped."
---

# research-skill

## Overview
A persistent, project-scoped knowledge base for Claude Code (and Codex) that keeps research
findings available across sessions, even after the conversation context is cleared or compacted.

## Key Techniques
- Store findings in a project-scoped store rather than only in the live conversation context.
- Support both quick and deep research depths depending on how much time/budget you want to
  spend on a given question.
- Run a contrarian pass to check findings for source-independence rather than accepting the
  first source found.

## How to Apply
1. Clone the skill into your Claude Code skills folder.
2. Use it whenever starting research on a project so findings are written to persistent
   storage instead of only living in the current chat's context.
3. On later sessions (even months later), the same project's prior findings are still
   available to Claude without re-researching.
4. Pair with a deeper research-pipeline skill (e.g. claude-deep-research-skill) when a finding
   needs full sourcing and validation, not just quick notes.

## Examples
The source video frames it as fixing Claude's memory: "Research it did in March is still
there in July" once findings are written through research-skill instead of staying only in
a since-cleared conversation.

## Source
Extracted from: [CLAUDE FORGETS EVERYTHING. THESE TWO FIX IT](https://www.youtube.com/watch?v=kqEToneO43g)
Channel: Dubibubi
Repo: hec-ovi/research-skill
