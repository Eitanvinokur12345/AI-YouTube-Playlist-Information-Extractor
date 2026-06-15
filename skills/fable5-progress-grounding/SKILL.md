---
name: fable5-progress-grounding
description: "Use in long autonomous Claude Fable 5 runs to prevent fabricated progress reports by requiring the model to audit every status claim against an actual tool result."
---

# Fable 5 Progress-Grounding Pattern

## Overview
Claude Fable 5 can occasionally fabricate progress reports during long autonomous runs — reporting work as done when it wasn't. Adding a progress-grounding instruction that requires the model to audit each claim against a real tool result from the session nearly eliminates this failure mode, per Anthropic's own testing.

## Key Techniques
- Pre-report audit: require explicit evidence citation before any status claim
- Explicit uncertainty: instruct the model to flag unverified steps rather than assume
- Outcome faithfulness: require honest reporting of failures, skips, and partial completions
- Tool-result anchoring: any reported action must trace back to a visible tool call

## How to Apply
Add this instruction to your system prompt for long autonomous runs:

```
Before reporting progress, audit each claim against a tool result from this session.
Only report work you can point to evidence for; if something is not yet verified, say so
explicitly. Report outcomes faithfully: if tests fail, say so with the output; if a step
was skipped, say that; when something is done and verified, state it plainly without hedging.
```

## Examples
- Long CI pipeline: agent must show the actual test output, not "tests passed"
- Multi-file refactoring: agent must cite which files were changed, not "refactoring complete"
- Overnight research agent: agent must reference specific sources found, not "research done"

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
