# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-311` (dept) · 2026-08-25T11:03:08.646712+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RIFE v4.17 into EXCAVA’s motion pipeline as the primary temporal upscaler.
2. Conduct a controlled test on a 1080p clip using a 4-core CPU, comparing RIFE v4.17 against Flowframes’ FILM.
3. Measure temporal quality gain (≥0.5%) and real-time stability; if passed, permanently replace FILM with RIFE v4.17.
4. Document artifacts, performance metrics, and hardware compatibility in the test report.
5. If RIFE v4.17 fails the threshold or breaks real-time, fallback to EMA-VFI for evaluation.
6. Gearbox to own test execution, data collection, and final artifact delivery.

**What changed:** Switched EXCAVA’s motion pipeline from FILM to RIFE v4.17 for temporal upscaling.
