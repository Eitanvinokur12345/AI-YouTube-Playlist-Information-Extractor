# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-636` (dept) · 2026-07-31T18:51:36.824232+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Procure dual-socket AMD EPYC cluster with MI300X GPUs (4 TB/s bandwidth, mature ROCm).
2. Deploy EXCAVA on the cluster, parallelizing sparse tensor streaming across MI300X.
3. Run 10% slice of EXCAVA workload on both H100 and MI300X concurrently for benchmarking.
4. Compare sparse tensor handling, compute efficiency, and memory bandwidth utilization.
5. If MI300X matches H100 performance, migrate full EXCAVA workload to MI300X cluster.
6. Decommission H100 nodes post-validation to reduce NVIDIA lock-in dependency.

**What changed:** Switched from single-GPU (MI325X/H100) to dual-socket EPYC + MI300X cluster for EXCAVA.
