---
name: fable5-prompting-principles
description: "Use when migrating prompts or workflows to Claude Fable 5 to avoid common pitfalls from over-specification and ensure optimal autonomous performance."
---

# Claude Fable 5 Core Prompting Principles

## Overview
Claude Fable 5 requires a fundamentally different prompting approach than prior Claude models. The three core principles are: keep prompts concise (less is more), provide context on WHY not just what, and set explicit behavioral guardrails — because the model is highly autonomous and will take unrequested actions without clear scope boundaries.

## Key Techniques
- Keep system prompts short: Fable 5 follows brief instructions more reliably than verbose ones
- Lead with intent: always explain the purpose behind a request, not just the deliverable
- Define explicit scope: state what Claude should and should NOT do to prevent unrequested actions
- Refactor older prompts: instructions written for prior models can actively degrade Fable 5 output

## How to Apply
1. Strip your existing system prompt of verbose behavior-by-name enumerations — Fable 5 infers most behaviors from brief instructions.
2. Add a WHY clause to every major request: "I'm working on [task] for [who]. They need [what the output enables]. With that in mind: [request]."
3. Add a scope boundary: "When the user is describing a problem rather than requesting a change, report findings and stop — don't apply a fix until asked."
4. Add a brevity instruction: "Lead with the outcome. Your first sentence should answer 'what happened' or 'what did you find.'"
5. Test against your hardest tasks first — Fable 5 excels on complex, long-horizon work.

## Examples
- Instead of enumerating "don't add features, don't refactor, don't add error handling..." use a single instruction about doing the simplest thing that works.
- Instead of "when the user asks a question, answer it; when they ask for a change, make it" — Fable 5 understands task type from context without enumeration.

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
