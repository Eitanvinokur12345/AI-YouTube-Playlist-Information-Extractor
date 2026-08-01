# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-461` (dept) · 2026-07-31T04:58:34.206920+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
The Warden's LLM Guard scan must complete and confirm no leaks/injections before proceeding.

**Plan:**
1. Warden runs LLM Guard scanner on conversation input/output.
2. Warden generates report in `/var/log/llm_guard/w1`.
3. Bastion verifies report confirms no leaks, injections, or anomalies.
4. If scan passes, proceed with next steps.
5. If scan fails, quarantine conversation and escalate.
6. Document scan results in `data/excava/artifacts/dept-security-paranoid-guard-scan-461.md`.

**What changed:** Warden's scan is now the blocking prerequisite before Bastion proceeds.
