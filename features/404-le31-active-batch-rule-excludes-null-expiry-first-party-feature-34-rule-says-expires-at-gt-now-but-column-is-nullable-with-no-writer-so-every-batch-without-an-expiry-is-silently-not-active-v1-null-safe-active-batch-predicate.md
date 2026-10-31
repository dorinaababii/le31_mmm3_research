# Feature 404 — LE31's own "active batch" rule silently excludes every batch whose expiry was never set

> **Pick B of Daily Brainstorm 2026-10-29 (91st pass).** **FIRST-PARTY, and the defect is in LE31's own written rule** — the rule is stated in LE31's own feature contracts (features 03 and 34) and **fails by execution**.
>
> Feature 34, Open questions #3, verbatim:
>
> > "**What counts as 'active batch'?** Same as feature 03's FIFO rule: oldest `Batch` consumed first; a batch is active while `SUM(qty_delta) > 0` and **`expires_at > now()`**. Confirm at code-review."
>
> `backend/app/models.py` line 108, verbatim:
>
> ```python
> expires_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
> ```
>
> **`expires_at` is nullable and defaults to `NULL`.** In SQL, `NULL > now()` evaluates to **NULL**, and **NULL is not TRUE**. A batch with no expiry therefore **fails LE31's own definition of "active"**.
>
> **Evidence, parent-verified by EXECUTION on 2026-10-29** (SQLite — the same engine `backend/app/db.py` targets; commands in the HANDOFF, re-runnable):
>
> ```
> id=1 expires_at=2026-10-29T22:00:00   is_active=1
> id=2 expires_at=None                is_active=None   <-- NOT selected
> rows selected as 'active': [1]
> ```
>
> **And nothing sets it.** `grep -rn 'Batch(' backend/` returns **only the class declaration** — there is no batch-creation path yet — but the **specification** is equally silent: `expires_at` appears in exactly **one** feature's data-model tuple (feature 03) and is **read** by feature 34's rule, while **no feature says who writes it**.
>
> **The external instrument** was `zakariaelqannaa-dv/resto-management` (MIT): every kitchen ticket there carries *"a **service date** and a **day-scoped code number**"* (`K-YYMMDD-NNN`). The day is a **first-class key** in that artifact's ticket system, which made the parent go and read LE31's own `Batch` — whose docstring says *"a concrete prepared quantity of a MenuItem **for a specific day**"* while the table has **no day column at all**.
>
> **Bucket: v1** — this is the rule under the charter's P0 acceptance criterion *"order a tiramisu → stock goes 8 → 7"*. **Build verdict: `build`.** Evidence class: **OBSERVED** (executed).

## Goal

Make LE31's notion of an **active batch** mean the same thing in the schema, in the SQL, and in the code — so that **a batch which has not expired is never silently treated as expired.**

Two concrete outcomes:

1. **A batch with `expires_at IS NULL` is active** (it has not expired) — the current rule says the opposite.
2. **Someone is accountable for setting `expires_at`.** Either a feature says who writes it, or the column stops being optional.

**The single sentence this feature exists to make true:** *a batch with no expiry has not expired.*

## Scope

**In scope (v1):**

- **One decision, applied consistently:** how LE31 treats a `NULL` `expires_at` in the active-batch predicate.
- **One SQL-true predicate**, written once, in one place, and **used by every consumer** — the stock board (feature 34), the FIFO consumption query (feature 03), and the P0 sale path (charter §4.3).
- **A rule for who sets `expires_at`**, recorded in the feature that owns batch creation (feature 03) — or the column made non-nullable with a documented default.
- **A regression test** that asserts a `NULL`-expiry batch **is** active.

**Out of scope (v1):**

