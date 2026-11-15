# Slice contract — `le31-the-billed-floor-card-dereferences-an-absent-subtotal-and-crashes`

## Active feature path

`features/484-le31-the-billed-floor-card-dereferences-an-absent-subtotal-and-crashes-first-party-t-subtotal-tofixed-has-no-undefined-guard-so-a-tap-on-a-billed-table-throws-v1-floor-card-amount-guard.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven under Node v22 against LE31's own shipped `index.html`; confidence **high** for the defect and **medium** for how often a billed table lacks a `subtotal`.

1. **JTBD:** When the waiter taps a billed table on the floor to read its bill, they want the amount, but the handler dereferences an optional field without a guard, so the tap **throws instead of showing anything**.
2. **Viability:** pass — one guard and one fallback message; invisible to the waiter except that it no longer breaks.
3. **Practicability:** pass — no schema change, no stack change, no permission change. Rabbit holes: the fallback must state *why* the amount is unavailable rather than showing `0.00 €` (which would be a wrong number, not a missing one); and the shipped `T4` carries `subtotal: 87.00` while **six of the eight fixture rows carry no `subtotal` at all**, so the fixture is not a reliable guard.
4. **Conflict:** none. It changes no state, no money rule and no transition. It is **not** a duplicate of feature **467** (the fixture/API drift) nor of **465** (money arithmetic) nor of **485** (the field's meaning) — this is **a crash on a code path**.
5. **Outcome/scope:** v1 outcome *the floor view never breaks a waiter's tap*. Cap at the guard and the fallback message. **Do not** redesign the floor card, the fixture, or the bill flow.
6. **Cost/value:** tiny implementation cost (one conditional); the value is that a tap in the waiter's busiest surface does not abort mid-handler. **The cost of the current behaviour is that the waiter sees nothing at all and the console carries a stack trace.**
7. **Circuit breaker:** stop if the floor view is replaced. Revert one file, one region; no data risk.

## Files to touch

- `index.html` — the `onTableClick` function's **billed branch only**.
- A focused test/probe file for the billed branch if the repository's test structure supports it.

**Do not edit** `MOCK_TABLES` — in particular, **do not add a `subtotal` to `T4`**. That would hide the defect rather than fix it, and check 7 of the verification protocol exists to catch exactly that. Do not edit the floor card's markup (feature **24**), the fixture/API drift check (feature **467**), the money arithmetic (feature **465**), or what the `subtotal` field *means* (feature **485**).

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. The guard is **presence-based** — assert the billed branch does not dereference `t.subtotal` unconditionally. **It must use `== null`, not `!t.subtotal`** — a falsy check would silently turn a zero bill into "unavailable".
2. The **absent** case does not throw: a `billed` table with no `subtotal` must not raise, and the message must **contain no number**.
3. The **present** case still shows the amount: `subtotal: 87` → `87.00 €`.
4. **`null` is also safe** — a `billed` table with `subtotal: null` does not throw.
5. **Zero is not "absent"** — `subtotal: 0` → `0.00 €`, **not** the unavailable message.
6. `git diff -- index.html` confirms only the billed branch changed, and that `MOCK_TABLES` is unchanged.

The regression test **must fail against the current handler before the fix is applied** — checks 2, 4 and 5 specifically. **If they pass, the test is not testing the defect.** The check must run in a **browser-free DOM harness** (feature 467 records that the mock-up calls no API, so a server-side test cannot find this).

## Rollback path

Revert the `index.html` billed-branch change. No schema, data, migration, or persistent state is affected. **The one thing a rollback loses is the guard**, and with it the crash returns.

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

Intended as a Feature sub-issue under the 2026-11-15 research issue in project **`le31 v1 — Core MVP` (P-HMM-3)** (this is a v1 pick), label `Feature`, status `Done`. **The workspace contains only three projects — `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research` — so `le31 v2 owner-pains` and `le31 v2-AI` do not exist and must not be invented.** The parent research issue lives in `le31 Research` (P-HMM-1), and the fallback payload records both.

**Linear writes are blocked** (HTTP 400 `invalid_request` — *"You've exceeded the free issue limit for this workspace"*, requestId `a5ac4876ca6bdbbd`; 59th consecutive day). Use the fallback payload in `/opt/data/le31-daily-research-2026-11-15.linear-fallback.json` and record `linear: blocked`. **Do not claim an issue ID that was not returned by Linear.**
