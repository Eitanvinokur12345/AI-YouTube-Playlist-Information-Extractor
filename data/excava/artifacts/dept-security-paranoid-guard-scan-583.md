# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-583` (dept) · 2026-07-10T20:03:49.595350+00:00
> Participants: Warden · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a full asset inventory scan of all external-facing systems (web apps, APIs, databases, cloud buckets) using a trusted, read-only scanner (OpenVAS/Nessus).
2. Verify all detected elements are real (not fake/dead) by cross-referencing with known inventory and manual checks.
3. Scan for leaks/injection vulnerabilities in all identified assets.
4. Document all open ports, services, and potential misconfigurations.
5. Repeat scans weekly and after any infrastructure changes.
6. Implement automated alerts for unauthorized changes or new exposures.

**What changed:** Full asset verification and vulnerability scanning now mandatory for all external-facing systems.