- **Any new table.** This is a **predicate** defect, not a modelling gap.
- **The service-day / local-date question.** LE31's `Batch` has no service-date column, and charter §3.5 says *"Time is UTC"*, so a batch prepared at 23:30 UTC falls on the **next calendar day** in Europe/Zurich. That is a **real and separate** question — see *Open questions* — and it is **not** answered here. This feature makes the *predicate* correct; it does not make the *day boundary* exist.
- **`Batch.qty_remaining`.** That is **feature 374** (derive, don't store) and is **not** touched. The two features are adjacent and **must not be merged**: 374 is about a stored number with no derivation site; this one is about a **filter predicate that excludes rows it should include.**
- **The `StockEntry` ledger's write path.** There is none yet. This feature changes **how batches are selected**, not how stock is moved.
- **Auto-marking `sold_out` at expiry.** Feature 03's open question 2 (*"Should we auto-mark `sold_out` at expiry time? (Yes seems obvious but needs a periodic job.)"*) is **not** answered here — a periodic job is a separate change with its own gate.
- **Alembic / migrations.** §3.2's stated v1 policy is `init_db()`.
- **The `expires_at` on `ShiftBriefing` (feature 12) and `GiftCard` (feature 18).** Those are **different tables** with **different semantics** (a stale brief, an expiring gift card). Feature 153's FEFO discussion is about `StockEntry.expires_at`, which **does not exist** and is not added here.

## Description

### The defect, as observed in LE31's own code on 2026-10-29

**Shape (a) — contradiction.** The rule and the column disagree.

```
features/34  "a batch is active while SUM(qty_delta) > 0 and expires_at > now()"
models.py:108  expires_at: datetime | None = Field(default=None, ...)
```

`NULL > now()` is **NULL** in SQL, not `TRUE`. The rule, read literally in SQL, **excludes every batch whose expiry was never set** — including every batch the cook made this morning and did not give an expiry time.

**Shape (b) — omission.** `Batch.expires_at` is **read** by feature 34's rule and **written by nobody**. Its sibling `Batch.qty_start` has a documented writer — feature 03: `StockEntry(reason='initial', qty_delta = qty_start)` — and `Batch.prepared_at` has a documented default (`default_factory=utcnow`). `expires_at` has neither a writer nor a default that makes it meaningful.

**Shape (c) — missing inverse edge.** The expiry question has **no owner**. Nothing says whether the *cook*, the *shift*, or the *menu item* determines when a batch expires — so "the cook knows when the tiramisu runs out" is a true operational fact that has **nowhere to live** in the schema.

**Shape (d) — undefined term.** **"Active batch"** is used in **17 places** across `PROJECT_CHARTER.md`, the `research/` docs and the `coding-agent/skills/` files, and **defined in none of them**. Features 03 and 34 each leave it as an open question marked *"Confirm at code-review"* — which is where an **undecided** thing belongs, so the term has never actually been settled.

### Why the failure is silent, and why that is the whole point

The predicate is a **filter**, not an assertion. A batch that is wrongly excluded does not raise; it **disappears**. The stock board shows fewer batches. The FIFO query picks a different batch. The sale path finds no active batch and — depending on how the future write path is written — either **refuses a legitimate sale** or **sells from a batch the cook did not intend**.

There is **no ground truth to audit against**, because there is no query that reports "batches excluded because `expires_at` was NULL".

**Today this is completely inert**: no batch is ever created (`grep -rn 'Batch(' backend/` → only the class declaration), so no batch can be excluded. That is exactly the shape the 85th–90th passes found repeatedly — **cheap now, expensive after**, because the first batch-creation implementation will have to make this choice, and the plausible wrong answer is the quiet one:

> *"`expires_at` is optional, so I'll treat `NULL` as 'no expiry'."*

That is **true today** (there are no batches) and **silently false** the moment one exists.

### The service-day question this defect uncovered — recorded, not solved

`Batch`'s docstring says *"a concrete prepared quantity of a MenuItem **for a specific day**"*. The table has **no day column**: only `prepared_at`, a wall-clock UTC timestamp (charter §3.5: *"Time is UTC"*). So:

```
a batch prepared at 2026-10-29T23:30:00+00:00 UTC  is  2026-10-30T01:30:00+02:00 in Europe/Zurich
```

**"Today's batches" is not computable from `prepared_at` alone** without a service-day boundary LE31 does not have. That is a genuine gap, and it is **adjacent** rather than identical to this one. It is **recorded here** and left as an open question, because a service-day column is a **schema** decision and this feature is a **predicate** decision.

**The external artifact states the answer shape**: `resto-management` gives every ticket *"a **service date** and a **day-scoped code number**"* (`K-YYMMDD-NNN`) — the day is part of the ticket's **identity**, not a function of a timestamp. The **vocabulary transfers**; the **code-shape is not adopted** (Electron/React/Express/PGlite is off-stack for LE31's FastAPI/SQLModel/Postgres posture).

