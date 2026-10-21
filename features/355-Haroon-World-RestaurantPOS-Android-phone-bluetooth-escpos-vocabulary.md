# Feature 355 — `Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary` (defer)

> **NEW observation (2026-10-21).** Documents in-window GitHub repo `Haroon-World/RestaurantPOS_Android` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★1/⑂0 — recorded explicitly as NO traction evidence in either direction**, **129 KB tiny = the second-smallest pick of the 83-pass series** (after feature 349 `gfs-invoice-breakdown` at 18 KB), **Python ✓ ON-STACK + SQLite ✓ ON-STACK** (LE31 v1 is Python 3.13 / SQLModel / Postgres; SQLite is the local-tier analogue), **created 2026-06-24T10:53:23Z AND pushed 2026-10-03T12:11:50Z = IN-WINDOW BY PUSH**, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Mobile Point of Sale (POS) Android application built with Python and Kivy, featuring offline SQLite transactions and Bluetooth ESC/POS thermal printing."* Topics (verbatim, parent-verified, **9 topics**): `android, bluetooth-printing, buildozer, esc-pos, kivy, point-of-sale, pos, python, sqlite`. Bucket: **v1 (phone-first POS + Bluetooth ESC/POS thermal printing + offline SQLite vocabulary)** — Pick C of Daily Brainstorm 2026-10-21. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Retain the **phone-as-terminal + Bluetooth ESC/POS thermal printing + offline SQLite transactions + single-language Python app (Kivy)** vocabulary as a persistent cross-section reference for the LE31 v1 *operator-surface* wedge. This is deliberately filed as **the mobile sibling to feature 353** (`FreeOpenSourcePOS/FloCafe`, desktop/Electron kitchen display): together the two picks document that one order→kitchen→print flow can be rendered to two very different hardware surfaces over one deterministic kernel, which is LE31's §3.1 degradation posture expressed as a portable pair. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **phone-as-the-only-terminal + Bluetooth ESC/POS thermal printing + offline SQLite transactions** primitive: the operator's device IS the POS, and it prints to a nearby thermal printer over Bluetooth with no server involved in the transaction path. IS the canonical §3.1 *hands-busy phone-first* + §3.4 *deterministic kernel + hardware-as-first-class-output* invariant applied to the *phone-terminal* dimension.
- A written record of the **single-language app** posture: Python on both the app and the (local) data layer, with Kivy as the UI toolkit and Buildozer as the packaging path. IS the canonical §3.5 *single-binary-install-on-a-single-machine* invariant — one language, one toolchain, one artefact. Sister-shape to feature 348 (`ninondev/stove`, Python + ESC/POS + SQLite + single-binary-deploy).
- A written record of the **dual-surface invariant** formed with feature 353: kitchen display (screen) vs phone (printer) are two renderings of one flow, not two products.
- A decision record: today's verdict is `defer` because (1) LE31 v1's waiter surface is HTMX on a tablet and its cook surface is an aiogram Telegram bot — a native Android app is a third surface, not a replacement; (2) Bluetooth ESC/POS needs a physical printer in the restaurant, which is a procurement question before it is an engineering one; (3) ★1/⑂0 gives no traction evidence either way.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter HTMX UI or cook aiogram bot.
- Any Buildozer/Kivy/Android build-tooling decision.
- Any hardware procurement or ESC/POS device-driver work.
- Any claim that a native app is *better* than HTMX for LE31's waiter. It is not — HTMX is the charter's surface; this is a vocabulary note about a shape that exists elsewhere.

## Out of scope

- See "Scope" above. Vocabulary-only; no code today.

## Evidence / JTBD

When a future LE31 v1 surface asks "what happens when the tablet is out of battery mid-service", the owner wants *a proven shape where the operator device degrades to a printer and the transaction still commits*, but struggles because *LE31's waiter HTMX UI and cook Telegram bot both assume a working screen and a reachable network*.

- **Evidence class**: observed (the verbatim description names all four primitives — Python, Kivy, offline SQLite, Bluetooth ESC/POS — and the 9 verbatim topics corroborate; all counts/timestamps parent-verified by direct `/repos/` GET).
- **Confidence**: medium-high for the vocabulary match; **very low for urgency** (★1/⑂0, zero owner mentions across 83 brainstorm + 82 research passes).
- **Traction caveat, recorded plainly**: ★1/⑂0 is **not** evidence of adoption and **not** evidence of failure. It is a 129 KB hobby-shaped repo that names a real shape. Filing it is about the shape, not the project.

