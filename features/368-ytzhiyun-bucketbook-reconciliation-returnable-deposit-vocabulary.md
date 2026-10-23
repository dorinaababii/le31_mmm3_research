# Feature 368 — `ytzhiyun-bucketbook-reconciliation-returnable-deposit-vocabulary` (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub repo `ytzhiyun/bucketbook` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★2/⑂0**, **1,133 KB**, HTML (no backend), created **2026-10-22 AND pushed 2026-10-22 = IN-WINDOW BY BOTH FIELDS (one day old)**, `archived=false`, `fork=false`, 0 open issues. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-23. Description (verbatim from GitHub API, Chinese): *"送水与空桶对账助手：单文件 Web 应用 — 送水录单、空桶押金/欠桶追踪、小票台账、周期报表对账，数据只存浏览器本地。"* Topics (verbatim): `bookkeeping, bucket, local-first, single-file, small-business, water-delivery`. Bucket: **v1 (reconciliation-as-the-product + returnable-deposit round-trip vocabulary)** — Pick B of Daily Brainstorm 2026-10-23. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Record the **returnable-deposit round-trip** — an item that leaves with the customer carrying a monetary liability, and creates a debt on the business until it comes back — as a persistent cross-section reference, and record **reconciliation-as-the-product** (the ledger exists to be reconciled; the reconciliation report *is* the deliverable) alongside it. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **deposit-and-return accounting shape**: `空桶押金` (container deposit) and `欠桶` (outstanding containers). An item leaves the business and owes it money until it returns. **LE31 has no analogue for this.** Prepared-item stock is consumed, not returned; there is no liability concept anywhere in the v1 model.
- A written record of **reconciliation as the primary screen**: the app's purpose is `对账` — reconciling what was delivered against what was paid and what containers came back. Data entry is a means, not the product.
- A written record of the **single-file, local-only, no-server** posture (data stored only in the local browser). §3.5's self-contained purity, recorded as vocabulary — **not** a proposal for v1 architecture, which is server-side Postgres by charter.

**Out of scope (defer artifact):**

- Any change to the `StockEntry` model or any v1 code.
- Adopting the browser-local storage posture (would violate §3.5 server-side Postgres).
- Any liability/credit accounting surface.

## Out of scope

- See "Scope" above. Vocabulary-only; no v1 code.

## Evidence / JTBD

- **Evidence class**: observed. The description names the deposit and outstanding-container mechanics explicitly.
- **Confidence**: high that the *shape* exists and works in a real business (water delivery is a real trade with real deposit economics); **low** that it transfers — the case for it inside a restaurant is **inferred, not observed**, and is recorded as such.
- **Traction caveat**: ★2⑂0, one day old. **No traction evidence in either direction.** The pick is about the shape.
- **JTBD**: none for LE31 today — LE31 sells food, it does not lend containers. Recorded because the *accounting shape* is absent from the model and its absence is currently unfalsifiable (nobody has asked the question).

## Description

`bucketbook` is a Chinese-language single-file web app for a water-delivery business. Three sub-primitives:

1. **Reconciliation as the product.** `周期报表对账` — periodic report reconciliation. The ledger is a means to answer "do the books balance?", not an end in itself. This is a posture LE31 shares (StockEntry exists to derive current stock) but states less explicitly.
2. **The returnable-asset round-trip** (`空桶押金/欠桶追踪`). A customer takes N containers and owes a deposit. The business's receivable is a function of how many have not come back. This requires: a deposit amount per asset type, a per-transaction count of assets dispatched and returned, and a derived outstanding balance. **None of these exist in LE31's model.**
3. **Receipt ledger as an intermediary record** (`小票台账`) feeding the reconciliation — a paper-ticket-shaped ledger, closer to LE31's StockEntry than a typical accounting app.

## Data model

None shipped. The vocabulary implies a **ReturnableAssetType** (deposit amount per unit) and **AssetMovement** (dispatch/return counts, append-only, reconciling to a derived outstanding balance) — a liability projection layered beside the existing stock projection. **This is a new concept for LE31, not an extension of StockEntry**, and would require a charter-level decision.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition:** an owner or staff member describes a real case where a customer holds something of the business's with money attached — deposit bottles, reusable containers, loaned equipment, a signed-for item. Until then this is a curiosity.

## Telegram interaction if any

None. Worth noting only that if a returnable-asset surface ever existed, the cook would not own it — the waiter would, at handover.

## Dependencies

None.

## Open questions

1. **Does v1's stock model admit liabilities at all?** Unmade, charter-level. A deposit is a monetary claim, not a quantity.
2. **Is reconciliation a v1 feature?** It is implicit in the StockEntry projection but has no surface. Feature 349 (`gfs-invoice-breakdown`, 2026-10-20) filed the *supplier-document* side of the same question.
3. **The browser-local posture is explicitly rejected for v1** (charter §3.5 server-side Postgres) and is recorded only as a contrast case.

## Why this matters

Because it names a shape LE31's data model cannot currently express and has never been asked to: an asset that leaves and returns while carrying money. LE31's ledger assumes every movement is a consumption. Recording this keeps the question visible without pretending the answer is obvious — and the water-delivery business is a clean, well-documented instance of the economics.

## Cross-section

Features 108 (StockEntry audit), 225 (`shop-ledger`), 290 (`prime-cost`), 349 (`gfs-invoice-breakdown`, supplier-document ingestion, filed 2026-10-20 — three days ago), 353 (FloCafe inventory). GitHub `ytzhiyun/bucketbook` is unique vs features 1–363 (verified by ripgrep against `features/` and `specs/`). Fully reversible — documentation-only artifact.