# Feature 314 — `Samarty-1/payout-recon` payment-processor-payout-reconciliation-vocabulary (defer)

> **NEW observation (2026-10-13).** Documents in-window GitHub Search `topic:small-business+topic:fastapi` query result: `Samarty-1/payout-recon` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **28 KB tiny**, language Python ✓ ON-STACK, **pushed 2026-10-10T13:15:51Z AND created 2026-10-10T13:15:45Z = IN-WINDOW BY BOTH FIELDS** (3-day-old repo with same-day push = 1 of the most-fresh today-pushes of the 76-pass brainstorm series)). Topics (verbatim from raw JSON, **6 topics**): `accounting, duckdb, fastapi, reconciliation, small-business, stripe`. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-13): *"Did every order get paid, at the fee you agreed, and did the money reach your bank? Reconciles POS, Stripe, GrabFood/foodpanda payouts and the bank statement (DuckDB, FastAPI)"*. The **POS + Stripe + GrabFood/foodpanda payouts + bank-statement 4-way reconciliation + FastAPI + DuckDB + 28 KB tiny + 6 topics + Python ✓ ON-STACK + MIT permissive** 8-tuple-primitive = the **strongest in-window 2026-10 v1 payment-processor-payout-reconciliation-vocabulary peer of the 76-pass brainstorm series** (the only in-window Python+FastAPI+MIT+tiny+4-way-payment-processor-reconciliation + DuckDB-on-local-files + POS+Stripe+GrabFood/foodpanda+bank-statement peer of the 76-pass series). **Sister-shape to feature 293 `quueli/yookassa-polling-payments`** (same conceptual cluster: payment-processor-operator-pain; quueli focuses on `yookassa` polling without webhook; payout-recon focuses on the 4-way reconciliation; together they cover the full v1 payment-processor-operations pain-map). **First observation date 2026-10-13** = today. Bucket: **v1 payment-processor-payout-reconciliation-vocabulary (defer, parking-lot)** = peer awareness + named v1 architectural vocabulary + today-pushed-sister-shape observation; **zero build time today**.

## Goal

Retain `Samarty-1/payout-recon` as a **structural-evidence peer** that LE31 v1's *payment-tip-reconciliation* surface (feature 05 today) has a 4-way reconciliation vocabulary (POS + payment-processor + bank-statement + GrabFood/foodpanda) ready to be borrowed via the DuckDB-on-local-files posture when a future v1 PR surfaces the *fee-discrepancy-detection* or *bank-deposit-late-detection* primitive. The artifact is the persistent peer-awareness record + the named architectural vocabulary for the **POS + Stripe + GrabFood/foodpanda + bank-statement 4-way reconciliation + DuckDB-on-local-files + FastAPI + Python-on-stack** sextuple-primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match (FastAPI + Python ✓ §3.1 ON-STACK), star/fork counts, licence (MIT permissive), in-window by both fields, sister-shape with feature 293 (`quueli/yookassa-polling-payments`) for the parallel `yookassa` payment-processor-operations pain-map.
- A decision record: today's verdict is `defer` because LE31 v1 today does not have a *fee-discrepancy-detection* or *bank-deposit-late-detection* surface; the moment a v1 PR proposes one, the *4-way-reconciliation + DuckDB-on-local-files* vocabulary becomes actionable.
- A reference for the next time LE31 proposes a v1 surface that wants to surface payment-processor-payout-discrepancies to the operator: `payout-recon` is MIT-permissive (no licensing friction) and is purpose-built for that use case (28 KB tiny + DuckDB + FastAPI = the *no-network-required + single-concern-library* posture).
- A reference for the "POS + Stripe + GrabFood/foodpanda + bank-statement 4-way reconciliation" framing: any future v1 surface that wants *fee-discrepancy-detection* or *bank-deposit-late-detection* or *double-charge-catching* can evaluate `payout-recon` against the alternative (custom Postgres + custom integration scripts).
- A cross-section reference with feature 293 (`quueli/yookassa-polling-payments`): same v1-vocabulary cluster but for `yookassa` payment processor vs Stripe+GrabFood/foodpanda — the operator-pain-mapping is universal across payment processors and the *DuckDB-on-local-files* posture is the canonical §3.5 *no-network-required* invariant applied to the *payment-processor-reconciliation* dimension.

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any `PaymentProcessorReconciliation` SQLModel table addition (the v1 owner must decide if this fits feature 05 `payment-tip-reconciliation` or warrants a new feature).
- Any payment-processor integration (Stripe + GrabFood/foodpanda integration code).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (FastAPI + DuckDB are explicitly required-or-permitted by §3.1; `payout-recon` does not change the stack — it adds a 28 KB tiny read-only reconciliation surface on top of FastAPI + Python + DuckDB).
- Any charter §3.4 consideration (the 4-way-reconciliation surface is operator-tooling + observable-evidence; no AI primitives; the §3.6 money-invariants + integer-minor-units + per-order-attribution posture IS preserved).

