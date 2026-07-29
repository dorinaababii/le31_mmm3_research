# Repository Structure

This is a research repository. It is the single source of truth for product direction, contracts, and the discipline that any implementation must follow. The build code (`backend/`, `index.html`) is staged here for convenience and will be moved into its own repository once that repo exists.

## Top-level layout

| Path | What it holds |
|---|---|
| `README.md` | one-page research pitch |
| `INDEX.md` | master index — start here |
| `PROJECT_CHARTER.md` | mission, scope, principles, quality bar |
| `HANDOFF.md` | research-side repo tour for the next session |
| `REPO_STRUCTURE.md` | this file |
| `research/` | external research (12 survey/deep-dive files) |
| `features/` | feature contracts (22 files: v1 + v2 + v2-AI) |
| `specs/` | SPEC / PLAN / TASKS trail produced by my work |
| `skills/` | LE31 research-side skills (loaded by Hermes on this side) |
| `coding-agent/` | shippable LE31 skill pack, mirrored into the build repo |
| `agent/` | runtime snapshots (SOUL, USER, MEMORY, config template) |
| `hermes/` | Hermes installer; mirrors LE31 skills into the agent config |
| `backend/` | FastAPI + SQLModel + aiogram skeleton |
| `index.html` | waiter UI mock-up |

## What does not live here

- The actual production code is destined for the future `le31_mmm3_built` repository. A staged copy of it sits on the `feature/le31_mmm3_built-staging` branch.
- Per-session chat transcripts stay in Linear (`le31 Workflow`) and `/opt/data/`.
- Raw research fetches stay under `/tmp/le31-*/` (regenerated on demand by the le31-research skill).

## After the build repo exists

- `backend/` and `index.html` can be moved out of this repo.
- `coding-agent/` remains here as the canonical source; the build repo mirrors it.
- `agent/` and `hermes/` stay here (they serve this research agent).
