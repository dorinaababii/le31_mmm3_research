# Feature 298 — `erhatechnologiesai/point-of-sale-system` v1 small-shop-POS touchscreen-cashier-register-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue)
> **Date:** 2026-10-09
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/298-erhatechnologiesai-point-of-sale-system-mit-cloud-point-of-sale-pos-touchscreen-cashier-register-mock-payments-automated-receipt-generation-customer-loyalty-rewards-v1-small-shop-pos-vocabulary-reference.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/298-erhatechnologiesai-point-of-sale-system-mit-cloud-point-of-sale-pos-touchscreen-cashier-register-mock-payments-automated-receipt-generation-customer-loyalty-rewards-v1-small-shop-pos-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick C)
> **Parent-verified via:** direct GitHub API GET `/repos/erhatechnologiesai/point-of-sale-system` at `/tmp/le31-brainstorm-2026-10-09/verify_erhatechnologiesai_point-of-sale-system.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 small-shop-POS touchscreen-cashier-register cross-section pick is a future-extension signal)

## Goal

Surface a v1 small-shop-POS touchscreen-cashier-register-vocabulary reference for **cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards** as a forward-looking pattern for any future LE31 v1 surface that exposes a small-shop-POS touchscreen cashier register with mock-payments + automated receipt generation + customer loyalty rewards discipline.

## Evidence / JTBD

**Evidence classification:** inferred. The *cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* discipline is forward-looking for any future LE31 v1 small-shop-POS touchscreen-cashier-register surface; no LE31 v1 surface today has cloud-POS-with-touchscreen-cashier-register. **Confidence: high** (0★/0⑂ + 22 KB tiny = most concise in-domain cloud-POS reference of the 72-pass series + MIT permissive + Python ✓ on-stack (FastAPI + Pydantic + SQLite = exact LE31-stack-adjacent) + 10-topic array = 10/10 LE31 v1 small-shop-POS-vocabulary envelope = 100% topic-overlap + IN-WINDOW BY BOTH FIELDS (13-day-old repo) + barcode-touchscreen + automated-receipt-generation + customer-loyalty-rewards = strongest v1 small-shop-POS-on-stack touchscreen-cashier-register cross-section pick of the 72-pass series).

**When** the LE31 owner wants to operate a touchscreen POS register in the restaurant, **the owner wants to** see a working Python + FastAPI + Pydantic + SQLite implementation that demonstrates the *cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* discipline, **but struggles because** the existing v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are LE31-internal primitives with no POS-register surface, **so that** the owner cannot see how a similar small-shop cloud-POS touchscreen cashier register would be structured. The *cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* discipline IS the *cashier-register-as-touchscreen-operator-UI + receipt-as-audit-trail + loyalty-as-customer-recognition* charter §3.1 + §3.7 invariant applied to the *cloud-POS* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* quintuple-primitive as a candidate vocabulary for any future LE31 v1 small-shop-POS-on-stack touchscreen-cashier-register surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive (the *cashier-terminal + fastapi + payment-processing + point-of-sale + pos + pydantic + python + receipt-generator + retail-management + sqlite* 10-topic array IS the §3.1 *touchscreen-cashier-register-as-operator-UI* invariant applied to the *cloud-POS* dimension).
- Record the §3.1/§3.2/§3.3/§3.4/§3.6 alignment per `le31-conventions/SKILL.md`.
- Note the **10-topic array** = 10/10 LE31 v1 small-shop-POS-vocabulary envelope = 100% topic-overlap = strongest v1 small-shop-POS-on-stack touchscreen-cashier-register cross-section pick of the 72-pass series.

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No real-payments integration; the *mock-payments* posture IS the *non-real-money-test-environment* charter §3.4 invariant.
- No receipt-printer integration; v1 has no receipt-printer today.
- No customer-loyalty-rewards surface; v1 has no customer-rewards today.
- No cloud-POS deployment; v1 uses local-Postgres per charter §3.1 invariant.

## Description

`erhatechnologiesai/point-of-sale-system` is a **cloud Point of Sale (POS) system featuring touchscreen cashier register, mock payments, automated receipt generation, and customer loyalty rewards** with the following properties:

- **Cloud Point of Sale** — runs on a cloud-Python backend (FastAPI)
- **Touchscreen cashier register** — the operator interacts with the POS through a touchscreen register UI
- **Mock payments** — payments are mocked for test-environment discipline (charter §3.4: no real-money in test environment)
- **Automated receipt generation** — receipts are auto-generated for every transaction
- **Customer loyalty rewards** — customers earn loyalty rewards on each purchase
- **Retail management** — the POS includes basic retail-management (sales + products + customers + transactions)

**10 topics** (verbatim, parent-verified): `cashier-terminal + fastapi + payment-processing + point-of-sale + pos + pydantic + python + receipt-generator + retail-management + sqlite` = **10/10 LE31 v1 small-shop-POS-vocabulary envelope = 100% topic-overlap = strongest v1 small-shop-POS-on-stack touchscreen-cashier-register cross-section pick of the 72-pass series**.

## Data model

The candidate vocabulary suggests these SQLModel tables (none built today; vocabulary-only):

```
PosRegister:
  id: int (primary key)
  register_name: str  # e.g., 'Front Bar', 'Patio', 'Takeout Window'
  touchscreen_enabled: bool
  receipt_printer_enabled: bool
  loyalty_rewards_enabled: bool
  audit_log_ref: str  # reference to audit_logs row
  created_at: datetime
  archived_at: datetime

