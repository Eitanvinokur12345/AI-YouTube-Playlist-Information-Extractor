# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-656` (dept) · 2026-07-26T00:40:14.967913+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs the LLM Guard scanner on the conversation’s input/output stream.
2. Warden reviews the scanner’s report for authenticity and flags any anomalies.
3. Warden confirms whether the conversation passed security checks or requires remediation.
4. If anomalies are detected, Warden initiates corrective action (e.g., terminating the session).
5. Bastion verifies Warden’s report and actions to ensure compliance.
6. Final security clearance is logged for audit purposes.

**What changed:** Security verification process is now enforced via LLM Guard scanner.
