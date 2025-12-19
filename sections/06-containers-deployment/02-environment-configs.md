# Environment Configurations (Dev/Stage/Prod)

## Why this lesson

Separate configs by environment to avoid risky hard-coding and ease promotion.

## Outcomes

- ✅ Externalize settings (ports, model path, log level)
- ✅ Use env-specific config files or env vars
- ✅ Document defaults and overrides

**Time**: ~20 minutes

**Prerequisites**: Dockerized app

## Agenda

- Twelve-Factor config principles
- Env var patterns and `.env` files
- Config loading order and defaults

## Hands-on

- Add config module reading env vars with sane defaults
- Provide sample `.env.example`

## Deliverable

- `.env.example` and config loader

## Checkpoint

Can you switch from dev to prod settings without code changes?
