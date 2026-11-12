# HANDOFF — Feature 471: the stored `Batch.qty_remaining` and the charter's formula disagree

> **Slice contract for an external coding agent.** Read this file and the feature contract it names; you should need nothing else. **Do not paste chat excerpts.** If anything here is ambiguous, stop and say so — do not invent product behaviour.
>
> **Pick C of Daily Research 2026-11-12 (89th pass). FIRST-PARTY, execution-proven.** Bucket: **v1**. Gate verdict: **`build`**.

## 1. The active feature path

```
features/471-le31-the-stored-batch-qty-remaining-and-the-charter-formula-disagree-the-moment-the-first-sale-is-written-first-party-the-stored-column-is-a-second-copy-of-a-number-the-charter-says-must-be-derived-v1-stock-remaining-consistency.md
```

**The one-sentence claim:** the stored `Batch.qty_remaining` column and the charter's own formula disagree the moment the first sale is written, and nothing in the code reconciles them.

**The one sentence this feature exists to make true:** *the stored stock number and the ledger never disagree, because the stored number is written from the ledger.*

**The executed evidence (re-run it; do not trust this paragraph):**

```
charter P0 scenario: qty_start=8, one sale of -1
  charter §4.3 formula -> batch.qty_remaining = SUM(qty_delta) = 7
  stored column still says                       = 8
  DIVERGENCE = 1

after UPDATE qty_delta -> -100:
  ledger sum = -103, stored qty_remaining = 10
  (the stored column is UNCHANGED and never consulted)
```

**And the fact that makes this not "374 again":**

```
$ grep -rn qty_remaining backend/ --include='*.py' --include='*.html'
backend/app/models.py:106:    qty_remaining: int
```

**Exactly ONE hit — the declaration.** No derivation site. No reader. No writer. No test.

## 2. The seven-check gate verdict

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | When the owner reads "stock goes 8 → 7", the stored column says 8 and the ledger says 7, so the owner cannot tell which number is the restaurant's. |
| 2 | Viability | **Yes** — one write-path helper and one test. |
| 3 | Practicability & confidence | **Yes** — no schema change, no migration. **Rabbit hole: the charter's formula is ambiguous about whether `qty_start` folds in, and 374 will bake the same constant in. Escalate, do not guess.** |
| 4 | Conflict | **No invariant violated** — it *upholds* §4.3 and the P0 scenario. |
| 5 | Outcome / appetite / scope | **v1** — 1–2 hours. Scope fixed: **one helper + one call site**. |
| 6 | Cost to operational value | **High** — the stock number is the owner's most-trusted number and it has two copies with no tiebreaker. |
| 7 | Circuit breaker & reversibility | **Stop evidence:** a test asserting the stored column equals the ledger sum after a sale. **Rollback:** remove the helper call. |
| — | **Decision** | **`build`** |

**Evidence class:** **observed**. Confidence: **high**.

## 3. Files to touch

**Exactly these, and no others:**

