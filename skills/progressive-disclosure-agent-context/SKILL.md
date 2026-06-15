---
name: progressive-disclosure-agent-context
description: "Use when structuring a coding agent's context to give it access to many tools without flooding the context window — build a CLAUDE.md trunk file that auto-loads, then reference skills and tools as branches loaded on demand."
---

# Progressive Disclosure Context Engineering for Coding Agents

## Overview
A coding agent is simply an LLM with a context window; anything outside that window doesn't exist to it. Progressive disclosure structures your agent's context as a tree: a CLAUDE.md or agents.md trunk file auto-loads every session, then points to skills, scripts, MCP tools, and workflows as branches the agent only loads when the task needs them.

## Key Techniques
- Create a CLAUDE.md (or agents.md) trunk file as the single auto-loaded root for every agent session
- Reference skills, scripts, MCP tools, and workflows as branch pointers rather than embedding them in the trunk
- Let the agent follow breadcrumbs from trunk to leaf — loading only what the current task actually requires
- Keep the trunk lean: high-level instructions and pointers only; depth lives in the branches

## How to Apply
1. Create `CLAUDE.md` in your project root with: global instructions, a list of available skills/tools (with file paths), and when to use each
2. Store individual skills, scripts, and workflows as separate files the agent can read on demand
3. Reference MCP tool configurations as branch paths, not inline definitions
4. Test by running a task that only needs one skill — confirm only that branch loads (check context usage)
5. Scale to 100+ tools without context overflow because only the relevant branch loads per task

## Examples
- CLAUDE.md points to `skills/code-review/SKILL.md` — agent loads it only when asked to review code
- agents.md lists 50 MCP servers; agent reads only the Filesystem MCP config for a file task
- Workflow scripts referenced by name in trunk; full workflow content loads only when triggered

## Source
Extracted from: [Context engineering for coding agents in one minute](https://www.youtube.com/watch?v=r9rxEd3d7sQ)
Channel: James Goldbach
