---
name: claude-canary-hallucination-detection
description: "Use when running long Claude Code sessions to detect context-window degradation early via a canary instruction in CLAUDE.md, so you can reset before hallucinations compound."
---

# Claude Canary Trick: Early Hallucination Detection

## Overview
Claude doesn't go from perfect to hallucinating overnight — sessions degrade gradually. A canary instruction in CLAUDE.md acts as a sentinel: Claude must acknowledge it each turn, and its absence is an early warning that the context window is degrading. Based on Peter Steinberger's agentic engineering playbook.

## Key Techniques
- A small, specific instruction in CLAUDE.md that Claude must repeat or confirm in every response
- Monitoring for the canary's absence as a degradation signal (not hallucination itself)
- Resetting the context window immediately upon canary failure, before compounding bad output

## How to Apply
1. Add a canary instruction to your `CLAUDE.md` — for example: *"At the start of every response, include the phrase: [ACTIVE SESSION]."*
2. Run your agent loop or long task as usual.
3. Monitor output — the moment `[ACTIVE SESSION]` goes missing, the session is degrading.
4. Immediately reset: start a new session, re-anchor CLAUDE.md, and resume from the last clean checkpoint.

## Examples
- An overnight analysis run: the canary fires at response 47, catching drift before 53 more bad analyses accumulate.
- A code-generation loop: missing canary at step 12 → reset context, re-read the codebase, continue cleanly.

## Source
Extracted from: [This Tiny Trick Catches Claude Hallucinating Early](https://www.youtube.com/watch?v=C7Bm4ckgyuA)
Channel: Sebastian Hardy | AI Marketing
Credit: Peter Steinberger's agentic engineering playbook
