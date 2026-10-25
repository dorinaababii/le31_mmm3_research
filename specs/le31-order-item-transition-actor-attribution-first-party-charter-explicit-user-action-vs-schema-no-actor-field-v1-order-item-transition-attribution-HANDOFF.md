# HANDOFF — Feature 379: attribute every `OrderItem` state transition to the actor who made it (conventions *State* invariant vs schema — FIRST-PARTY)

**This is the second `build` pick of the 88-pass series.** It is a gap in LE31's own code, not a reference to someone else's. **Do not defer it.**

**Discovery chain:** Daily Brainstorm 2026-10-25 → the parent read two external READMEs (Feature 380 `boethius68/KitchenLink`, Feature 381 `sajeercherukottayil/Ordova`) plus the in-window design spec `hamidkhan069731-blip/restaurant-erp-system`, all of which treat *who did what, when, from what state* as a first-class record → the parent went and read LE31's own `backend/app/models.py` → found that `OrderItem` carries **no actor field and no transition history**, while `StockEntry.by_user_id` (line 125), `Shift.by_user_id` (line 191) and `Bill.closed_by` (line 168) all exist — three lines apart from the missing one.

**Full evidence record: `features/379-le31-order-item-transition-actor-attribution-first-party-charter-explicit-user-action-vs-schema-no-actor-field-v1-order-item-transition-attribution.md`**

## Active feature path

