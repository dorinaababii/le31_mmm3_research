# HANDOFF — Feature 500: v2 cross-ledger voucher register as the single reconciliation surface

## Active feature path

`features/500-v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface.md`

**Disposition:** `defer` — v2 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the register shape, the **upstream-of-feature-496** ordering constraint, and the trigger for a future, separately-gated reconciliation scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — the owner's question is "did the day balance?"; no LE31 operator has asked for a register, and the JTBD is inferred from the gap feature 496 leaves open |
| 2. Viability | PASS in principle — the mechanism is stated in one source line and its API surface in the source README; the source is MIT |
| 3. Practicability / confidence | MEDIUM — the source's day book spans ledgers LE31 does not have (tax ledger, GSTR-1); the transferable shape is narrower, and the **voucher structure over LE31's ledger shapes is unspecified** |
| 4. Conflict | No hard conflict — it is **upstream of** feature 496 rather than a duplicate of it, and it consumes rather than replaces feature 81's single-ledger integrity walk |
| 5. Outcome, appetite, scope | DEFER — a second consecutive `defer` day on the reconciliation theme (496 yesterday, this today). The signal is to stop refining this theme, not to keep elaborating it |
| 6. Cost to operational value | LOW now (one document); a real cross-ledger read model over a multi-ledger schema is a substantial slice with no v1 caller |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future reconciliation feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `LedgerVoucher` view/table, **if** the register is materialised;
- `backend/app/services/reconciliation.py` — future voucher derivation and **identity evaluation**;
- `backend/app/routers/reconciliation.py` — future single register endpoint and identity-evaluation endpoint;
- `backend/app/services/export.py` — the future call site where feature 496's export would source its identities from this register instead of asserting them;
- tests — voucher lines balance, the register is a **pure function** of ledger state, a failing identity is **fail-visible**, and the register has **no direct write path**.

**Ordering constraints (not optional):**
1. This feature must land **before** feature 496, not after. 496 exports reconciliation identities; if 496 is built first, the identities are asserted by the export itself and the register arrives later to retrofit a surface that already claims to be checking.
2. Features 373 (`append-only-stock-ledger`), 374 (`derive-current-stock`) and 470 (`ledger-delete-guard`) must be closed first — the register must read ledgers it cannot undermine, and must never become a write path around the append-only guard.
3. The register must be **derived**. A writable register is a second source of truth and cannot detect disagreement.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/500-v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-19/gh/readme_07_nikhilb2_simple-invoicing-free-gst-billing-software.md` (the *Day Book Register* and `/api/ledgers` bullets) and the repository metadata at `/tmp/le31-daily-2026-11-19/gh/repo_07_nikhilb2_simple-invoicing-free-gst-billing-software.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-19.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE 'day ?book|voucher register' features/ specs/` → **0 files**, and `grep -ril 'cross-ledger' features/ specs/` → **1 file** (feature 81, a single-ledger hash-chain walk — not a cross-ledger register).

For a future implementation, required verification includes a test proving **every voucher's lines balance**, a test proving the **register is a pure function of ledger state** (writing to the ledger changes the register; there is no other input), a test proving a **failing reconciliation identity is surfaced visibly** rather than silently dropped, and a test proving the register **has no direct write path**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

**Nothing was executed against Postgres during this research pass.** The findings are README- and schema-level. A future implementation must verify against a live database, not only against the DDL rendering.

## Rollback path

- Delete `features/500-v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface.md`.
- Delete `specs/500-v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface-HANDOFF.md`.
- Remove the feature-500 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.1 single-location / single-currency invariants, the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold:

1. feature 496 is scheduled to be built — the register exists to produce 496's identities, so without 496 there is no consumer;
2. features 373, 374 and 470 are closed;
3. the contract's central open question has an owner answer: **how does a balanced voucher correspond to a stock movement or a bill total over LE31's ledger shapes?** If LE31 has two ledgers rather than a set, the honest outcome is that this feature is **deleted**, not promoted — the contract says so explicitly;
4. the materialised-vs-computed-on-read and the period-boundary questions have owner answers;
5. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**.
