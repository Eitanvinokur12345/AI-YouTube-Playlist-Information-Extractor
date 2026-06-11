---
name: agentcrew-multi-agent
description: "Use when building multi-agent systems that need disciplined role boundaries and structured coordination protocols to prevent agent drift."
---

# AgentCrew Multi-Agent Coordination Framework

## Overview
AgentCrew is an open-source framework for enforcing discipline in multi-agent systems. It requires each agent to have an explicitly defined role, responsibility scope, and coordination protocol before deployment. This prevents the common failure mode where agents drift outside their intended scope and create unpredictable cascading behaviors.

## Key Techniques
- Define each agent's role and responsibility boundary in a config file
- Set explicit coordination protocols for inter-agent communication
- Use the framework's audit logs to trace agent decision paths

## How to Apply
1. Clone AgentCrew from GitHub (mlguyYT/AgentCrew)
2. Define each agent's role in the crew config (name, scope, tools, boundaries)
3. Set up coordination rules (which agents can message which, in what format)
4. Initialize the crew and assign the top-level task
5. Monitor agent communication via the built-in audit log
6. Iterate on role boundaries based on observed behavior

## Examples
- Building a research crew with a planner, researcher, writer, and reviewer—each with strict scope
- Creating a code review crew where agents can only modify files in their assigned module

## Source
Extracted from: [Your Agents Need Discipline](https://www.youtube.com/watch?v=4PP_bodyqc0)
Channel: ML Guy
