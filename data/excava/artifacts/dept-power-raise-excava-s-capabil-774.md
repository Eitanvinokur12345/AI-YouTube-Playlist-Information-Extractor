# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-774` (dept) · 2026-07-31T06:05:55.185346+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet vs. 3.5 Sonnet on EXCAVA’s power workloads; the artifact is a signed report proving ≥0.5% gain or rejecting the upgrade, owned by Torque.

**Plan:**
1. Spin up parallel EXCAVA instances with identical workloads, one running 3.7 Sonnet (Gearbox’s choice) and the other 3.5 Sonnet (Torque’s fallback).
2. Log all performance metrics (latency, accuracy, token cost) via EXCAVA’s telemetry pipeline for 48 hours.
3. Freeze model versions and disable auto-updates during the test to ensure consistency.
4. Assign Torque ownership of the benchmark report, with Gearbox as secondary reviewer for validation.
5. Set a hard threshold: if 3.7 Sonnet’s gain is ≥0.5%, proceed with the upgrade; otherwise, default to 3.5 Sonnet.
6. Publish results in a signed GitHub Gist with SHA-256 hash for immutability.

**What changed:**
A/B benchmark replaces unilateral model switch, shifting risk mitigation to empirical validation.