## Data model

**No new table. No new column.**

**Changed:**

```
backend/app/models.py
  class Batch:
      expires_at: datetime | None = Field(default=None, ...)   # UNCHANGED in this feature
```

**The schema is deliberately left alone.** Two options exist and **both are recorded**; the owner picks:

| Option | Change | Effect | Cost |
|---|---|---|---|
| **A — NULL means "no expiry"** (NULL-safe predicate) | **no schema change**; the predicate becomes `expires_at IS NULL OR expires_at > now()` | a batch with no expiry is active **forever** | a batch can never be retired by expiry; needs an explicit `sold_out`/void path to leave the active set |
| **B — expiry is mandatory** | `expires_at: datetime` (NOT NULL) with a documented default (e.g. end of service day) | every batch has an expiry; the predicate is unambiguous | requires deciding the default, which drags in the service-day question |

**This feature's deliverable is the predicate and the decision record, not the column change.** Option B's column change is **not** made here because choosing the default *is* the service-day decision.

**The predicate, written once:**

```sql
-- active batch
WHERE SUM(qty_delta) > 0
  AND (expires_at IS NULL OR expires_at > now())
```

**In Python** (the same logic; note that `None` must be checked **before** the comparison, because `None > now()` raises `TypeError` in Python 3):

```python
def is_active(batch, now) -> bool:
    return batch.expires_at is None or batch.expires_at > now
```

**Both forms are NULL-safe, and both are written down.** The SQL form and the Python form differ in their failure mode if the null check is omitted — SQL yields NULL (row excluded), Python **raises** — so the null check must appear in **both**, and the two must be tested against each other.

## Implementation steps

