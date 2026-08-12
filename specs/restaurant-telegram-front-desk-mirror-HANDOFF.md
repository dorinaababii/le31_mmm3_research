# restaurant-telegram-front-desk-mirror — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/60-restaurant-telegram-front-desk-mirror.md` before
> touching any code.
> **DO NOT START THIS SLICE UNTIL THE CHARTER §5 PRIVACY REVISION IS
> SIGNED OFF.** This slice is parked today and ships as a dead-code-
> on-arrival module behind `CHAT_INGEST_ENABLED=False`.

## Frozen identifiers (do not rename)

- Feature ID: `60`
- Slug: `restaurant-telegram-front-desk-mirror`
- Contract file: `features/60-restaurant-telegram-front-desk-mirror.md`
- Bucket: v2 owner-pains (deferred / parking-lot)
- Linear parent: HMM-66 (Brainstorm 2026-08-12 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (4 in-source anchors today: `weebzone/ForwardX`
just-pushed 2026-08-03, 22★; `BethanyJep/Safaricom-Decode-Agents-
Workshop` pushed 2026-07-16, 16★; OpenAlex W7197042220 in-window;
`waifuengineer/taller_restaurant_telegram` pushed 2026-07-16).
Confidence: **high**.

**Decision: parking-lot today.** Strong evidence, but charter §5
currently forbids PII in v1; the charter revision must explicitly
include *"telegram chat ingest of staff messages in a private
staff-only group is permitted, and no PII from customer-side chats is
captured."* Once that revision is signed off, this slice becomes a
**build (v2 owner-pains, M effort, ≤1 week)** pick.

The slice ships as code in this PR (so the artifact is durable) but
is dead-on-arrival (`CHAT_INGEST_ENABLED=False`) until the charter
revision is signed off.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job, parked today).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                            # NEW: CHAT_INGEST_ENABLED=False, STAFF_GROUP_CHAT_IDS=[]
backend/app/services/chat_ingest.py              # NEW: parse_message(), ledger_event_to_row(), audit_link() — ≤250 lines
backend/app/bot/cook_bot.py                      # EDIT: register aiogram.Message listener on STAFF_GROUP_CHAT_IDS only (~5 lines, gated on CHAT_INGEST_ENABLED)
backend/tests/test_chat_ingest.py                # NEW: 5 fixtures (one per event type + one ambiguous fallback)
backend/README.md                                # note the privacy posture explicitly + the parking-lot reason
```

No new pip dependencies. No new SQLModel tables. No mandatory Alembic
migration; an **optional** `AuditLog.source_message_id` column is a
v3 hardening (skip at v1).

## Endpoints and bot commands added

No new HTTP routes. No new bot *commands*. One new `aiogram.Message`
handler, registered only on the `STAFF_GROUP_CHAT_IDS` whitelist:

- The handler silently parses the message; if a parse succeeds, the
  code:
  - Writes the parsed event as `StockEntry` / `VoidRationale` /
    `OrderItem`.
  - Writes the source message id and the destination row id to
    `AuditLog`.
  - Sends a one-line summary **only to the owner chat** (not the
    staff chat): *"Captured from cook-2: focaccia comp, table 6 →
    VoidRationale #392."*

The source chat receives no reply.

## Privacy posture (the parking-lot blocker)

This slice parses **staff-side** messages in a **staff-only**
Telegram group, identified by a whitelist of chat ids in
`STAFF_GROUP_CHAT_IDS`. Customer-side chats are *not* parsed by this
slice; they are the responsibility of feature 56
(`walk-in-front-desk-channel`).

The LE31 charter §5 currently reads *"v1 guest demographics are
counts, not identity or contact data"* — this forbids storing PII
about customers in v1. The slice does not store customer PII (it
only stores what staff write in the staff chat). But the
*principle* — "LE31 may ingest inbound text from a Telegram group"
— is novel enough that it must be on the charter record before code.

Until the charter is revised to include the *"telegram chat ingest
of staff messages in a private staff-only group is permitted"* clause,
`CHAT_INGEST_ENABLED` stays `False`, and the parser is dead code.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test `parse_message()` deterministically: same input → same
   output across 5 fixtures (comp, void, stockout, order, ambiguous).
2. Unit-test `ledger_event_to_row()` deterministically: each event
   type produces one row in the correct table.
3. Unit-test `audit_link()` deterministically: source message id is
   stored in the audit row.
4. Whitelist test: an `aiogram.Message` arriving from a chat id *not*
   in `STAFF_GROUP_CHAT_IDS` must be **silently dropped** — no row
   is written, no log entry is generated beyond a debug-level entry
   marked `[chat-ingest] out-of-scope chat id`.
5. Disabled-by-default test: with `CHAT_INGEST_ENABLED=False`, the
   handler is a no-op even for whitelisted chat ids.

After implementation, run the parent's verify-before-fixing protocol
on the slice branch.

## Rollback path

- Feature flag `CHAT_INGEST_ENABLED=False` (default OFF). Setting
  it to `True` does not enable the handler; the *code* must also
  be reached.
- No schema change at v1; rolling back = reverting the PR.
- Reversible in <5 min: env-set + (optionally) disable the
  `aiogram` handler registration.

## What is explicitly NOT in this slice

- **Customer-side messages.** This pick is *staff-only*. Inbound from
  customer-side chats is feature 56.
- **LLM parsing.** The parser is regex + keyword (deterministic), not
  LLM. LLM-fallback parsing is a v3 follow-up.
- **Image / voice message handling.** Out of scope at v2.5+.
- **Editing / undoing parsed rows.** Out of scope: each parsed row
  gets an `AuditLog.undoable=True` flag, but the UI to *act* on
  undo is feature 47 (`decision-rationale-mixin`) or a v3 follow-up.
- **Multi-group support.** v1 is single-group whitelisted.

## Charter conformance

- **Charter §5 (privacy):** ⚠ — *Hard conflict* until revision.
  Parking-lot today.
- Stock invariant: A new `StockEntry` row is written only on parse
  success; the parser synthesizes no StockEntry directly. ✓
  (Charter conformant *after* privacy revision.)
- State invariant: Parses are explicit operator actions (typed by
  staff in chat); no automatic transitions. ✓
- Money invariant: N/A.
- AI invariant: No AI call. The parser is deterministic regex +
  keyword. ✓
