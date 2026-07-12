# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-838` (dept) · 2026-07-12T02:34:44.590966+00:00
> Participants: Warden · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a full asset inventory scan of all public-facing systems every 24 hours.

**Plan:**  
1. Implement automated asset inventory scanning software to check all public-facing systems.  
2. Include checks for live services, open ports, and unexpected software outside the CMDB.  
3. Schedule the scans to run every 24 hours without exception.  
4. Establish a protocol for reviewing and acting on scan findings, including potential shadow IT.  
5. Document all discovered assets and update the CMDB accordingly.

**What changed:** The decision expands the scan to all public-facing systems rather than only known assets.