| File | Change |
|---|---|
| `backend/app/services/__init__.py` | **Create** (the directory does not exist). |
| `backend/app/services/stock_service.py` | **Create.** The three functions specified in the contract's *Data model*. |
| `backend/tests/test_stock_remaining_consistency.py` (or the repo's existing test location) | **Add** the regression tests. |
| `features/471-…md` | The contract. Read-only for you except for fixing a typo. |
| `specs/le31-the-stored-batch-qty-remaining-and-the-charter-formula-disagree-the-moment-the-first-sale-is-written-first-party-the-stored-column-is-a-second-copy-of-a-number-the-charter-says-must-be-derived-v1-stock-remaining-consistency-HANDOFF.md` | This file. |

**Files you must NOT touch:** `backend/app/models.py` (no column, no table, no enum member), `backend/app/db.py` (no Alembic), `backend/app/routers/**` (**no router — see below**), `backend/app/bot/cook_bot.py`, `backend/app/config.py`, anything under `features/` other than 471, anything under `specs/` other than this one, `PROJECT_CHARTER.md`, `INDEX.md` (the parent owns the INDEX rows).

## 4. The implementation, in order

1. **Create `backend/app/services/`** with `__init__.py`. **This path is named by features 26, 34, 371 and 372** — you are realising a path the corpus already assumes, not inventing one.
2. **Add the formula constant** and the three functions. The contract's *Data model* section gives the signatures and the semantics; follow it exactly:
   - `apply_stock_delta(session, batch_id, qty_delta, reason, ref_order_item_id=None, by_user_id=None) -> StockEntry` — writes **one** `StockEntry`, then updates `Batch.qty_remaining` **from the ledger's new sum**, **in one transaction**.
   - `reconcile_batch(session, batch_id) -> dict` — returns `{"batch_id", "stored", "derived", "agrees"}`. **Never mutates.**
   - `reconcile_all_batches(session) -> list[dict]`.
3. **Write the failing test first, in its honest form.** Because there is no helper today, the test must first insert the ledger row **directly** and assert the column **stays at 8** — recording the divergence. **That failure output is the evidence.** Then assert that through the helper it becomes 7.
4. **Write the reconciliation test**: after the helper writes, `reconcile_batch(...)["agrees"] is True`; after the column is tampered with (`qty_remaining = 999`), `agrees is False`. **The detector must be shown to work, not just the writer.**
5. **Write the no-drift test:** two sales of `-1` and `-2` from `qty_start=8` → stored `5`, ledger sum `-3`.
6. **Record the decision notes** for Open questions 1 (the `qty_start` folding question) and 2 (the column's fate).
7. **Run the whole test suite.** `init_db()` and `create_all()` must still work — **this feature adds no schema change.**
8. **Do NOT wire the helper into a router.** No selling route exists and this feature does not create one. **The helper is a library the next selling feature will call.** If you find yourself writing an endpoint, you have left the scope.

## 5. The five things that will go wrong if nobody tells you

1. **⚠️ You will be tempted to drop the column.** Do not. **That is feature 374**, and 374 is **blocked on feature 446** (the schema-evolution mechanism) because `create_all()` never drops a column. **This feature makes the column correct in the interim and provides the service module 374 will need.** Do not add Alembic.
2. **⚠️ You will be tempted to write the column as `stored + qty_delta`.** That agrees with the ledger **only while nothing else writes the ledger**. **Derive from the ledger** (`qty_start + SUM(qty_delta)`) so the value is right by construction. The contract's *Data model* explains why.
3. **⚠️ You will be tempted to resolve the `qty_start` ambiguity by guessing.** The charter's formula says `SUM(qty_delta)`; its P0 scenario says *"stock goes 8 → 7"*. **They disagree by `qty_start`.** **Recorded default: `qty_start + SUM(qty_delta)`** — it is the reading that satisfies the charter's own worked example. **Put it in ONE named constant** and **escalate it**, because feature 374 will bake the same constant into the derivation it builds.
4. **⚠️ You will be tempted to auto-correct a divergent row.** Do not. **The reconciliation helper reports; it does not rewrite.** If it finds one, the owner decides. **No `Batch` row has ever been written by shipped code, so there should be none.**
5. **⚠️ You will be tempted to add the `StockReason` reversal member, a `Batch` preparer column, a `CHECK` constraint, or an `OrderItem.batch_id` column.** All belong to other features — 421, 445, 404 and 385 respectively. **This feature adds a service module and nothing else.**

## 6. Verification protocol

Run each of these and record the **actual output**. **"The helper returns the right number" is not the acceptance criterion — the two numbers agreeing *after a real write* is.**

```bash
# 1. The contract file exists and is parseable.
python3 - <<'PY'
import pathlib
p = pathlib.Path("features/471-le31-the-stored-batch-qty-remaining-and-the-charter-formula-disagree-the-moment-the-first-sale-is-written-first-party-the-stored-column-is-a-second-copy-of-a-number-the-charter-says-must-be-derived-v1-stock-remaining-consistency.md")
assert p.exists(), "contract file missing"
txt = p.read_text()
for h in ("## Goal", "## Scope", "## Description", "## Data model",
          "## Implementation steps", "## Telegram interaction if any",
          "## Dependencies", "## Open questions", "## Why this matters"):
    assert h in txt, f"missing section {h}"
print("PASS contract sections")
PY

# 2. THE load-bearing check — the two numbers agree after a real sale.
python3 - <<'PY'
from decimal import Decimal
from sqlmodel import Session, create_engine
from app import models
from app.services import stock_service as svc

engine = create_engine("sqlite:///:memory:")
models.SQLModel.metadata.create_all(engine)
with Session(engine) as s:
    mi = models.MenuItem(name="Tiramisu", category="dessert", unit_price=Decimal("5.00"))
    s.add(mi); s.commit(); s.refresh(mi)
    b = models.Batch(menu_item_id=mi.id, qty_start=8, qty_remaining=8)
    s.add(b); s.commit(); s.refresh(b)

    # THE FAILING FORM: today there is no helper, so insert the ledger row
    # directly and observe the column NOT following.
    s.add(models.StockEntry(batch_id=b.id, qty_delta=-1, reason=models.StockReason.sale))
    s.commit()
    stored_before = s.get(models.Batch, b.id).qty_remaining
    print("stored after a direct ledger insert:", stored_before)
    assert stored_before == 8, "unexpected: the column already follows"

    # THE FIXED FORM: the helper writes both, from the ledger.
    svc.apply_stock_delta(s, batch_id=b.id, qty_delta=-2,
                          reason=models.StockReason.sale)
    s.commit()
    rec = svc.reconcile_batch(s, b.id)
    print(rec)
    assert rec["agrees"] is True, "FAIL: stored and derived still disagree"
    assert rec["stored"] == 5, rec          # 8 + (-1) + (-2)
    assert rec["derived"] == 5, rec
    print("PASS stored and derived agree")
PY

# 3. THE detector works — it must be able to REPORT a disagreement.
python3 - <<'PY'
from sqlmodel import Session, create_engine
from app import models
from app.services import stock_service as svc
engine = create_engine("sqlite:///:memory:")
models.SQLModel.metadata.create_all(engine)
with Session(engine) as s:
    mi = models.MenuItem(name="T", category="d", unit_price="1.00")
    s.add(mi); s.commit(); s.refresh(mi)
    b = models.Batch(menu_item_id=mi.id, qty_start=8, qty_remaining=8)
    s.add(b); s.commit(); s.refresh(b)
    b.qty_remaining = 999            # simulate the tampered column
    s.commit()
    rec = svc.reconcile_batch(s, b.id)
    assert rec["agrees"] is False, "FAIL: the detector cannot see a divergence"
    assert rec["stored"] == 999 and rec["derived"] == 8, rec
    print("PASS the detector reports the divergence")
PY

# 4. The charter's P0 scenario, verbatim.
#    -> asserts: qty_start=8, one sale of -1, stored becomes 7
#    -> asserts: this is the value the charter's own worked example names

# 5. The formula constant is in ONE place.
grep -rn "qty_start" backend/app/services/stock_service.py
#    -> asserts: the formula appears once, in a named constant

# 6. The helper is the only writer — no direct StockEntry construction.
grep -rn "StockEntry(" backend/app/ --include='*.py' | grep -v models.py | grep -v services/
#    -> asserts: no other module constructs a StockEntry directly

# 7. No router was written.
ls backend/app/routers/
#    -> asserts: still only __init__.py and tables.py

# 8. No schema change — create_all() still works and the columns are unchanged.
python3 -c "
from sqlmodel import SQLModel, create_engine
from app import models
SQLModel.metadata.create_all(create_engine('sqlite:///:memory:'))
print([c.name for c in SQLModel.metadata.tables['batch'].columns])"
#    -> asserts: batch's columns are exactly the same list as before this feature

# 9. The corpus agrees: this concern is now owned.
grep -rl "apply_stock_delta" features/ specs/
#    -> asserts: exactly one feature contract names it

# 10. Nothing but the named files changed.
git status --short
#    -> asserts: only backend/app/services/**, the test file, this feature file
#                and this HANDOFF changed
```

## 7. Rollback path

**One file to delete, one import to remove.**

- **Delete `backend/app/services/stock_service.py`** (and `__init__.py` only if the directory is otherwise empty).
- **No data is at risk.** The feature writes `StockEntry` rows that are **correct** and a `Batch.qty_remaining` value that is **correct** — removing the helper does not invalidate either. The ledger rows remain valid append-only history.
- **No schema change**, so no migration and no rollback of a migration.
- **If a sale was written through the helper and the helper is then removed**, the ledger row and the column **remain in agreement** — because the helper wrote them that way. **The rollback is safe in the data, not just the code.**
- **The empty `services/` directory is harmless** and **must not be deleted if any other feature has created files in it** — features 26, 34, 371 and 372 name this path and a future one may land beside it.

## 8. The mandatory LE31 skill list

**Load these before you write code. In this order:**

1. `le31-conventions` — the seven-check gate, the hard invariants, and §3.2's non-goals. **This is why you are not adding Alembic and not writing a router.**
2. `le31-v1-feature-pattern` — the contract shape, the slicing rules, and the definition of done.
3. `le31-handoff-spec` — the frozen-contract discipline: **do not silently change the slice, the scope or the verification path.** If something must change, **surface it and stop.**
4. `development` — the generic pipeline: specify → plan → tasks → implement → **independent review**.
5. `speckit-specify`, `speckit-plan`, `speckit-tasks` — as `development` directs.
6. `pre-merge-review` — **product code does not merge on your own say-so.** It merges on green checks **and** a review from an agent or person who did not author the change.
7. `verify-before-fixing` — when a check fails, **fix what it is flagging. Never weaken a check to make it pass.**

**The project skills live in the repository** at `skills/<name>/SKILL.md`. If the Hermes loader cannot find one by name, **read the file directly** — do not proceed without it.

## 9. The one thing that matters

**The two numbers are identical today only because neither has a writer.**

The stored column and the ledger cannot disagree yet — not because they agree, but because **no code touches the column at all**. That coincidence ends the moment the first selling path lands, and **the corpus contains at least four features that plan to write stock** (03, 26, 34, 385), each of which names `backend/app/services/stock_service.py` — **a path that has never existed.** Whichever lands first will write that file, and it will decide by omission whether the two numbers stay in agreement.

**Your job is to make that decision once, correctly, and in one place.** Cost: one module, three functions, no schema change, therefore not blocked on feature 446.

Two things to carry out of this slice:

- **The `qty_start` folding question is an escalation, not a decision.** Put it in one named constant, record the default, and say so in your report.
- **You are laying the foundation feature 374 will build on.** Do not drop the column, and do not rename the service module — 374's implementer will expect this path.
