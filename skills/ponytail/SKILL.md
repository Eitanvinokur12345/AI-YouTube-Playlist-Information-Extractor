---
name: ponytail
description: "Guiding AI agents to write more efficient, minimal, and robust code by questioning the necessity of new code and promoting reuse or deletion."
---

# Ponytail

## Overview
A skill that makes an AI agent ask whether it should write code before writing anything, forcing it to reason like the laziest senior developer. It prioritizes deleting, reusing, or not building at all, leading to less code, less surface area, and fewer bugs.

**Use case:** Guiding AI agents to write more efficient, minimal, and robust code by questioning the necessity of new code and promoting reuse or deletion.

## Key steps
1. Before writing code, the agent stops at the first rung that holds: Does this need to exist? (no: skip it (YAGNI)), Stdlib does it? (use it), Native platform feature? (use it), Installed dependency? (use it), One line? (use it), Only then: the minimum that works.
2. The skill forces the agent to consider if a task can be done by deleting something, reusing existing components, or not building it at all.
3. It aims for the best code being the code you never wrote.

## Details
- **Category:** agents
- **Tool:** claude  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=bMfUtbD-EDU
