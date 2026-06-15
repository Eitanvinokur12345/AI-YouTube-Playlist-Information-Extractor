---
name: fable5-anti-overplanning
description: "Use when Claude Fable 5 at high effort levels is deliberating excessively before acting — surveying options, re-deriving facts, or narrating choices instead of using tool calls."
---

# Fable 5 Anti-Overplanning Instruction

## Overview
At high and xhigh effort settings, Claude Fable 5 can over-plan — re-deriving already-established facts, surveying options it will not pursue, narrating reasoning in user-facing messages when action is needed. Because Fable 5's instruction-following is so strong, a single brief instruction eliminates this without needing to enumerate each specific anti-pattern.

## Key Techniques
- Single-instruction fix rather than enumerating each behavior
- "When you have enough information to act, act" as the core trigger
- Recommendation-over-survey for decision points
- Applies to user-facing output only — thinking blocks can still deliberate freely

## How to Apply
Add to system prompt:
```
When you have enough information to act, act. Do not re-derive facts already established
in the conversation, re-litigate a decision the user has already made, or narrate options
you will not pursue in user-facing messages. If you are weighing a choice, give a
recommendation, not an exhaustive survey. This does not apply to thinking blocks.
```

For code tasks specifically, add:
```
Don't add features, refactor, or introduce abstractions beyond what the task requires.
A bug fix doesn't need surrounding cleanup. Don't design for hypothetical future requirements:
do the simplest thing that works well.
```

## Examples
- Bug fix request → fix the bug, do not also refactor the surrounding code
- "Should I use approach A or B?" → give a recommendation with one-line rationale, don't survey both
- User already decided on a framework → proceed with it, do not re-examine alternatives

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
