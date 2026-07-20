# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-190` (dept) · 2026-07-20T14:41:36.077202+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection attempts, or unreal elements.
2. Generate a security report confirming the integrity of the conversation’s data.
3. Verify all elements (messages, participants, context) are real and not fake/dead.
4. If anomalies are detected, flag and quarantine the session for further analysis.
5. Log the scan results for audit purposes.
6. Proceed only if the report confirms no integrity violations.

**What changed:** Warden’s scanner is now actively monitoring and verifying the session.
