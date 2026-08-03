# Coding-Agent Skill Pack

A drop-in bundle of 7 SKILL.md files for the separate LE31 coding-agent repository (Hermes running Kimi K3). The pack encodes the same LE31 standards the research-side Hermes enforces, so the implementation passes the same gates whether it is built by the research agent or by the coding agent.

## What's in here

- `skills/le31-conventions-coder/SKILL.md`
- `skills/le31-arch-patterns/SKILL.md`
- `skills/le31-quality-gates/SKILL.md`
- `skills/le31-verification-protocol/SKILL.md`
- `skills/le31-cook-bot-ux/SKILL.md`
- `skills/le31-data-correctness/SKILL.md`
- `skills/le31-handoff-protocol/SKILL.md`
- `checklist.md` — one-page field checklist
- This `README.md`

## How it was justified

Standard-by-skill justification lives in `/opt/data/le31-coding-agent-research-2026-07-27.md` (research report). Each SKILL.md also embeds the relevant primary sources in its body.

## How to ship to the coding-agent repo

1. Clone the destination repo (where the coding agent runs).
2. Copy the entire `coding-agent/` folder to its `skills/le31-pack/` (or your preferred path) inside the destination repo. Use the same nested `skills/<name>/SKILL.md` layout.
3. Wire the destination repo's Hermes config (`config.yaml`) so that `skills.external_dirs` includes the new folder:
   ```yaml
   skills:
     external_dirs:
       - /abs/path/to/destination-repo/skills/le31-pack
   ```
4. Restart the destination Hermes gateway.
5. Verify the new skills are listed:
   ```bash
   hermes skills list | grep le31-
   ```
6. Drop a `coding-agent/.gitignore` marker in the destination repo so the pack is ignored locally after copying:
   ```gitignore
   /skills/le31-pack/
   ```

## How it stays in sync

The pack is rooted in this research repository. When standards change:

- Open a PR in this repository.
- Update the affected `SKILL.md` files.
- Push. The branch is `feature/le31-coding-agent-skill-pack`.
- The user copies the updated folder to the destination repo.

The research-side `le31/` skills and the coding-agent-side `le31-*-coder` skills reference each other; treat them as siblings, not duplicates.

## Verification

A coding agent should, after loading the pack, be able to:

- run the seven-check feature gate on a new feature
- emit append-only events for stock and money
- round-trip timezone-aware timestamps
- block float in money arithmetic
- pre-commit the static gates (`ruff`, `mypy --strict`, `pip-audit`, `bandit`, `gitleaks`)
- require a non-author reviewer before merge for schema/auth/ledger changes
