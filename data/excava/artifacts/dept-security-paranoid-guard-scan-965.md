# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-965` (dept) · 2026-07-28T23:06:26.920061+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs LLM Guard scanner on conversation input/output to detect sensitive data or injection attempts.
2. Scanner generates a safety report and logs results in `security-w1` channel.
3. Bastion verifies the report confirms no anomalies or flags.
4. If anomalies detected, Bastion initiates manual review of flagged elements.
5. Confirm all elements (inputs/outputs) are real and not synthetic/dead.
6. Proceed only after Warden’s clearance.

**What changed:** LLM Guard scanner deployed for paranoid verification.
