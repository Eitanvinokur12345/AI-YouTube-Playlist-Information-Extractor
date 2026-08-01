---
name: chatgpt-codex-goal-long-running-task-build
description: "Use when you want ChatGPT desktop's Codex to ship a complete, working app end-to-end from a single prompt instead of iterating turn-by-turn."
---

# ChatGPT Codex Goal Mode for Long-Running App Builds

## Overview
Codex inside the ChatGPT desktop app has a "goal" feature that spins up a single
long-running autonomous coding task instead of a normal back-and-forth chat turn. Give it
one detailed prompt and it keeps working unattended until it produces a full, working
result.

## Key Techniques
- Write one detailed prompt describing the entire target outcome, not an incremental step.
- Use the goal feature (not a normal chat turn) so the task keeps running unattended for
  as long as it needs.
- State platform-specific constraints up front (e.g. watchOS's strict image size/memory
  limits) so the agent doesn't have to rediscover them through trial and error.

## How to Apply
1. Open Codex in the ChatGPT desktop app.
2. Write a single prompt describing the full app you want built, including any known
   platform constraints (data sources, target device, resource limits).
3. Launch it as a goal/long-running task rather than a normal chat message.
4. Let it run unattended; review the shipped result when it completes.

## Examples
The source video shipped a companion Apple Watch app for an existing iPhone app in about
2 hours from one goal prompt — including syncing data from the iPhone app to the watch app
and loading images on the watch face within Apple's tight size/memory limits. The creator
had previously spent up to 3 days stuck on the same class of problem when building it by
hand, and had given up on shipping a watch app for 3 years before this.

## Source
Extracted from: [How I built an Apple Watch app for Amy in 2 hours with Codex in ChatGPT desktop](https://www.youtube.com/watch?v=fsOqjZIiJVA)
Channel: Chris Raroque
