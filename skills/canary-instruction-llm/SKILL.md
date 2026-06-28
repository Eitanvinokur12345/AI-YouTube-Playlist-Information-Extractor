---
name: canary-instruction-llm
description: "Ensuring LLMs like Claude maintain context and follow specific instructions throughout a session, providing an early warning when the model starts to 'forget' or deviate."
---

# Canary Instruction for LLMs

## Overview
A technique to embed a small, consistent instruction (a 'canary') into an LLM's rules or prompt to monitor its adherence to instructions and detect when its context or rules start to degrade.

**Use case:** Ensuring LLMs like Claude maintain context and follow specific instructions throughout a session, providing an early warning when the model starts to 'forget' or deviate.

## Key steps
1. Add a simple instruction like 'Start every reply with my name' to your Claude rules.
2. Monitor for the absence of this instruction as an early warning sign of context degradation.
3. Clear the session and start fresh when the canary 'dies' (the instruction is forgotten).

## Details
- **Category:** productivity
- **Tool:** claude  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=C7Bm4ckgyuA
