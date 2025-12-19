# Reproducible Training Pipelines

## Why this lesson

Make training runs repeatable so results can be trusted and debugged.

## Outcomes

- ✅ Parameterize data paths, seeds, hyperparams
- ✅ Log configs and outputs per run
- ✅ Separate code, config, and data

**Time**: ~30 minutes

**Prerequisites**: Prior model training experience

## Agenda

- Config-driven training (YAML/JSON)
- Seeding for reproducibility
- Run artifacts and logs

## Hands-on

- Wrap your training script to read config and set seeds
- Emit a run artifact folder with config+metrics

## Deliverable

- `train.py` that consumes `config.yaml` and writes `runs/<timestamp>/`

## Checkpoint

Can you rerun with the same config and get identical metrics (within tolerance)?
