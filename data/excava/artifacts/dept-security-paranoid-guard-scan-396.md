# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-396` (dept) · 2026-07-31T18:45:24.845557+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the current input/output stream to detect leaks or injection attempts.
2. Verify all elements (inputs, outputs, and internal states) are real and not fake/dead.
3. Output the real-time security verdict from the scanner to `security-w1`.
4. If leaks/injection are detected, terminate the session and log the incident.
5. If no issues are found, proceed with the next step in the workflow.
6. Repeat the scan periodically or after significant state changes.

**What changed:** Initialized real-time security scanning and verification protocol.
