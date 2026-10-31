# HANDOFF — 402-rockcut-restaurant-reservation-system

**Status**: defer (v1 vocabulary + two decisions, no build today)
**Date**: 2026-10-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/402-rockcut-restaurant-reservation-system-mit-typescript-nextjs-supabase-rls-real-restaurant-auvingtquatre-reservation-seats-joined-tables-seat-swap-editor-viewer-v1-database-level-permission-enforcement-vocabulary.md`
**LE31 feature gate verdict**: **defer** — vocabulary-only; no code is adopted. The gap is OBSERVED (parent-verified against `backend/app/`); the demand is not. **The artifact's domain (reservations) is out of v1 scope and is deliberately NOT proposed.**

## Trigger policy

This is a **defer artifact** — a vocabulary record plus **two named decisions**. It does **not** start a build.

It surfaces `rockcut/restaurant-reservation-system` (MIT, Next.js + TypeScript + Supabase, in-window by `pushed_at` only) as the **only in-window artifact describing a system actually running in a real restaurant**, and records two rules LE31's charter implies but never makes operational:

1. **The guard must live below the UI** — *"Editor / Viewerの権限制御はフロントエンドだけに依存せず、Supabase RLSでも制御しています"*.
2. **One control, state-dependent intent** — *"予約済みの席をクリックした場合は「予約詳細の確認」を優先し、空席をクリックした場合は「新規予約の席選択」として扱います"*.

**Trigger conditions** — if ANY of these is met, the external coding agent should:

1. Load this artifact, the linked feature file, and the raw README (`/tmp/le31-daily-2026-10-29/parent/rockcut__restaurant-reservation-system__README.md`, Japanese).
2. Load the companion features **388** (table state machine — owns `Table` and `OrderItem.status`), **382** (stock-deduction idempotency — owns a write path a guard would protect) and **397** (menu availability — a state-dependent control on the waiter UI).
3. Load **feature 400** (the same window's idempotency-key / reversal vocabulary — **both are permission-bearing writes**) and **feature 401** (the same window's pending-order reservation vocabulary).
4. Decide, in writing: **(a)** whether a storage-layer guard is required by LE31's charter, and **if so, what mechanism**; **(b)** whether a state-dependent control requires server-read state to be *rendered* or only *enforced*.
5. If (a) is decided "yes, with RLS", the implementation is a **separate, freshly-gated architecture feature** — not this artifact. **Do not** implement it under this contract.
6. If no decision can be made, close this artifact and leave the current (UI-only) permission posture as-is.

**If the trigger condition is NOT met, do nothing.** In particular: **do not** add row-level-security policies, **do not** add a reservation model, and **do not** add a table-join table.

**Disambiguation**: this artifact is about **permission enforcement and state-dependent actions**. It is **not** about the idempotency key or the reversal event (**feature 400**) and **not** about the pending-order reservation quantity (**feature 401**). Three separate artifacts, one window, three different concepts — do not merge them.

## Mandatory inputs

- **Active feature**: `features/402-rockcut-restaurant-reservation-system-…-v1-database-level-permission-enforcement-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-29/`
  - `parent/rockcut__restaurant-reservation-system__repo.json` — direct `GET /repos/`
  - `parent/rockcut__restaurant-reservation-system__README.md` — README, 9,133 B (Japanese)
  - `parent/rockcut__restaurant-reservation-system__tree.json` — file tree, 37 files (incl. `docs/requirements.md`, `docs/database.md`, `docs/api.md`, `frontend/components/Seat.tsx`)
- **LE31 source of truth**:
  - `backend/app/security.py` — the existing JWT + PBKDF2-SHA256 layer. **It proves identity; it does not constrain action.**
  - `backend/app/models.py` — `ItemStatus` (lines 35–40), `Table` (line 64, `__tablename__ = "table_"`), `OrderItem` (line 151)
  - `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **no output** (there is no storage-layer guard anywhere)
