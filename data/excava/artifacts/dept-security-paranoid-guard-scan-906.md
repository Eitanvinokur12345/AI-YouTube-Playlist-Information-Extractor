# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-906` (dept) · 2026-07-17T21:24:03.837993+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the input/output stream of this conversation to detect leaks or injection attempts.
2. Verify all elements (inputs, outputs, references) are real and not fake/dead by cross-checking against trusted sources or prior sessions.
3. Generate a real-time anomaly report from LLM Guard and review for policy violations.
4. If anomalies are detected, quarantine the session and log the incident for further analysis.
5. If no anomalies are found, proceed with the session under monitored conditions.
6. Document the scan results and verification steps for audit purposes.

**What changed:** LLM Guard scanner is now actively monitoring the session for security compliance.
