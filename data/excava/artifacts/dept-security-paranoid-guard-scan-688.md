# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-688` (dept) · 2026-07-30T20:44:54.220435+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve Warden’s LLM Guard real-time scan for leaks/injections/fake elements.

**Plan:**
1. Warden runs LLM Guard in real-time scan mode against the current input/output stream.
2. LLM Guard produces a security verdict for every message before further processing.
3. Store the scan output in `data/excava/artifacts/llm-guard-scan-current-payload-689.md`.
4. Verify all elements in the payload are real (not fake/dead) post-scan.
5. Reject or quarantine any message flagged by LLM Guard.
6. Log all security verdicts for audit.

**What changed:** Activated real-time LLM Guard scanning for the current payload.
