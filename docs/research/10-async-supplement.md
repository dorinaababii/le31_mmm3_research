# Async Subagent Supplement — Additional Projects

This is a follow-up to `00-landscape-overview.md` and the per-category files.
The async subagent dispatched earlier (running while the main research was
being written up) returned additional projects that are worth documenting:

## Additional POS / KDS-bundled projects

### chefcito — https://github.com/alfi-j/chefcito

- **Stars**: 5 · **Last push**: 2026-07-24 · **License**: MIT
- **Stack**: Next.js 14 + MongoDB
- **Why interesting**: a POS+KDS combo with **real-time** sync between
  service and kitchen. Worth looking at for the WebSocket/real-time patterns
  when we wire the waiter UI to the kitchen Telegram bot (so the cook sees
  new orders instantly).

### amritmaurya1504/Restaurant_POS_System — https://github.com/amritmaurya1504/Restaurant_POS_System

- **Stars**: 253 · **Last push**: 2025-03-02 · **License**: NOASSERTION
- **Stack**: MERN (Mongo / Express / React / Node), integrates Razorpay
- **Why interesting**: classic full-stack POS with payment gateway integration.
  Useful as a learning reference, **not** as a fork target (unmaintained since
  March 2025, license is unclear).

### satisfecho/pos — https://github.com/satisfecho/pos

- **Stars**: 22 · **Last push**: 2026-07-24 · **License**: NOASSERTION
- **Stack**: TypeScript, self-hosted multi-tenant
- **Why interesting**: actively maintained, includes menu / tables /
  reservations / payments (Stripe + Revolut) / KDS / shift / inventory in one
  bundle. Very recent commits (July 2026). Worth a quick look for the shift
  management module if we punt on URY/ERPNext.

## Additional OCR project

### Umi-OCR — https://github.com/hiroi-sora/Umi-OCR

- **Stars**: 46,222 · **Last push**: 2025-11-20 · **License**: MIT
- **Stack**: Python, offline desktop OCR (Qt UI)
- **Why interesting**: bulk OCR with batch processing and built-in screenshot
  OCR. Could be useful if the cook wants to upload multiple menu photos at
  once (e.g. several pages) — but it's a **desktop** app, so we'd use the
  underlying engines (PaddleOCR / RapidOCR) directly, not the Qt frontend.

## Additional Telegram framework

### AstrBot — https://github.com/AstrBotDevs/AstrBot

- **Stars**: 38,008 · **Last push**: 2026-07-24 · **License**: AGPL-3.0
- **Stack**: Python, multi-IM (Telegram / Discord / Slack) + LLM plugins
- **Why interesting**: chat bot framework with built-in LLM integration.
  **Heavyweight for our needs** — we're sticking with `aiogram` for now.
  Worth knowing about if we ever want to add Discord or Slack as alternative
  interfaces.

## Tip reconciliation reference

### Dev-Lueders/Tip_Reconciliation — https://github.com/Dev-Lueders/Tip_Reconciliation

- **Stars**: 0 · **Last push**: 2025 · **License**: MIT-ish
- **Stack**: Excel macro (not Python — but the algorithm is documented)
- **Why interesting**: a reference for the **tip-distribution algorithm**
  (split a daily tip pool across staff by hours worked / role / points).
  Out of scope for v1, but a useful artifact when we revisit tip pooling in
  v2. See `../features/05-payment-tip-reconciliation.md` for the v1 scope.

---

## Updated verdict

The 5 already-documented fork candidates in `08-deep-dive-top-5.md` remain the
right targets. These additional projects either:
- Have very small communities (chefcito, satisfecho, Tip_Reconciliation), or
- Are heavier-weight than we need (URY, ERPNext), or
- Are frameworks we already plan to use libraries from (aiogram, RapidOCR).

**No change** to the recommended path: build fresh in Python (FastAPI +
aiogram + PostgreSQL + RapidOCR). The new projects inform *which patterns*
to borrow, but none of them change the architectural decision.

---

## Refined gaps list (from the async subagent's analysis)

The async subagent also produced a sharper "Gaps & Opportunities" list.
Each gap is documented in our features; here's the mapping:

| Gap (from subagent) | Our feature |
|---|---|
| Finite stock of prepared items | [03-kitchen-stock-tracker](../features/03-kitchen-stock-tracker.md) |
| Telegram-driven menu photo OCR → stock | [04-menu-photo-bot](../features/04-menu-photo-bot.md) |
| Party demographics as first-class schema | [06-guest-demographics](../features/06-guest-demographics.md) |
| Derived tip = paid − items | [05-payment-tip-reconciliation](../features/05-payment-tip-reconciliation.md) |
| Single-binary install | [09-recommended-stack](../research/09-recommended-stack.md) |
| Idempotent re-upload menu photo | [04-menu-photo-bot](../features/04-menu-photo-bot.md) — Open Questions |
| One-click docker-compose demo | Not yet specced — flag for v1.5 |