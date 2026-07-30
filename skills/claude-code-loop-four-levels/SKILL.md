---
name: claude-code-loop-four-levels
description: "Use when deciding how much autonomy to hand Claude Code for a repetitive or long-running task — picks the right loop level instead of an all-or-nothing choice."
---

# Claude Code Loop Automation Levels

## Overview
Anthropic's own framework for scaling loop-based automation in Claude Code across four
progressive levels of control. Start simple and only add complexity the task actually needs.

## Key Techniques
- Level 1 — Manual, turn-based: prompt Claude, review each output, decide whether to continue.
- Level 2 — Goal-based: give Claude an objective (e.g. "improve this Lighthouse score") and let
  it loop until an evaluator model confirms success or a max-attempts cap is hit.
- Level 3 — Time/schedule-based: run the same prompt on a recurring local or cloud schedule for
  continuous, unattended checks and updates.
- Level 4 — Fully autonomous: combine goal + schedule + workflow so Claude executes multi-step
  processes, explores parallel solutions, and self-assesses outcomes without human input.

## How to Apply
1. Start at Level 1 for anything new or risky — you want to see every turn.
2. Once the task's success criteria are clear and checkable, move to Level 2 and let an
   evaluator model gate when the loop stops.
3. If the same goal-loop needs to run repeatedly over time (not just once), add scheduling
   (Level 3).
4. Only reach for full Level 4 autonomy once the task is well-understood and the evaluator is
   trustworthy — it removes the human checkpoint entirely.

## Examples
Anthropic's guide uses a Lighthouse-score improvement task as the Level 2 example: Claude keeps
iterating on the page until the evaluator confirms the target score, or a maximum number of
attempts is reached, rather than stopping after one pass.

## Source
Extracted from: [Claude Code loops automate tasks with four levels of control from manual to autonomous](https://www.youtube.com/watch?v=68TY4Fhrf2Y)
Channel: Matty | AI Models & Monetization
