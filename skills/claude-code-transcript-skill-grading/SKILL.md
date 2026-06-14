---
name: claude-code-transcript-skill-grading
description: "Use when you want to automatically improve Claude Code skills overnight by having one agent grade session transcripts and rewrite skill files based on observed failures."
---

# Auto-Improving Agent Skills via Transcript Grading

## Overview
Every Claude Code session stores a complete JSONL transcript in `~/.claude/` capturing every tool call, response, and thought. This is a complete behavioral record that almost nobody uses — but it's the foundation for self-improving AI coding setups.

## Key Techniques
- **Transcript mining**: Read JSONL session logs to see exactly how a skill influenced agent behavior and whether instructions were followed
- **Auto-research grading loop**: One agent reads a transcript, grades skill adherence, identifies failures, and rewrites the skill
- **Overnight improvement**: Schedule the grading loop to run while you sleep so skills improve automatically

## How to Apply
1. Identify a skill you want to improve (e.g., a SKILL.md in `~/.claude/skills/`)
2. Find the most recent session transcript in `~/.claude/` that invoked the skill
3. Create a grading agent with this system prompt:
   - "Read the attached JSONL transcript. Identify all tool calls where skill X was active. Grade each on: (a) did the agent follow the skill's instructions? (b) what went wrong? (c) rewrite the skill to prevent these failures."
4. Apply the rewritten skill file
5. Run the grading agent again on the next session to verify improvement

## Examples
- Skill says "always write tests before implementation" — grading transcript reveals agent skips tests for small functions → rewrite skill to specify minimum test requirements
- Skill instructs "use TypeScript types everywhere" — transcript shows agent using `any` type → rewrite skill to explicitly prohibit `any` with examples of correct alternatives

## Source
Extracted from: [My Claude Code improves its own skills overnight: here's how](https://www.youtube.com/watch?v=tOJz4jTrIxU)
Channel: James Goldbach