`features/379-le31-order-item-transition-actor-attribution-first-party-charter-explicit-user-action-vs-schema-no-actor-field-v1-order-item-transition-attribution.md` — **build** (Pick A of Daily Brainstorm 2026-10-25).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When the cook or waiter moves an order item from `new` to `ready` to `served`, the owner wants to be able to tell who made each change, but the schema records only the resulting status and three timestamps, so that the actor is unrecoverable.* The pain is **not inferred** — LE31's own conventions (`le31-conventions/SKILL.md`, hard invariant *State*) state: *"operational transitions are explicit user actions. Do not silently send, serve, close, or reconcile an order."* The schema enforces the *timing* half and not the *attribution* half. Evidence class: **OBSERVED** — parent-run greps, re-runnable in five commands (below). |
| 2 | Viability | ✓ | The change is small and wholly internal: one nullable column, one new append-only table, one service function, one test file. No third-party dependency, no licence question, no traction question (**the subject is LE31's own code**). |
| 3 | Practicability and confidence | ✓ | On-stack: `backend/app/models.py` is SQLModel; `AppUser` and `ItemStatus` already exist; `StockEntry.by_user_id` and `Bill.closed_by` are the **exact pattern to copy**, so there is no new design to invent. **Confidence: high** — the gap is directly observable and the conventions rule specifies the target precisely. **Named rabbit hole:** whether a bot-originated transition may have a null actor — see Open questions 1. |
| 4 | Conflict | ✓ | **No conflict — the change restores compliance with an existing LE31 invariant.** The conventions *State* rule *requires* explicit, attributable user actions. The missing actor is the deviation, and the deviation is what is being removed. **Note the one adjacent tension:** LE31's *Privacy* invariant says "store only data needed for restaurant operations". An actor id on a transition **is** operationally needed (it is the same data already stored on `StockEntry`, `Shift` and `Bill`), so there is no privacy conflict. **Do not extend this into per-guest identity** — v1 guest demographics remain counts. |
| 5 | Outcome + appetite + scope | ✓ | Maps to a v1 build (core operational-state correctness). Maximum time worth spending: **3–5 hours including the table, the service function and the regression tests.** Scope is deliberately: one column, one table, one write path, one test file. **Explicitly NOT in scope:** dropping `OrderItem.status` (see Open questions 2), ticket aging (feature 09), split tender (feature 14), `qty_remaining` (feature 374). |
| 6 | Cost to operational value | ✓ | High, and **the value rises with time**. Value today: disputes about a served item become answerable. Value in six months if deferred: **unrecoverable** — there is no history to back-fill from, only a mutable `status` column and three timestamps. Features 03, 09, 15, 17, 30 and 45 all plan to write to `OrderItem.status`; each one that lands first makes the attribution permanently unavailable. Cost: one day of work, no training, no new surface, no new dependency. |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible: drop the table and the column.** No existing data is affected, because no code writes `OrderItem.status` today (parent-verified). The **only irreversible part is if a selling path lands first** — the transition log cannot be reconstructed retroactively — which is exactly why this is `build` and not `defer`. **Stop evidence:** if the pre-flight below shows a transition write path already exists that records an actor elsewhere, **stop and re-read the contract.** **Review point:** after the first real transition is written in production, confirm the log row and the cached `status` agree. |

**Gate verdict: `build`** — check 1 passes on **observed** evidence, the same standard the 85th-pass first-party pick (feature 374) established.

## Bucket

**v1 (correctness of the core operational-state invariant)** — Pick A of Daily Brainstorm 2026-10-25. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-25 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 38th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**The change itself (ordered — the replacement must exist before the thing it replaces is bypassed):**

- `backend/app/models.py` — **ADD** `class OrderItemTransition(SQLModel, table=True)` with `__tablename__ = "order_item_transition"` and fields `id`, `order_item_id` (FK `order_item.id`, indexed), `from_status: ItemStatus | None`, `to_status: ItemStatus`, `by_user_id: int | None` (FK `app_user.id`), `at: datetime`. **ADD** `by_user_id: int | None = Field(default=None, foreign_key="app_user.id")` to `class OrderItem`. **DO NOT** change `ItemStatus`, `fired_at`, `ready_at`, `served_at`.
- `backend/app/services/__init__.py` — **NEW** (the directory does not exist today; `backend/app/` contains only `__init__.py`, `bot/`, `config.py`, `db.py`, `main.py`, `models.py`, `routers/`).
- `backend/app/services/order_state.py` — **NEW.** One public function `transition(session, order_item, to_status, by_user_id, at=None) -> OrderItemTransition`. It writes the transition row, updates `order_item.status`, sets the matching timestamp, sets `order_item.by_user_id`, commits. **It rejects `by_user_id=None` unless `allow_system_actor=True` is explicitly passed.**
- `backend/app/db.py` — **verify** that `init_db()` creates the new table via SQLModel `create_all`. **Do not assume** — read the file. Per §3.2, v1 uses `init_db()`, not Alembic; `backend/requirements.txt` already pins `alembic>=1.13` but **do not silently introduce Alembic** — follow §3.2's stated v1 policy and record the prod-migration step as known debt.
- `backend/app/bot/cook_bot.py` — **only if** a status write is added: route it through `transition()` and resolve the Telegram user id to an `AppUser`. The file currently carries `# TODO: filter incoming messages to allowed user IDs.` — **this feature does NOT implement that TODO**; it only requires that the actor be resolvable.
- `tests/test_order_transitions.py` — **NEW.** The load-bearing tests (below).

**Do NOT touch (out of scope, explicitly):**

- `backend/app/routers/` — **do not add an orders router, a selling endpoint, or a status-change endpoint.** No selling path is in scope.
- `StockEntry`, `Shift`, `Bill`, `DerivedTip`, `Batch` — **no schema change.** (Feature 374 owns `Batch`.)
- `PROJECT_CHARTER.md` — **no edit required**; the conventions skill already states the invariant. Add a pointer only if the charter's §4.2 schema overview lists tables.
- The Telegram bot's **message surface** — no new commands, no new message types.

## The load-bearing tests

`tests/test_order_transitions.py` must contain, at minimum:

1. **A transition without an actor is rejected** — calling `transition(..., by_user_id=None)` without `allow_system_actor=True` raises. **This is the test that makes the gap impossible to reintroduce silently.**
2. **Two transitions produce two log rows** — with the correct `from_status` / `to_status` / `by_user_id` on each.
3. **`OrderItem.status` equals the last log row's `to_status`** — i.e. the column is a cache of the log, not an independent truth. A cached-column implementation passes test 2 and fails this one.
4. **The log is the history** — after a transition, the *previous* status is still recoverable from the log (this is what the current schema cannot do).
5. **The actor is recorded, not just the status** — assert `by_user_id` on the transition row equals the acting user, and that `OrderItem.by_user_id` matches.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. The observable behaviour here is **the attribution in a running system**: perform a transition through the actual service function, then read back the log and confirm both the row and the cached status.

**The pre-flight that must be re-run before starting (parent-run on 2026-10-25; re-run it — the answer is the whole point of this feature):**

```bash
cd /opt/data/le31_mmm3_research_work
sed -n '/^class OrderItem/,/^class Bill/p' backend/app/models.py   # expect: NO by_user_id / actor field
grep -rn 'by_user_id\|actor\|performed_by\|changed_by\|created_by' --include=*.py backend/
# expect: exactly TWO hits — StockEntry.by_user_id and Shift.by_user_id (plus Bill.closed_by if you grep 'closed_by')
grep -rn 'class .*Transition\|class .*History\|class .*Event\|order_item_event\|status_history' --include=*.py backend/
# expect: NO output
grep -rn 'ItemStatus\.\|\.status = \|status=' --include=*.py backend/
# expect: exactly ONE hit — the declaration at backend/app/models.py:151
```

If the second command now shows a `by_user_id` on `OrderItem`, or the third shows a transition table, **the gap has already been closed by someone else — stop and re-read the feature contract before implementing.**

**Post-implementation, the same commands must show: a `by_user_id` on `OrderItem`, a new `OrderItemTransition` class, and the `status =` grep now hitting `backend/app/services/order_state.py`.** That inversion is the proof of the change.

## Rollback path

`git revert` the commit, or drop the table and the column. **No existing data is affected on revert**, because no code writes `OrderItem.status` today (parent-verified). If a selling path lands before this feature, the rollback becomes an impossible backfill — there is no history to recover the actor from — **which is the entire reason this is `build` and not `defer`.**

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *State* rule first, then *Privacy*) **— this is the invariant being restored**
- `le31-data` — append-only rules (the new transition log is append-only; never update or delete a transition row)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.2 migrations via `init_db()`, §4.2 schema overview)

