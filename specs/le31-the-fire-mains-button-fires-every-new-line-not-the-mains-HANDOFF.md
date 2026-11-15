# Slice contract — `le31-the-fire-mains-button-fires-every-new-line-not-the-mains`

## Active feature path

`features/483-le31-the-fire-mains-button-fires-every-new-line-not-the-mains-first-party-the-shipped-button-is-labelled-fire-mains-and-fires-every-new-line-regardless-of-category-v1-course-fire-filter.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven under Node v22 against LE31's own shipped `index.html`; confidence **high** for the defect and **medium** for demand frequency (no operator incident was observed).

1. **JTBD:** When the waiter taps *Fire mains* to send the main courses to the kitchen, they want **only the mains** sent, but the button fires **every** `new` line including drinks and desserts, so the kitchen receives courses the guest has not ordered yet.
2. **Viability:** pass — one filter and one button pair in one file; nothing for staff to operate or administer; no new command.
3. **Practicability:** pass — the fixed stack is untouched; **the category data is already present** in `MOCK_MENU` (`Mains` / `Sides` / `Drinks` / `Desserts`), so no schema change and no new field are required. Rabbit holes: (a) whether "mains" means the `Mains` category or a course sequence — the spec's own wording (*"send all mains now, hold desserts"*) is category-shaped and the fixture's categories make it literal; (b) the screen has **no** category on an **order line** (`state.visit.items` carries `menu_item_id`, `name`, `qty`, `unit_price`, `status` — **no `category` field**), so the line must be joined to `MOCK_MENU` by `menu_item_id`.
4. **Conflict:** none. It restores a distinction LE31's own informal spec (`features/02-order-taking.md`) already asked for and the charter does not contradict. It does **not** touch the FSM, the bill, the money rules, or feature 476's `addToOrder` defect. **It must not introduce `course`** — feature 430 records the charter's silence on sequencing as deliberate.
5. **Outcome/scope:** v1 outcome *the waiter can send the right courses to the kitchen*. **Cap the scope at the filter and the restored second button.** Do **not** build a course/sequencing model.
6. **Cost/value:** small implementation cost; the value is avoiding the kitchen preparing courses the guest has not ordered and the waiter having to re-fire or retract them. Frequency is not observed — **the defect is certain and its frequency is unknown.**
7. **Circuit breaker:** stop if the order-taking surface is replaced before implementation (feature 02's rewrite). Revert one file, one region. **No data at risk** — no persisted state changes.

## Files to touch

- `index.html` — the `btn-fire` button, the `btn-fire` click handler, and a named filter helper. **Read `MOCK_MENU` for the category lookup; do not edit it.**
- A focused test/probe file for the fire filter if the repository's test structure supports it.

**Do not edit** the waiter money arithmetic, the seat form, the fixture statuses, the floor grid, the per-table order state, the sold-out rendering, or the quantity-phase logic owned by features **465, 466, 467, 474, 475** and **476**. **Feature 476 explicitly says *"Do NOT touch: … the `btn-fire` handler"* — this contract touches exactly that handler, so the two must be sequenced, not developed in parallel against the same file.**

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. The filter is **named and callable** — a helper returns the mains set for a given `state.visit.items`.
2. The mains control fires **mains only**: with one `Mains`, one `Sides`, one `Drinks` and one `Desserts` line all at `status: 'new'`, invoking it transitions **only the `Mains` line** to `preparing`.
3. `Fire all` still fires **everything**.
4. The **alert tells the truth** — it must not say "all new items" when only mains were fired.
5. A **category-less line** (a `menu_item_id` that does not resolve in `MOCK_MENU`) must not be fired by the mains control and **must not throw**. The implementer records what `Fire all` does with it.
6. `git diff -- index.html` confirms only the fire-control region changed.

The regression test **must fail against the current handler before the fix is applied** — checks 2 and 4 specifically. **If they pass, the test is not testing the defect.** The implementer must **record which direction was taken** (filter by category, or rename the button and correct the spec) and must not introduce `course`.

## Rollback path

Revert the `index.html` fire-control change (handler, button, helper). No schema, data, migration, or persistent state is affected. **The one thing a rollback loses is the filter rule**, and the drift returns with it.

## Mandatory LE31 skill list

- `le31-conventions`
- `le31-v1-feature-pattern`
- `development`
- `speckit-specify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `verify-before-fixing`
- `pre-merge-review`

## Linear reference

Intended as a Feature sub-issue under the 2026-11-15 research issue in project **`le31 Research` (P-HMM-1)**, label `Feature`, status `Done`. **The workspace contains only three projects — `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research` — so this v1 pick is attached to `le31 v1 — Core MVP` (P-HMM-3) per the feature-pipeline skill; the parent research issue lives in `le31 Research` (P-HMM-1), and the fallback payload records both.**

**Linear writes are blocked** (HTTP 400 `invalid_request` — *"You've exceeded the free issue limit for this workspace"*, requestId `a5ac4876ca6bdbbd`; 59th consecutive day). Use the fallback payload in `/opt/data/le31-daily-research-2026-11-15.linear-fallback.json` and record `linear: blocked`. **Do not claim an issue ID that was not returned by Linear.**
