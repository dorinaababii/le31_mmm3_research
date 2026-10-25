# Feature 379 — Attribute every `OrderItem` state transition to the actor who made it (charter/conventions require explicit user actions; the schema records no actor) (build — v1)

> **NEW observation (2026-10-25, parent-verified first-party).** This is **not** a third-party reference. It is a **gap inside LE31's own repository**, found by the parent while reading external project READMEs during the Daily Brainstorm 2026-10-25 pass (see Features 380 and 381). LE31's own conventions (`le31-conventions/SKILL.md`, hard invariant *State*) require: *"operational transitions are explicit user actions. Do not silently send, serve, close, or reconcile an order."* — but **nothing in the schema records who performed a transition on an order item.**
>
> **The evidence, all parent-run on 2026-10-25 (commands in the HANDOFF, re-runnable):**
> 1. `backend/app/models.py` — `class OrderItem(SQLModel, table=True)` declares `status: ItemStatus = ItemStatus.new`, plus `fired_at`, `ready_at`, `served_at`. **There is no `by_user_id`, no `actor_id`, no `performed_by`, no `changed_by` on this class.**
> 2. `grep -rn 'by_user_id\|actor\|performed_by\|changed_by\|created_by' --include=*.py backend/` returns **exactly two hits**: `StockEntry.by_user_id` (line 125) and `Shift.by_user_id` (line 191). Both are on *stock* and *shift* records. **Neither is on `OrderItem`.**
> 3. `grep -rn 'class .*Transition\|class .*History\|class .*Event\|order_item_event\|status_history' --include=*.py backend/` returns **nothing** — there is no transition-history table anywhere in the codebase.
> 4. `grep -rn 'ItemStatus\.\|\.status = \|status=' --include=*.py backend/` returns **exactly one hit**, and it is the *declaration* `backend/app/models.py:151`. **There is no write site for an order-item transition at all** — so the cook bot (`backend/app/bot/cook_bot.py`) cannot currently change an item's status.
> 5. `StockEntry` already carries `by_user_id` and `ref_order_item_id` — **so the ledger knows which order item a stock movement came from, but not which user moved the item.** The attribution exists one hop away and is simply not connected.
> 6. `Bill` carries `closed_by: int | None = Field(foreign_key="app_user.id")` — **the bill records its closer. The item does not record its server.** The asymmetry is inside one file, ~10 lines apart.
>
> **Why this is a `build` and not a `defer`:** the defect is **currently inert** — because no order-item write path exists yet (point 4), nothing is currently lost. But it is precisely the class of defect that gets **frozen in** by the first feature that writes to the field: features 03, 09, 15, 17, 30, 45 and the whole waiter/cook workflow all plan to move items through `ItemStatus`. The first `status = ItemStatus.served` assignment written without an actor argument permanently makes the attribution unrecoverable — because there is no transition history to back-fill from, only a mutable `status` column and three timestamps. **Cheap now, expensive after.**
>
> **Evidence class: OBSERVED.** Every claim above is a command the parent ran on 2026-10-25, and each is re-runnable in five commands (listed in the HANDOFF). Gate check 1 rests on observed evidence, not on an inference.
>
> **Relationship to Feature 374 (the 85th-pass first-party pick):** both are the same shape — a charter/conventions invariant that the schema does not implement. Feature 374 restores *"stock is computed on read, not stored"*; Feature 379 restores *"transitions are explicit user actions"* by making the actor **present**. They are independent: 374 touches `Batch`/`StockEntry`, 379 touches `OrderItem`. Feature 374 is **still open** (the `qty_remaining: int` column is still at `backend/app/models.py:106` — verified again on 2026-10-25) — **this feature does not replace it and does not close it.**
>
> Bucket: **v1 (correctness of the core operational-state invariant)** — Pick A of Daily Brainstorm 2026-10-25. Build verdict: **`build`**. This is the **second** `build` verdict of the 88-pass series.

## Goal

Make `backend/app/models.py` obey the LE31 conventions *State* invariant by **recording the actor on every order-item state transition**, and by making the transition **append-only** rather than a mutable overwrite of a single `status` column.

**The invariant being restored:** every operational transition on an order item is (a) an explicit user action, and (b) attributable to the user who performed it. Today LE31 can record *that* an item reached `served` (via `served_at`), but not *who* served it, and cannot record *how it got there*.

## Scope