## Open questions carried into any future build

1. **Can a transition legitimately have no actor?** The only legitimate system actor is the cook bot acting for the cook — and even then the Telegram user id must resolve to an `AppUser`, not stay null. **Owner decision needed** between: (a) every bot action must resolve to a real `AppUser`; or (b) LE31 creates a dedicated `AppUser` row of role `cook` that the bot acts as. **(b) is simpler and matches `config.telegram_allowed_user_ids`** (currently an empty list). The parent has not decided. **Until decided, the service function must reject null actors by default** — the `allow_system_actor=True` escape hatch is the only way through, and it must be used deliberately.
2. **Should `OrderItem.status` be dropped entirely** (pure log, derived status — the same "derive, never store" discipline as Feature 374)? More consistent, but it is a **read-path change** for features 09/15/45, which all read `status` directly. **Recommendation: keep `status` as a cache this pass; drop it in a follow-up.** Do not expand this feature's scope.
3. **Should the transition log carry a denormalised `order_id`?** `OrderItem.visit_id` → `Visit` already gives the path. **Recommendation: no** — do not add a column that can go stale.
4. **Can a transition be reverted** (e.g. `ready` → `preparing` after a mistake)? If yes, the append-only log handles it naturally as a new row — but the **allowed-transition graph must be defined first**, and that is a separate decision.
5. **Does this interact with Feature 374?** **No** — different tables (`OrderItem` vs `Batch`/`StockEntry`). But both features edit `backend/app/models.py`; if both land, the second one re-reads the file. **Feature 374 is still open** (`qty_remaining: int` is still at `backend/app/models.py:106`, re-verified 2026-10-25) — **this feature does not replace it and does not close it.**
