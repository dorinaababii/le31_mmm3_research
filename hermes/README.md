# Hermes Workflow Pack

Ports the spec-driven development workflow used in this repo (see the root
`CLAUDE.md`) to a [Hermes Agent](https://hermes-agent.nousresearch.com/)
instance — e.g. one running on a VPS, driven from Telegram.

This folder is self-contained on purpose: the VPS clones **only this
subtree**, not the rest of the repo.

## What's in here

- `SOUL.md` — global operating principles (loaded by Hermes as agent
  identity, applies to every conversation).
- `AGENTS.md.template` — per-project context file template. Copy into a
  project as `AGENTS.md`; Hermes auto-loads it when working in that
  directory.
- `skills/software-development/` — the workflow itself:
  - `development` — router; invoke this first for any coding task.
  - `speckit-specify`, `speckit-plan`, `speckit-tasks`, `speckit-implement`
    — the pipeline phases.
  - `pre-merge-review` — the merge gate.
- `install.sh` — wires the above into a Hermes install (see below).

## VPS setup

### 1. Sparse-clone just this folder

```bash
git clone --filter=blob:none --no-checkout https://github.com/dorinaababii/le31_cc.git ~/hermes-config
cd ~/hermes-config
git sparse-checkout init --cone
git sparse-checkout set hermes
git checkout main
```

Only `hermes/` lands on disk — the rest of the repo (Telegram bot config,
the restaurant app, etc.) is never fetched or checked out.

### 2. Run the installer

```bash
cd ~/hermes-config/hermes
./install.sh
```

This symlinks `SOUL.md` into `$HERMES_HOME` (default `~/.hermes`) and
registers `skills/` as an external skills directory in
`$HERMES_HOME/config.yaml`, without touching anything else already there.

### 3. Optional: wire up Linear

The `speckit-*` skills store specs/plans/tasks in Linear by default (same as
this repo). To enable that on the Hermes side:

```bash
hermes mcp add linear --url https://mcp.linear.app/mcp
```

It'll prompt for an OAuth login. If you'd rather not use Linear here, the
skills fall back to a local `specs/NNN-feature-name/` directory in whatever
project you're working on — no extra setup needed, just skip this step.

### 4. Restart Hermes

Restart the gateway/CLI so it picks up the new `config.yaml` and `SOUL.md`.
Then confirm:

```bash
hermes
/development
```

It should load the router skill from this pack.

## Updating later

```bash
cd ~/hermes-config
git pull
```

New or edited skills show up immediately — `external_dirs` points straight
at this checkout, nothing needs re-copying. If `SOUL.md` or the skill
frontmatter changed shape, re-run `./install.sh`.

## Using this in a project

1. `cp hermes/AGENTS.md.template <project>/AGENTS.md`
2. Fill in the bracketed sections (structure, stack, conventions, where specs
   live for this project).
3. Work in that project directory — Hermes auto-loads `AGENTS.md` on
   startup, `SOUL.md` is already global.
