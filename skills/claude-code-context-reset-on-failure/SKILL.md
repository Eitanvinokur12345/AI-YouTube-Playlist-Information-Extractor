---
name: claude-code-context-reset-on-failure
description: "Use when Claude Code has failed on the same problem twice in a row — clear the context and rewrite the prompt rather than making a third correction in the same session."
---

# Claude Code Context Reset on Repeated Failure

## Overview
When Claude Code fails twice on the same coding problem, each failed fix accumulates in the context window. Subsequent corrections are then grounded in failure — the agent tries to fix its own broken solutions rather than reasoning from scratch. The correct response is to stop, clear the context, and write a new prompt that incorporates what the failures revealed.

## Key Techniques
- **Two-failure trigger**: The moment the same problem fails twice, stop — do not attempt a third fix in the same context.
- **Extract failure learnings**: Before clearing, note what specifically went wrong in both attempts (error type, wrong assumption, approach that failed).
- **Fresh context, informed prompt**: Open a new Claude Code session and write a prompt that explicitly describes the goal AND what approaches to avoid, based on the failures.

## How to Apply
1. Identify if Claude Code has failed on the same underlying problem twice.
2. Read both failure messages and extract the key insight (e.g., "both attempts tried to mutate state — that's the wrong approach").
3. Clear the Claude Code context (start a new session or use `/clear`).
4. Write a new, targeted prompt: "Do X. Do NOT do Y or Z (I tried both and they failed because...)."
5. Submit the fresh prompt and let Claude Code reason from a clean state.

## Examples
- Claude Code fails to fix an API authentication bug twice (tries JWT, then session cookies — both wrong). Clear context, write: "Fix authentication — not JWT, not session cookies — the issue is missing CORS headers."
- Claude Code tries to refactor a function twice and keeps breaking tests. Clear context, write: "Refactor this function without changing its external interface — previous attempts changed the return type."

## Source
Extracted from: [Why You Should Never Correct Claude Twice](https://www.youtube.com/watch?v=1lHRsMg0VCI)
Channel: Sebastian Hardy | AI Marketing
