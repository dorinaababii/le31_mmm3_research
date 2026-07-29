# LE31 mmm3 built — repo tour (placeholder)

> Status: this repo does not exist yet. The contents of this folder are a **staged copy** of what it will receive.

## What goes here when you create `le31_mmm3_built`

```text
docs/le31_mmm3_built/        ← (this folder, the staging area)
├── backend/                 ← FastAPI + SQLModel + aiogram code
├── index.html               ← waiter UI mock-up (lives here until the SPA choice)
├── coding-agent/            ← the LE31 skill pack (mirrors docs/coding-agent in research)
├── HANDOFF.md               ← this file (after first commit, this is the build-side HANDOFF.md)
├── KIMI_K3_PROMPT.md        ← paste-in prompt for the coding agent
└── README.md                ← one-page project summary
```

## When you create the new repo

1. Create an empty `le31_mmm3_built` repository on GitHub under your account.
2. Clone it locally.
3. Copy the four items in this staged folder into the new repo's root, preserving structure.
4. Add `/skills/` for the LE31 skill pack if you want the coding agent to load it via Hermes `external_dirs`. Keep it git-ignored after copy.
5. Wire Hermes `config.yaml` `external_dirs` to point at the staged `coding-agent/` folder if Hermes runs in that repo too.

## What stays in `le31_mmm3_research`

- All `docs/research/`, `docs/features/`, the LE31 skills (`hermes/skills/le31/`), the agent runtime snapshots (`agent/`), and the project charters.
- All Linear projects.
- `/opt/data/` dated reports.

## Boundary rules (after split)

- A change to behaviour starts in the research repo: amend or add a feature spec, run the gate, then update the build-side pack.
- A change to implementation only lives in the build repo.
- A skill-pack change lives in both: research repo owns the canonical version, build repo mirrors it.
- Reports, audits, and gate evidence live in the build repo under `coding-agent/evidence/<slice-id>/`.