- **Charter §3.2** (two fixed surfaces: waiter web UI + cook Telegram bot; fixed stack), **§3.4** (AI may assist staff only, with observable evidence and a non-AI fallback — **a permission question is never an AI question**) — `PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — the seven-check feature gate and the hard invariants (charter §3.2 fixed surfaces, §3.4 AI boundary).
- `le31-v1-feature-pattern` — the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — the source-of-truth discipline on the artifact's README quotes.
- `le31-handoff-spec` — the frozen-contract discipline.

The agent must **NOT** load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The two recorded rules:

- **Guard below the interface** — an action the charter calls *explicit* must be enforced by something that is **not the interface**. Consequence, as the artifact states it: a forbidden change **cannot be made even by going straight at the database**. LE31's current answer is: **nowhere below the UI** — `security.py` authenticates, and every permission rule is a UI convention.
- **State-dependent intent** — one control may resolve to different actions depending on the state behind it. **This rule has a hard dependency on the guard rule:** if the enforcement is only in the UI, the state-dependent branch is a *suggestion*, not a rule.

The recorded out-of-scope observation:

- **Joined tables** — a booking that occupies tables 1+2+3 has **no analogue** in LE31's model (`Table` is one row per table) and LE31 has **no reservation concept at all**. **Recorded, explicitly NOT proposed.**

**Anti-goals, stated so they are not drifted into:**

- **No reservation model, no waitlist, no seat-swap, no table-join table.** §3.2 fixes the surface count and LE31 has no reservation surface. This artifact is excellent and it is still out of scope.
- **No RLS policies** under this contract. If the owner decides a storage-layer guard is required, that is a **separate, freshly-gated architecture feature**.
- **No change to the waiter/cook role split.** The mapping to the artifact's Editor/Viewer is recorded as a **question** (it may well be "neither" — LE31's roles are not permission levels).
- **No adoption of the kana-normalised search** (*"たなか"* / *"タナカ"*) — a nice idea, out of scope.

## Files to touch (when the defer is promoted to build)

**None today.** When promoted:

- `backend/app/security.py` — **only** if the decision is that the *service layer* (not the database) enforces the guard. That is a **separate** architecture decision with its own gate.
- `backend/app/` — the state-dependent action rules, if decision (b) is "rendered from server-read state".
- A new alembic migration under `backend/migrations/versions/` — **only** if RLS is chosen (policies are DDL). **Note the charter's known unresolved migration-strategy inconsistency; surface it, do not settle it by accident.**

**Not in scope under any of these decisions:** `backend/app/models.py` reservation tables, any table-join table, any waiter-UI reservation screen.

## Verification protocol

When promoted, the external coding agent must verify:

1. **The frozen contract fields match the recorded rules** — "guard below the interface" and "state-dependent intent".
2. **If a storage-layer guard is implemented, the forbidden write is attempted DIRECTLY against the database** — bypassing the API, the service layer, and the UI. **An API-level test proves nothing about this rule.** This is the acceptance test that matters.
3. **A state-dependent control produces the correct action for each state**, and the state it reads comes from the **server**, not from a client-side guess.
4. **No permission rule is enforced ONLY in the UI.** Enumerate the permission-bearing writes (a `StockEntry` write, an `OrderItem.status` transition, a `Bill` write) and assert each has an enforcement point **below** the interface — or record explicitly that it does not, and why.
5. **The end-to-end acceptance path is executable in the configured environment**: a user without permission attempts a forbidden write through **every** available path, including a direct database session, and it fails in all of them.
6. **The rollback path is present and reversible**: drop the policies / remove the service-layer checks; no data is lost, because **guards protect writes and never mutate the ledger**.

## Rollback path

- Today: **nothing to roll back** — this defer writes **no** code, **no** schema, **no** policies, and **no** data.
- When promoted (service-layer guard): remove the checks. **Ledger rows written under the guard remain valid** — a guard that is removed does not invalidate history, and **no row is edited or deleted to roll back** (charter §3.3).
- When promoted (RLS): drop the policies. **Note that dropping a policy widens access, not narrows it** — the rollback path must state the access that becomes available, and the owner must accept it explicitly.

## Sign-off gap

No build today. This defer artifact does **not** require owner sign-off; it surfaces a dated, in-window reference and two open decisions.

**The open decisions DO require owner sign-off before implementation** — specifically:
1. **Does LE31's charter require a storage-layer guard, and if so, by what mechanism?** The artifact proves *that* some layer below the UI must enforce; it does **not** prove that Postgres RLS is the right mechanism for a one-restaurant, two-role system. **This is the most important open question in this feature.**
2. **Does a state-dependent control require server-read state to be rendered, or only to be enforced?**

The external coding agent must mirror this contract back to the owner before implementing and **stop if it cannot**.