**In scope (v1):**
- Add `by_user_id: int | None = Field(default=None, foreign_key="app_user.id")` to `OrderItem`.
- Add an append-only `OrderItemTransition` table recording **every** transition: `order_item_id`, `from_status`, `to_status`, `by_user_id`, `at`.
- Provide one single write path (a service function) that performs a transition, writes the transition row, and updates `OrderItem.status` + the matching timestamp. **No other code path may set `status` directly.**
- A "last transition" convenience read (the current `OrderItem.status` column) stays, so the read path does not change shape for features 09/15/45 — **the column becomes a cache of the transition log, not the source of truth.**
- A regression test that asserts a transition performed without an actor is **rejected**, and that the transition log is the authoritative history.

## Out of scope (v1)

- Retro-fitting actors onto historical rows (there are no historical rows — no write path exists yet).
- Any change to the `ItemStatus` enum values or the order of transitions.
- Ticket aging / "kitchen is X minutes behind" — **already filed as Feature 09**; not re-picked.
- Split-tender / tip work — **already filed as Feature 14** and Feature 05; not re-picked.
- The `qty_remaining` derivation — **already filed as Feature 374**; not re-picked.
- Staff-shift time tracking, payroll, permissions rework.
- **Hash-chaining / tamper-evidence on the transition log.** `laravel-chronicle/core` does this; LE31's `StockEntry` ledger is append-only but **not** tamper-evident. That is a **separate, larger question** (it affects the ledger, not just transitions) and is recorded in `## Cross-section` — **do not bundle it here.**
- Any allergen or dish-metadata work — **Feature 380** owns that vocabulary.
- Any device-discovery or LAN-relay work — **Features 380/381** own that vocabulary.

## Description

Today the schema records the *result* of a transition but neither the *path* nor the *actor*:

```
OrderItem.status   → a mutable column; the previous value is destroyed on write
OrderItem.fired_at / ready_at / served_at → three nullable timestamps, one per status
```

That shape cannot answer the two questions an owner or a dispute actually needs:

1. **"Who moved this item to `served`?"** — unanswerable today.
2. **"Did the waiter or the cook move it to `ready`?"** — unanswerable today; the intermediate state is gone.

The transition log answers both by making the history append-only, in the same spirit as LE31's existing `StockEntry` ledger (`PROJECT_CHARTER.md` §4.3) and the existing `StockEntry.by_user_id` / `Shift.by_user_id` / `Bill.closed_by` fields. **The pattern already exists in this codebase three times.** This feature makes the fourth case consistent with the other three rather than inventing a new mechanism.

**Why an external project prompted this:** the 2026-10-25 brainstorm read two external READMEs (Features 380 and 381) that both describe *who did what, when* as a first-class record — `hamidkhan069731-blip/restaurant-erp-system` (the third-party design spec picked in the same window) specifies an audit log recording *"actor, timestamp and before/after value"* for every price change, void, discount, stock adjustment and permission change; `laravel-chronicle/core` (in-window, MIT, ★127) is a verifiable append-only audit trail. Those projects were the *prompt*; the finding and the fix are LE31's own.

## Data model

```python
class OrderItemTransition(SQLModel, table=True):
    """Append-only history of every OrderItem state change.

    LE31 conventions (State): operational transitions are explicit user actions.
    This table is where 'who did it' lives. OrderItem.status is a cache of
    the last row here; this log is the source of truth.
    """
    __tablename__ = "order_item_transition"

    id: int | None = Field(default=None, primary_key=True)
    order_item_id: int = Field(foreign_key="order_item.id", index=True)
    from_status: ItemStatus | None = None   # None = creation (new -> fired)
    to_status: ItemStatus
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

Plus, on `OrderItem`:

```python
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")  # last transition actor
```

**Field-name note:** `OrderItemTransition` is a **new table**, so the model must not collide with any existing table name. `grep -rn 'class .*Transition' backend/` returns nothing today — verified 2026-10-25.

## Implementation steps

1. **`backend/app/models.py`** — add `class OrderItemTransition`; add `by_user_id` to `OrderItem`.
2. **`backend/app/services/order_state.py`** (new file — note `backend/app/services/` **does not exist today**; `backend/app/` contains only `__init__.py`, `bot/`, `config.py`, `db.py`, `main.py`, `models.py`, `routers/`) — one function:
   ```python
   def transition(session, order_item: OrderItem, to_status: ItemStatus,
                  by_user_id: int | None, at: datetime | None = None) -> OrderItemTransition
   ```
   It writes the transition row, updates `order_item.status`, sets the matching `fired_at`/`ready_at`/`served_at`, sets `order_item.by_user_id`, and commits. It **rejects** a transition with `by_user_id is None` unless an explicit `allow_system_actor=True` is passed (the only legitimate system actor being the cook bot acting for the cook — and even then the bot's Telegram user id must be resolved to an `AppUser`, not left null).
3. **`backend/app/db.py`** — ensure `init_db` creates the new table (SQLModel `create_all` behaviour must be checked, not assumed).
4. **`backend/app/bot/cook_bot.py`** — route any status change through `transition()` and resolve the Telegram user id to an `AppUser` (the file currently has `# TODO: filter incoming messages to allowed user IDs.` — this feature does **not** implement that TODO; it only requires the actor be resolvable).
5. **Regression test** — assert that a transition without an actor is rejected, that two transitions produce two log rows with correct `from_status`/`to_status`, and that `OrderItem.status` equals the last log row's `to_status`.

