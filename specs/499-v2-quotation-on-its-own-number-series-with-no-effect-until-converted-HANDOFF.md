# HANDOFF — Feature 499: v2 quotation on its own number series with no effect until converted

## Active feature path

`features/499-v2-quotation-on-its-own-number-series-with-no-effect-until-converted.md`

**Disposition:** `defer` — v2 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the effect-semantics rule, the boundary with the append-only ledger, and the trigger for a future, separately-gated quoting scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator has asked for quotes; the JTBD is inferred ("the table asks what it will cost and nothing has happened yet") |
| 2. Viability | PASS in principle — the mechanism is stated in one source sentence and the source is MIT |
| 3. Practicability / confidence | MEDIUM — the source is a GST/India invoicing app; the **effect-semantics rule** transfers, but the number-series format, the PDF machinery and the share-link machinery do not |
| 4. Conflict | No hard charter conflict, but it touches two owned areas: feature 448 (a bill's human-facing identity) and feature 415 (a bill closes a visit). A customer-facing shared offer would additionally collide with §3.2 |
| 5. Outcome, appetite, scope | DEFER — LE31 v1 records orders, not offers; no v1 caller |
| 6. Cost to operational value | LOW now (one document); a real second document class with its own series and a conversion event is not a v1 slice |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future quoting feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `Offer` model and a **distinct** number-series allocator;
- `backend/app/services/offers.py` — future offer lifecycle: issue, convert, cancel;
- `backend/app/services/orders.py` — the **conversion** call site, which is the only point at which effects begin;
- `backend/app/routers/offers.py` — future offer and conversion routes;
- tests — offer-writes-nothing-to-the-ledger, offer-number-not-drawn-from-the-invoice-series, conversion-writes-exactly-once, **conversion-is-not-an-edit** (a second conversion of the same offer is refused, not applied twice).

**Ordering constraints (not optional):**
1. Features 373 (`append-only-stock-ledger`) and 374 (`derive-current-stock`) must be closed first. "No effect" is only a meaningful guarantee once the thing it does not affect is trustworthy.
2. Feature 448 (`a-bill-has-no-human-facing-identity`) must be closed first — the offer's own number series is the same identity class, and two conflicting answers would be worse than one.
3. The offer must **not** be given a customer-facing surface without an explicit owner ruling against charter §3.2.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/499-v2-quotation-on-its-own-number-series-with-no-effect-until-converted.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-19/gh/readme_07_nikhilb2_simple-invoicing-free-gst-billing-software.md` and the repository metadata at `/tmp/le31-daily-2026-11-19/gh/repo_07_nikhilb2_simple-invoicing-free-gst-billing-software.json` (MIT, ★22 / ⑂80, pushed 2026-11-18T16:00:00Z).
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-19.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE 'proforma|pro forma|no effect on (stock|ledger)|number series' features/ specs/` → **0 files**.

For a future implementation, required verification includes a test proving that **issuing an offer writes no `StockEntry` row and changes no derived quantity**, a test proving the **offer number and the invoice number are allocated from different counters**, a test proving **conversion is idempotent-by-refusal** (a second conversion is refused rather than applied), and a test proving a **cancelled offer cannot be converted**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

## Rollback path

- Delete `features/499-v2-quotation-on-its-own-number-series-with-no-effect-until-converted.md`.
- Delete `specs/499-v2-quotation-on-its-own-number-series-with-no-effect-until-converted-HANDOFF.md`.
- Remove the feature-499 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.2 non-goals (customer-facing surfaces, discounts), the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold:

1. the owner asks for a quoting or pre-order capability — this is a **customer-facing-adjacent** scope and §3.2 excludes customer-facing surfaces in v1, so it needs an explicit owner ruling, not just a request;
2. features 373 and 374 are closed;
3. feature 448 is closed;
4. the contract's open questions on partial conversion, cancellation and post-conversion number fate have owner answers, because "no effect **until then**" is unenforceable without them;
5. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**.
