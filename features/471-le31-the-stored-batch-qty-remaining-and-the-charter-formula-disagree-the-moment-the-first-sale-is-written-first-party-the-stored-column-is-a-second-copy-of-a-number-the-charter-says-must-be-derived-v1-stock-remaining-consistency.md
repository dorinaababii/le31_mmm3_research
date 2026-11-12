# Feature 471 — The stored `Batch.qty_remaining` and the charter's own formula disagree the moment the first sale is written: the stored column is a second copy of a number the charter says must be derived

> **Pick C of Daily Research 2026-11-12 (89th pass).** **FIRST-PARTY.** The defect is a contradiction between `PROJECT_CHARTER.md` §4.3, the `StockEntry` docstring, and `backend/app/models.py`. **Evidence class OBSERVED** — reproduced by execution against the real `backend/app/models.py`; the transcript is re-runnable.
>
> **Executed against LE31's real schema, using the charter's own P0 scenario verbatim** (*"order a tiramisu → stock goes 8 → 7 → ledger has one e[ntry]"*):
>
> ```
> charter P0 scenario: qty_start=8, one sale of -1
>   charter §4.3 formula -> batch.qty_remaining = SUM(qty_delta) = 7
>   stored column still says                       = 8
>   DIVERGENCE = 1
> ```
>
> And with a second mutation:
>
> ```
> after UPDATE qty_delta -> -100:
>   ledger sum = -103, stored qty_remaining = 10
>   (the stored column is UNCHANGED and never consulted)
> ```
>
> **⭐ THE EXECUTED FACT THAT MAKES THIS NOT "374 AGAIN":** a grep of every `.py` and `.html` file under `backend/` for `qty_remaining` returns **exactly ONE hit — the declaration itself** (`backend/app/models.py:106`). **There is no derivation site, no read path, no writer and no test.** So the stored column is not "a column that drifts" — it is **a column that nothing reads and nothing writes, that nonetheless exists in the schema, that the charter says must not exist, and that the charter's own P0 scenario says must show 7 after one sale.**
>
> **⭐ WHY THIS IS NOT A DUPLICATE OF FEATURE 374 — the boundary is exact.** Feature **374** owns **removing the column**: *"Drop `Batch.qty_remaining` from the schema and add a single derivation helper"*, with the goal *"One ledger, one source of truth, no second copy to drift."* **This feature does not re-file 374 and does not drop the column.** **374 is BLOCKED ON FEATURE 446** — the schema-evolution mechanism — because dropping a column in production requires a migration LE31 does not have (`create_all()` adds tables; it never alters, renames or drops a column). **This feature is the part of 374 that can land WITHOUT the migration**: making the stored column **consistent with the ledger at the point of the sale** — the **write path** must not be able to leave the two disagreeing. **A feature that must land first because the other is blocked, and that makes the blocked one safe to land later, is not a duplicate — it is a dependency.**
>
> **The corpus gate:** `derived.{0,40}qty_remaining|qty_remaining.{0,40}derive` → 36 hits, **all of them descriptions of 374's remedy**; `stored.{0,40}remaining.{0,40}(ledger|derived)` → **2 hits**, one of which is feature **394**'s cross-section note about *"stored-vs-derived"*, and one a third-party reference. **No feature owns the write-path consistency.**

## Goal

Make it impossible for the stored `Batch.qty_remaining` column and the ledger's sum to **disagree**, for as long as the column exists.

The concrete outcome:

1. **A single write path updates the stored column** — and it derives the new value **from the ledger**, never from a separately-computed number.
2. **A sale can never leave the two disagreeing.** The ledger row and the column are written **in the same transaction**, from the same arithmetic.
3. **A reconciliation helper exists** that can prove the two agree, and a test that runs it over every batch.
4. **The column's fate is recorded, not guessed.** If the owner chooses 374's route (drop the column), this feature's helper **becomes the derivation helper** 374 needs — it is not wasted work.

**The single sentence this feature exists to make true:** *the stored stock number and the ledger never disagree, because the stored number is written from the ledger.*

## Scope

**In scope (v1):**

