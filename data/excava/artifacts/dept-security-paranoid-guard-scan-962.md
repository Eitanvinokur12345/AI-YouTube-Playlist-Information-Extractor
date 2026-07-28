# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-962` (dept) · 2026-07-28T12:58:14.808687+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output to generate a security report.
2. Flag any detected prompt injections, data leaks, or suspicious patterns.
3. Verify all referenced elements (e.g., tools, actions) are real and not fake/dead.
4. Cross-check Warden’s proposed actions against Bastion’s directives for consistency.
5. If violations are found, quarantine the conversation and notify stakeholders.
6. If clean, proceed with the verified plan.

**What changed:** Security scan executed; plan formalized.
