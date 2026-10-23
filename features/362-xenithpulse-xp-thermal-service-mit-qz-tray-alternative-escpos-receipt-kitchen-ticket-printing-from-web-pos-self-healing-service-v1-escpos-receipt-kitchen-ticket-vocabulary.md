# Feature 362 — `xenithpulse/xp-thermal-service` QZ-Tray-alternative-ESC/POS-receipt-+-kitchen-ticket-printing-from-any-web-POS-+-self-healing-Windows-service (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub Search `restaurant-pos` result: `xenithpulse/xp-thermal-service` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★5 / 3⑂**, **1026 KB modest**, TypeScript/Node.js **OFF-STACK**, **pushed 2026-10-22T15:20:56Z AND created 2026-03-19T16:57:44Z = IN-WINDOW BY BOTH FIELDS**). Topics (verbatim from raw JSON, **17 topics**): `barcode, esc-pos, esc-pos-printer, esc-pos-printer, nodejs, point-of-sale, pos, printing, qz-tray-alternative, receipt-printer, restaurant-pos, restaurant-pos-software, restaurant-pos-system, thermal-printer, thermal-printer-driver, typescript, windows-service`. Description (verbatim, parent-verified via direct `GET /repos/` 2026-10-23): *"Free, open-source QZ Tray alternative. Print ESC/POS receipts & kitchen tickets from any web POS to USB or network thermal printers. Self-healing Windows service."*. **Fully reversible** (vocabulary-only artifact). Trigger condition = first v1 PR proposing printer output of any kind, OR an offline-sync decision being opened.

## Goal

Retain `xenithpulse/xp-thermal-service` as a **structural-evidence peer** documenting the **ESC/POS-as-a-decoupled-print-boundary** primitive for LE31's not-yet-existing printer surface. The artifact is the peer-awareness record plus the named vocabulary for **print-as-a-sidecar-service that any web POS can drive, with a self-healing supervisor**. No code today.

**Why this pick is different from feature 348/355:** features 348 (`ninondev/stove`) and 355 (`Haroon-World/RestaurantPOS_Android`) both carry ESC/POS, but both are *single-application* shapes — the print path is welded to the app. This pick's distinctive idea is the **boundary**: printing is a **Windows service** with its own lifecycle, reachable from *any* web POS. The protocol is not copyrightable, so the primitive is reusable regardless of licence.

## Scope

**In scope (defer artifact):**
- A written record of the peer: licence (MIT), ★5 / 3⑂, 1026 KB, 17 topics, in-window by both fields, language OFF-STACK.
- A decision record: verdict is `defer` because LE31 v1 has **no printer surface today** and no trigger has fired.
- A named vocabulary: **print-boundary / sidecar-service / self-healing-supervisor / QZ-Tray-substitution**.
- A cross-section reference with feature 355 (`Haroon-World/RestaurantPOS_Android` — Bluetooth ESC/POS from a Kivy phone app) and feature 348 (`ninondev/stove`).

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any `PrinterConfig` SQLModel table, any print-service module, any ESC/POS byte encoding.
- Any hardware procurement — ESC/POS requires a physical thermal printer (**procurement before engineering**).
- Any Windows-service adoption — LE31 v1 runs Linux; this pick's *service-supervisor* idea transfers, its *Windows-service* implementation does not.

## Description

GitHub `xenithpulse/xp-thermal-service` — *"Free, open-source QZ Tray alternative. Print ESC/POS receipts & kitchen tickets from any web POS to USB or network thermal printers. Self-healing Windows service."*

**Stack match matrix:**

| `xp-thermal-service` component | LE31 charter §3.1 | Match? |
|---|---|---|
| ESC/POS protocol | transport, not stack | ✅ protocol is platform-independent and non-copyrightable |
| Sidecar print service | — | ⚠️ **off-stack shape**; transferable as a boundary, not as code |
| Self-healing supervisor | §3.4 *chokepoint-governed + observable-evidence* | ✅ portable — a print chokepoint that reports its own health |
| USB / network printers | §3.5 *self-hosted single-install* | ⚠️ LE31 v1 has no hardware posture; **unmade decision** |
| TypeScript / Node.js | Python 3.13 + FastAPI | ❌ OFF-STACK |
| Windows service | LE31 v1 = Linux VPS + Postgres | ❌ OFF-STACK |

**The primitives worth keeping:**
1. **Print as a chokepoint, not a call site.** The order flow does not know how printing works. Every print goes through one boundary. This is §3.4 applied to a hardware edge — and it is the *same* boundary feature 355's HANDOFF names (`backend/services/print_service.py`). Implementing either pick alone forks the business logic per surface.
2. **Self-healing = observable evidence.** A supervisor that restarts and reports is §3.4's "observable evidence" in hardware form. If LE31 ever prints, an unobservable printer is worse than no printer.
3. **QZ Tray substitution.** QZ Tray is a closed-source signed native helper. Replacing it with a plain service is the §3.2 *permissive-dependency* posture in hardware form.

**⚠️ Recorded tensions:**
- **Physical hardware is required.** Unlike every other pick in this series, this one cannot be evaluated from code alone.
- **Two conflicting v1 questions, both unmade:** does LE31 print at all, and if so does it print from the server or from a client device? These are different architectures with different failure modes, and the pick does not settle it.

## Data model

None today. If ever built, the minimal shape would be a `PrintJob` **append-only** row (per §3.3 — a print job is an event, not mutable state) carrying: `order_id`, `station`, `template_kind`, `payload_bytes_ref`, `created_at` (tz-aware, §business time). **Deliberately not specified**: retry state. A retry counter is mutable state on a ledger row, which §3.3 forbids. Retries belong in a separate non-ledger table or not at all. **This is an unmade decision and is recorded as one.**

## Implementation steps

1. Re-run the seven-check gate with a real printer in hand and the owner's answer on server-side vs client-side printing.
2. Read `xp-thermal-service`'s service/supervisor code — not the ESC/POS byte layer, which is already covered by features 348/355.
3. Decide the print chokepoint boundary in LE31's own terms and write it into a `features/` contract.
4. Only then consider a prototype behind a non-AI fallback that leaves printing switchable off.

## Telegram interaction

None proposed. The cook's Telegram surface (§3.1 two-role discipline) must not gain a print button without an owner decision — a failed print silently dropped in a Telegram message is exactly the kind of unobservable state §3.4 prohibits.

## Dependencies

- **Unmade:** whether LE31 acquires hardware at all.
- **Unmade:** server-side vs client-side printing. Feature 355 argues client-side (phone + Bluetooth); this pick argues server-side (service). **They disagree and both are on file.**
- **Procurement before engineering** — a thermal printer must be bought before any of this can be tested.

## Open questions

1. Does LE31 print receipts, kitchen tickets, both, or neither?
2. Server-side or client-side? (Unresolved conflict with feature 355.)
3. What happens when a print fails at the moment of service — is that an explicit operational state (§State invariant) or a silent drop? §State says explicit; the answer needs an owner, not an implementation.
4. Is the print job ledger append-only, and if so where do retries live?

## Why this matters

LE31's two roles are a waiter web UI and a cook Telegram bot. A kitchen that produces paper output is the normal shape of that business, and two prior picks (348, 355) already brush against it. This pick adds the one thing neither has: **the boundary itself**. Recording it now means that if a printer decision is ever opened, the architecture question is already framed rather than being rediscovered under time pressure.