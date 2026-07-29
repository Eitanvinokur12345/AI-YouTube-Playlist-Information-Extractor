---
name: codex-plugin-bounded-debate-review
description: "Use when you want a genuine second opinion on a Claude Code plan or diff from a different model family before shipping, via OpenAI's official Codex plugin for Claude Code."
---

# Codex Plugin Bounded-Debate Review for Claude Code

## Overview
OpenAI publishes an official Claude Code plugin that runs Codex inside the same terminal
session. It adds 8 slash commands (a real 4-command core setup), including a read-only code
review, an adversarial review, and a rescue subagent.

## Key Techniques
- Plan/build handoff: one model plans, the other builds, instead of one model doing both.
- Second-opinion review: run Codex's review pass on a diff/plan before shipping it.
- Bounded debate: time-box a back-and-forth where Claude and Codex critique each other's
  answer, so disagreement resolves to a clear verdict instead of dragging on.

## How to Apply
1. Install the official Codex plugin for Claude Code.
2. After Claude Code produces a plan or diff, invoke `/codex-review` for a read-only pass, or
   `/codex-adversarial` when you specifically want the review to hunt for flaws.
3. For genuinely uncertain decisions, run the bounded-debate workflow so both models respond
   and critique each other before you pick a final answer.
4. Budget for both models — running Codex alongside Claude does not lower total spend.

## Examples
- Claude Code drafts a refactor plan; Codex reviews it read-only before the build starts.
- Before shipping a diff, an adversarial Codex pass looks specifically for edge cases Claude
  may have missed.
- A genuinely ambiguous design decision goes through a bounded Claude-vs-Codex debate instead
  of trusting a single model's first answer.

## Source
Extracted from: [OpenAI Just Put Codex Inside Claude Code](https://www.youtube.com/watch?v=D3kmstnDVY0)
Channel: Sebastian Hardy | AI Marketing
