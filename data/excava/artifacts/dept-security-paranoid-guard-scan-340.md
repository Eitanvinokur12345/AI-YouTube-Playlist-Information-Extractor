# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-340` (dept) · 2026-07-12T12:17:09.051304+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy LLM Guard in monitor-only mode with real-time alerts for one full production cycle.
2. Warden configures LLM Guard’s default rule set and monitors false-positive rates against real traffic.
3. Audit develops a synthetic attack corpus to validate rule efficacy and edge cases.
4. After the production cycle, enforce blocking rules only if validation metrics meet security thresholds.
5. Warden tunes LLM Guard’s rules based on audit feedback and production data.
6. Audit retains ownership of the synthetic corpus and validation metrics for ongoing review.

**What changed:** Shifted from audit-mode tuning to monitor-only + synthetic validation before enforcing blocking.