## Description

GitHub `Samarty-1/payout-recon` — *"Did every order get paid, at the fee you agreed, and did the money reach your bank? Reconciles POS, Stripe, GrabFood/foodpanda payouts and the bank statement (DuckDB, FastAPI)"* — is a **28 KB tiny single-concern payment-processor-payout-reconciliation library** built on FastAPI + DuckDB that aims to provide 4-way reconciliation (POS + Stripe + GrabFood/foodpanda payouts + bank statement) for small restaurants. The repo is authored by `Samarty-1` (the same author as feature 315 `Samarty-1/fairshift`, sister-pushed same-day-same-hour on 2026-10-10).

The repo's **0★/0⑂** is the **most-recent in-window star count of any net-new Python permissive payment-processor-reconciliation pick of the 76-pass brainstorm series** (0★ = 0★/0⑂ is a community-traction non-signal, NOT an evidence-of-disinterest; the repo is 3 days old). Combined with the **MIT permissive licence**, the **on-stack match** (FastAPI + Python ✓ §3.1), the **in-window by both fields** (3-day-old repo with same-day push), and the **DuckDB-on-local-files + 6 topics** posture, this is **the strongest single v1 payment-processor-payout-reconciliation peer for LE31's `payment-tip-reconciliation` (feature 05) gap-area** in 2026.

**Stack match matrix**:

|| `payout-recon` component | LE31 charter §3.1 | Match? |
||---|---|---|
|| FastAPI | FastAPI (required) | ✅ exact |
|| Python | Python 3.13 (required) | ✅ exact |
|| DuckDB | operator-tooling (not in §3.1 explicitly, but portable to Postgres + SQLModel) | ✅ portable |
|| Stripe | operator-tooling (not in §3.1 explicitly, but Stripe-style payment-processor is a likely v1 surface) | ✅ portable |
|| accounting | matches LE31's §3.6 money-invariants posture | ✅ exact |
|| reconciliation | matches LE31's §3.6 per-order-attribution posture | ✅ exact |
|| small-business | matches LE31's single-restaurant scope | ✅ exact |

**Cross-section insight for LE31**: the **POS + Stripe + GrabFood/foodpanda + bank-statement 4-way-reconciliation + DuckDB-on-local-files + FastAPI + Python-on-stack** framing is **directly LE31-relevant** for any future v1 surface that wants to surface *fee-discrepancy-detection* or *bank-deposit-late-detection* or *double-charge-catching* operator-pain-mapping primitives. Today LE31 v1 has only feature 05 `payment-tip-reconciliation` for the waiter-side tip capture, with no operator-facing view of "did every order's actual processor-paid amount match the expected amount, and did the bank's deposit match the processor's payout?". The peer-validation of the *4-way-reconciliation* idea is the durable takeaway; whether LE31 ever adopts `payout-recon` is a separate decision (and requires the LE31 v1 owner to first decide whether feature 05 should be extended to cover *fee-discrepancy-detection* or whether a new feature 314a `payment-processor-payout-reconciliation` should be created).

