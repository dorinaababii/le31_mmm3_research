# HANDOFF — Feature 493: The bill-close write has no idempotency key, so a retry is indistinguishable from a first attempt

## Active feature path

`features/493-bill-close-write-has-no-idempotency-key.md`

**Disposition:** `build` — **a named, first-party gap plus the vocabulary and the rule
that close it.** This handoff **does not itself authorize the schema change**; the
migration belongs to the feature that owns the bill-close write (feature **415**).

**What this slice delivers:** the rule, the narrow instance, the three properties, the
409-on-key-reuse case, and a **required test shape** that the implementing feature
must satisfy.

**What this slice explicitly does NOT deliver:** a table, a column, a route change,
or a client-side token minting. Do **not** add an `idempotency_key` column to `Bill`
under this handoff — feature **415** owns the bill-close write and its migration.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | **PASS.** Proved by execution: the backend has **zero** idempotency tokens and the schema's only UNIQUE index is `bill.visit_id`. A retry of the money-moving write is therefore not distinguishable from a first attempt. |
| 2. Viability | **PASS in principle.** The mechanism is a documented rule (caller-minted key, stored with the outcome, server reconciles its number back) with two existing in-corpus shapes to copy from. |
| 3. Practicability / confidence | **MEDIUM-HIGH for the rule, LOW for the source.** The rule is simple and standard; the source is ★0, off-stack (Python/Frappe-ERPNext), README-only. The corpus already holds the vocabulary (features 400, 401, 259, 412). |
| 4. Conflict | **No hard conflict.** The seat write's idempotency is feature 388's; the stock write's is features 400/401's. This feature names the **bill close** only and must not re-implement the other two. |
| 5. Outcome, appetite, scope | **BUILD the rule and the test requirement.** The implementation lands with feature 415's write. |
| 6. Cost to operational value | **LOW** (one column + one lookup + one test); **HIGH** value — it is the write that moves money. |
| 7. Circuit breaker / reversibility | **PASS.** The migration is additive and reversible (drop the column, drop the index). |

## Files to touch

**In this disposition:**

- `features/493-bill-close-write-has-no-idempotency-key.md` — this slice's only
  repository artefact besides the HANDOFF.

**NOT to be touched in this disposition:**

- `backend/app/models.py` — **no `Bill` change here.** Feature 415 owns it.
- `backend/app/routers/*` — **no route change here.**
- `index.html` — **no shipped-surface change here.**
- `features/388-*.md`, `features/400-*.md`, `features/401-*.md` — **upstream
  references; do not edit.**

**For the implementing feature (feature 415), the likely touch points are:**

- `backend/app/models.py` — an idempotency-key column on `Bill` (or a dedicated
  key→outcome table; the corpus contains both shapes — see the contract's
  "Dependencies");
- `backend/app/routers/bills.py` (or wherever the bill-close route lands) — accept
  the key, look it up, return the stored outcome on a repeat, and bind the key to
  the request body;
- `backend/tests/` — the retry test described below.

## Verification protocol reference

**Documentary verification (required):**

1. Read `features/493-bill-close-write-has-no-idempotency-key.md` in full.
2. Read the source evidence at
   `/tmp/le31-brainstorm-2026-11-17/gh/shyampandey1104__erpnext-pos-offline-pwa-hybrid-counter.README.md`
   and the metadata at
   `/tmp/le31-brainstorm-2026-11-17/gh/shyampandey1104__erpnext-pos-offline-pwa-hybrid-counter.repo.json`.
   Re-derive the in-window claim from the metadata: `created_at` **and** `pushed_at`
   must both fall in 2026-10-18..2026-11-17.
3. Confirm the parent's report at `/opt/data/le31-brainstorm-2026-11-17.md` records
   the pick and that it explicitly labels the source as a **vocabulary reference with
   no code adopted**.

**Executed verification (required before this feature may be called `build`):**

4. **Re-run the parent's probe** and confirm the absence still holds:
   `/opt/data/le31-brainstorm-2026-10-27/.venv/bin/python /opt/data/le31-brainstorm-2026-11-17-scripts/audit_lifecycle.py`
   must still print `idempotency tokens in backend: NONE` and
   `UNIQUE indexes in the real schema: [('bill', 'sqlite_autoindex_bill_1')]`.
   If either line has changed, **feature 415 or another feature has landed the
   change** — re-derive the gap before implementing.
5. **The corpus sweep must still return 0** for the bill-close instance:
   `grep -rliE "(bill close|closing (a|the) bill).{0,120}idempot|idempot.{0,120}(bill close|closing (a|the) bill)" features/ specs/`
   must return **no files**. If it now returns files, this feature is a **duplicate**
   and must be withdrawn.
6. **The retry test** (owned by feature 415, required by this contract): issue the
   same bill-close request **twice with the same key** and assert
   - exactly **one** `Bill` row exists for the visit;
   - exactly **one** `DerivedTip` row exists;
   - exactly **one** set of `StockEntry` rows was written;
   - the second call returns the **same body** as the first, with status **200**
     (not 201, not an error).
7. **The key-reuse guard:** the same key with a **different** body must return
   **409**, and must not create a second bill.
8. **Negative control:** remove the idempotency lookup (or delete the key column's
   unique constraint), confirm the retry test **fails**, restore, confirm it
   **passes**, and assert no residue.

**Charter checks:**

9. Charter §3.2 — no third-party code adopted. The source is MIT but **off-stack**
    (Python/Frappe-ERPNext vs LE31's FastAPI/SQLModel/Postgres) and is an
    offline-first design LE31 explicitly does not have. The *rule* transfers; the
    *code* does not.
10. The source README's "100% coverage" badge is **self-reported by the repository
    author and is NOT independently verified**. Do not repeat it as a fact.

## Rollback path

- Delete `features/493-bill-close-write-has-no-idempotency-key.md`.
- Delete `specs/493-bill-close-write-has-no-idempotency-key-HANDOFF.md`.
- Remove the feature-493 row from `/opt/data/INDEX.md` and from the in-repo
  `INDEX.md`.
- **No application rollback** is needed in this disposition, because this slice
  changed no runtime code.
- For a future implementation: drop the idempotency-key column (or the key→outcome
  table) and its unique index. The migration is additive and reversible; **no
  existing `Bill` row needs rewriting.**

## Mandatory LE31 skill list

Before any implementation, load and follow:

- `le31-conventions` — money invariants and charter boundaries (§3.2, §7);
- `le31-research-workflow` — source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

This feature is already `build`; it needs **no** promotion trigger. What it needs is
an **implementation owner**.

**The ordering constraint is the important part:** this contract lands **before or
in the same pull request as feature 415**, because 415 implements the bill-close
write and would otherwise implement it **without** the idempotency key. Feature 415's
own text must be read before the migration is designed.

**Do not re-implement** the seat write's idempotency (feature **388**) or the stock
write's (features **400** / **401**). If a future pass finds a *different* write
without a key, that is a new instance of this shape and belongs in its own contract
— not here.