## Description

GitHub `Haroon-World/RestaurantPOS_Android` (MIT ✓, ★1/⑂0, 129 KB, Python ✓ ON-STACK, pushed 2026-10-03, created 2026-06-24, archived=false).

Sub-primitives:

1. **Phone as the POS terminal** — no separate till, no desktop. IS the canonical §3.1 *hands-busy phone-first* invariant in its most literal form.
2. **Bluetooth ESC/POS thermal printing** — the byte protocol is the output contract and Bluetooth is the wire. **The ESC/POS byte protocol itself is not copyrightable**, so this specific primitive is reusable regardless of licence — the same reasoning already applied to feature 348.
3. **Offline SQLite transactions** — the transaction commits locally. IS the canonical §3.4 *deterministic kernel* invariant; note this is the **same unresolved sync question** feature 353 raises, here without a server to reconcile against.
4. **Single-language Python app (Kivy + Buildozer)** — IS the canonical §3.5 *single-binary-install* invariant; the `buildozer` topic is the explicit packaging-pipeline marker.
5. **No server in the transaction path** — the strongest reading of the deterministic-kernel invariant in this pass: the operator's action is durable with no network dependency at all.

## Data model

None shipped. The implied shape: a **local SQLite** file holding orders and payments, with ESC/POS as a pure byte-emitting function of an order (no device knowledge inside the order logic), and any server sync strictly deferred to a later, separate concern. The **device-queue shape from feature 348** (`ESC/POS-byte-emit-to-device-queue`) composes directly: emit bytes, never block on the printer.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):** (1) a v1 PR proposes printer output of any kind (then this and feature 348/353 are the reference set); (2) the owner decides the waiter surface should be a native app rather than HTMX; (3) the offline-sync question from feature 353 is opened, in which case this repo's local-SQLite shape is the strongest counter-example to a server-authoritative model.

## Telegram interaction if any

None today, and worth flagging as a tension: LE31 v1's cook is **already** a Telegram bot (aiogram v3). A native phone app for the waiter would create a third client alongside the HTMX waiter and the Telegram cook. The surface-count discipline in §3.1 (two roles) argues against adding a third client without an owner decision. Recorded, not resolved.

## Dependencies

- LE31 charter §3.1 (two-role surface, hands-busy phone-first), §3.4 (deterministic kernel, no inference, hardware as output), §3.5 (single-binary install, self-hosted).
- Sister features: **353** (`FreeOpenSourcePOS/FloCafe` — the desktop counterpart; paired deliberately), 348 (`ninondev/stove` — ESC/POS byte-emit-to-device-queue), 302 (`mhmd2042/cafe-pos`), 323 (`KitchenQ`), 304 (`the-pass`).
- Physical hardware: a Bluetooth-capable ESC/POS thermal printer. Procurement, not engineering.

## Open questions

1. **Surface count.** HTMX waiter + Telegram cook is two roles. Does a native app make three clients? Unmade and it is a charter-level question, not an implementation detail.
2. **Offline sync.** Same unanswered question as feature 353: local-authoritative or server-authoritative? This repo is the strongest local-authoritative data point on file.
3. **Bluetooth vs USB ESC/POS.** Feature 348's `stove` is USB; this one is Bluetooth. Different failure modes, different pairing UX. Not compared.
4. **Kivy specifically.** LE31 has no GUI-toolkit precedent; HTMX was chosen deliberately. Nothing argues for revisiting that here.

## Why this matters

Filed as the **mobile half of a deliberate pair with feature 353**. The pair's value is the invariant neither repo states on its own: *one deterministic order→kitchen→print kernel, two hardware renderings, no per-surface business-logic fork.* LE31's charter already demands this in spirit (§3.1 degradation, §3.4 determinism) but has never had a concrete reference for what it looks like on both surfaces at once.

Its second contribution is the **strongest local-authoritative data point on file** for the offline-sync question that features 347, 348, 349 and 353 all brush against. Four picks have now circled it without naming it; this one names it by committing to the opposite posture. That is useful precisely because it is a counter-example.