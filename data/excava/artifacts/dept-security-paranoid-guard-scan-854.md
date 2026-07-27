# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-854` (dept) · 2026-07-27T22:26:08.990910+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs the LLM Guard scanner on the conversation’s input/output stream to detect injection or leakage.
2. Generate a report flagging any suspicious patterns or anomalies.
3. Verify all elements in the conversation are real (not fake/dead) by cross-referencing with trusted sources.
4. If anomalies are detected, quarantine the affected input/output and initiate a manual review.
5. Log all scanner results and verification steps for audit purposes.
6. Proceed only after confirming no unresolved security risks remain.

**What changed:** Scanner integration and verification steps added to enforce security.
