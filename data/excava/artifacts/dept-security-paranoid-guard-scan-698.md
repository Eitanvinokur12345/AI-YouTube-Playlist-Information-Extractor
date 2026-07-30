# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-698` (dept) · 2026-07-30T07:17:00.244094+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute LLM Guard scanner on the conversation’s input/output to generate a security report.
2. Review the report to flag any leaks, injections, or unreal elements detected.
3. Verify all elements in the exchange are real (not fake/dead) based on the report.
4. If anomalies are found, isolate and quarantine the affected data.
5. Document findings and actions taken for audit purposes.
6. Proceed only after confirming no unresolved security risks remain.

**What changed:** Security verification via LLM Guard scan is now required before proceeding.
