# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-927` (dept) · 2026-07-27T22:19:06.902065+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks or injection attempts.
2. Verify all elements (inputs, outputs, references) are real and not fake/dead.
3. Flag any suspicious content flagged by the scanner for review.
4. Cross-check detected anomalies with Bastion’s internal validation protocols.
5. If no leaks/injections are found, proceed with the conversation; otherwise, terminate and quarantine the session.
6. Log the scan results and validation steps for audit purposes.

**What changed:** LLM Guard scanner deployed for real-time monitoring and validation.
