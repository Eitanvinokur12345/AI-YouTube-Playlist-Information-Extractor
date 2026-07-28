---
name: two-layer-prompt-injection-defense
description: "Use when designing or hardening a browser/tool-using AI agent against prompt-injection attacks, to add a pre-model input scan plus a pre-execution action gate."
---

# Two-Layer Prompt-Injection Defense (Scan-then-Gate)

## Overview
A defense pattern for agents that consume untrusted external content (web pages, emails,
tool output). It adds two independent checkpoints instead of relying on the model alone to
resist injected instructions.

## Key Techniques
- **Layer 1 — pre-model scan:** inspect incoming data for injected instructions or suspicious
  patterns before the model ever sees it.
- **Layer 2 — pre-execution gate:** even if something slips past layer 1, block risky actions
  (file writes, purchases, credential use, etc.) before they actually run.
- Evaluate the defense on a large, realistic scenario set and report attack-success-rate with
  the defense on vs off, not just anecdotes.

## How to Apply
1. Wrap any tool/browser-using agent's data-ingestion path with an injection scanner.
2. Add an action-approval gate in front of side-effecting tools, independent of the scanner.
3. Benchmark against many scenarios (the source cited 129 browser-agent scenarios) and track
   attack-success-rate with/without the defense to prove it actually helps.
4. Treat this as risk reduction, not a guarantee — prompt injection is widely considered an
   open, possibly unsolvable problem.

## Examples
Anthropic's Claude Opus 5 'Auto Mode' is cited as implementing exactly this pattern: a data
scan before the model sees content, then an action gate before risky steps run, reportedly
reaching 0% attack success across 129 browser-agent scenarios (vs 3.7% with the defense off).

## Source
Extracted from: [Opus 5 Just Killed Prompt Injection: 0% Attack Success](https://www.youtube.com/watch?v=BUQb7kpmy7w)
Channel: Evgenii Arsentev
