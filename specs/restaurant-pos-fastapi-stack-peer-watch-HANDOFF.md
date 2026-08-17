# restaurant-pos-fastapi-stack-peer-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/79-restaurant-pos-fastapi-stack-peer-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `79`
- Slug: `restaurant-pos-fastapi-stack-peer-watch`
- Contract file: `features/79-restaurant-pos-fastapi-stack-peer-watch.md`
- Bucket: **v1 (watch-list)** — defer; `StockEntry` ledger not yet shipped
- Linear parent: `Brainstorm 2026-08-17 — daily` (HMM-94, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub `restaurant POS created:>2026-07-17 language:python` cluster — `Ing-JuanDavid/restaurant-backend-POS` 0★ 2026-08-15T22:39:51Z + `tlongmx4/restaurant-pos` 0★ 2026-08-16T16:02:47Z + `satisfecho/pos` 27★ carry-over, the strongest in-window stack match).

**Confidence:** **high** for the stack pattern (the description of `Ing-JuanDavid/...` explicitly confirms the FastAPI + SQLModel + Postgres stack); **low** for the LE31 differentiator (no peer has the `StockEntry` ledger + Telegram cook + cook-as-decision-maker combination; the differentiator is not yet observable).

**Decision: defer (watch-list).** The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. Circuit breaker: delete this file + the corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-17).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/79-restaurant-pos-fastapi-stack-peer-watch.md   # NEW (this artifact)
specs/restaurant-pos-fastapi-stack-peer-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                  # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/79-restaurant-pos-fastapi-stack-peer-watch.md` and confirm it matches the brainstorm report's "79-restaurant-pos-fastapi-stack-peer-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-17), pick slug (`restaurant-pos-fastapi-stack-peer-watch`), feature path (`features/79-restaurant-pos-fastapi-stack-peer-watch.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub `restaurant POS created:>2026-07-17 language:python` cluster and confirm the 2 first-pushes (`Ing-JuanDavid/...`, `tlongmx4/...`) sustain or grow. If either crosses ≥10★ sustained for 7+ days, the watch re-activates (re-evaluate the gate). If `satisfecho/pos` (27★ carry-over) crosses 50★, the watch may upgrade.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature` (label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 79 — restaurant-pos-fastapi-stack-peer-watch`.
- Body: the contract from `features/79-restaurant-pos-fastapi-stack-peer-watch.md` (or a short summary + the file path).
- Parent: `Brainstorm 2026-08-17 — daily` (HMM-94, the Linear index issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/79-restaurant-pos-fastapi-stack-peer-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The LE31 FastAPI+SQLModel+Postgres stack is **the LE31 v1 foundation** (PROJECT_CHARTER.md + the charter §3.2 stack rule). The 3-repo in-window cluster confirms that the stack is at a 2026-08 GitHub-space pattern in the broader ecosystem. The LE31 differentiator (per-batch append-only `StockEntry` ledger + Telegram cook surface + cook-as-decision-maker) is intact because no peer has yet shipped the combination.

**Risk of NOT tracking**: the stack match peers may consolidate in 2026-H2; if the watch-list is not in place when that happens, LE31 either re-derives the same conclusions (wasted cycles) or misses the validation (strategic risk).

**Risk of over-tracking**: the pattern is observed at the repo level only; the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until either `StockEntry` ledger ships to production or peer-velocity re-activates it." Re-evaluate when one of the 2 first-pushes crosses ≥10★ sustained for 7+ days.
