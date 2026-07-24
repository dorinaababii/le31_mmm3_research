# Agent context

Snapshots of the runtime files that define the agent's persona, configuration,
and persistent memory. These are normally only readable on the agent's host
machine (`~/SOUL.md`, `~/config.yaml`, `~/memories/`).

We commit them here so:

1. **Other agents** picking up this project can see exactly which model / persona / provider was used.
2. **You** have a backup you can pull from anywhere — if the host machine dies, the agent's "self" is in version control.
3. **Auditing** — a record of how the project was set up.

## Contents

| File | Source | Purpose |
|---|---|---|
| `SOUL.md` | `~/SOUL.md` | Agent persona + behavior rules (verbatim). |
| `config.yaml.template` | `~/config.yaml` (redacted) | Active model + provider config. **API keys stripped** — see comments. |
| `USER.md` | `~/memories/USER.md` | Your profile + style + workflow preferences (verbatim). |
| `MEMORY.md` | `~/memories/MEMORY.md` | Operational facts about this machine + git setup (verbatim). |

## What is NOT here

- **Live `config.yaml`** — contains `MINIMAX_API_KEY`, `TELEGRAM_BOT_TOKEN`,
  `HERMES_GITHUB_TOKEN`, and other secrets. **Never committed.** The live
  version lives at `~/config.yaml` on the agent's host only.
- **Live `.env`** — same reason. Gitignored.

## How to refresh this folder

After meaningful changes to any of the source files, ask the agent to:

> "Back up the agent context files to the repo."

The agent will overwrite the 4 files in this folder and push a commit.

## Why this folder is at the repo root (not in `docs/`)

These files are **not project documentation** — they're **agent metadata**.
Keeping them at the root makes the distinction clear: `docs/` is for the
restaurant app, `agent/` is for the agent running on it.