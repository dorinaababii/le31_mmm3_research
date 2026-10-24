# HANDOFF — Feature 373: `ramaraihan12/warung-pos` — offline-first, derive-never-store, integer-money vocabulary

**Upstream source repo: [`ramaraihan12/warung-pos`](https://github.com/ramaraihan12/warung-pos)** — see `features/373-ramaraihan12-warung-pos-mit-offline-first-pos-no-network-idempotent-sync-uuidv7-outbox-stock-derived-never-stored-integer-money-no-floats-v1-offline-first-derive-never-store-integer-money-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> ⚠️ **This HANDOFF is an audit instrument, not a citation.** Feature 373's reference was used to check LE31's own code, and the check found a real defect: `Batch.qty_remaining` is persisted, but charter §4.3 says it must be derived. **That defect is Feature 374, which has its own HANDOFF. If you are here to fix a stock bug, go to Feature 374's HANDOFF, not this one.**

## Active feature path

`features/373-ramaraihan12-warung-pos-mit-offline-first-pos-no-network-idempotent-sync-uuidv7-outbox-stock-derived-never-stored-integer-money-no-floats-v1-offline-first-derive-never-store-integer-money-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | No operator pain is reported. LE31 is online, single-VPS, server-authoritative (§3.2); nothing in LE31's history says "we lost sales because the network dropped". Evidence class **inferred**. **A failing check 1 is what makes this a defer.** |
| 2 | Viability | ✓ | MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★0⑂0, 575 KB, TypeScript **off-stack**. **Traction caveat: ★0⑂0 and created 2026-10-24 (same day as this pass) — the project is unproven and the shape is the artifact, not the code.** The upstream is 3 days old. |
| 3 | Practicability and confidence | ✓ | The *patterns* are portable (derive-never-store, idempotent outbox, integer money, no-refusal oversell). The *stack* is not (Next.js/Drizzle/Dexie/Postgres 17 vs FastAPI/SQLModel/SQLite). Evidence strength: **high** for the invariant statements (they are in the upstream README, in upstream's own words), **low** for present urgency. |
| 4 | Conflict | ✓ | The vocabulary violates nothing — it *is* §3.6 + §4.3. **But adopting the substance WOULD conflict:** a client-side outbox and device-generated ids are an offline-first architecture, and §3.2 commits LE31 to a single VPS with a server-authoritative model. The reference is therefore **vocabulary-only, deliberately.** |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Maximum time worth spending: **30 min documentation**. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is that a reference was used as an *audit*, which found Feature 374. ~30 min of documentation; no build, no training, no maintenance. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. |

**Gate verdict: `defer` (parking-lot)** — check 1 fails on evidence class. The other six pass because the *vocabulary* is sound; what LE31 does not have is the pain.

## Bucket

**v1 (offline-first + derive-never-store + integer-money vocabulary)** — Pick A of Daily Brainstorm 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**None today.** Documentation-only.

**One optional, cheap, and genuinely actionable residue** — record it, do not do it as part of this feature:

- `backend/app/models.py` — the money fields are already `Decimal = Field(max_digits=10, decimal_places=2)` (parent-verified: `unit_price`, `subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`, `amount`, `opening_float`, `counted_cash`, `variance`). **The type is right; the guard is missing.** A `Decimal` write with a third decimal place is *rounded*, not rejected. The upstream reference's stronger property is *"a guard that throws on a fractional value"*. **This is a separate small feature and is NOT bundled here** — it is recorded as an open question in the feature contract. Do not add it silently to a money-path PR; file it.
- `tests/test_money_precision.py` — if a fractional-money guard is ever implemented, the test must prove the guard *raises* rather than rounds.

**The load-bearing verification for this pick was already performed by the parent on 2026-10-24.** It is reproduced here so a future reader can re-run it and get the same answer rather than trusting this document:

```bash
cd /opt/data/le31_mmm3_research_work
# 1. the persisted column
grep -n "qty_remaining" backend/app/models.py
# 2. the absence of a derivation site (expect: no code hits)
grep -rn "qty_remaining" . --include=*.py --include=*.html --include=*.sql | grep -v "\.venv"
# 3. the absence of the services directory that two HANDOFFs name
ls backend/app/services/ 2>&1
# 4. the routers that exist (expect: only tables.py)
ls backend/app/routers/
```

Parent-run result on 2026-10-24: (1) `backend/app/models.py:106: qty_remaining: int`; (2) **no code hits** — only the declaration; (3) `No such file or directory`; (4) `__init__.py  tables.py`. **The consequence is filed as Feature 374.**

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For a `defer` reference feature, the observable behaviour is **that a future builder can find the reference and the audit it produced** — the verification is that the two files (this HANDOFF and the feature contract) name the same upstream repo, the same upstream README sentences, and the same four features that need updating (26, 34, 371, 372). There is nothing to run.

For the **audit** half (already done, and the thing worth repeating), the observable behaviour is **that the grep output above still says what it said on 2026-10-24** — i.e. the check is re-runnable and its result is recorded, not asserted.

## Rollback path

`git rm features/373-*.md specs/ramaraihan12-warung-pos-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Money* and *Stock* rules first)
- `le31-data` — append-only ledger rules (`StockEntry`: never update or delete)
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.2, §3.6, §4.3)

## Open questions carried into any future build

1. **Should LE31 add a fractional-value guard on money writes?** The reference says yes; the reference is right that a guard is stronger than a type. **Unmade owner decision.**
2. **What is LE31's oversell policy?** Never asked, never written down. The upstream answer is: never refuse a sale, record the negative stock, surface it in an attention list. **Unmade owner decision.**
3. **Should LE31 ever be offline-first?** That is a v2-scale architectural decision, not a feature, and §3.2 currently commits to the opposite. **Unmade owner decision — and this reference is the starting point for it, whenever it is made.**
4. **Does LE31 need an "attention"/anomaly surface?** The upstream policy implies one (a list of things the owner should look at). LE31 has `features/15-inventory-variance.md` and `features/34-stockout-prep-board-snapshot.md` but no anomaly surface in the waiter UI. A new surface would conflict with §3.1's two roles; the natural home is the existing end-of-day recap. **Unmade owner decision.**
