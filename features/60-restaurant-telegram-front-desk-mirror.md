# Feature 60 — Restaurant Telegram Front Desk Mirror

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm
> 2026-08-12 (cross-section pick C, **parking-lot / deferred pending
> charter revision**).
> 2026-08-12 · **Bucket**: v2 owner-pains (deferred to v2.5+).
> **One-line**: an *inbound* mirror of feature 56
> (`walk-in-front-desk-channel`) — watch the existing Telegram group
> that staff already use for live updates, parse orders / comps /
> voids / stock-outs from chat, and append them as new
> `StockEntry` / `VoidRationale` / `OrderItem` rows.

> **Status**: parked today. Charter §5 currently forbids PII in v1
> (privacy stance on customer-side chat). This pick requires the same
> charter revision as feature 56. Until the charter is revised and the
> privacy stance is signed off, no coding agent should start this slice.
> The file is written so the artifact is not lost — per the
> `le31-daily-brainstorm` skill's "parking-lot" rule.

## Goal

Most small restaurants already have *one* shared chat — a cook + owner
+ manager private group — where staff type:

- *"Focaccia comp for the birthday table (cook-2)"*
- *"Lamb 86ed at 21:30, ran out"*
- *"2 × lamb ragu at table 4"*
- *"Sold out: osso buco for the night"*

Today, those messages live *only* in chat. The cook remembers them.
The owner reads them with a delay. `StockEntry`/`VoidRationale` rows
are written by separate actions in the LE31 UI. The data is split.

`restaurant-telegram-front-desk-mirror` watches that chat and parses
those messages to the same append-only `StockEntry` /
`VoidRationale` / `OrderItem` ledger. The LE31 UI does not change.
Telegram chat becomes the *primary input surface* for the data the
cook already writes there.

