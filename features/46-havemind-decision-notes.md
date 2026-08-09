# Feature 46 — Havemind Decision Notes

> **Priority**: P2 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-08 (cross-section pick A) · **Bucket**: v2-AI (no-LLM core, optional LLM digest)
> **One-line**: A new `DecisionNote` append-only SQLModel table stores signed `(decision_id, body, author_chat_id, author_role, effective_from, expires_at, tags_csv)` rows. The cook bot gets a one-line digest at start-of-service and four new commands (`/note <body>`, `/notes [date]`, `/notes tag:<tag>`, `/notes week`). The owner gets a 30-second weekly digest.

## Goal

Close the LE31 owner's middle-tier observation: *the owner often makes a policy decision mid-service ("we 86 the lamb on slow days", "Tuesdays we open at 18:00 not 18:30", "if the chef is alone, table 6 cannot be seated") but these decisions live in the owner's head, in SMS chat, or on a paper notebook — and the cook does not always get the same message the owner intended.* Today there is no audit chain for *decisions* (only for *events* via `StockEntry`). A simple `/note <body>` from the Telegram bot writes one signed `DecisionNote` row; the cook bot reads today's still-effective rows at start-of-service; the owner can `/notes [date]`, `/notes tag:<tag>`, or `/notes week` to query. A weekly cron sends a 30-second digest to the owner every Monday morning.

Inspired by today's brainstorm: GitHub `topic:append-only` repo `MikolajSapek/havemind` (pushed 2026-08-07T19:47:12Z, 0★, "Private, self-hosted, real-time sync for a shared Obsidian vault — **one shared brain for your team and their AIs**. Append-only history, full authorship, zero silent overwrites"). The repo comes from the *team-productivity / knowledge-management* world — completely outside hospitality — and shares the same primitive: a *shared* append-only brain that humans and AI agents both write to, with full authorship. Translated to LE31, this is the missing *decision audit trail* paired with the existing *event audit trail*.

Distinct from feature 39 (`owner-daily-recap-telegram`) because 39 is a recap of *events* (covers, voids, top movers); this is a record of *decisions* (which precede events). Distinct from feature 37 (`void-rationale-ledger-field`) because 37 captures per-event rationale on stock voids; this captures per-policy decisions that span multiple events.

## Evidence / JTBD

When the owner makes a policy decision mid-service, the owner wants to record it so the cook follows it tomorrow, but struggles because notes live in SMS or nowhere, so that a single Telegram `/note <body>` from the bot writes one signed `DecisionNote` row and the cook bot reads today's still-effective rows at start-of-service.

## Scope

**In scope (v2-AI, no-LLM core):**
- A new append-only `DecisionNote` SQLModel table:
  `(id, decision_id, body, author_chat_id, author_role, effective_from, expires_at, tags_csv, created_at)`. Append-only — the only mutable column is `effective_from` and `expires_at` (set by the bot at insertion; never updated after).
- A new bot command `/note <body>` — both cook and owner can use (chat-id in `TELEGRAM_ALLOWED_USERS`). Bot writes one `DecisionNote` row with `effective_from=now()`, `expires_at=now()+24h` (default), `author_role=cook|owner` (inferred from chat-id), and replies "OK ✓ note <head> logged as <decision_id>".
- A new bot command `/notes [date]` — both cook and owner can use. Bot replies with the list of `DecisionNote` rows for that date (default today), one per line: `<HH:MM> <role>: <body> [tags: ...]`.
- A new bot command `/notes tag:<tag>` — both cook and owner. Filters by tag.
- A new bot command `/notes week` — owner-only. Bot replies with the 7-day digest of notes.
- A new APScheduler cron job: every Monday morning at 09:00 Europe/Paris, the bot sends a weekly digest to the owner chat-id: "Last week's notes (N): <one-line per body>".
- A new start-of-service hook in the existing cook-bot: when the cook first sends any message after 06:00, the bot replies with "Today's notes (N): <one-line per body>" if any note is in-window and effective.
- A new derived view `compute_decision_digest(date) -> str` in `backend/app/services/decisions.py` that returns the markdown digest for the date.
- A new `backend/app/routers/decisions.py` router with `GET /api/decisions/list?date=...` (owner-only), `GET /api/decisions/week` (owner-only), plus the bot-command handlers.

**Out of scope (v2-AI):**
- LLM-based free-text note classification (auto-tagging) — the v1 form is regex tag parsing (`<text> #tag1 #tag2`). LLM is a v3 follow-up if the v2-AI feature is green-lit.
- Note-to-StockEntry auto-linking — v1 keeps notes and stock events in separate tables. Linking is a v3 follow-up.
- Voice-input for `/note` — the existing typed-Telegram channel is the only input. Voice-to-text for decisions is a v3 follow-up.
- Owner-only notes from cook — v1 allows both roles to write; role is recorded. A future filter ("only show owner notes") is a v3 follow-up.
- Web-UI for `/notes` — v1 is Telegram-only. The web UI is a v3 follow-up.

## Description

The owner today has no fast way to record a *policy decision* and have the cook see it the next day. The cook today has no fast way to record a *cook observation* ("the lamb is 86ed today because we ran out at 14:00") for the owner to review. Both are write-only today; this feature gives both a 3-second `/note <body>` flow with a full audit chain.

The pattern is *append-only* (same SQLAlchemy listener pattern as `StockEntry` and `OwnerAuditEvent`): rows are inserted, never updated, never deleted. The `effective_from` / `expires_at` columns are mutable at insertion time only — a future feature can query "is this note still in effect for today?".

