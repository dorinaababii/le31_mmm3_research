# geminka-agent-aiogram-3-telegram-premium-markup-pattern — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/120-geminka-agent-aiogram-3-telegram-premium-markup-pattern.md`
> before touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `120`
- Slug: `geminka-agent-aiogram-3-telegram-premium-markup-pattern`
- Contract file: `features/120-geminka-agent-aiogram-3-telegram-premium-markup-pattern.md`
- Bucket: **v2 owner-pains (parking-lot, future-cook-bot-rich-markup-surface)**
- Linear parent: HMM-155 (Brainstorm 2026-08-26 — daily)
- Linear sub-issue: see `le31 v2 owner-pains` project (or `le31 Research` if project naming unclear), label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "LE31 gate verdict". **Decision: defer, watch-list**.

Evidence precondition: **inferred** (highest-star aiogram-3 + Telegram peer
in window with the architectural primitives LE31's cook-bot surface already
plans). Confidence: **medium for pattern-record, low for LE31-specific
urgency**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be
   sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the
research-side Hermes instance before writing code.

## Files the slice touches

```
# None. This is a watch-list artifact; zero code today.
```

The slice ships **zero code, zero new files, zero new dependencies**. The
deliverable is the contract file `features/120-geminka-agent-aiogram-3-telegram-premium-markup-pattern.md`
plus this HANDOFF plus the Linear sub-issue.

## Endpoints and contracts added

**None.** No new tables, no new columns, no new endpoints, no new
endpoints, no new migrations, no new pip dependencies. The slice is a
research observation that records `SkrudjReal/geminka-agent` as a
pattern-record peer for the LE31 v2 cook-bot rich-markup + auth-pattern
consideration.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions behave
as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Schema**: nothing to migrate; no `init_db()` change.
3. **Endpoints**: nothing to add; the SSE channel `GET /api/cook/stream`
   (feature 23) is unchanged.
4. **Telegram bot**: nothing to change; the aiogram 3.x cook-bot surface
   (feature 04) is unchanged. The architectural primitives
   (`Deny-by-Default Auth Middleware` + `Per-User Concurrency Lock` +
   `SQLite WAL State`) are *individually familiar to LE31 charter §3.1*
   and require no change to the existing Telegram cook-bot surface.
5. **Pattern-record artifact**: confirm `SkrudjReal/geminka-agent`
   README contains the aiogram-3 architectural primitives verbatim:
   - `aiogram 3.x` (LE31's own framework, charter §3.1)
   - `Telegram Updates` (LE31's own input surface)
   - `Deny-by-Default Auth Middleware` (mirrors charter §3.1 chat-id
     allowlist)
   - `Per-User Concurrency Lock` (race-condition guard for chat_id
     updates; v2 polish item)
   - `SQLite WAL State` (single-writer append-only surface; charter
     §3.2 keeps v1 on Postgres but the SQLite WAL pattern is
     informational)
6. **README verification**: fetch `https://api.github.com/repos/SkrudjReal/geminka-agent/readme`
   with the same `HERMES_GITHUB_TOKEN` and verify the aiogram-3
   primitives are present.
7. **License verification**: fetch `https://api.github.com/repos/SkrudjReal/geminka-agent`
   and verify `license.spdx_id` is `MIT` (permissive).
8. **Regression**: confirm all existing LE31 v1 flows still work
   (seat, order, serve, bill, tip, OCR menu upload, append-only
   `StockEntry` ledger, chat-id allowlist deny-by-default).
9. **Watch-list continue**: this is a research observation; no build
   today. The "should LE31 v2 adopt a Telegram Premium markup surface
   for the cook-bot?" question is parked pending the v2 charter
   review.

## Rollback / feature-removal path

- Delete `features/120-geminka-agent-aiogram-3-telegram-premium-markup-pattern.md`.
- Delete `specs/geminka-agent-aiogram-3-telegram-premium-markup-pattern-HANDOFF.md`.
- Remove the Linear sub-issue.
- Remove the row from `/opt/data/INDEX.md` "Active feature pipeline" table.
- No data migration, no data retention — the artifact is research;
  no rows were added to LE31.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected.
- The explicit-state rule is unaffected.
- The chat-id allowlist deny-by-default (charter §3.1) is unaffected.
- The aiogram 3.x Telegram cook-bot surface is unaffected.

## Sign-off gap

External coding agent must mirror the five frozen identifiers (Feature ID,
slug, contract file path, bucket, Linear parent HMM-155) back to the
research-side Hermes before implementing. If any of these conflict with what
the agent sees locally, **stop and ask** — do not silently rename.