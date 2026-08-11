# walk-in-front-desk-channel — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/56-walk-in-front-desk-channel.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `56`
- Slug: `walk-in-front-desk-channel`
- Contract file: `features/56-walk-in-front-desk-channel.md`
- Bucket: **v2 owner-pains** (REQUIRES charter §5 revision before code
  is written; see Blockers)
- Linear parent: HMM-62 (Brainstorm 2026-08-11 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build (v2)** with one hard precondition: charter §5
revision signed off before any line is written. (Confidence: high;
evidence: OpenAlex W7197042220 + architectural precedent
`djblack1209-coder/OpenClaw-Bot`.)

Evidence precondition: **observed** (4 in-source anchors today:
OpenAlex W7197042220; HN Ventora mention; `djblack1209-coder/OpenClaw-Bot`;
`indmdev/Free-Telegram-Store-Bot` 146★). Confidence: **high** on the
operator pain, **medium** on the privacy posture change.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
PROJECT_CHARTER.md                               # EDIT §5: add v2 customer-pseudonymity stance (BLOCKER, see Blockers)
backend/app/config.py                            # NEW: TELEGRAM_CUSTOMER_BOT_TOKEN
backend/app/models.py                            # NEW: CustomerChannel, CustomerChatLine SQLModel
backend/app/bot/customer_bot.py                  # NEW: customer-side aiogram bot (/start, /menu, /waitlist, /close)
backend/app/bot/customer_bridge.py               # NEW: bridge (customer_bot <-> cook_bot), appends to CustomerChatLine
backend/app/bot/cook_bot.py                      # EDIT: add /reply <handle>, /walkin forward, /walkin block commands
backend/app/main.py                              # EDIT: register customer_bot dispatcher (1 line)
backend/alembic/versions/<new>_customer_chat.py  # NEW migration (one migration, two tables)
backend/scripts/list_open_customer_channels.py   # NEW: owner-side read-only CLI
backend/tests/test_customer_chat_line.py         # NEW: append-only tests
backend/tests/test_customer_bot_e2e.py           # NEW: bridge tests
backend/README.md                                # note the customer-bot onboarding + new env vars
```

No new pip dependencies. aiogram v3 is already imported.

## Endpoints and contracts added

No new HTTP routes. All logic lives in the customer-bot + bridge +
cook-bot command handlers.

Two new SQLModel tables (one Alembic migration):

```python
# backend/app/models.py

class CustomerChannel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cook_chat_id: int = Field(index=True)         # the cook/owner-facing chat where the bridge forwards lines
    customer_handle: str = Field(index=True)      # Telegram @username (no PII; see charter §5 v2)
    opened_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    last_msg_at: datetime | None = Field(default=None)
    status: str = Field(default="open", index=True)  # 'open' | 'closed' | 'escalated'
    closed_at: datetime | None = Field(default=None)
    closed_by: str | None = Field(default=None)   # 'customer' | 'cook' | 'system'


class CustomerChatLine(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    channel_id: int = Field(index=True)
    customer_handle: str = Field(index=True)
    line_text: str = Field(max_length=4000)
    line_kind: str = Field(index=True)            # 'customer_msg' | 'cook_reply' | 'system_note'
    ref_order_item_id: int | None = Field(default=None, index=True)
    ref_walkin_pin_id: int | None = Field(default=None, index=True)
    at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")), index=True)
    by_role: str = Field(index=True)              # 'customer' | 'cook' | 'system'

    __table_args__ = (
        # append-only enforced via SQLAlchemy event listener (mirror feature 49 listener pattern).
        # No UPDATE / DELETE listeners at v1 cut — listener is added by the existing events module.
    )
```

Append-only: rows never updated, never deleted. The bridge enforces the
rule by code path; the existing `events/` module adds a SQLAlchemy
listener (mirror feature 49's pattern).

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "customer_channel",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cook_chat_id", sa.BigInteger, nullable=False),
        sa.Column("customer_handle", sa.String(64), nullable=False),
        sa.Column("opened_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_msg_at", sa.DateTime(timezone=True)),
        sa.Column("status", sa.String(16), nullable=False, server_default="open"),
        sa.Column("closed_at", sa.DateTime(timezone=True)),
        sa.Column("closed_by", sa.String(16)),
    )
    op.create_index("ix_customer_channel_cook_handle",
                    "customer_channel", ["cook_chat_id", "customer_handle"])
    op.create_index("ix_customer_channel_status",
                    "customer_channel", ["status"])

    op.create_table(
        "customer_chat_line",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("channel_id", sa.Integer, nullable=False),
        sa.Column("customer_handle", sa.String(64), nullable=False),
        sa.Column("line_text", sa.String(4000), nullable=False),
        sa.Column("line_kind", sa.String(16), nullable=False),
        sa.Column("ref_order_item_id", sa.Integer),
        sa.Column("ref_walkin_pin_id", sa.Integer),
        sa.Column("at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("by_role", sa.String(16), nullable=False),
        sa.ForeignKeyConstraint(["channel_id"], ["customer_channel.id"], name="fk_customer_chat_line_channel"),
    )
    op.create_index("ix_customer_chat_line_channel_at",
                    "customer_chat_line", ["channel_id", "at"])
    op.create_index("ix_customer_chat_line_handle_at",
                    "customer_chat_line", ["customer_handle", "at"])

def downgrade():
    op.drop_table("customer_chat_line")
    op.drop_table("customer_channel")
```

## Endpoints and bot commands added

**Customer bot (`customer_bot.py` — new aiogram dispatcher):**

- `/start` — opens a `CustomerChannel` row if none open for the
  customer's `@handle`; otherwise resumes. Greets with the 1-line
  "Welcome — answer questions about waitlist, menu, hours. Replies come
  from the cook in <2 min."
- `/menu` — returns today's menu in text, sourced from `MenuItem`
  where `is_active=True`.
- `/waitlist` — returns the customer's current position in the walk-list
  (the pin row from feature 33) if they are on it; else "You are not on
  the waitlist."
- `/close` — closes the channel. Either party can issue it.

**Cook bot (existing `cook_bot.py`) — three new commands:**

- `/reply <handle> "text"` — appends `cook_reply` row, forwards to
  customer.
- `/walkin forward <pin_id> "text"` — appends `cook_reply` row tied to
  that walkin pin, forwards to customer.
- `/walkin block <handle>` — marks the customer's most recent
  `CustomerChannel` row as `escalated`, freezes any new channels from
  the same `@handle` for 24 hours.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test the bridge: customer sends "table for 4 at 20:30" →
   asserts 1 `CustomerChatLine` row with `line_kind='customer_msg'`
   exists, asserts the cook-side forward is dispatched.
2. Append-only test: attempt `UPDATE` and `DELETE` on `CustomerChatLine`
   from a test fixture; assert both raise (mirroring feature 49 test
   pattern).
3. Bot test: `/reply @alice "yes"` appends a `cook_reply` row with
   `by_role='cook'` and triggers the outbound send via mocked aiogram
   API.
4. End-to-end test: `/waitlist` returns the expected position for a
   fixture `WalkinPin` row.
5. Privacy test: confirm `customer_handle` column contains only
   `@username` strings (regex check), never phone numbers, never email
   addresses.

After implementation, run the parent's verify-before-fixing protocol
on the slice branch.

## Rollback path

- Migration is reversible (two `op.drop_table` calls).
- The customer bot is a separate aiogram dispatcher, fully isolated —
  feature-flag it in `main.py` behind `TELEGRAM_CUSTOMER_BOT_ENABLED=1`
  (default OFF until charter §5 is revised).
- Cook-bot new commands are additive and gated behind the same flag.
- Reversible in <10 min per deployment: feature-flag OFF + alembic
  downgrade + stop the customer-bot dispatcher.

## Hard blockers (see Blockers in contract)

**Charter §5 revision must be signed off BEFORE the first line of code
is written.** Without the revision, the `@username` pseudonymity stance
is undocumented and the slice is in scope creep.

The research parent has flagged this in HMM-62 and in the report under
"Blockers" for Pick B.

## What is explicitly NOT in this slice

- Phone-number identity (PII). Not in scope at v2.
- Voice messages. Not in scope at v2.
- Image attachments. Not in scope at v2.
- Multi-restaurant routing. v3.
- Auto-translation. v3.
- Spam filtering beyond `/walkin block`. v3.
