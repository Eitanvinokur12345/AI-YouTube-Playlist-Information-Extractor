# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-475` (dept) · 2026-07-30T19:32:40.433540+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Proceed with real-time LLM Guard scanning for security verification.

**Plan:**
1. Warden runs LLM Guard in real-time scan mode against the current input/output stream.
2. Verify all elements (tokens, entities, responses) are real and not fake/dead.
3. Detect leaks, injections, or tampering in real-time.
4. Flag any anomalies or compromised data for immediate review.
5. Log scan results for audit and forensic analysis.
6. Terminate or quarantine the session if security risks are detected.

**What changed:** Real-time LLM Guard scanning is now active for security enforcement.
