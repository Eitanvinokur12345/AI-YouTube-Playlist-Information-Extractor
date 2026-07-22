# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-552` (dept) · 2026-07-22T17:27:19.902869+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection, or tampering.
2. Verify all elements (tokens, responses, metadata) are real and not fake/dead.
3. Flag and quarantine any anomalies or unauthorized elements identified by the scanner.
4. Cross-validate the scanner’s report with Bastion’s internal integrity checks.
5. If anomalies are found, isolate the affected data and trigger a manual review.
6. Log the scan results and actions taken for audit purposes.

**What changed:** Scanner integration and verification steps added to enforce security.
