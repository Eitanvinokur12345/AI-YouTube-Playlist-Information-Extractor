# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-949` (dept) · 2026-07-10T17:18:02.871312+00:00
> Participants: Warden · synthesized by mistral/mistral-small-latest

**Decision:** Implement mandatory pre-production network scans for all new systems to eliminate default services/credentials.

**Plan:**
1. Deploy automated port/service discovery (e.g., `nmap` or `masscan`) on every new system prior to deployment.
2. Block deployment if non-approved ports/services are detected (fail-closed).
3. Require manual review for any unexpected services, even if non-critical.
4. Log scan results and approvals in a tamper-evident audit trail.
5. Integrate scan results into the system’s deployment metadata (e.g., CI/CD pipeline).
6. Schedule periodic re-scans for systems already in production (quarterly minimum).

**What changed:** Added automated pre-production scanning with fail-closed enforcement.