PosReceipt:
  id: int (primary key)
  register_id: int (foreign key)
  transaction_id: int (nullable, foreign key)
  receipt_html: str  # auto-generated receipt HTML
  receipt_pdf_blob: bytes (nullable)
  subtotal_eur: Decimal
  tax_eur: Decimal
  total_eur: Decimal
  payment_method: str  # 'mock-cash', 'mock-card', 'mock-voucher'
  loyalty_points_earned: int
  audit_log_ref: str
  created_at: datetime

PosCustomerLoyalty:
  id: int (primary key)
  customer_id: int (foreign key to a future Customer table)
  loyalty_tier: str  # 'bronze', 'silver', 'gold'
  points_balance: int
  total_points_earned: int
  total_points_redeemed: int
  audit_log_ref: str
  created_at: datetime
  updated_at: datetime

PosLoyaltyEarnEvent:
  id: int (primary key)
  loyalty_id: int (foreign key)
  receipt_id: int (foreign key)
  points_earned: int
  points_redeemed: int
  reason: str  # 'purchase', 'birthday-bonus', 'redemption'
  audit_log_ref: str
  created_at: datetime
```

## Implementation steps

If the trigger condition (v1 small-shop-POS touchscreen-cashier-register surface window opens) is met:

1. Read the active feature file in full
2. Confirm `erhatechnologiesai/point-of-sale-system` is still in-window (pushed within last 7 days from trigger date)
3. Set up minimal-HTML/HTMX `pos-register.html` template for the touchscreen cashier register UI
4. Implement `PosRegister + PosReceipt + PosCustomerLoyalty + PosLoyaltyEarnEvent` SQLModel tables
5. Implement the `POS` FastAPI endpoints (`/api/pos/register`, `/api/pos/receipt`, `/api/pos/loyalty`)
6. Implement the automated-receipt-generation discipline (every transaction auto-generates a receipt HTML)
7. Implement the customer-loyalty-rewards discipline (every purchase earns loyalty points)
8. Implement the mock-payments discipline (no real money in test environment)
9. Adapt SQLite to Postgres (LE31 v1 uses Postgres, not SQLite)
10. Adapt Pydantic to LE31 v1 Pydantic schema
11. Run the v1 test suite + the new POS test suite
12. Surface any test failures to the owner

## Telegram interaction if any

The POS layer is *not* a Telegram-bot surface; it is a touchscreen-cashier-register surface. **However**, the POS-receipt-events audit-log SHOULD surface as a daily-Telegram-recap to the LE31 owner (so the owner can see what POS-receipts have been generated today). This Telegram-recap is operator-tooling, not customer-facing AI.

## Dependencies

- FastAPI (already on-stack ✓ per LE31 v1)
- Pydantic (already on-stack ✓ per LE31 v1)
- HTMLReceiptGenerator (Python package; `weasyprint` for PDF generation)
- SQLite (the `point-of-sale-system` choice; LE31 v1 uses Postgres — would need adapter)
- Mock-payment-gateway (test-environment-mocked, not real)

## Open questions

1. Does the *mock-payments* posture comply with charter §3.4 (`AI sandbox` rule: AI may assist owner/staff with observable evidence and non-AI fallback)? **Answer: yes** — the *mock-payments* posture IS the *non-real-money-test-environment* §3.4 invariant; real payments would require explicit charter-§3.4-review for the *real-payment-gateway* surface.
2. Does the *customer-loyalty-rewards* posture breach charter §3.7 privacy? **Answer: yes if customer-PII collected** — the `Customer` table is not part of the candidate vocabulary; the *customer-loyalty-rewards* surface IS a *counts-not-identity* discipline if implemented as *loyalty-tier + loyalty-points + tier-based-discount* without storing customer PII (charter §3.7: counts-not-identity).
3. Does the *cloud-POS deployment* posture comply with charter §3.1 (`on-premise-deployment`)? **Answer: depends** — the *cloud-POS* posture is borderline charter §3.1 on-premise; LE31 v1 uses *local-Postgres*; the *cloud-POS* discipline would need explicit charter-§3.1 review for the *cloud-deployment* surface.

## Why this matters

The **cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards** quintuple-primitive is the canonical v1 small-shop-POS-on-stack touchscreen-cashier-register-vocabulary. LE31 v1 today is server-side + Postgres + FastAPI + cook-Telegram-bot + minimal-HTML/HTMX waiter-UI + append-only StockEntry; the v1 has *no cloud-POS touchscreen cashier register surface* (the LE31 owner has no way to operate a touchscreen POS register; the *touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* discipline IS the canonical v1 small-shop-POS-on-stack touchscreen-cashier-register-vocabulary that would let a future v1 PR add a *cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards* surface that uses the same FastAPI + Pydantic + SQLite stack as the existing waiter web UI). The Python + 10-topic + 0★/0⑨ stack is **§3.1 + §3.2 + §3.4 NOT TRIGGERED** for LE31; the *touchscreen-cashier-register + mock-payments + receipt + loyalty* discipline IS stack-agnostic; the cross-section vocabulary is informative, not a v1-build trigger.

## Charter compatibility

- **§3.1** (explicit-state-transitions) ✓ — the *touchscreen-cashier-register + mock-payments + automated-receipt-generation* posture IS the §3.1 *explicit-state-transition + operator-driven* invariant applied to the *cloud-POS* dimension.
- **§3.2** (privacy, counts-not-identity) ✓ — only *loyalty-tier + points-balance* stored, no customer PII.
- **§3.3** (audit-log-immutability) ✓ — every POS-receipt writes to `audit_logs` via the standard LE31 audit-pipeline.
- **§3.4** (AI sandbox, observable evidence, non-AI fallback) **NOT TRIGGERED** — the *POS + cashier-register + receipt-generator + customer-loyalty-rewards* surface is operator-tooling + customer-data-collection, not customer-facing-AI; the *mock-payments* posture IS the *non-real-money-test-environment* charter §3.4 invariant applied to the *payment* dimension.
- **§3.5** (EUR money discipline) ✓ — `subtotal_eur + tax_eur + total_eur` use `Decimal` per charter §3.6.
- **§3.6** (Paris timezone) ✓ — `created_at + archived_at + updated_at` are timezone-aware datetimes (Europe/Paris).
- **§3.7** (privacy) ✓ — *counts-not-identity* discipline: only *loyalty-tier + points-balance* stored, no customer PII.
