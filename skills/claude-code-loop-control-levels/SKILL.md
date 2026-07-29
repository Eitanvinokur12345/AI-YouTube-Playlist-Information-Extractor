---
name: claude-code-loop-control-levels
description: "Use when deciding how much autonomy to give a Claude Code automation loop — picks the right control level (manual, goal-based, scheduled, or fully autonomous) for a repetitive coding/maintenance task."
---

# Claude Code Loop Control Levels

## Overview
Anthropic's own guide to looping in Claude Code describes four progressively autonomous loop
types, each trading operator oversight for hands-free reach. The guide's core advice: start at
the simplest level and only escalate when the task genuinely needs it.

## Key Techniques
- Level 1 — manual, turn-based: prompt Claude, review each output before continuing.
- Level 2 — goal-based: the loop runs until a stated objective is met (or a max-attempt cap is
  hit), with an evaluator model checking the objective so the loop doesn't stop early.
- Level 3 — time-based: the same prompt runs on a schedule (locally or in the cloud), enabling
  continuous checks/updates with no manual trigger.
- Level 4 — fully autonomous: combines goal + schedule + workflow so Claude executes multi-step
  processes, explores parallel solutions, and self-assesses outcomes without human input.

## How to Apply
1. Default to Level 1 for anything novel or high-risk — review every turn.
2. Move to Level 2 once the success condition is objectively checkable (tests pass, a metric
   like a Lighthouse score crosses a threshold) and pair it with an evaluator model so a
   plausible-looking but wrong result can't end the loop early.
3. Add Level 3 scheduling once the goal-based loop is proven reliable and the task benefits from
   running unattended on a cadence (e.g. nightly maintenance).
4. Reserve Level 4 for tasks that justify full autonomy — multi-step, parallelizable, and
   tolerant of self-assessment replacing a human review step.

## Examples
- Goal-based loop improving a Lighthouse score: Claude iterates, an evaluator model scores each
  attempt, and the loop stops only once the target score is confirmed (or attempts run out).
- Fully autonomous loop: a scheduled, goal-driven loop that explores several parallel fixes for
  a task and self-selects the best outcome without a human in the loop.

## Source
Extracted from: [Claude Code loops automate tasks with four levels of control from manual to full autonomy](https://www.youtube.com/watch?v=68TY4Fhrf2Y)
Channel: Matty | AI Models & Monetization
