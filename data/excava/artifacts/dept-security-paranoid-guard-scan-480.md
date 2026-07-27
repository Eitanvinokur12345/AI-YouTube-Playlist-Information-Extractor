# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-480` (dept) · 2026-07-27T22:32:54.540284+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection, or fake elements.
2. Generate a scan report flagging any anomalies for immediate review.
3. Verify all elements in the conversation are real (not fake/dead).
4. Cross-check detected anomalies against the scan report for validation.
5. If anomalies are found, quarantine the affected data and initiate a manual review.
6. Confirm all elements pass verification before proceeding.

**What changed:** Scanner deployed and verification steps added.
