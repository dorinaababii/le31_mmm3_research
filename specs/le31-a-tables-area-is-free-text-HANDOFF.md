# HANDOFF — Feature 460: a table's area is free text

> **Slice contract for the coding agent.** Feature: `features/460-le31-a-tables-area-is-free-text-main-main-and-main-are-three-areas.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed against LE31's real schema on 2026-11-08).
> Filed by: Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass), Pick B.

---

## 1. The active feature path

```
features/460-le31-a-tables-area-is-free-text-main-main-and-main-are-three-areas.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 431 / 455 / 404 / 442 / 453, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | Executed against LE31's real schema. Two tables with `section="Main"` and `section="main"` → **both ACCEPTED**; `SELECT DISTINCT section FROM table_` → **`['Main', 'main']`**; `PRAGMA table_info(table_)` shows `section VARCHAR`, **notnull=0, no UNIQUE**; `PRAGMA index_list(table_)` → **`[]`**. |
| 2 | The defect is in LE31's own code | **PASS** | `backend/app/models.py` line 68: `section: str = "main"` — a bare annotation with a default, **no `Field()`, no constraint, no index**. |
| 3 | No filed feature owns it | **PASS** | Sweep over **947** feature contracts + HANDOFFs: `floor.{0,30}collision` → **0**, `coordinate.{0,40}unique` → **0**, `overlapping table` → **0**, `Table.section` outside model-quoting code blocks → **0**. |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | Feature **431** owns `MenuItem.category` (a *different column*, same shape). Feature **455** owns `Table.label` (the *same table*, a different column, and a `UniqueConstraint` — this slice adds **no constraint**). **Independent, reviewable units.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a broken floor plan. **No route in the shipped backend creates a table at all** (`routers/` contains only `tables.py`, with no create route), so no inconsistent section can exist in a database this code built — **yet**. |
| 6 | It is cheap now and expensive later | **PASS** | One helper, one decision, one test. **No schema change** under the recorded default. Expensive later: the moment the table-creation route ships, a typo in `section` is **invisible on the floor** — the table is in the right place with the right seats, just in a group the query did not return. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it does NOT fire, and that is the finding** | **No feature is about to write `Table.section`.** The reason it is cheap is precisely that nothing owns it — **so it must be landed before the table-creation route exists.** |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as Pick A: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `backend/app/config.py` | **The decision record** — whether the vocabulary is fixed or open, and the case rule | **One home.** Do not put the vocabulary in a DDL string (see §5.1). |
| `backend/app/services/tables_service.py` — **or `backend/app/models.py`** if no services directory exists | **Add `canonical_section(raw: str \| None) -> str`** | **One helper, one definition.** Record which path you chose. |
| The table write path — **there is none today** | **Add the call site** | **The shipped backend has no route that creates a table.** The helper may have no call site today — **that is the point.** Record the intended call site in your report. |
| `features/431-le31-menu-item-category-is-case-sensitive-free-text-first-party-three-spellings-of-one-category-are-three-categories-v1-category-canonicalisation.md` | **One line** — name this feature | **If the mechanisms match, they should share ONE helper, not two copies.** |
| `tests/` (whatever the repo's test path is — **check**) | **One regression test** | Two tables, `"Main"` and `"main"`, must yield **one** distinct `section`. |

**Do NOT touch:** `Table.label` (feature 455), `MenuItem.category` (feature 431), `Table.status` (feature 388), `Table.seats` (feature 414), `Table.x` / `Table.y` (**see §5.2 — not this slice**), any `CHECK` constraint (feature 404), `index.html` (features 01 / 24).

## 4. The implementation, in order

1. **Decide and record the mechanism** — canonicalise-on-write, a fixed vocabulary, or both. **Recorded default: canonicalise-on-write with an OPEN vocabulary** (feature 431's option (a): *"A restaurant that adds a 'Kids' section should not need a code change."*). **Do not start implementing before the decision is recorded.**
2. **Record the case rule** — *Recorded default: **case-insensitive** — the stored value is lower-cased and stripped.* **See §5.1 for why the case rule must not be left to the database.**
3. **Add `canonical_section()`** — one helper, one home, with the comment block from the feature.
4. **Call it at the write path** — wherever a `Table` row is created or its `section` is updated. **If there is no call site today, say so explicitly in your report** — do not invent a route.
5. **Write the regression test** — it must **fail on today's code** (two distinct sections) and pass after.
6. **Amend feature 431 by one line.**
7. **Record what was and was not verified** in this HANDOFF (see §6).

## 5. The four things that will go wrong if nobody tells you

1. **Putting the vocabulary in a `CHECK` constraint string.** Two copies — `config.py` and the DDL — **will drift**. And feature **427**'s finding applies: SQLite never enables `PRAGMA foreign_keys`, and a `CHECK` on a non-`STRICT` table (feature **404**) is not portable. **Application-level validation is primary; a `CHECK` is optional reinforcement only** — feature **411**'s precedent, applied to a string.
2. **Leaving the case rule to the database.** **SQLite's default `BINARY` collation and Postgres's default collation do not agree** on `"Main"` vs `"main"`. A constraint that differs between dev and prod is exactly the defect class feature **453** filed. **Normalise to lower case on write, in Python**, so the comparison is a plain `=`.
3. **Writing a data migration to fix existing rows.** **Do not.** The helper affects writes only. **A data migration is feature 446's territory** and feature **409** owns the open-decisions register. **Recorded in the feature's Open questions 3 so nobody reads the omission as an oversight.**
4. **Adding the floor-map coordinate uniqueness.** `(x, y)` is **also** unconstrained — two tables may sit at the same spot (executed: **2** rows at `(3, 7)`), and `PRAGMA index_list(table_)` is `[]`. **That is a `UniqueConstraint` over a coordinate pair — a different mechanism from a spelling rule — and it is owned by no feature.** **It is recorded in the feature's Open questions 5 so the next pass files it as its own slice.** **Do not bolt it on here:** two rules in one contract make both harder to review, and this slice's mechanism (normalise a string) cannot express a coordinate constraint anyway.

## 6. Verification protocol

Four offline commands, plus the executed test:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The helper exists and has exactly ONE definition.
grep -rn "def canonical_section" backend/ | wc -l         # must be 1

# 2. It is called somewhere (the write path).
grep -rn "canonical_section(" backend/ | wc -l             # >= 2 (def + call site)

# 3. There is no SECOND copy of the vocabulary in a DDL string.
grep -rn "CHECK" backend/app/models.py | grep -i section   # must print nothing

# 4. The corpus agrees: the area rule is now owned.
grep -rn "Table.section" features/ | wc -l                 # must now hit 460
```

**The executed regression test** — build the real schema, insert two tables with `section="Main"` and `section="main"`, and assert `SELECT DISTINCT section FROM table_` returns **one** value. **It must fail before the change and pass after.**

**The negative control** — make `canonical_section` return its input unchanged (or remove the call site) and confirm the test **fails**. A test that only ever passed proves nothing.

**Record in the HANDOFF:** whether the call site actually exists today (**it probably does not** — there is no table-creation route), and **which path you chose** for the helper.

## 7. Rollback path

**Fully reversible in one step.** Remove the helper and the call; behaviour returns to today's. **No data is at risk** — no route creates a table today, so no `section` value was ever written by this code. **No column, no table, no migration, no backfill** under the recorded default.

**If you chose a fixed vocabulary with a `CHECK` constraint, the rollback becomes a migration** — and that is feature **446**'s territory. **That is the reason the recorded default avoids the constraint.**

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (strings, enums, money, timestamps).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-backend` — the FastAPI/SQLModel conventions.
5. `le31-handoff-spec` — the handoff format itself.
6. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these four feature contracts in full before you start:**

- `features/431-le31-menu-item-category-is-case-sensitive-free-text-first-party-three-spellings-of-one-category-are-three-categories-v1-category-canonicalisation.md` — **the sibling with the identical shape, and the source of the mechanism.** If the mechanisms match, **share one helper.**
- `features/455-le31-two-tables-can-carry-the-same-label.md` — **the sibling on the same table.** It owns the *label* (a `UniqueConstraint`); you own the *area* (a spelling rule). **Independent.**
- `features/404-le31-sqlite-tables-not-strict-first-party-stock-entry-qty-delta-accepts-text-and-sum-silently-returns-zero-so-a-corrupt-ledger-row-reads-as-sold-out-v1-check-constraints-on-silent-corruption-columns.md` — **why the rule is in the application, not in a `CHECK`.**
- `features/453-le31-sqlite-silently-drops-the-utc-offset-time-is-utc-is-not-enforced-and-dev-and-prod-disagree.md` — **the precedent for "dev and prod must not disagree"**, which is why the case rule is decided in Python.

## 9. The one thing that matters

**A typo in `Table.label` is visible to the waiter; a typo in `Table.section` is visible to nobody until a query runs.** The table is in the right place, with the right number of seats — it is just in a group the query did not return. **The error is a *split*, not an extra: the count is smaller than reality, and the missing tables are the newest ones.** A smaller count is what a manager reads as "quiet".
