---
name: fable5-agent-memory-pattern
description: "Use when setting up recurring or long-running Claude Fable 5 agents to enable persistent cross-session memory via a structured markdown file system."
---

# Fable 5 Persistent Memory Pattern

## Overview
Claude Fable 5 performs substantially better when it can reference lessons learned from previous sessions. The pattern is simple: provide a markdown file (or folder of files) where the model stores one lesson per file with a one-line summary at top. Bootstrap by having the model review past session history with subagents and extract core themes and corrections.

## Key Techniques
- One lesson per file with a one-line summary at top
- Record both corrections (what went wrong) and confirmed approaches (what worked and why)
- Subagent-powered bootstrapping from past session history
- Update existing notes rather than duplicating; delete notes that turn out to be wrong

## How to Apply
1. Create a `memory/` directory and give the agent read/write access to it.
2. Add to system prompt:
```
Store one lesson per file in memory/ with a one-line summary at the top. Record corrections
and confirmed approaches alike, including why they mattered. Don't save what the repo or
chat history already records; update an existing note rather than creating a duplicate;
delete notes that turn out to be wrong.
```
3. To bootstrap from history, run once:
```
Reflect on the previous sessions we've had together. Use subagents to identify core themes
and lessons, and store them in memory/. Make sure you know to reference memory/ for future use.
```
4. At the start of each session, instruct the agent to read the memory files before starting work.

## Examples
- "memory/python-type-hints.md" — lesson about always using strict type annotations in this codebase
- "memory/api-rate-limits.md" — confirmed approach for batching requests to the project's external API
- Deleting "memory/use-async-everywhere.md" after learning synchronous code is preferred in this project

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
