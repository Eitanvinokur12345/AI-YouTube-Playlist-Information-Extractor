---
name: dual-model-planner-executor-orchestration
description: "Use when a coding task's token cost needs cutting by splitting judgment/planning work onto an expensive frontier model and mechanical execution onto a cheaper model."
---

# Dual-Model Orchestration: Expensive Planner + Cheap Executor

## Overview
Most tokens spent on a coding task go to mechanical execution ("typing"), not high-judgment
decisions ("thinking"). This workflow routes each kind of work to the model best suited (and
priced) for it, instead of running one frontier model for the whole job.

## Key Techniques
- Let the expensive/frontier model (e.g. Claude) handle architecture and judgment calls only.
- Route repetitive, instruction-following execution work to a cheaper model (e.g. GPT).
- Pass work back and forth between the two until the project is complete.
- Use a plugin/bridge so the two tools share one workflow instead of manual copy-paste.

## How to Apply
1. Install a bridge plugin, e.g. the Codex Plugin for Claude Code:
   `/plugin marketplace add openai/codex-plugin-cc`, then run `/codex:setup`
   (requires a ChatGPT subscription or OpenAI API key, Node.js 18.18+).
2. Use the plugin's commands to delegate specific work: `/codex:review`,
   `/codex:adversarial-review`, `/codex:rescue`, `/codex:transfer`, `/codex:status`.
3. Keep the expensive model in the loop only for decisions that need its judgment; let it
   delegate execution-heavy chunks to the cheaper model via the plugin.
4. Compare token spend against a single-model baseline to confirm the split is actually
   cutting cost for your workload.

## Examples
The source video pairs Claude ("Fable 5") as the planner with GPT 5.6 as the executor via
OpenAI's Codex Plugin for Claude Code, reporting the same output for roughly half the tokens
of running one frontier model end-to-end.

## Source
Extracted from: [Use GPT 5.6 Inside Claude Code](https://www.youtube.com/watch?v=u8o8OAbLuDo)
Channel: Jack Roberts
