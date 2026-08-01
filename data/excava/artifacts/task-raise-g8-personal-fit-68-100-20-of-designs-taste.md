# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-35419` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via Arena learning pipeline, wire NOSG, then extend taste beyond.

**Steps:**
1. **Tag 20% of designs** – Run `python scripts/taste_tag.py --split 0.2 --output data/tagged_designs.json` (uses `data/designs/` input).
2. **Arena learning live** – Deploy `arena/serve.py` with `torchrun --nproc_per_node=4 arena/train.py --data data/tagged_designs.json --epochs 10`.
3. **NOSG wiring** – Edit `config/nosg.json` to enable `taste_module: true`, then restart `nosg/daemon.py` with `systemctl --user restart nosg`.
4. **Taste beyond** – Add `scripts/extend_taste.py` to poll `data/new_designs/` hourly and tag via `arena/predict.py`.

**Needs:**
- `data/designs/` (17 small files, raw designs).
- `arena/` repo (PyTorch training pipeline).
- `nosg/daemon.py` (systemd service, config in `config/nosg.json`).
- GPU node (4x A100, CUDA 12.1).
```