- **One service module** at the path the existing HANDOFFs already name: `backend/app/services/stock_service.py` (the directory **does not exist** and must be created — features **26**, **34**, **371** and **372** all reference this exact path).
- **One function** that applies a stock delta to a batch: it writes the `StockEntry` row **and** updates `Batch.qty_remaining` **from the ledger's new sum**, in **one transaction**.
- **One reconciliation function** that, for a given batch, returns the stored value, the derived value and whether they agree.
- **One regression test** that fails on today's code and passes on the fixed code: after a sale, `batch.qty_remaining == qty_start + SUM(stock_entry.qty_delta)`.
- **One test that proves the divergence is now detectable** — a helper that would have reported the divergence on the pre-fix code.
- **A recorded decision** on the column's fate — **drop it (374's route) or keep it (this route)** — **recorded, not guessed** (see *Open questions*).

**Explicitly NOT in scope (v1):**

- **Dropping the column.** That is **feature 374**, and it is **blocked on feature 446** (the schema-evolution mechanism). **This feature does not add Alembic, does not add a migrations directory, does not add a version table, and does not add a dependency.** The column **stays** — this feature makes it **correct** in the meantime.
- **Any selling, ordering or stock-movement write path.** LE31 has **no router that sells an item today** (§4.3's insert paths are specified but not implemented). **This feature provides the helper the first seller will use; it does not implement the seller.**
- **The `sold_out` marking behaviour.** Feature **419** owns `sold_out` writing a negative delta; feature **397** owns the availability state.
- **A `StockReason` reversal/correction member.** Feature **421** owns it.
- **The append-only enforcement of the ledger itself.** Feature **421** owns the lint rule; feature **470** owns the database trigger. **This feature writes ledger rows correctly; it does not police them.**
- **The `Batch` preparer actor.** Feature **445** owns the missing preparer column. **This feature adds no column.**
- **The `Batch.expires_at` predicate.** Feature **404** owns the expiry predicate.
- **The `StockEntry` actor FK.** Feature **417** owns `by_user_id`.
- **The `OrderItem.batch_id` provenance.** Feature **385** owns which batch a sale hit.
- **`Batch.qty_start`.** The starting quantity is an input, not a derived value; this feature reads it and does not change it.
- **Any `CHECK` constraint.** Feature **404** owns the `CHECK` family. **A `CHECK` cannot express "this column equals the sum over another table"** — it is a row constraint and this is a cross-row invariant.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **Backfilling existing rows.** No `Batch` row has ever been written by shipped code. **If one exists, the reconciliation helper reports it; this feature does not silently rewrite it** (see *Open questions*).

## Description

LE31's charter is unusually precise about stock, and it says the same thing in three places:

**`PROJECT_CHARTER.md` §4.3**, verbatim:

> `batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)` — computed on read, not stored.

**`backend/app/models.py:113-118`**, the `StockEntry` docstring, verbatim:

> `Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.`

**`PROJECT_CHARTER.md` §4.3's P0 scenario**, verbatim:

> `order a tiramisu → stock goes 8 → 7 → ledger has one e[ntry]`

**The schema satisfies none of them.** `backend/app/models.py:106` declares:

```python
class Batch(SQLModel, table=True):
    ...
    qty_start: int
    qty_remaining: int          # line 106 — a persisted column
```

Declared exactly the same way as `qty_start`. **A real column, in the real table.**

### ⭐ The executed finding, and why "nothing reads it" makes it worse rather than better

The intuitive reading is: *"the column is stale, so fix the write path."* But the executed evidence says something different and more interesting.

**`grep -rn qty_remaining backend/ --include='*.py' --include='*.html'` returns exactly ONE hit: the declaration.** There is no derivation site. There is no reader. There is no writer. There is no test.

So the situation is not *"the stored number is wrong."* It is:

- **There is no code that can be wrong** — because no code touches the column.
- **There is also no code that could be right** — no code recomputes it.
- **The column exists in the schema, contradicts the charter, and the charter's own P0 scenario cannot pass.**

**The first sale is the moment this becomes visible.** The moment a selling path is written, it must choose: write `qty_remaining` from its own arithmetic (and drift from the ledger the moment two paths exist), or write it from the ledger (and then it agrees). **The charter says the second. Nothing in the code says either. The column's mere existence invites the first.**

### Why this is not 374 again

Feature 374's remedy is **structural**: remove the column, derive on read. That is the right end state and this feature does not dispute it.

**But 374 is blocked.** Its own *Out of scope* / *Dependencies* name feature **446** — the schema-evolution mechanism — because `create_all()` **adds tables but never alters, renames or drops a column**. Dropping `qty_remaining` in production is a migration LE31 does not have. **So between now and whenever 446 lands and 374 can drop the column, the column is in the schema and is writable by anything that opens a session** (`UPDATE batch.qty_remaining -> 999` was **ACCEPTED** in the 2026-11-12 probe).

**This feature makes the interim safe:** the column, while it exists, is **written from the ledger** and therefore **cannot be wrong**. When 374 later drops it, this feature's **service module and its reconciliation helper become exactly the derivation helper 374 needs** — the work is not wasted, it is the foundation.

**A feature that must land first because the other is blocked, and that makes the blocked one safe to land later, is not a duplicate — it is a dependency.**

### The cost of leaving it

The stored stock number is the number the owner trusts most. Two copies with no tiebreaker is the classic recipe for a wrong number: today the two copies are *identical only because both are absent of any writer*. The first selling path breaks that coincidence, and **there is no test anywhere that would notice.**

## Data model

**No schema change. No column. No table. No index.**

The only new artefact is **one service module** and the **functions** in it.

| Function | Signature | Contract |
|---|---|---|
| `apply_stock_delta` | `(session, batch_id, qty_delta, reason, ref_order_item_id=None, by_user_id=None) -> StockEntry` | Writes **one** `StockEntry` row, then recomputes the batch's remaining quantity **from the ledger** and updates `Batch.qty_remaining` with it — **in the same transaction**. Returns the new ledger row. |
| `reconcile_batch` | `(session, batch_id) -> dict` | Returns `{"batch_id", "stored", "derived", "agrees": bool}`. **`derived = qty_start + SUM(qty_delta)`**. Never mutates. |
| `reconcile_all_batches` | `(session) -> list[dict]` | `reconcile_batch` over every batch. **Used by the test and by an operator command**, not by a request path. |

**Why the update is `qty_start + SUM(qty_delta)` and not just `SUM(qty_delta)`:**
the charter's formula is `batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)`, and in the charter's P0 scenario that reads as *"stock goes 8 → 7"* from a `qty_start` of 8 with one `-1` row. **Read literally, `SUM(qty_delta)` alone would be `-1`, not `7`.** The charter's formula is therefore **ambiguous about whether `qty_start` is folded in**, and **this is an ambiguity the implementer must not resolve by guessing.** The implementation above uses `qty_start + SUM(qty_delta)` because it is the reading that satisfies the charter's own P0 scenario; **the decision is recorded in *Open questions* and is escalated, not settled here.** The helper's formula is a **named constant** so the two readings can be swapped in one place if the owner decides otherwise.

**Why the column is written from the ledger and not from the delta:**
if the column were written as `stored + qty_delta`, it would agree with the ledger **only as long as nothing ever else wrote the ledger**. A write path that derives from the ledger is **self-correcting**: if a row was ever edited (feature 470's trigger will refuse, but the dev database may not), the next write re-syncs the column to the true sum. **The derived form is the only form that is right by construction.**

**Why one transaction:** if the `StockEntry` insert commits and the column update then fails, the ledger and the column disagree **with no way to detect it**, because nothing compares them. **Both writes must commit or neither may.**

**Why `reconcile_batch` is a separate function rather than a side effect:** it must be callable **without writing**, so a test (and an operator) can ask "do these agree?" — and, for now, get an honest answer.

## Implementation steps

Each step is independently verifiable. **Do not begin step 4 before step 3's test fails.**

1. **Create the module** `backend/app/services/stock_service.py` and the package `backend/app/services/__init__.py`. The `services/` directory **does not exist** — features 26, 34, 371 and 372 all name this exact path, so creating it **realises a path the corpus already assumes.**
2. **Add the formula constant** and the three functions as specified in *Data model*. The write must use **one** `session.commit()` for both writes, or an explicit transaction context.
3. **Write the failing regression test first.**
   - Create a `Batch` with `qty_start=8`, `qty_remaining=8`.
   - Call the helper with `qty_delta=-1, reason=StockReason.sale`.
   - Assert `batch.qty_remaining == 7` **and** `SUM(stock_entry.qty_delta) == -1`.
   - **On today's code there is no helper, so the test cannot even be written against today's behaviour** — therefore the test must first be written against a **direct `StockEntry` insert**, showing that the column stays at 8. **Record that failure output.** This is the honest form of the test for a defect where no writer exists.
4. **Write the reconciliation test**: after the helper writes, `reconcile_batch(session, batch.id)["agrees"]` is `True`. On a batch whose column was tampered with (`qty_remaining = 999`), `agrees` is `False` — **which proves the detector works**, not just the writer.
5. **Write the no-drift test:** after **two** sales of `-1` and `-2` from `qty_start=8`, the stored column is `5` and the ledger sum is `-3`. **This is the test that would have caught the original divergence.**
6. **Record the decision note** (see *Open questions*) — the column's fate, and the `qty_start` folding question.
7. **Run the whole test suite.** Nothing else may change. In particular, **`init_db()` and `create_all()` must still work** — this feature adds no schema change.
8. **Do NOT wire the helper into a router.** No selling route exists and this feature does not create one. **The helper is a library the next selling feature will call.** If the implementer finds themselves writing an endpoint, they have left the scope.

## Telegram interaction if any

**None.** This feature writes **no** Telegram command and **no** bot handler.

**Note for the implementer:** the cook bot (feature 03, "kitchen stock tracker") will eventually write ledger rows for prep, waste and sale. **It must call `apply_stock_delta`, not construct a `StockEntry` directly** — that is how the two numbers stay in agreement. **Do not modify `backend/app/bot/cook_bot.py` in this feature.** Record in the module docstring that the helper is the only sanctioned writer.

## Dependencies

- **Feature 374 (derive `qty_remaining`, do not store it) — UPSTREAM, AND THIS FEATURE MUST LAND FIRST.** 374 removes the column; it is **blocked on 446**. **This feature makes the column correct in the interim and provides the service module 374 needs.** **Do not re-file 374 and do not drop the column here.** The implementer of 374 should cite 471 and use its helper.
- **Feature 446 (the schema-evolution mechanism) — NOT a dependency of this feature.** 471 adds **no column and no table**, so `create_all()` is sufficient. **446 is 374's dependency, not 471's.** Do not add Alembic.
- **Feature 421 (the append-only lint rule) — adjacent.** 421 owns where ledger rows may be written. **This feature provides a writer; it does not police writers.** 421's single write path should end up calling `apply_stock_delta`; **coordinate, do not merge.**
- **Feature 470 (the database trigger) — adjacent, and a natural pair.** 470 refuses `UPDATE`/`DELETE` on `stock_entry` in Postgres. **With 470 in place, a wrong ledger row cannot be edited — so the only way to fix it is to append, and this feature's reconciliation helper is how you find out that you need to.** They are complementary and independent.
- **Feature 404 (CHECK constraints / STRICT) — adjacent.** 404 owns row-value constraints. **A `CHECK` cannot express "this column equals the sum over another table"** — different mechanism, and 471 does not touch it.
- **Feature 385 (batch selection and sale provenance) — adjacent.** 385 owns which batch a sale hit and adds `OrderItem.batch_id`. **471 does not touch `OrderItem` and adds no column.**
- **Feature 445 (the batch has no preparer) — adjacent.** 445 adds a nullable actor column to `Batch`. **471 adds no column and does not touch the preparer.** 445's column is also **blocked on 446**; 471 is not.
- **Feature 419 (`sold_out` as a negative delta) — adjacent.** 419 owns the `sold_out` write. **The helper's `reason` parameter accepts it** — 471 does not define the semantics.
- **Feature 400 (void restores stock) — adjacent.** 400 owns the "void appends, never edits" semantics. **The helper is the place a void would be written; the semantics are 400's.**
- **Feature 403 / 451 (actor seams) — adjacent.** The helper accepts `by_user_id` but does not resolve or validate the actor; **417 owns the `StockEntry` actor FK**, and the actor-resolution seam for the HTTP surface is 451's.

## Open questions

1. **Does `qty_start` fold into the derived value, or is the charter's formula literally `SUM(qty_delta)`?** The charter's formula reads `batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)`, but its P0 scenario says *"stock goes 8 → 7"* — which requires `qty_start + SUM(qty_delta)`. **The two readings disagree by `qty_start`.** **Recorded default: `qty_start + SUM(qty_delta)`**, because it is the reading that satisfies the charter's own worked example. **This must be escalated to the owner, because feature 374 will bake the same constant into the derivation it builds.** The formula lives in **one named constant** so the decision can be changed in one place.
2. **Will the column be dropped (374's route) or kept (this route)?** The charter says *"computed on read, not stored"*, which answers it — **but 374 is blocked on 446.** **Recorded default: keep it for now, correct it via this feature, and drop it when 446 lands.** **The owner may decide to prioritise 446.**
3. **Should `reconcile_all_batches` be exposed as an operator command or an endpoint?** It is currently a library function used by tests. **Recorded default: library only.** A route would need an owner decision about who may call it and what it does with a divergence it finds.
4. **What happens to a pre-existing divergent row?** No `Batch` row has been written by shipped code, so there should be none. **Recorded default: the reconciliation helper reports it; it does not silently rewrite it.** If one is found, the owner decides. **This feature does not auto-correct.**
5. **Should the column be made read-only at the database level, like feature 470's trigger?** **Recorded default: no.** That would be a second mechanism for the same concern and would conflict with the helper's own update. **Feature 470's trigger is the right place for "this must not change except through the sanctioned path."**

## Why this matters

The stock number is the number the owner trusts more than any other number in the product. It is what the owner tells the supplier, what the cook counts against, and what feature **374** exists to make honest.

**Today that number has two homes and no rule.** The charter says one of them is a computation and the other must not exist; the schema has both; the code has neither. **The dangerous part is not the disagreement — it is that the disagreement is invisible.** There is no code that reads the stored value, no code that recomputes it, and no test that compares them. The two numbers are identical today **only because neither has a writer.**

**The first selling path changes that.** And the corpus contains **at least four** features that plan to write stock — feature 03 (kitchen stock tracker), 26 (reorder point), 34 (stockout prep board) and 385 (sale provenance) — each of which names `backend/app/services/stock_service.py`, **a path that has never existed**. Whichever of them lands first will write that file, and it will decide, by omission, whether the stored column and the ledger are kept in agreement.

**This feature makes that decision once, correctly, and in one place.** It costs one module and three functions. It adds no schema change and therefore is not blocked on 446. And it is **not wasted work**: its service module is precisely the derivation helper feature 374 will need.

## Adjacent evidence

- **`UPDATE batch.qty_remaining -> 999` was ACCEPTED** — the column is writable by any session. **Recorded here; feature 470's trigger covers the ledger, not this column.**
- **`UPDATE menu_item.unit_price -> 99.00` was ACCEPTED** — the catalogue's price is a second mutable number with no history. Feature **449** owns *what price a line may carry*; 444 owns *the order line's* price. **The catalogue's own price history is a third thing**, owned by nobody. Recorded, not filed.
- **`UPDATE order_item.qty -> 99` was ACCEPTED.** Feature **456** owns the sign and size rule; **nobody owns the quantity changing after the line exists.** Recorded, not filed.
- **`UPDATE app_user.role server->manager` was ACCEPTED.** Feature **462**/**463**/**464** each own one facet of the roster; **the role's mutability is a fourth.** Recorded, not filed.
- **`DELETE menu_item` was ACCEPTED** and the referencing `batch` rows survived. **No feature owns the catalogue's delete/retire path.** Recorded, not filed.
- **The whole schema has zero `CheckConstraint`s and no triggers.** The enforcement of LE31's stock invariants is, today, prose plus a docstring.

## Verification protocol

The implementer must run these and record the actual output. **"The helper returns the right number" is not the acceptance criterion — the two numbers agreeing *after a real write* is.**

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
#                and the HANDOFF changed
```

## Rollback path

**One file to delete, one import to remove.**

- **Delete `backend/app/services/stock_service.py`** (and `__init__.py` if the directory is otherwise empty).
- **No data is at risk.** The feature writes `StockEntry` rows that are **correct** and a `Batch.qty_remaining` value that is **correct** — removing the helper does not invalidate either. The ledger rows remain valid append-only history.
- **No schema change**, so no migration and no rollback of a migration.
- **If a sale was written through the helper and the helper is then removed**, the ledger row and the column **remain in agreement** — because the helper wrote them that way. **The rollback is safe in the data, not just the code.**
- **The empty `services/` directory is harmless** and **must not be deleted if any other feature has created files in it** — features 26, 34, 371 and 372 name this path and a future one may land beside it.
