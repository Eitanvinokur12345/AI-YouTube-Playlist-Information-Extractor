---
name: ai-agent-safety-design-principles
description: "Use when designing or auditing production AI agents to prevent permission sprawl, silent failures, and unobservable behavior."
---

# AI Agent Safety Design: Least Privilege, Fallbacks, and Observability

## Overview
A three-principle framework for building robust AI agents that covers minimum permissions, human escalation paths, and interaction logging. Applying all three prevents the most common agent failure modes that destroy business deployments.

## Key Techniques
- Grant agents only the permissions they need for their specific task (least privilege)
- Define explicit fallback rules to route uncertain, out-of-scope, or keyword-triggered requests to a human
- Log every agent interaction and review a sample weekly to catch hallucinations and drift early

## How to Apply
1. **Audit permissions**: List every tool/API the agent can call. Remove any that aren't strictly necessary for its task scope.
2. **Write fallback rules**: Define at least three escalation triggers — low confidence score, specific keywords, anything outside the agent's defined scope.
3. **Instrument everything**: Log inputs, outputs, tool calls, and errors. Set up a weekly review sample (even 10-20 interactions per week).
4. **Set blast-radius limits**: If a permission is needed, scope it narrowly (read-only vs. write, single table vs. full DB).
5. **Test failure modes**: Deliberately send edge-case inputs to verify the fallback routes work before going live.

## Examples
- A customer support agent with CRM read-only access (not write), routing any request outside its FAQ scope to a human queue.
- A weekly agent log review catching a hallucination pattern on pricing questions before it costs deals.

## Source
Extracted from: [The 3 Biggest Mistakes People Make Building AI Agents](https://www.youtube.com/watch?v=HZHf--HTSHs)
Channel: Doby Lanete Highlights
