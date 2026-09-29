# Feature 248 — `Antosha122-qr_qod_mobile_menu-mit-qr-menu-telegram-bot-restaurant-business-fine-tuning-ordering-in-telegram-bot-v1-qr-menu-telegram-bot-cross-section` (defer)

> **NEW observation (2026-09-29).** Documents in-window GitHub Search `telegram+bot+restaurant` query result: `Antosha122/qr_qod_mobile_menu` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **1★/0⑂**, Python, **pushed 2026-09-27T18:03:49Z** (in-window by `pushed_at` only — *4 days before fetch time*), **created 2026-06-18T17:29:41Z** (~3 months before window start = OUT-OF-WINDOW by `created_at`; in-window by `pushed_at` only), **198 KB modest repo** (parent-verified via raw GitHub API JSON), `default_branch=main`, `archived=false`). **No topics** (parent-verified from raw JSON: `"topics": []`). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-29): *"A project for further development and fine-tuning for the restaurant business, QR codes for menus and food ordering in a Telegram bot"*. The **QR-menu + Telegram-bot + restaurant ordering** triple-primitive + the *Python + MIT + QR-code-for-menu + Telegram-bot + ordering* discipline is the **first in-window 2026 Python repo combining QR-menu + Telegram-bot + restaurant ordering** = the canonical **v1 cross-section reference to feature 11 (QR-menu)** with the **Telegram-bot vocabulary** vocabulary. LE31 v1's cook-bot is text-only today; a customer-facing Telegram-bot QR-menu ordering surface would integrate with the existing cook-bot and reuse the `StockEntry` ledger for prep-item count updates. Bucket: **v1 qr-menu-+-Telegram-bot cross-section (defer, parking-lot, vocabulary reference)** — zero build time today.

## Goal