## Data model

```sql
CREATE TABLE decision_note (
  id              BIGSERIAL PRIMARY KEY,
  decision_id     UUID NOT NULL UNIQUE,           -- uuid4, generated at insertion
  body            TEXT NOT NULL,                  -- the note text, immutable
  author_chat_id  BIGINT NOT NULL,                -- Telegram chat-id of author
  author_role     TEXT NOT NULL CHECK (author_role IN ('cook','owner')),
  effective_from  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  expires_at      TIMESTAMPTZ,                    -- NULL = persistent (until manually expired)
  tags_csv        TEXT NOT NULL DEFAULT '',       -- "#lamb-86 #slow-day"
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_decision_note_effective_from ON decision_note (effective_from);
CREATE INDEX idx_decision_note_tags ON decision_note USING gin (string_to_array(tags_csv, ' ') array_ops);
```

## Implementation steps

1. **New fixture**: `backend/app/models/decision_note.py` — SQLModel class matching the schema above. Append-only invariant enforced by SQLAlchemy `@event.listens_for` `before_update` and `before_delete` that raises if the row is *not* being inserted.
2. **New service**: `backend/app/services/decisions.py` with `compute_decision_digest(date, role=None) -> str`, `insert_decision_note(body, author_chat_id, author_role, effective_from=None, expires_at=None, tags_csv=None) -> DecisionNote`, `list_decision_notes(date=None, tag=None) -> list[DecisionNote]`.
3. **New router**: `backend/app/routers/decisions.py` with `GET /api/decisions/list?date=...` (owner-only auth via existing `require_user` dependency), `GET /api/decisions/week` (owner-only).
4. **New bot commands**: in `backend/app/bot/commands.py`, add `cmd_note`, `cmd_notes_list`, `cmd_notes_tag`, `cmd_notes_week`. All four route through the existing `TELEGRAM_ALLOWED_USERS` allowlist.
5. **New start-of-service hook**: in `backend/app/bot/startup.py`, add `_maybe_send_start_of_service_digest` that runs when the cook first sends any message after 06:00 Europe/Paris and there is at least one in-window note.
6. **New APScheduler job**: in `backend/app/scheduler.py`, add `weekly_decision_digest` that fires every Monday at 09:00 Europe/Paris. Reuses the existing APScheduler primitive from feature 39.
7. **New Alembic migration**: `alembic/versions/2026_08_08_havemind_decision_notes.py` — creates the `decision_note` table.
8. **New unit tests**: `backend/tests/test_decisions.py` with: append-only invariant, `/note` roundtrip, `/notes list` filter, `/notes week` digest, start-of-service hook trigger condition.
9. **New fixture**: `backend/app/templates/notes.md.j2` — Jinja2 template for the digest markdown (used by the weekly cron and the start-of-service hook).

## Telegram interaction

- **Cook**: `/note <body>` → "OK ✓ note logged as d-7f3a1c. Expires in 24h."
- **Owner**: `/note <body> #tag1 #tag2` → "OK ✓ note d-7f3a1c logged. Expires in 24h. Tags: tag1, tag2."
- **Cook or Owner**: `/notes` → "Today's notes (2): <NN:MM> <role>: <body> [tags: ...]"
- **Cook or Owner**: `/notes tag:lamb-86` → "Notes tagged lamb-86 (3, last 7 days): ..."
- **Owner**: `/notes week` → "Last week's notes (N): <one-line per body>"
- **Cook (start-of-service)**: bot auto-message: "Today's notes (N): <one-line per body>" (only if N > 0).

## Dependencies

- Existing `TELEGRAM_ALLOWED_USERS` / `TELEGRAM_OWNER_CHAT_ID` / `TELEGRAM_COOK_CHAT_ID` env vars (cook + owner allowlist).
- Existing `apscheduler` (already pulled for feature 39).
- Existing `uuid4` import (standard library).
- Postgres 14+ (existing).
- Existing `pytz` for Europe/Paris timezone (existing).
- **No new packages.**

## Open questions

1. **Default expiry**: 24h or 7d? Spec says 24h default with `/note keep` for persistent. Lean: 24h default, explicit `/note keep` (or `expires_at=NULL`) for the "policy decision" use case. Owner can disable.
2. **Owner-only-on-write**: should `/note` be cook-disabled and owner-only? The current proposal allows both. Conservative: allow both, role-filter at read time. Open.
3. **Note collapse**: if a note is older than 7 days and unchanged, should it auto-archive? Spec says no auto-archive; v3 follow-up.
4. **Note-to-StockEntry link**: when the cook writes a note and then 86s the lamb, should the note auto-attach as rationale? Spec says no — they are separate primitives. v3 follow-up.

## Why this matters

The LE31 cookbook is currently an *event log* (StockEntry + Visit + Order), and the LE31 daily recap (feature 39) is a *recap of events*. What it is *not* is a *decision log*. The owner makes 3-5 policy decisions per week that affect how the cook preps and the waiter seats; today those decisions live in the owner's head or in SMS chat. With this feature, the owner makes a decision and the cook sees it tomorrow. The 30-second weekly digest gives the owner a way to review "what decisions did I make this week" without leaving Telegram. This is the smallest useful primitive for the *management memory* gap that no current peer (small restaurant POS) addresses. Total implementation cost: 1 day, 1 new table, 4 new bot commands, 1 cron job, 1 start-of-service hook. Total operational value: closes the "owner says X, cook hears Y" gap that compounds across services.
