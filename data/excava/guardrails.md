# EXCAVA guardrails — the law the orchestrator enforces

_Phase 0 of EXCAVA_PROGRAM.md. The mechanical rules below are enforced in code
(`src/excava_bus.py`, `src/excava.py`); this file is the single human-readable copy the
Phase-2 self-audit will diff the code against. Changing a rule here without changing the
code (or vice versa) is itself a guardrail violation._

## G-1 Free only, forever
No action may require payment or a card on file. A "free tier needing a card" is paid → skip.

## G-2 The verification gate comes first
No task is claimed while `data_guard` or `security` checks fail. Outward actions
(create / promote / publish / self-code / leverage) additionally require G3 ≥ 70 **and**
owner approval. The gate is checked at every beat, before routing.

## G-3 Resource check before claim
A task is only routed to a department whose required capability is `ok` in
`data/resources.json`. Missing resource → task held with the exact reason, never attempted blind.

## G-4 Hand-offs require a real hand-off doc — no doc, no hand-off
A hand-off must carry non-empty `what_was_done`, `artifacts`, `what_remains`,
`context_for_next`. The bus **rejects** the hand-off otherwise and logs the rejection to the
task's trace. This is the rule that keeps EXCAVA an OS instead of a tab pile.

## G-5 Done-criteria and max-steps on every task
Every task carries `done_criteria` (what finished looks like) and `max_steps`. A task that
exceeds `max_steps` escalates; it never loops silently.

## G-6 Three-tier escalation, owner last
Worker (tier 1) → department lead (tier 2) → core (tier 3) → **owner** (held in the inbox
with the reason). Nothing retries forever; nothing outward escalates past the gate.

## G-7 Scoped tools only
An agent may only use the tools listed for it in `agents.json`. The orchestrator refuses to
route work to an agent without a declared scope.

## G-8 Owner outranks
Tasks from `data/excava_inbox.json` outrank auto-priorities at routing time, always.

## G-9 Shared memory: vectors read, state written
Agents read context from the semantic index (`data/memory_index.json`) and write facts only
to `data/excava/state.json` (through the bus) — no agent invents its own side-channel state file.

## G-10 CI owns the data files
`data/*.json` regenerate hourly in CI. Local test artifacts of CI-owned files are reverted,
never committed. New `data/excava/*` files are bus-owned and committed by the bus only.

## G-12 Creations are labeled and independently tested (owner rule 2026-07-03)
Anything the Creators department makes may enter the project autonomously **only** with the
visible label "Created by EXCAVA", and an **independent test re-runs before its first use**
(`python -m src.excava_creators --test-before-run "<name>"`). Publishing beyond the project
stays behind G-2's outward gate. "Packages" (multi-element bundles) follow the same rule.

## G-11 Security first, quality over quantity
Untrusted content passes `security_preflight` before any agent consumes it. 300 verified
items beat 3,000 dead ones — a department that can't verify its output hands off to
`security`, it does not publish.
