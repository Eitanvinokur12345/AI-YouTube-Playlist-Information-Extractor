---
name: fable5-checkpoint-stopping
description: "Use when building autonomous Claude Fable 5 pipelines to define exactly when the agent should pause for human input versus proceed unattended."
---

# Fable 5 Checkpoint-Stopping Instruction

## Overview
Without explicit guidance, Claude Fable 5 may ask for permission unnecessarily (blocking long pipelines) or proceed through actions that needed human review. This pattern defines the exact criteria for pausing: only destructive/irreversible actions, genuine scope changes, or inputs only the user can provide — everything else proceeds autonomously.

## Key Techniques
- Positive definition of stop conditions (not a general "check first" instruction)
- End-of-turn self-check: if the last paragraph is a plan or promise, execute it now
- Async-aware language: explicitly state the user is not watching in real time
- Reversible vs irreversible distinction: proceed on reversible actions, pause on irreversible ones

## How to Apply
For interactive use, add:
```
Pause for the user only when the work genuinely requires them: a destructive or irreversible
action, a real scope change, or input that only they can provide. If you hit one of these,
ask and end the turn.
```

For unattended pipelines, extend with:
```
You are operating autonomously. The user is not watching in real time and cannot answer
questions mid-task. For reversible actions that follow from the original request, proceed
without asking. Before ending your turn, check your last paragraph — if it is a plan, an
analysis, a list of next steps, or a promise about work not done, do that work now with
tool calls. End your turn only when the task is complete or you are blocked on input only
the user can provide.
```

## Examples
- File deletion: pause and confirm (irreversible)
- Config edit that can be reverted: proceed
- "Should I also refactor X?": scope change → stop and ask
- Writing a test for the fix: proceed (follows from original request)

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
