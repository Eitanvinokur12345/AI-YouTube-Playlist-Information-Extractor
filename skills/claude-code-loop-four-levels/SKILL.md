---
name: claude-code-loop-four-levels
description: "Use when deciding how much automation to give a Claude Code agent loop — choose the simplest of Anthropic's four loop levels (manual, goal-based, time-based, fully autonomous) that fits the task instead of defaulting to full autonomy."
---

# Claude Code Loop: Four Levels of Control

## Overview
Anthropic's own guide to automating repetitive Claude Code tasks describes four progressively
more autonomous loop types, each cycling through work until a stop condition is met. The guide's
core advice is to start simple and only scale up loop complexity as the task actually demands it.

## Key Techniques
- **Level 1 — Manual/turn-based loop.** You prompt Claude, review the output, and decide whether
  to continue each turn. Full human oversight, zero automation.
- **Level 2 — Goal-based loop.** The loop runs continuously until a stated objective is met (e.g.
  "improve the Lighthouse score above 90") or a max-attempt cap is hit. An evaluator model checks
  the objective so the loop can't stop prematurely on a bad attempt.
- **Level 3 — Time-based/scheduled loop.** Prompts run at regular intervals, locally or in the
  cloud, enabling continuous checks/updates with no manual trigger each time.
- **Level 4 — Fully autonomous loop.** Combines goal + schedule + workflow: Claude executes
  multi-step processes, explores parallel solutions, and self-assesses outcomes without human
  input in the loop.

## How to Apply
1. Default to Level 1 for anything you don't yet trust an agent to judge on its own.
2. Move to Level 2 once you can write a concrete, checkable objective and hook up an evaluator
   (a second model call, a test suite, a metric like Lighthouse score) to grade the result.
3. Add Level 3 scheduling only once the goal-based loop reliably converges — scheduling an
   unreliable loop just multiplies bad runs.
4. Reserve Level 4 for tasks mature enough to run fully unattended (goal + schedule + multi-step
   workflow + self-assessment) — this is the highest-risk, highest-leverage tier.

## Examples
- A goal-based (Level 2) loop iterating on frontend code until an evaluator confirms the
  Lighthouse performance score crosses a target threshold.
- A time-based (Level 3) loop running a scheduled Claude Code prompt every night in the cloud to
  check for and fix newly broken CI tests, with no one watching.

## Source
Extracted from: [Claude Code loops automate tasks with four levels of control from manual to full autonomy](https://www.youtube.com/watch?v=68TY4Fhrf2Y)
Channel: Matty | AI Models & Monetization
