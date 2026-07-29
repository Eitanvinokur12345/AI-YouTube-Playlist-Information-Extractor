# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-961` (dept) · 2026-07-29T20:31:41.839478+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input and output to detect leaks, injection, or unreal elements.
2. Generate a security report confirming whether the conversation passes all checks or requires intervention.
3. If the report flags any issues, escalate to the Warden for manual review and remediation.
4. If the report is clean, proceed with the conversation under verified security conditions.
5. Log the scan results for audit purposes.
6. Repeat the scan if the conversation undergoes significant changes.

**What changed:** Security verification via LLM Guard scanner is now mandatory for this conversation.
