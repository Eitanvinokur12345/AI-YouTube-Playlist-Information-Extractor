---
name: tiered-model-execution
description: "Use when you want to reduce AI coding costs by separating codebase auditing and planning (frontier model) from implementation execution (cheap model)."
---

# Tiered Model Execution Workflow

## Overview
This workflow splits AI coding tasks into two phases: a frontier model audits the codebase and writes self-contained execution plans (with file paths, code excerpts, and verification commands), then a cheaper, faster model carries out the plans step-by-step. This achieves frontier-quality direction at a fraction of the token cost.

## Key Techniques
- Use your most capable model only for the intelligence-intensive phase: understanding the codebase, judging what is worth doing, writing the spec
- Plans are self-contained: every step includes file paths, relevant code excerpts, and a verification command with expected output
- Cheaper executor models follow the plan without needing to re-analyze the whole codebase
- Verification gates at each step catch failures before they compound
- Parallel audit fans across nine categories: correctness, security, performance, test coverage, tech debt, dependencies, DX, docs, and feature direction

## How to Apply
1. Install the skill: `npx skills add shadcn/improve`
2. Run `/improve` (full audit) or `/improve quick` / `/improve deep` / `/improve security` to generate a plan with your frontier model
3. Review the generated plan file
4. Switch to a cheaper model and run `/improve execute <plan>` to carry out the implementation
5. After each step, verify with the provided command and expected output
6. Use `/improve reconcile` to update and verify previously created plans

## Examples
- Run `/improve security` with Claude Sonnet to audit for vulnerabilities, then execute the remediation plan with a cheaper model
- Use `/improve plan "add pagination to the user list"` to generate a targeted plan, then hand it to a budget model for execution
- Run `/improve deep` for exhaustive analysis across all nine quality dimensions before a major refactor

## Source
Extracted from: [Improve: your best model plans, your cheapest model builds](https://www.youtube.com/watch?v=QZk0VAhapP8)
Channel: Github Awesome
Linked resource: https://github.com/shadcn/improve