It is the **inbound** half of feature 56 (`walk-in-front-desk-channel`,
yesterday's pick B). 56 lets the *restaurant* talk to the *customer*
via Telegram. This pick lets the *staff chat the restaurant already
uses* talk to the *LE31 ledger*. Both pieces together turn the
existing Telegram group into the single real-time ledger.

## Scope

**In scope (v2 owner-pains, M effort, deferred):**

- A new module `backend/app/services/chat_ingest.py` (NEW) with
  three pure functions:
  - `parse_message(text: str, sender: UserMeta) -> Optional[
    LedgerEvent]` — deterministic regex + keyword parser.
    Returns one of `None | CompEvent | VoidEvent |
    StockoutEvent | OrderEvent`.
  - `ledger_event_to_row(event: LedgerEvent, source_msg_id: str)
    -> StockEntry | VoidRationale | OrderItem` — pure projection.
  - `audit_link(event: LedgerEvent) -> AuditLog` — links back to
    the source message id with sha256 hash.
- A new `aiogram` handler in `backend/app/bot/cook_bot.py` that
  registers a `Message` listener on the configured staff group(s)
  only (whitelist via `STAFF_GROUP_CHAT_IDS` env var, list of int).
- One new config knob `CHAT_INGEST_ENABLED = False` (default OFF
  in v1 deploy; flip ON only after privacy stance signed off).
- `backend/tests/test_chat_ingest.py` (NEW) — 5 fixtures covering
  each event type and one ambiguous-input fallback.
- `backend/README.md` — note the privacy posture and the
  whitelist.

**Out of scope (v2.5+, deferred):**

- **Customer-side messages.** This pick is *staff-only*. Inbound
  from customer-side chats is feature 56.
- **LLM parsing.** The parser is regex + keyword (deterministic),
  not LLM. LLM-fallback parsing is a v3 follow-up.
- **Image / voice message handling.** Out of scope at v2.5.
- **Editing / undoing parsed rows.** Out of scope: each parsed row
  gets an `AuditLog.undoable=True` flag, but the UI to *act* on
  undo is feature 47 (`decision-rationale-mixin`) or a v3 follow-up.

## Description

The strongest in-window evidence today is:

1. **`weebzone/ForwardX`** (22★, pushed 2026-08-03, Android) —
   *Always-on Telegram chat-to-chat forwarder with filtering.*
   Architecturally identical to "wire a chat to a system, with
   filters". Confirms this is a solved pattern, not new ground.
2. **`BethanyJep/Safaricom-Decode-Agents-Workshop`** (16★, pushed
   2026-07-16) — *Bilingual AI agent for Savanna Bites restaurant,
   Nairobi.* Direct restaurant anchor: a bilingual chatbot for
   a real small restaurant exists in OSS today.
3. **OpenAlex `WhatsApp como ferramenta de atendimento na hotelaria`**
   (W7197042220, 2026-07-24) — empirical evidence that messaging
   channels *are* the front desk in small hospitality. Already cited
   in feature 56 (yesterday's pick B). Anchor that the *operator-pain
   shape* is real.

This pick asks: if feature 56 turns the *customer* ↔ restaurant link
into a ledger-aware channel, what about the *staff chat the
restaurant already uses*? The staff chat already has the right
messages — lamb 86ed, focaccia comp, sold out — in natural language.
Wiring that to the same ledger is a one-way bridge.

## Data model

No schema change. Reuses:

- `StockEntry` (feature 03) — for stockout events.
- `VoidRationale` (feature 37) — for comp events.
- `OrderItem` (existing) — for order events.
- `AuditLog` (feature 30) — for the source-message link.

A new optional column on `AuditLog.source_message_id` (text, nullable)
is the *only* change. Implementation can ship without the column;
the column is optional v3 hardening.

## Implementation steps

1. Add `backend/app/services/chat_ingest.py` — three pure
   functions. ≤250 lines of code.
2. Add `aiogram.Message` handler in `backend/app/bot/cook_bot.py`
   that fans into `chat_ingest.parse_message`. Register only for
   the whitelisted chat ids (~5 lines).
3. Add `CHAT_INGEST_ENABLED` and `STAFF_GROUP_CHAT_IDS` to
   `backend/app/config.py`.
4. Add `backend/tests/test_chat_ingest.py` (5 fixtures).
5. Add `backend/README.md` section that explicitly states: *"This
   pick is parked until the charter §5 privacy revision
   (customer-side PII posture) is signed off. See
   `charter.PRIVACY.md`."*

> All of steps 1-5 can ship in a single PR **as long as
> `CHAT_INGEST_ENABLED=False`** is hard-coded. The slice is
> dead-code-on-arrival if not enabled. This preserves the artifact
> without violating the charter.

## Telegram interaction if any

- **Inbound**: an `aiogram` handler registered on the
  `STAFF_GROUP_CHAT_IDS` whitelist. Listens for messages with
  parsed-able content. Posts nothing to the source chat (silent).
- **Outbound**: when a parse succeeds, the system posts to the
  *owner* chat only (NOT back to the staff chat) with a one-line
  summary: *"Captured from cook-2: focaccia comp, table 6 →
  VoidRationale #392."* This is to make the capture observable.
- **No new commands.** Disabled by default.

## Dependencies

- **Feature 30** (`append-only-audit-redirect`) — every parsed row
  gets an `AuditLog` entry.
- **Feature 47** (`decision-rationale-mixin`) — for the
  `VoidRationale` schema.
- **Feature 56** (`walk-in-front-desk-channel`) — for the
  *outbound* half of the same pattern.
- **A charter revision** — the LE31 charter §5 privacy revision
  must explicitly include *"telegram chat ingest of staff messages
  in a private staff-only group is permitted, and no PII from
  customer-side chats is captured."* Until this revision is signed
  off, `CHAT_INGEST_ENABLED` stays `False`.

No new pip dependencies. No mandatory schema change.

## Why this matters (today, parked)

In-window evidence is strong. The pattern has an OSS precedent
(`ForwardX`), a restaurant anchor (`Safaricom-Decode-Agents-
Workshop`), and academic evidence (W7197042220). The
implementation is ≤1 week.

But the privacy posture is the blocker: even though this pick is
*staff-only*, it sets the precedent for how LE31 handles inbound
text streams. That precedent must be on the record *before* the
code is written — and the charter §5 revision that gates feature
56 also gates this pick.

So this pick is parked today. The file is committed so the
*artifact* is durable. A future brainstorm (or a calmer day) can
pick it up once the charter is revised.

## Open questions

- Which chat ids constitute "the staff group"? v1 is single-group;
  multi-group is a v3.
- Should the parsed-event confirmation be sent to the *owner* chat
  or the *staff* chat? Recommendation: owner only at v1; staff chat
  is the source of truth, owner chat is the audit surface.
- Is the regex parser good enough? v1 yes; v2 keyword-fallback LLM
  parser is feature 61 (TBD).

## Evidence (recorded)

- **Cross-section anchor 1**: `weebzone/ForwardX` (22★, pushed
  2026-08-03, Android). Read at
  `/tmp/le31-brainstorm-2026-08-12/gh_topic_telegram-bot.json`.
- **Cross-section anchor 2**: `BethanyJep/Safaricom-Decode-Agents-
  Workshop` (16★, pushed 2026-07-16) — bilingual restaurant AI
  agent.
- **Literature anchor**: OpenAlex `Utilização do WhatsApp como
  ferramenta de atendimento na hotelaria` (W7197042220,
  2026-07-24).
- **Restaurant anchor**: `waifuengineer/taller_restaurant_telegram`
  (12★, pushed 2026-07-16) — concrete restaurant Telegram bot
  precedent.

## LE31 gate verdict (recorded)

**parking-lot**: *Strong evidence; private decision blocked by
charter §5. Revisit when charter revision is signed off.*

Evidence precondition: **observed** (4 in-source anchors today:
ForwardX just-pushed 2026-08-03, Safaricom-Workshop 2026-07-16,
W7197042220 2026-07-24, waifuengineer 2026-07-16).
Confidence: **high**.

Decision rationale (per `skills/le31-conventions/SKILL.md`):

- **1. Raison d'être / JTBD**: "When the cook pings in the staff
  Telegram group, the owner wants to *trust* the chat as the
  source of truth, but struggles because the chat isn't recorded,
  so that the owner can review decisions without re-typing."
- **2. Viability**: Owner can read chat + Telegram. No hidden
  admin. ✓
- **3. Practicability**: Fits fixed stack. aiogram already
  integrated. **Confidence: high.**
- **4. Conflict**: Charter §5 currently forbids PII in v1.
  *Hard conflict* — must be resolved before code. →
  **Parking-lot.**
- **5. Outcome / appetite**: v2 owner-pains, M effort (≤1 week).
- **6. Cost to operational value**: Compared to the operational
  value (single-source-of-truth ledger), the cost is small. But
  the privacy risk is non-zero until the charter posture is on
  the record.
- **7. Circuit breaker**: Feature flag `CHAT_INGEST_ENABLED=False`
  by default. Reversible by env-set.
