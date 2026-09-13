# HANDOFF — Feature 172: `mshykhov-expense-ledger-bot-approval-telegram-outbox`

**Slice contract for the coding agent. This is an `experiment` feature — code-read experiment, no code change to LE31 v1 today. The HANDOFF documents the experiment + the cross-section primitives.**

## Active feature path

`features/172-mshykhov-expense-ledger-bot-approval-telegram-outbox.md` — experiment (Pick C of Brainstorm 2026-09-13, parent research issue HMM-241).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | PostgreSQL transactions + outbox = LE31 v1 surface (every state change is wrapped) |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | zero AI (deterministic Telegram bot + approval gate) |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-13T05:19:30Z (within 30-day window) |
| 5 | Ripgrep-verified unique vs features/ 1..169 | ✓ | no existing feature documents the *Telegram + Postgres + outbox + approval + Sheets projection* stack as a *unified reference* |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 30/33/35/39/41/43/57/60/61/78/108 |
| 7 | Experiment verdict (code-read, no code change) | ✓ | 0★ + 2-minute-old repo + 233 KB → code-read experiment recommended before any adoption decision |

**Gate verdict**: **experiment** — 7/7 gate checks pass, but the build verdict is `experiment` because (a) the codebase is brand-new and small; (b) the experiment is a *code-read*, not a *code-adoption*; (c) the *architecture-confidence signal* is the value, not the code.

## Bucket

**v1** (operator-surface reference) — the *shape* is the value, not the code.

## Files to touch

**None today.** The experiment is a *code-read* in a separate session:

1. `git clone https://github.com/mshykhov/expense-ledger-bot` (NOT to be done today — defer)
2. Read the README + the entry-point script + the outbox worker + the Sheets projection
3. Evaluate the implementation quality:
   - Is the approval gate deterministic?
   - Is the outbox pattern correct (outbox row inserted in the same transaction as the state change)?
   - Is the Sheets projection transactional?
4. If the implementation is clean, file a cross-section evidence note in the feature contract
5. If the implementation is sloppy, downgrade to parking-lot

**Do NOT do step 1 today.** The experiment verdict means the code-read is *deferred to a separate session*, not executed today.

## Verification protocol

The experiment verifies four primitives:

1. **Approval gate is deterministic**:
   - Read the entry-point script; find the approval handler.
   - Verify the approval gate is a discrete subsystem (not interleaved with the entry handler).
   - Verify the approval is recorded as a state change in the outbox (not as a side-effect).

2. **Outbox pattern is correct**:
   - Read the outbox worker; find the outbox-to-Sheets dispatch.
   - Verify the outbox row is inserted in the *same transaction* as the state change (not in a separate transaction).
   - If the outbox row is inserted in a separate transaction, this is the *vulnerability pattern* — flag it.

3. **Sheets projection is transactional**:
   - Read the Sheets projection; find the Sheets API call.
   - Verify the Sheets projection reads from the outbox (not directly from the state table).
   - Verify the Sheets projection handles outbox failures (retry, dead-letter, or skip-and-continue).

4. **Stack-shape matches LE31 v1**:
   - The expense-ledger-bot uses aiogram (Telegram) + PostgreSQL + SQLAlchemy (likely) + Sheets API.
   - LE31 v1 uses aiogram + SQLModel + PostgreSQL + (no Sheets integration today).
   - The stack-shape matches. The Sheets projection is the *secondary* surface that LE31 v1 could add in v2.

## Rollback path

**N/A** — no code change today. The HANDOFF documents the experiment.

If the experiment verdict is *implementation is clean*, the next step is to file a cross-section evidence note (no code change to LE31 v1). If the experiment verdict is *implementation is sloppy*, the next step is to downgrade to parking-lot.

## Mandatory LE31 skill list

- `le31-conventions` — naming, file structure, charter invariants
- `le31-v1-feature-pattern` — v1 feature template + experiment verdict semantics
- `le31-coding-agent-brief` — coding-agent invocation pattern
- `le31-handoff-spec` — HANDOFF.md template

## Cross-section evidence

- **features/ 30, 33, 35, 39, 41, 43, 57, 60, 61, 78, 108** — sister-shape references (each covers one slice of the four primitives)
- **feature 35** (`sse-replay-buffer`) — outbox pattern (cook-facing); the expense-ledger-bot outbox is the *generic* version of this pattern
- **feature 61** (`holdfast-approval-ledger`) — approval gate; the expense-ledger-bot approval is the *generic* version of this pattern
- **feature 39** (`owner-daily-recap-telegram`) — owner-recap export (Sheets-projection pattern); the expense-ledger-bot Sheets projection is the *generic* version of this pattern
- **ad-hoc evidence**: `mshykhov/expense-ledger-bot` GitHub direct-GET verified by parent 2026-09-13

## Notes

- **Do not adopt the expense-ledger-bot codebase**. The experiment verdict is based on (a) 0★ with single-maintainer cadence; (b) 2-minute-old repo at push time; (c) the codebase is 233 KB and unverified. The *experiment* is a code-read to verify the implementation quality, not a code-adoption.
- **Do not propose code changes** to LE31 v1 today. The experiment artifact is documentation only.
- **The cross-section pattern** is the *unified external reference* for the four primitives. The existing features cover each primitive individually (features 33/35/39/41/43/61); the expense-ledger-bot is the *integration* of all four primitives in a 233 KB Python codebase.
- **The architecture-confidence signal** is the value: an independent maintainer arrived at the same stack-shape in 2026 for a different use case (expense ledger vs restaurant stock). The signal is the *demand-signal* for the v1 backend-shape, not the *adoption-signal* for the v1 backend-shape.
- **Parent-verified**: GitHub API direct-GET `/repos/mshykhov/expense-ledger-bot` saved to `/tmp/verify_mshykhov_expense-ledger-bot.json` on 2026-09-13. All star/fork/license/pushed_at/created_at/description/topics/size values in the feature contract re-parsed byte-for-byte by parent.

---

**End of HANDOFF.**