Retain the **QR-menu + Telegram-bot + restaurant ordering** triple-primitive + the **Python + MIT + customer-facing-Telegram-bot-as-ordering-channel** stack-shape as a persistent cross-section reference for any future LE31 v1 surface that introduces (a) **customer-facing QR-menu** (a customer scans a QR code at the table and lands on a Telegram bot to browse the menu), (b) **Telegram-bot as ordering surface** (the customer places the order via the Telegram bot, not via the waiter web UI), and (c) **prep-item count updates via existing `StockEntry` ledger** (every order placement triggers a `StockEntry` decrement via the existing cook-bot flow). The artifact is the persistent cross-section reference + the verbatim description + the 3 named primitives. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 198 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **QR-menu + Telegram-bot + restaurant ordering** triple-primitive (the *customer scans QR → lands on Telegram bot → browses menu → places order* flow).
- A written record of the **Telegram-bot as customer-facing ordering channel** primitive (LE31 v1's Telegram-bot today is the cook-bot, not customer-facing; the *customer-facing-Telegram-bot-as-ordering-channel* primitive is the *Telegram-bot receives order + relays to cook-bot + decrements StockEntry* discipline).
- A written record of the **MIT permissive license** posture (charter §3.2 STRICTLY-COMPATIBLE for future code adoption if a v1 PR is triggered).
- A decision record: today's verdict is `defer` because LE31 v1 has no customer-facing Telegram-bot surface today (charter §3.1 v1 surfaces are waiter web UI + cook Telegram bot; the customer-facing Telegram-bot surface is a future v1 surface expansion that requires explicit owner/charter sign-off per charter §3.1 invariant).
- A cross-section reference with the prior QR-menu + Telegram-bot cluster: features 02 (order-taking), 11 (customer-QR-menu), 116 (aiogram-3.31.0-stable-track), 207 (redtidev1918/TelePost telegram-channel + multi-bot + moderation + Mini App + HTTP-API + webhook + self-hosted).

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI (HTMX).
- Any change to the cook Telegram bot (today's cook-bot is text-only; the cross-section reference documents a future customer-facing surface, not a cook-bot expansion).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI; the QR-menu + Telegram-bot ordering surface is purely menu browsing + order placement without AI in the loop).
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema (the QR-menu + Telegram-bot ordering surface would trigger existing `StockEntry` decrements via the existing cook-bot flow; no schema change required).
- Any v2 surface expansion (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any QR-menu + Telegram-bot ordering implementation in v1 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).

## Description

The pick is **`Antosha122/qr_qod_mobile_menu`** — a Python + MIT + QR-menu-for-restaurant + Telegram-bot-ordering vocabulary artifact. **Charter §3.4 NOT triggered** because the artifact is operator-tooling + customer-facing-but-no-AI (the QR-bot receives orders from customers but does not perform AI inference on the customer; the order is placed via pure menu browsing + form submission; the AI-free ordering surface is the safer §3.4 posture). The artifact is the persistent cross-section reference for the verbatim description + the 3 named primitives + the MIT license posture.

**Stack-shape match (the load-bearing primitive):** the *Python* language is on the LE31 pin set; the *MIT permissive license* is charter §3.2 STRICTLY-COMPATIBLE; the *Telegram-bot* vocabulary aligns with LE31 v1's existing aiogram 3.31.0 cook-bot (feature 116). The verbatim description *"QR codes for menus and food ordering in a Telegram bot"* is the **first in-window 2026 Python repo** that combines these three primitives simultaneously.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v1 surface that adopts the *QR-menu + Telegram-bot ordering* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `qr_table` table with `qr_id, table_id, restaurant_id, qr_token, generated_at, expires_at`; a `customer_session` table with `session_id, telegram_user_id, restaurant_id, table_id, started_at, last_active_at`; or a `customer_order` table that links to the existing `Order` + `OrderItem` tables for prep-item count updates via the existing `StockEntry` decrement flow). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would:
1. Read the `Antosha122/qr_qod_mobile_menu` README at https://github.com/Antosha122/qr_qod_mobile_menu for the *QR-menu + Telegram-bot + restaurant ordering* triple-primitive.
2. Cross-reference with LE31 v1's `Order` + `OrderItem` + `StockEntry` schemas to identify the *delta* (the *delta* = `Antosha122/qr_qod_mobile_menu` introduces the *customer-facing-Telegram-bot + QR-menu-as-entry-point + restaurant-ordering-via-Telegram* primitives that LE31 v1's cook-Telegram-bot + waiter-HTMX-UI does not cover for customer-facing ordering).
3. Apply charter §3.1 explicit-state-transitions review to the *delta* (any new v1 surface requires explicit owner/charter sign-off; the *customer-facing-Telegram-bot + QR-menu-as-entry-point* surface is charter §3.1-compatible provided the explicit state transitions are preserved — i.e., the customer order is recorded via the existing `Order` + `OrderItem` schema, the prep-item count is decremented via the existing `StockEntry` decrement flow, the cook receives the order via the existing aiogram cook-bot).
4. Apply charter §3.4 review to the *delta* (the QR-menu + Telegram-bot ordering surface must be pure menu browsing + order placement without AI inference on the customer input; the surface is §3.4-compatible because the AI-free ordering surface is the safer §3.4 posture; any future AI-augmented menu recommendation or AI-augmented order suggestion would require explicit §3.4 review before adoption).
5. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `Antosha122/qr_qod_mobile_menu` reference is the *vocabulary* for *QR-menu + Telegram-bot + restaurant ordering*, NOT for *customer-facing-Telegram-bot replacement*.

## Telegram interaction

Zero Telegram interaction today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would add (a) a customer-facing Telegram-bot instance (separate from the cook-bot) that receives customer orders, (b) a relay channel that forwards customer orders to the cook-bot (the existing aiogram cook-bot receives the order via the existing aiogram sendMessage API), (c) a /qr_menu command that generates a per-table QR code via the existing FastAPI endpoint, (d) a /start command on the customer bot that links the customer's Telegram user ID to the table via the QR token.

## Dependencies

- **LE31 v1 customer-ordering surface** — currently waiter-HTMX-UI only; the QR-menu + Telegram-bot ordering surface would be a future v1 surface expansion that requires explicit owner/charter sign-off per charter §3.1 invariant.
- **LE31 v1 `Order` + `OrderItem` + `StockEntry` schemas** — the QR-menu + Telegram-bot ordering surface would reuse these existing schemas for prep-item count updates; no schema change required.
- **LE31 v1 aiogram 3.31.0 cook-bot** — already pinned; the customer-facing Telegram-bot would be a new instance that relays to the existing cook-bot via the existing aiogram sendMessage API.
- **Cross-references:** features 02 (order-taking), 11 (customer-QR-menu), 116 (aiogram-3.31.0-stable-track), 207 (redtidev1918/TelePost telegram-channel + multi-bot + moderation + Mini App + HTTP-API + webhook + self-hosted).

## Open questions

- Does LE31 v1 want a *customer-facing Telegram-bot* surface at all? The current v1 waiter-HTMX-UI is the customer-facing surface; the *customer-facing-Telegram-bot* primitive would change this to a *Telegram-bot-receives-order* surface that the waiter no longer handles directly. The trade-off is: (a) waiter-HTMX-UI = single surface, waiter-mediated, no customer-Telegram-account-required; (b) customer-Telegram-bot = direct customer-to-kitchen ordering, no waiter bottleneck, but introduces the *customer-Telegram-account-required* requirement. The decision is **owner's** — the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off.
- Does LE31 v1 want a *QR-menu-as-entry-point* surface? The current v1 menu surface is the waiter-HTMX-UI; the *QR-menu-as-entry-point* primitive would let customers scan a QR code at the table to access the menu + ordering. The trade-off is: (a) waiter-mediated-menu = waiter reads out the menu, no QR-code infrastructure; (b) QR-menu = self-serve menu browsing, requires QR-code-printing + per-table-QR-generation. The decision is **owner's**.
- Does LE31 v1 want *customer-facing-Telegram-bot-relays-to-cook-bot* or *customer-facing-Telegram-bot-is-the-cook-bot*? The *relay-to-cook-bot* posture separates the customer-facing channel from the cook-only channel (cleaner separation of concerns but requires a relay mechanism); the *customer-facing-Telegram-bot-is-the-cook-bot* posture unifies the two channels (simpler but requires the customer to be added to the cook-bot's chat). The decision is **owner's**.

## Why this matters

- The **verbatim description** *"QR codes for menus and food ordering in a Telegram bot"* is the **first in-window 2026 Python repo** that combines the QR-menu + Telegram-bot + restaurant ordering primitives simultaneously. The cross-section reference is high-value for any future LE31 v1 surface that introduces customer-facing Telegram-bot ordering.
- The **MIT permissive license** posture makes this the **STRICTLY-ADOPTABLE QR-menu + Telegram-bot ordering primitive** of the 60-pass series.
- The artifact is **vocabulary-only**; zero build time today; fully reversible (delete the feature file + the HANDOFF + the Linear sub-issue is the complete rollback).
- The trigger condition is **the first v1 PR that proposes a customer-facing Telegram-bot ordering surface, a QR-menu-as-entry-point surface, or a QR-menu + Telegram-bot integration**.

## Cross-section evidence (one-line each)

- The `QR-menu + Telegram-bot + restaurant ordering` triple-primitive is the canonical v1 cross-section reference to feature 11 (QR-menu) with Telegram-bot vocabulary.
- The `Python + MIT + customer-facing-Telegram-bot-as-ordering-channel` stack-shape is the verbatim LE31 v1 cross-section to feature 116 (aiogram-3.31.0-stable-track).
- The verbatim description *"QR codes for menus and food ordering in a Telegram bot"* is the load-bearing value of the artifact.
- Net-new observation 2026-09-29 (ripgrep-confirmed unique vs features 1–247).