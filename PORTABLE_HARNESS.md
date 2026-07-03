# The EXCAVA harness as a portable package (Phase 7 — port later, by owner decision)

Owner checkpoint 2026-07-03: **build the harness clean, wire no second project yet.**
When Budoaris/FreeDup (or anything else) wants an agentic spine, these five files move as a
unit — they only assume "a repo with a `data/` folder", nothing Excavatortron-specific:

| file | role | repo-specific bits to swap |
|---|---|---|
| `src/excava_bus.py` | file bus: enqueue/route/claim/hand-off(gated)/trace/lease/prune | none — paths derive from repo root |
| `src/excava_agents.py` | registry + Worker contract + specialization routing | the `WORK` handlers (department assessors) |
| `data/excava/agents.json` | tiers/departments/scoped tools | department list |
| `data/excava/guardrails.md` | the law the orchestrator enforces | G-rules that don't apply |
| `src/project_memory.py` + `PROJECT_MEMORY.md` | recall-before-change memory master | none |

The orchestrator (`src/excava.py`) is the only heavily project-coupled piece (gate checks,
priorities sync); a port writes its own thin beat over the same bus API.

Heartbeat: any scheduler that runs `python -m src.excava` periodically (GitHub Actions cron
here — D1). Free, stdlib-only, no daemon host needed.

Phase-7 items still open (deliberately): provider-agnostic runtime, rules engine,
auto-provisioning, auto-reports, meta-brain, per-tab self-improvement, deprecation protocol,
version-compat matrix.
