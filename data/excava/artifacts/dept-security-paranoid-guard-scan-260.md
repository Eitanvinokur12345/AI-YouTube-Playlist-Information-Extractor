# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-260` (dept) · 2026-07-31T19:58:51.445855+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the current input/output stream to detect leaks or injection attempts.
2. Generate a security-w1 report flagging any anomalies detected by the scanner.
3. Verify all elements in the stream are real (not fake/dead) by cross-referencing with trusted sources.
4. If anomalies are found, quarantine the affected input/output and flag for manual review.
5. Log the scan results and verification steps for audit purposes.
6. Proceed only if the security-w1 report is clean and all elements are verified.

**What changed:** Security-w1 scan and verification added to the workflow.