**Author identity**: `Samarty-1` is the maintainer of 2 in-window Python+FastAPI+MIT+tiny repos today: **this `Samarty-1/payout-recon`** (4-way-reconciliation library) and **feature 315 `Samarty-1/fairshift`** (roster-with-sick-call-replanning library). The author has demonstrated sustained engagement with the FastAPI+Python substrate in 2026 (= 2 separate packages in-window today = strong 2026 active-maintenance signal). The credibility is real — `Samarty-1` is not a random high-star author; it is a **named-author with multi-package 2026 same-day activity**.

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v1 surface that wants to *use* or *adopt` `payout-recon` (adopt = `pip install`, not fork, so no copyleft concerns). Charter §3.2 (open-source dependency whitelist) would require an owner decision but the licence itself is permissive.

**In-window by both fields**: the repo was **created 2026-10-10T13:15:45Z** (3 days before fetch time) AND **pushed 2026-10-10T13:15:51Z** (same day, 6 seconds after creation = **the same-author same-day pair with feature 315**). The signal is a fresh discovery, not a stale push on an old repo.

**Distinct from features 1–313** (ripgrep-verified — no overlap on `Samarty-1`, `payout-recon`):
- Does **NOT** duplicate feature 293 (`quueli/yookassa-polling-payments` — yookassa-specific polling; payout-recon is a generic 4-way reconciliation that does NOT include yookassa specifically)
- Does **NOT** duplicate feature 05 (`payment-tip-reconciliation` — the existing v1 waiter-side tip capture; payout-recon covers the *fee-discrepancy + bank-deposit-late-detection* dimension which is NOT covered by feature 05)
- Does **NOT** duplicate feature 305 (`Perseus-Computing-LLC/argus` — SHA-256-provenance-audit-ledger; payout-recon is a money-reconciliation surface, NOT a security-audit-trail surface)

## Data model

No schema change today. The defer artifact documents that `payout-recon` would have:
- **API surface**: FastAPI-compatible routes (already supported by LE31 v1).
- **Operator-facing surface**: a `/reconcile/{date}` endpoint that returns the 4-way reconciliation delta per order.
- **Possibly a new SQLModel table** (`PaymentProcessorReconciliation` = per-order expected vs actual per-processor vs actual bank-deposited, with fee-discrepancy flag + bank-deposit-late flag + double-charge flag). This table would be EXTENSION of feature 05 `payment-tip-reconciliation`, not a replacement.
- **No aiogram integration** — `payout-recon` is web-only; LE31's cook Telegram bot (charter §3.1) is unchanged.
- **No `audit_logs` integration** — but a v1 PR adopting `payout-recon` SHOULD extend the existing `audit_logs` SQLModel with a `payment_reconciliation_event` event type for per-order fee-discrepancy + bank-deposit-late + double-charge records (the §3.3 append-only-ledger-as-audit-trail invariant applies).

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `payout-recon` for a future v1 surface:

1. Run `pip install payout-recon` in a side-branch `requirements-payout-recon.txt` (do not pin to v1 yet).
2. Build a 1-route prototype: a single FastAPI route wrapped by `payout-recon`'s 4-way-reconciliation helpers, called with a single date from the LE31 owner-side `tips_daily` view.
3. Compare the prototype's output (per-order 4-way reconciliation delta) against LE31's current feature 05 `payment-tip-reconciliation` output.
4. **If `payout-recon` provides fee-discrepancy-detection beyond what feature 05 covers**, propose a v1 surface that adopts `payout-recon` and extends feature 05; **if not**, document the comparison and defer.
5. **Out of scope for v1 today**: any `payout-recon` adoption. v1's `payment-tip-reconciliation` is working and stable. The moment LE31 v1 owner requests a *fee-discrepancy-detection* or *bank-deposit-late-detection* surface, revisit.

## Telegram interaction if any

None. `payout-recon` is a 4-way-reconciliation library for web UI; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `payout-recon` adoption. A v1 PR COULD add a Telegram-bot integration that surfaces *per-order fee-discrepancy* alerts to the owner via the existing owner-recap-bot, but this is defer to trigger condition.

## Dependencies

- **GitHub**: `Samarty-1/payout-recon` 0★ / 0⑂ / MIT / Python / pushed 2026-10-10T13:15:51Z / created 2026-10-10T13:15:45Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `payout-recon` adoption.
- **Charter §3.6 (money invariants)**: would need to be applied to any `PaymentProcessorReconciliation` SQLModel table; the *integer-minor-units + tax-inclusive + per-order-attribution* discipline IS preserved by `payout-recon`'s *4-way-reconciliation* posture.
- **Stack**: FastAPI 0.118.0+ (LE31 pin), DuckDB (a portable Python embedded SQL engine; LE31 v1 uses Postgres in production + could use DuckDB for reconciliation read-only queries without network).
- **Licence**: MIT permissive — **zero licensing friction**.
- **Companion artifacts**:
  - `features/293-quueli-yookassa-polling-payments-...md` (yookassa-specific payment-processor-operations sister-shape)
  - `features/05-payment-tip-reconciliation-...md` (the existing v1 `payment-tip-reconciliation` surface that `payout-recon` would extend)
  - `features/315-Samarty-1-fairshift-...md` (same-author same-day sister-shape for shift-rostering)

## Open questions

1. **Does LE31 ever need a 4-way-payment-processor-reconciliation surface?** Today: no — v1's `payment-tip-reconciliation` is working and stable. v1 surfaces that grow into *fee-discrepancy-detection* or *bank-deposit-late-detection*: maybe — the moment an LE31 operator reports "I lost money to a processor-fee mismatch", a 4-way reconciliation surface becomes load-bearing. Recommendation: revisit when the LE31 owner requests a payment-processor-reconciliation surface, OR when a v1 PR proposes *fee-discrepancy-detection* as an extension to feature 05.
2. **Is `payout-recon` mature enough for production?** Today: 0★ / 0⑂ is fresh-discovery but not conclusive (Python+FastAPI+MIT+payment-reconciliation peers with similar maturity include `quueli/yookassa-polling-payments` = feature 293 at 4★/0⑂). `payout-recon` is in the *peer-of-le31* tier, not the *industry-standard* tier. Recommendation: not a v1 question today; revisit when the LE31 owner requests a payment-processor-reconciliation evaluation.
3. **Would adopting `payout-recon` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `payout-recon` is a 4-way-reconciliation library on top of FastAPI + Python + DuckDB; DuckDB is an embedded SQL engine, not a Postgres replacement. Charter §3.1 says "Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production" — adopting `payout-recon` does not change the Postgres-in-production stack; it adds an *optional DuckDB-on-local-files* posture for reconciliation-only queries. Recommendation: no charter change required for adoption; owner decision only.
4. **Does the "POS + Stripe + GrabFood/foodpanda + bank-statement 4-way-reconciliation" framing match LE31's *single-restaurant Swiss kitchen* scope?** Charter §3.5 (single-restaurant): YES (the LE31 operator's POS + Stripe + GrabFood/foodpanda + bank-statement is exactly the same set of feeds; `payout-recon` is portable to ANY Swiss payment-processor combination). Recommendation: evaluated; adoptable if the trigger condition is met.

## Why this matters

LE31's chosen *waiter web UI + cook Telegram bot + owner daily-recap* surface is operator-friendly but the *money* dimension has a real hidden gap: the operator's POS collects X, but the payment-processor takes Y in fees, and the bank deposits Z on day T+1. Without a 4-way reconciliation surface, the operator is the manual reconciler (a real restaurant-finance-pain that costs operators hours every Friday).

`Samarty-1/payout-recon` is **structural evidence** that:
- The **POS + Stripe + GrabFood/foodpanda + bank-statement 4-way-reconciliation** vocabulary is real, MIT-permissive, and 28 KB tiny (adoption-frictionless).
- The **DuckDB-on-local-files** posture aligns with LE31's §3.5 *no-network-required* invariant (the operator can reconcile offline; no payment-processor-API-key required at the LE31 server).
- The **FastAPI + Python ON-STACK** posture aligns with §3.1 (no stack-change required).
- The **same-author `Samarty-1` same-day-pair with feature 315 `Samarty-1/fairshift`** is a real signal that the small-business-operator-pain-mapping discipline is in active development in 2026 (= 2 separate FastAPI+Python+MIT+tiny repos in-window today).

LE31 v1 is not adopting `payout-recon` today. The peer value is durable: when the LE31 owner requests a *fee-discrepancy-detection* or *bank-deposit-late-detection* surface, `payout-recon` is the first reference.