1. **Write the decision record.** One paragraph in this feature's own docs (and one line in `features/03-kitchen-stock-tracker.md`) stating the chosen option — **A or B** — and the one-sentence rule: *"a batch with `expires_at IS NULL` is active"* (option A) or *"every batch carries an expiry"* (option B).
2. **Write the predicate once.** Add `backend/app/services/batches.py` with `is_active(batch, now)` and `active_batches(session, now)`. **`backend/app/services/` does not exist today** — create it with `__init__.py`. The point of the module is that **the predicate has exactly one definition** and every caller imports it.
3. **Express the predicate in SQL as well as Python.** `active_batches()` must issue `expires_at IS NULL OR expires_at > :now` — **not** `expires_at > :now` — so that the SQL and the Python agree. The two are tested against each other in step 5.
4. **Replace every existing occurrence of the rule.** `grep -rn 'expires_at > now' features/ backend/` and update the **spec** in feature 34 (its Open questions #3) to the new rule, so the written rule and the code agree. **A feature contract that still states the old rule is the defect, still present.**
5. **Add the regression test.** For a batch with `expires_at = None`: `is_active(batch, now) is True`, and the SQL query returns that batch's id. For a batch with `expires_at` in the past: both forms return `False`. For a batch with `expires_at` in the future: both return `True`. **The test must compare the SQL result set to the Python result set** — the two failing differently is the whole failure mode.
6. **Decide the writer, or say explicitly that there is none yet.** If option B is chosen, record in feature 03 who sets `expires_at` (the most likely writer is the batch-creation path from feature 04's `/start_today` flow, where the cook already states prep quantities). **If there is no writer yet, say so in the feature — an unwritten column must be named as unwritten.**

## Telegram interaction if any

**None.** This feature does not add a command, does not change a command, and does not change what the cook sees.

**What changes observably**: the stock board (feature 34) and the FIFO consumption query (feature 03) will begin to **include** batches they currently exclude. Today they include *nothing* (no batch exists), so the user-visible effect is nil — but it is **not nil** once the batch-creation path lands, which is why this must be fixed **before** that path, not after.

**One consequence to note, because it is a *behaviour* change and not only a code change**: with option A, a batch that is never given an expiry stays active **indefinitely**. The cook's way out is `/sold_out` (which feature 397 files as a state) or `/leftover`. The **help text does not need to change**, but the **owner should know** that "no expiry" now means "always active".

## Dependencies

- **No new package.**
- **Must not be merged with feature 374** (`Batch.qty_remaining` derive-don't-store). They are adjacent and **different**: 374 is a stored number with no derivation site; this is a **filter that excludes rows**. **If they are implemented in the same PR, both must be stated separately** — a reviewer must be able to check each on its own.
- **Related, not blocking:** feature 03 (batch creation — owns the writer), feature 34 (the stock board — owns the rule's original text), feature 397 (`sold_out` state — the way a batch leaves the active set), feature 372 (expiry-first vocabulary — a household-kitchen analogue, explicitly *not* directly portable), feature 153 (FEFO discipline — a **v2** surface, and it is about `StockEntry.expires_at`, which does not exist).
- **The service-day question** blocks **option B**'s default value but **not** this feature's predicate. It is recorded, not resolved.

## Open questions

1. **Option A or option B?** The owner picks. The feature states both, applies the NULL-safe predicate either way, and records the decision. **Until then, the predicate is correct and the column is unchanged.**
2. **What is a *service day*?** A local date at the venue, or a UTC date? Does it start at midnight, or at the venue's opening time? This is **the** question behind option B's default, and behind "today's batches" (charter P0: *"Waiter can browse **today's** menu"*). **Not answered here.** It also interacts with the charter's stated timezone: project `le31 v1 — Core MVP` records *"EUR, Paris timezone"*, while charter §3.5 says *"Time is UTC"* — **two different statements in LE31's own documents**, which is itself worth reconciling.
3. **Who sets `expires_at` in practice?** The cook states prep quantities at `/start_today` (feature 04); the owner does not know when a tiramisu runs out. **Most likely answer: the cook, at creation, with a default of end-of-service-day** — which is option B with a default, and which therefore depends on question 2.
4. **Should a batch with no expiry ever be allowed?** Option A says yes, forever. Is there a case where the cook genuinely means "this never expires"? **Owner to confirm.**
5. **Is expiry even the right mechanism for LE31's v1?** Feature 153 argued that *"the cook is the system"* for perishables and recommended **no** automatic expiry tracking in v1. That is a **counter-argument to this feature's premise** and it is recorded here: the honest resolution may be that **expiry is deferred and the predicate is written so that deferring it is safe** — which option A does.

## Why this matters

**Because this is LE31's own rule failing against LE31's own schema, and the rule is under a P0 acceptance criterion.** The charter's P0 test is *"order a tiramisu → stock goes 8 → 7 → ledger has one entry"*. **Finding the batch is step one of that test.** With the current predicate, a batch with no expiry is not found — so the P0 criterion is not satisfiable for a batch the cook made without setting an expiry time, and **the failure is an empty result, not an error.**

**The asymmetry that argues for `build` over `defer`.** Today no batch is ever created, so the defect is **completely inert** — it cannot hurt anyone. The moment the batch-creation path lands (feature 04's `/start_today` wiring), the defect becomes **live**, and the wrong answer is the quiet one: *"`expires_at` is optional, so `NULL` means no expiry"* — which is precisely the reading the column's own default invites. **Cheap now, expensive after.**

**And this is the second time in two passes that the "undefined term" shape has fired on a phrase that LE31's own documents use repeatedly and settle nowhere.** The 87th pass found *"active batch"* — **the same term** — used 5 times and defined 0 times, and filed it as part of feature 385. This pass found it again, **now at 17 uses**, and the finding is *sharper*: the 87th pass noted the term was undefined; this pass shows that **the two places that try to use it each wrote a rule, the two rules do not agree with the schema, and neither rule was settled.** That is what "undefined" means in practice — not that nobody wrote it down, but that **nobody decided**, so each writer invented a different version.

**Why the external artifact mattered.** `resto-management` did not tell LE31 anything about NULL semantics or about expiry. It told LE31 that **a day is part of a ticket's identity**. That was enough to make the parent read LE31's own `Batch` — and to notice that LE31's `Batch` docstring promises *"for a specific day"* while the table cannot name a day. **Ninety citations had not found the first defect; four greps and a `sqlite3` probe did.** This is the **sixth consecutive pass** on which that has held, and the **first** on which the finding came out of a *rule* rather than out of a *missing field*.
