---
name: n8n-vs-claude-code-selection
description: "Use when deciding between n8n (fixed workflow graph) and Claude Code (flexible plain-language SOP) for an automation or agentic coding task."
---

# n8n vs Claude Code Selection Framework

## Overview
n8n wires steps and gives AI one constrained execution square—ideal for predictable, repeatable workflows. Claude Code receives a plain-language SOP and interprets the entire job—ideal for tasks requiring adaptive reasoning.

## Key Techniques
- n8n: fixed node graph, constrained AI actions, reliable repetition
- Claude Code: plain-language SOP, AI interprets and adapts
- Key question: Does the task need strict constraint or flexible interpretation?

## How to Apply
1. Define the task's variability: are all steps known and fixed?
2. If yes → n8n (visual workflow, constrained AI node)
3. If no → Claude Code (plain SOP, AI interprets)
4. For hybrid: wrap Claude Code inside an n8n orchestration for structured + flexible segments

## Examples
A recurring job automation: n8n handles the scheduling and data I/O nodes; Claude Code interprets the processing logic from a plain-English SOP.

## Source
Extracted from: [n8n vs Claude Code: fixed vs flexible](https://www.youtube.com/watch?v=Jh551lxK61I)
Channel: Professor Glitch
