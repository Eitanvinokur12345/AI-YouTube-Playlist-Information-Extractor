# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-712` (dept) · 2026-07-27T21:51:08.922778+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection, or fake elements.
2. Generate a scan report flagging any anomalies or violations.
3. Verify all elements in the conversation are real (not fake/dead).
4. Cross-reference the scan report with the conversation’s content for discrepancies.
5. If anomalies are found, quarantine or redact the affected parts.
6. Confirm the integrity of the conversation before closing the room.

**What changed:** Scanner integration and verification steps added to ensure security.