## Telegram interaction if any

None beyond the existing cook bot. The cook's existing "ready" action must now pass a resolved actor id. **No new bot commands, no new message types.** The Telegram surface stays exactly as-is; only the write path changes.

## Dependencies

- `backend/app/models.py` (edit), `backend/app/db.py` (edit), `backend/app/services/order_state.py` (new), `backend/app/bot/cook_bot.py` (edit — only if a status write is added).
- Existing `AppUser` model and `app_user.id` foreign key (already present).
- Existing `ItemStatus` enum (no change).
- **None on Feature 374** — different tables. But both features touch `backend/app/models.py`; if both land, the second one re-reads the file.

## Open questions

1. **Can a transition legitimately have no actor?** The planned `system` actor (cook bot relaying) needs a decision: either every bot action must resolve to a real `AppUser`, or LE31 gets an `AppUser` row of role `cook` that the bot acts as. **Owner decision needed** — the second option is simpler and matches `config.telegram_allowed_user_ids` (which is currently an empty list).
2. **Should `OrderItem.status` be dropped entirely** (pure log, derived status — the same "derive, never store" discipline as Feature 374)? That is *more* consistent, but it is a **read-path change** for features 09/15/45 which all read `status` directly. **Recommendation: keep `status` as a cache this pass, drop it in a follow-up.** Do not expand this feature's scope.
3. Does the transition log need an `order_id` denormalised column for cheap "show me everything that happened to this order" reads? `OrderItem.visit_id` gives the path via `Visit`.
4. Should a transition ever be *reverted* (e.g. `ready` → `preparing` after a mistake)? If yes, the log handles it naturally as a new row — but the allowed-transition graph must be defined first.

## Why this matters

LE31's single most-cited safety principle is that **no operational transition happens silently**. Today LE31 enforces *half* of that: the transition cannot happen silently in *time* (timestamps exist), but it can happen silently in *attribution* (no actor). The two halves are the same promise, and one of them is missing.

The cost asymmetry is what makes this a `build` now rather than a `defer`:

- **Today:** one nullable column and one table. Roughly a day's work. No consumer reads them yet, so there is no migration cost and no behavioural change to any existing surface.
- **After the first selling path ships:** the attribution is **unrecoverable**. There is no history to back-fill from — only a mutable `status` column and three timestamps. Any dispute ("the waiter says the customer already paid, the cook says the item was never served") becomes permanently unanswerable, and LE31's own ledger discipline (§4.3's "never update or delete") cannot be applied retroactively to a column that was never append-only.

**This is the second first-party defect in two passes.** The 85th pass found the `qty_remaining` contradiction by reading an external README and then reading LE31's own schema. This pass found the missing actor by reading two external READMEs that specify actor-and-timestamp audit records and then reading LE31's own schema. Both times the external artifact was a *prompt*, not the finding. **The finding is always in `backend/app/models.py`, and it takes about ninety seconds to look.** Features 03, 09, 15, 17, 30 and 45 all plan to write to `OrderItem.status`; every one of them makes this more expensive to fix later.

## Cross-section

Two external artifacts in the 2026-10-25 window (read by the parent, quoted as facts about *those* projects, not as claims about LE31):

- `hamidkhan069731-blip/restaurant-erp-system` (MIT, ★0, in-window by both `created_at` and `pushed_at` 2026-10-17) — its design spec lists an audit log recording *"actor, timestamp and before/after value"* for every price change, void, discount, stock adjustment and permission change. **Third-party design-specification, not adopted code** — the repo is a design document and roadmap, with no implementation.
- `laravel-chronicle/core` (MIT, ★127, in-window by `pushed_at` 2026-10-23, PHP/Laravel — **off-stack**) — verifiable append-only audit trails with hash chaining. **Vocabulary reference only**; LE31 does not adopt PHP, Laravel, or hash-chained Merkle roots (LE31's ledger is append-only but not tamper-evident — a separate question, and one the `StockEntry` table already answers with a plain append).

**The convergence:** three independent projects in one 30-day window — the design spec, the Laravel audit library, and the two smartphone-first POS apps in Features 380/381 — all treat *who did what, when, and from what state* as a first-class record rather than a debugging nicety. LE31 treats it as optional.
