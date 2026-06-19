---
name: cross-harness-skill-porting
description: "Use when you need to share AI agent skills and configuration between Claude Code and OpenAI Codex without maintaining separate copies."
---

# Cross-Harness Skill Porting

## Overview
This skill enables a single canonical agent configuration to work across both Claude Code and OpenAI Codex harnesses. Skills use identical YAML frontmatter; only the storage folder differs (.claude/ vs .agents/).

## Key Techniques
- Use agents.md as the single source of truth for agent instructions, imported into CLAUDE.md
- Store skills in `.agents/` for Codex and `.claude/` for Claude Code with the same YAML frontmatter
- Use the `/duplicate` command to port any skill from one harness to the other in one operation
- Keep shared memory in plain markdown files and an external knowledge base both agents can read

## How to Apply
1. Create `agents.md` with canonical agent instructions
2. Add `@agents.md` import to `CLAUDE.md`
3. Write skills with standard YAML frontmatter (`name`, `description`, `triggers`)
4. Place skills in `.claude/` for Claude Code sessions, `.agents/` for Codex
5. Run `/duplicate <skill-name>` to copy a skill to the other harness automatically

## Examples
- Skill created for Claude Code → `/duplicate my-skill` → available instantly in Codex
- Shared memory file updated by either agent is visible to both without extra sync

## Source
Extracted from: [Share agent config between Codex and Claude Code](https://www.youtube.com/watch?v=nuNf4HON3U0)
Channel: James Goldbach
