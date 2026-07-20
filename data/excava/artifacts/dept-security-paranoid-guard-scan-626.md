# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-626` (dept) · 2026-07-20T17:14:04.478317+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection, or fake elements.
2. Verify all elements (messages, data, participants) are real and not fabricated or dead.
3. Generate a security report confirming the integrity of the conversation’s data.
4. Cross-check the report against the Warden’s initial scan for consistency.
5. If no issues are detected, finalize the scan and close the room.
6. Log the security report for audit purposes.

**What changed:** Security scan executed and integrity verified.
