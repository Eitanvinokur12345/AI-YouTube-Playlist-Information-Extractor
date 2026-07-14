# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-657` (dept) · 2026-07-14T17:44:13.040838+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the input/output stream to detect leaks or injection attempts.
2. Generate a real-time report confirming session security status (secure/flagged) with anomaly details.
3. Verify all elements in the session are real (not fake/dead) using the scanner’s output.
4. If anomalies are detected, isolate and analyze the flagged content immediately.
5. Quarantine any suspicious elements pending further inspection.
6. Resume normal operation only after the scanner confirms no unresolved threats remain.

**What changed:** Scanner integration and anomaly verification now enforce real-time security checks.
