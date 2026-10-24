---
name: multirun-evaluation
description: "Evaluating the consistency, decision-making, and reliability of AI agents, particularly for tasks where ground truth is hard to establish."
---

# Multirun Evaluation

## Overview
A technique for evaluating AI agents by running multiple isolated instances of the same agent in parallel on the same task. The consistency and divergence of their outputs are then compared (e.g., via a diff) to serve as an evaluation metric, without requiring a judge model, golden dataset, or hand-labeled ground truth.

**Use case:** Evaluating the consistency, decision-making, and reliability of AI agents, particularly for tasks where ground truth is hard to establish.

## Key steps
1. Ensure each agent runs in a completely isolated environment (e.g., separate git worktrees, database branches).
2. Compare outputs using diff tools to identify consensus and points of divergence.
3. The split in decisions among agents can itself serve as an evaluation metric.

## Details
- **Category:** agents
- **Tool:** Claude Code  ·  **Quality:** 5/10

## Source
Extracted from: https://dev.to/mech_app_ai/multirun-how-running-ten-isolated-agents-in-parallel-becomes-the-cheapest-eval-youll-ever-run-4c2h
