# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-736` (dept) · 2026-07-29T20:59:27.675571+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on conversation input/output to detect leaks, injection, or policy violations.
2. Review scanner report for anomalies or policy breaches.
3. Verify all elements (inputs, outputs, references) are real and not fake/dead.
4. If anomalies detected, quarantine or redact affected content.
5. Log scan results and actions taken for audit.
6. Proceed only if no critical violations remain.

**What changed:** Scanner integration confirmed; verification steps formalized.
