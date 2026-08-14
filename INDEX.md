# Master Index — Restaurant App Research

> **Status**: Research phase complete. Mock-up built. Backend skeleton in place.
> **Next**: Implementation phase — features 02 → 07 in `INDEX.md` order.
> **Start here** (if you're the next agent): [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) → [`HANDOFF.md`](HANDOFF.md) → [`KIMI_K5_PROMPT.md`](KIMI_K5_PROMPT.md).

---

## What we recommend

A **thin Python (FastAPI + aiogram + PostgreSQL) app** with three surfaces:

1. **Waiter UI** — `index.html` + REST API (FastAPI)
2. **Cook UI** — Telegram bot (aiogram)
3. **Manager UI** — `index.html` reports + CSV export

**Why not fork an existing project?** None of the open-source POS systems
match the spec (Telegram-driven kitchen + first-class prepared-item stock +
table-side ordering with demographics). TastyIgniter is the closest but
Laravel-heavy and lacks Telegram integration. URY is great but requires
ERPNext (overkill for one restaurant).

See [`research/09-recommended-stack.md`](research/09-recommended-stack.md) for the full architecture.

---

## Research findings (broad survey + deep-dive)

| File | Topic |
|---|---|
| [research/00-landscape-overview.md](research/00-landscape-overview.md) | Overview + verdict on the existing landscape |
| [research/01-pos-systems.md](research/01-pos-systems.md) | TastyIgniter, URY, Flutter POS, RestoPOS, ... |
| [research/02-kitchen-display.md](research/02-kitchen-display.md) | URY Mosaic, CampusBites, OpenKDS, ... |
| [research/03-inventory-stock.md](research/03-inventory-stock.md) | **The killer feature gap** — no one does prepared-item batches well |
| [research/04-menu-ocr.md](research/04-menu-ocr.md) | PaddleOCR, RapidOCR, donut, OCRmyPDF |
| [research/05-telegram-bots.md](research/05-telegram-bots.md) | python-telegram-bot vs aiogram |
| [research/06-payments-tips.md](research/06-payments-tips.md) | Tip derived from `paid − consumed` (cleaner than manual entry) |
| [research/07-guest-analytics.md](research/07-guest-analytics.md) | Demographic capture + privacy stance |
| [research/08-deep-dive-top-5.md](research/08-deep-dive-top-5.md) | Top 5 fork candidates — verdict each |
| [research/09-recommended-stack.md](research/09-recommended-stack.md) | **Architecture sketch + DDL** |
| [research/10-async-supplement.md](research/10-async-supplement.md) | 5 additional projects from the async subagent (chefcito, satisfecho, Umi-OCR, AstrBot, Tip_Reconciliation) + refined gaps list |
| [research/11-adjacent-categories-summary.md](research/11-adjacent-categories-summary.md) | v2 feature ideas — 10 new feature specs driven by owner-pains + AI/ML + adjacent OSS research |
| [research/12-ai-ml-summary.md](research/12-ai-ml-summary.md) | AI/ML extensions — menu engineering, waste prediction, recipe generation, sentiment analysis |

---

## Features we could build (one file each)

Priority: 🟢 high, 🟡 medium, ⚪ low.

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 01 | Table management | [features/01-table-management.md](features/01-table-management.md) | 🟢 | Visual floor grid |
| 02 | Order taking | [features/02-order-taking.md](features/02-order-taking.md) | 🟢 | Waiter-side core flow |
| 03 | **Kitchen stock tracker** | [features/03-kitchen-stock-tracker.md](features/03-kitchen-stock-tracker.md) | 🟢 | **The killer feature** — finite stock of prepared items |
| 04 | **Menu photo bot** | [features/04-menu-photo-bot.md](features/04-menu-photo-bot.md) | 🟢 | Cook's morning Telegram photo → today's menu |
| 05 | Payment + tip derivation | [features/05-payment-tip-reconciliation.md](features/05-payment-tip-reconciliation.md) | 🟢 | `tip = paid − consumed` |
| 06 | Guest demographics + reports | [features/06-guest-demographics.md](features/06-guest-demographics.md) | 🟡 | Privacy-respecting, no PII in v1 |
| 07 | Demand estimation | [features/07-demand-estimation.md](features/07-demand-estimation.md) | 🟡 | Simple 14-day average + 10 % buffer |
| 08 | index.html mock-up | [features/08-index-mockup.md](features/08-index-mockup.md) | 🟢 | **Build this first** — visualizes 01–03 + 06 |

**v2 features (research complete, awaiting build decision):**

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 09 | Kitchen delay visibility | [features/09-kitchen-delay-visibility.md](features/09-kitchen-delay-visibility.md) | 🟢 | **Top v2 pick** — uses existing timestamps, no new deps |
| 10 | Allergen & dietary tracking | [features/10-allergen-tracking.md](features/10-allergen-tracking.md) | 🟢 | EUFIC 14-allergen standard |
| 11 | QR customer menu | [features/11-customer-qr-menu.md](features/11-customer-qr-menu.md) | 🟢 | Live stock display = differentiator |
| 12 | Pre-shift briefing | [features/12-pre-shift-briefing.md](features/12-pre-shift-briefing.md) | ⚪ | Cheapest feature in backlog (1–3 days) |
| 13 | Reservations & deposits | [features/13-reservations-deposits.md](features/13-reservations-deposits.md) | ⚪ | First feature touching real money (Stripe) |
| 14 | Split bills | [features/14-split-bills.md](features/14-split-bills.md) | 🟢 | #2 most-requested owner feature |
| 15 | Inventory variance | [features/15-inventory-variance.md](features/15-inventory-variance.md) | ⚪ | Builds on feature 03 ledger; data-discipline heavy |
| 16 | Supplier orders & receiving | [features/16-supplier-orders.md](features/16-supplier-orders.md) | ⚪ | Closes the inventory loop |
| 17 | ML demand forecasting | [features/17-demand-forecasting-ml.md](features/17-demand-forecasting-ml.md) | ⚪ | Prophet / NeuralForecast — needs 4+ weeks history |
| 18 | Gift cards & store credit | [features/18-gift-cards.md](features/18-gift-cards.md) | ⚪ | Append-only ledger pattern |

**v2 AI/ML features (research complete):**

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 19 | Menu engineering (Kasavana-Smith) | [features/19-menu-engineering.md](features/19-menu-engineering.md) | 🟡 | **Top AI/ML pick** — 2-3 days, pure SQL |
| 20 | Waste prediction | [features/20-waste-prediction.md](features/20-waste-prediction.md) | 🟡 | Uses prepared-item ledger; 5-10% food cost reduction |
| 21 | Recipe generation from leftovers | [features/21-recipe-generation.md](features/21-recipe-generation.md) | 🟡 | Local Qwen2.5-3B; "wow" demo |
| 22 | Sentiment analysis of reviews | [features/22-sentiment-analysis.md](features/22-sentiment-analysis.md) | ⚪ | "Weekend polish" — defer |

---

## Suggested build order

1. **Mock-up** (08) — `index.html` showing floor + order + reports. Pure HTML/JS, no backend.
   *Iterate on UX with the user until happy.*
2. **Backend skeleton** — FastAPI app, PostgreSQL schema, auth (PIN per user).
3. **Table mgmt + order taking** (01, 02) — waiter can seat a party, take orders, close visit.
4. **Menu photo bot** (04) — cook's morning Telegram flow.
5. **Stock tracker** (03) — batches, ledger, sold-out alerts.
6. **Payment + tip** (05) — bill, derived tip, shift close.
7. **Reports** (06) — manager dashboard.
8. **Demand estimation** (07) — once we have 14 days of data.

**v2 build order (after v1 ships):**

1. **Kitchen delay visibility** (09) — 5 days, no new deps. Uses existing timestamps.
2. **Pre-shift briefing** (12) — 2 days, Telegram-native. Cheapest win.
3. **Split bills** (14) — 5 days for ledger + UI; defer terminal integration.
4. **Allergen tracking** (10) — 4 days; needed before customer-facing menu.
5. **QR customer menu** (11) — 5 days; builds on allergen + stock display.
6. **Reservations** (13) — 7 days; first feature touching real money (Stripe).
7. **ML forecasting** (17) — 2 days to integrate Prophet; needs 4+ weeks of data first.
8. **Inventory variance** (15) + **Supplier orders** (16) — build together, ~3 weeks.
9. **Gift cards** (18) — 1 week. Append-only ledger pattern.

---

## Open questions for the user (blocks before we code)

These are listed in `research/09-recommended-stack.md` — repeated here for visibility:

1. **Menu language**? Drives OCR engine choice (PaddleOCR for CN, RapidOCR for EU languages).
2. **Currency**? Single or multi.
3. **Tax**? Flat or per-category.
4. **Hardware** for waiters? Tablet / phone / desktop.
5. **Single restaurant or chain**? Drives tenancy.
6. **Service charge** (auto-added %)? EU common, US not. Decide before bill code.
7. **Tip pool** (split tips across staff)? In scope v1 or v2?

---

## Repo conventions

- `research/` — broad surveys + deep dives (read first to get the lay of the land).
- `features/` — one file per feature with Goal / Scope / Description / Data Model / Dependencies / Open Questions.
- `HANDOFF.md` — repo tour + build order + constraints (read this if picking up).
- `research/meta/KIMI_K5_PROMPT.md` — ready-to-paste prompt for the next coding agent.
- `PROJECT_CHARTER.md` — full project brief (scope, goals, deliverables, quality bar, risks). Read first.
- `index.html` (root) — the working mock-up (4 views, mobile-responsive, no build).
- `backend/` — FastAPI app skeleton (see `backend/README.md`).
- `agent/` — snapshots of the agent's runtime files (SOUL.md, config.yaml.template, USER.md, MEMORY.md). See [`agent/README.md`](agent/README.md).

---

## Daily Brainstorm index

| Date | Headline | Picks (slugs) | Report |
|---|---|---|---|
| 2026-08-04 | `owner-no-account-live-floor-link`, `append-only-audit-redirect`, `shelf-threshold-receiving-bot` | 28/29/30 | [`/opt/data/le31-brainstorm-2026-08-04.md`](/opt/data/le31-brainstorm-2026-08-04.md) |
| 2026-08-05 | `solo-operator-floor-pin`, `telegram-walkin-pin`, `stockout-prep-board-snapshot` | 32/33/34 | [`/opt/data/le31-brainstorm-2026-08-05.md`](/opt/data/le31-brainstorm-2026-08-05.md) |
| 2026-08-06 | `void-rationale-ledger-field`, `cook-voice-note-to-stockentry`, `owner-daily-recap-telegram` | 37/38/39 | [`/opt/data/le31-brainstorm-2026-08-06.md`](/opt/data/le31-brainstorm-2026-08-06.md) |
| 2026-08-07 | `telegram-prep-checkoff-adherence`, `tether-day-card-fold`, `print-fallback-floor-sheet` | 43/44/45 | [`/opt/data/le31-brainstorm-2026-08-07.md`](/opt/data/le31-brainstorm-2026-08-07.md) |
| 2026-08-08 | `havemind-decision-notes`, `decision-rationale-mixin`, `pipecat-voice-watch` (parking-lot) | 46/47/48 | [`/opt/data/le31-brainstorm-2026-08-08.md`](/opt/data/le31-brainstorm-2026-08-08.md) |
| 2026-08-09 | `postledger-tamper-evident-hash`, `lifecycle-citation-mixin`, `realtime-cook-coach-watch` (parking-lot) | 49/50/51 | [`/opt/data/le31-brainstorm-2026-08-09.md`](/opt/data/le31-brainstorm-2026-08-09.md) |
| 2026-08-10 | `drailver-handoff-protocol`, `zentra-offline-first-fb-pattern`, `corner-mart-pos-double-entry` (parking-lot) | 52/53/54 | [`/opt/data/le31-brainstorm-2026-08-10.md`](/opt/data/le31-brainstorm-2026-08-10.md) |
| 2026-08-11 | Cross-section: `evidence-review-surface` (Pick A — `paulmurphynet/chronicle` pushed today `local, append-only evidence review for consequential answers`), `walk-in-front-desk-channel` (Pick B — OpenAlex `WhatsApp as a service tool in hospitality` W7197042220 + `djblack1209-coder/OpenClaw-Bot` multi-bot FastAPI/aiogram + `indmdev/Free-Telegram-Store-Bot` 146★), `owner-recap-persona-voice` (Pick C — OpenAlex kama muta W7172434674 + chatbot-emotion SR W7172493963 + Hakka Kitchen W7172068431, bound by uncanny-valley SR W4417084818); yesterday's picks (33/34/45/46/47/48/49/50/51/52/53/54) and today's daily-research picks skipped as already filed; parking-lot: `second-opinion-council-recap`, `floor-flow-review-skill` | 55/56/57 | [`/opt/data/le31-brainstorm-2026-08-11.md`](/opt/data/le31-brainstorm-2026-08-11.md) |
| 2026-08-12 | Cross-section: `operator-ai-action-surface` (Pick A — `sirquy/bestie` 153★ just-pushed 2026-08-12 "local-first AI action assistant for operators, permission gates"; charter invariant *"AI may assist owner/staff, with observable evidence and a non-AI fallback"* is the *central* design constraint; anchored by `RobbieRao/hci-paper-writing` just-pushed 2026-08-12 evidence-tracing pattern + OpenAlex W7171961487 UTAUT+AI + W4417084818 uncanny-valley bound). `recap-replay-evidence-card` (Pick B — `Lulzx/memo` 1★ pushed 2026-07-27 "150-line append-only projection in Python"; deterministic, no LLM, companion to feature 57 not a duplicate; anchored by `RobbieRao/hci-paper-writing` + OpenAlex W7172434674/W7172493963). `restaurant-telegram-front-desk-mirror` (Pick C — `weebzone/ForwardX` 22★ pushed 2026-08-03 always-on Telegram forwarder; `BethanyJep/Safaricom-Decode-Agents-Workshop` 16★; OpenAlex W7197042220 WhatsApp-as-front-desk — PARKING-LOT pending charter §5 privacy revision, file left in place). Parking-lot: `paired-ai-decision-council`, `cook-coach-watch-v2`. HN quiet day (5/6 queries zero hits); 121 GitHub in-window items; OpenAlex restaurant/HCI 25 in-window. | 58/59/60 | [`/opt/data/le31-brainstorm-2026-08-12.md`](/opt/data/le31-brainstorm-2026-08-12.md) |
| 2026-08-13 | Cross-section v2-AI control-plane day: `holdfast-approval-ledger` (Pick A — `dallascrilley/holdfast` just-pushed 2026-08-12, MIT, TypeScript — *"append-only decision ledger with a human approval gate: AI can propose, only a person can publish"*; complement to feature 58's `AIActionAttempt` outcome row, ships a two-row proposal/decision ledger in the same `StockEntry`-grade hash chain; corroborated by `chiga0/marshal-harness` pushed 2026-08-13 evidence-gated orchestration). `agents-yaml-ontology-config` (Pick B — `cruxible-ai/cruxible` 16★ just-pushed 2026-08-12 Python Apache-2.0 *"Governed state engine for AI agents: typed, executable knowledge artifacts"*; HN Cruxible Show HN 2026-07-14 "Terraform-like ontology config"; corroborated by `Org-EthereaLogic/adws-pipeline-skill` pushed 2026-08-13 — externalizes `backend/app/config.py::AI_PERMISSIONS` into repo-root `agents.yaml`, EXPERIMENT gate, ≤2 days). `second-opinion-verifier-role` (Pick C — `Frantz103/agent-os-opensource` 1★ just-pushed 2026-08-13 Python Apache-2.0 *"independent-review layer for AI coding runtimes"* — adds an independent-verifier model role between AI proposal and owner approval, PARKING-LOT because charter §4 single-model assumption + cost/benefit unproven; preserves the option for when a second LLM provider is added, most plausibly at the menu-photo OCR multimodal upgrade). HN `local-first-ai` cluster 38 in-window hits (Kor's `Korvo`, `EXXETA/exxperts`, `Cruxible`, `Lethe`, `Lance-bundle`, `SquadCue`, `OpenLore`) is the strongest HN signal this month; GitHub 9/10 creative queries returned hits (`topic:append-only` 21 incl. `holdfast`/`memento`/`agent-ledger`/`tamperlog`/`git-everref`; `evidence_review` 970 incl. `marshal-harness`/`agent-os-opensource`; `topic:no-build` 147); OpenAlex `restaurant-hospitality-hci` 25 in-window carry-over; ProductHunt reachable 50 entries with 0 restaurant/operator mentions (soft source honest zero); HN `crossover-restaurant-app` / `micro-saas-small-business` / `low-effort-ux` / `phone-first-pos` / `kitchen-workflow` 0 hits in window (5/8 HN queries zero). Skipped: `RobbieRao/hci-paper-writing` (pick 55/59), `Korvo`/`OpenLore`/`cruxible-ai` corroborators (covered by pick 61/62), WhatsApp-as-hospitality W7197042220 (pick 60 parking-lot), `anteneh263-ux/kitchen-prep-taskmaster` (covered by pick 17 demand-forecasting-ml + pick 21 recipe-generation, no gap). | 61/62/63 | [`/opt/data/le31-brainstorm-2026-08-13.md`](/opt/data/le31-brainstorm-2026-08-13.md) |
| 2026-08-14 | Cross-section v2 owner-pains + cook-surface UX + academic offline-first architecture day: `retail-localization-reference-pattern` (Pick A — `misall-software/retail-localization-reference` Python pushed 2026-08-12 NOASSERTION — *"Retail and restaurant POS localization reference: currency formatting, tax display, receipt requirements, e-invoicing, script direction and thermal-printer behaviour, by country and language"*; 20 topics incl. `arabic/bidi/e-invoicing/escpos/fiscalization/multi-currency/rtl/tax-compliance/thermal-printer/VAT`; adds 5-country profile table `FR/DE/IT/ES/NL` replacing hard-coded EUR + Europe/Paris + French-format; charter-aligned §Money + §Business time + EU tax/receipt compliance; NOASSERTION license → pattern only, not the file; corroborated by `vul-os/beepbite` carry-over from feature 42 with `multi-currency` tag). `cook-photo-stock-list-pwa` (Pick B — `Sreenivas-Sadhu-Prabhakara/shelftrack` HTML PWA MIT created 2026-07-15 + re-pushed 2026-08-14 — *"Photo-first stock list for a tiny shop — snap a product, set a reorder level, see what's running low at a glance, export to CSV. 100% offline, nothing leaves your device."*; first surfaced 2026-08-04 (HMM-24) as reference, today's re-push after 30 days of stable development elevates to brainstorm-grade; adds Telegram `/stock-snap` command: photo upload → optional annotation → confirmation → `StockEntry` row with `photo_file_id` (additive nullable migration); distinct from feature 04 menu-photo-bot (dish recognition) — this is stock entry; corroborated by same author's `slotone` JS MIT 2026-08-14 + `gaganjainse/ClinicLedger` Kotlin 1★ 2026-07-15 offline-first voice-assisted clinic ledger). `offline-first-pwa-transactional-arch` (Pick C — Nugraha, Somantri, Rofiqi (2026-08-10). *Implementation of an Offline-First Progressive Web App Architecture for Transactional System Resilience.* **bit-Tech 9(1):4044, doi:10.32877/bt.v9i1.4044 (diamond-OA, free to read)** — single strongest academic anchor in this pass, maps the existing LE31 surfaces (cook bot + waiter UI + append-only ledger + hash chain) to the paper's 4-component pattern (local cache + sync queue + idempotency keys + reconciliation); identifies smallest-next-experiment as transactional idempotency keys for the cook bot photo upload flow from feature 65; EXPERIMENT ships one design doc + zero code, distinct from feature 53 waiter-side replay queue — code, and feature 49 hash chain — code). HN Algolia **silent for 15th consecutive day** on LE31-target queries (8/10 zero in-window hits; 2/10 returned raw hits = Show HN substring noise only); GitHub 12/12 returned hits but 8/12 = 0 LE31-relevant (mostly generic/aggregator noise); 4 fresh in-window anchors: `misall-software/retail-localization-reference` Python 2026-08-12 + `Sreenivas-Sadhu-Prabhakara/shelftrack` HTML PWA MIT 2026-07-15 + `gaganjainse/ClinicLedger` Kotlin 1★ 2026-07-15 + `Lantern-svg/lantern` Python 2026-08-10. **Carries-over from yesterday (61/62/63)**: `dallascrilley/holdfast` (TS, 2026-08-12, pick 61 anchor), `cruxible-ai/cruxible` 16★ (Python, 2026-08-12, pick 62 anchor), `Frantz103/agent-os-opensource` (Python, 2026-08-13, pick 63 anchor) — **v2-AI control-plane cluster NOT re-picked today** per skill rule. Skipped: `longnick/small-pos-open-source` 91★ (today's daily-research parking-lot watch-list candidate), `uvicorn 0.52.3` pin bump (today's daily-research next-pass build candidate), `drailver-handoff-protocol` (already pick 52), `vul-os/beepbite` (already feature 42), `Sreenivas-Sadhu-Prabhakara/slotone` (cross-section reading only). | 64/65/66 | [`/opt/data/le31-brainstorm-2026-08-14.md`](/opt/data/le31-brainstorm-2026-08-14.md) |

---

## Active feature pipeline

| Date | Pick | Bucket | Feature path | Linear ID | Handoff |
|---|---|---|---|---|---|
| 2026-08-08 | `havemind-decision-notes` | v2-AI (no-LLM core) | [`features/46-havemind-decision-notes.md`](features/46-havemind-decision-notes.md) | HMM-51 (sub) | [`specs/havemind-decision-notes-HANDOFF.md`](specs/havemind-decision-notes-HANDOFF.md) |
| 2026-08-08 | `decision-rationale-mixin` | v2 utility | [`features/47-decision-rationale-mixin.md`](features/47-decision-rationale-mixin.md) | HMM-52 (sub) | [`specs/decision-rationale-mixin-HANDOFF.md`](specs/decision-rationale-mixin-HANDOFF.md) |
| 2026-08-08 | `pipecat-voice-watch` | parking-lot | [`features/48-pipecat-voice-watch.md`](features/48-pipecat-voice-watch.md) | HMM-53 (sub) | [`specs/pipecat-voice-watch-HANDOFF.md`](specs/pipecat-voice-watch-HANDOFF.md) |
| 2026-08-09 | `postledger-tamper-evident-hash` | v2 (audit) | [`features/49-postledger-tamper-evident-hash.md`](features/49-postledger-tamper-evident-hash.md) | HMM-53 (sub) | [`specs/postledger-tamper-evident-hash-HANDOFF.md`](specs/postledger-tamper-evident-hash-HANDOFF.md) |
| 2026-08-09 | `lifecycle-citation-mixin` | v2 (state machine) | [`features/50-lifecycle-citation-mixin.md`](features/50-lifecycle-citation-mixin.md) | HMM-54 (sub) | [`specs/lifecycle-citation-mixin-HANDOFF.md`](specs/lifecycle-citation-mixin-HANDOFF.md) |
| 2026-08-09 | `realtime-cook-coach-watch` | parking-lot | [`features/51-realtime-cook-coach-watch.md`](features/51-realtime-cook-coach-watch.md) | HMM-55 (sub) | [`specs/realtime-cook-coach-watch-HANDOFF.md`](specs/realtime-cook-coach-watch-HANDOFF.md) |
| 2026-08-10 | `drailver-handoff-protocol` | v2 owner-pains (audit) | [`features/52-drailver-handoff-protocol.md`](features/52-drailver-handoff-protocol.md) | HMM-58 (sub) | [`specs/drailver-handoff-protocol-HANDOFF.md`](specs/drailver-handoff-protocol-HANDOFF.md) |
| 2026-08-10 | `zentra-offline-first-fb-pattern` | v2 owner-pains (resilience) | [`features/53-zentra-offline-first-fb-pattern.md`](features/53-zentra-offline-first-fb-pattern.md) | HMM-59 (sub) | [`specs/zentra-offline-first-fb-pattern-HANDOFF.md`](specs/zentra-offline-first-fb-pattern-HANDOFF.md) |
| 2026-08-10 | `corner-mart-pos-double-entry` | parking-lot | [`features/54-corner-mart-pos-double-entry.md`](features/54-corner-mart-pos-double-entry.md) | HMM-60 (sub) | [`specs/corner-mart-pos-double-entry-HANDOFF.md`](specs/corner-mart-pos-double-entry-HANDOFF.md) |
| 2026-08-11 | `evidence-review-surface` | v2 owner-pains (audit, composes 30+47+49+50) | [`features/55-evidence-review-surface.md`](features/55-evidence-review-surface.md) | HMM-63 (sub) | [`specs/evidence-review-surface-HANDOFF.md`](specs/evidence-review-surface-HANDOFF.md) |
| 2026-08-11 | `walk-in-front-desk-channel` | v2 owner-pains (customer chat — REQUIRES charter §5 revision) | [`features/56-walk-in-front-desk-channel.md`](features/56-walk-in-front-desk-channel.md) | HMM-64 (sub) | [`specs/walk-in-front-desk-channel-HANDOFF.md`](specs/walk-in-front-desk-channel-HANDOFF.md) |
| 2026-08-11 | `owner-recap-persona-voice` | v2 owner-pains (extension of feature 39) | [`features/57-owner-recap-persona-voice.md`](features/57-owner-recap-persona-voice.md) | HMM-65 (sub) | [`specs/owner-recap-persona-voice-HANDOFF.md`](specs/owner-recap-persona-voice-HANDOFF.md) |
| 2026-08-12 | `operator-ai-action-surface` | **v2-AI control-plane** (new bucket name) | [`features/58-operator-ai-action-surface.md`](features/58-operator-ai-action-surface.md) | HMM-67 (sub) | [`specs/operator-ai-action-surface-HANDOFF.md`](specs/operator-ai-action-surface-HANDOFF.md) |
| 2026-08-12 | `recap-replay-evidence-card` | v2 owner-pains (S effort, deterministic) | [`features/59-recap-replay-evidence-card.md`](features/59-recap-replay-evidence-card.md) | HMM-68 (sub) | [`specs/recap-replay-evidence-card-HANDOFF.md`](specs/recap-replay-evidence-card-HANDOFF.md) |
| 2026-08-12 | `restaurant-telegram-front-desk-mirror` | v2 owner-pains (PARKING-LOT, pending charter §5 revision) | [`features/60-restaurant-telegram-front-desk-mirror.md`](features/60-restaurant-telegram-front-desk-mirror.md) | HMM-69 (sub, Backlog) | [`specs/restaurant-telegram-front-desk-mirror-HANDOFF.md`](specs/restaurant-telegram-front-desk-mirror-HANDOFF.md) |
| 2026-08-13 | `holdfast-approval-ledger` | v2-AI control-plane (M effort, append-only two-row proposal/decision ledger) | [`features/61-holdfast-approval-ledger.md`](features/61-holdfast-approval-ledger.md) | HMM-72 (sub, le31 v1 — Core MVP) | [`specs/holdfast-approval-ledger-HANDOFF.md`](specs/holdfast-approval-ledger-HANDOFF.md) |
| 2026-08-13 | `agents-yaml-ontology-config` | v2-AI control-plane (S effort, experiment) | [`features/62-agents-yaml-ontology-config.md`](features/62-agents-yaml-ontology-config.md) | HMM-73 (sub, le31 v1 — Core MVP) | [`specs/agents-yaml-ontology-config-HANDOFF.md`](specs/agents-yaml-ontology-config-HANDOFF.md) |
| 2026-08-13 | `second-opinion-verifier-role` | v2-AI control-plane (PARKING-LOT — pending charter §4 multi-model revision) | [`features/63-second-opinion-verifier-role.md`](features/63-second-opinion-verifier-role.md) | HMM-74 (sub, le31 v1 — Core MVP, Backlog) | [`specs/second-opinion-verifier-role-HANDOFF.md`](specs/second-opinion-verifier-role-HANDOFF.md) |
| 2026-08-14 | `retail-localization-reference-pattern` | v2 owner-pains (EU/Paris/compliance, S effort, build candidate) | [`features/64-retail-localization-reference-pattern.md`](features/64-retail-localization-reference-pattern.md) | HMM-77 (sub, le31 v1 — Core MVP) | [`specs/retail-localization-reference-pattern-HANDOFF.md`](specs/retail-localization-reference-pattern-HANDOFF.md) |
| 2026-08-14 | `cook-photo-stock-list-pwa` | v2 owner-pains (cook-UX, M effort, build candidate) | [`features/65-cook-photo-stock-list-pwa.md`](features/65-cook-photo-stock-list-pwa.md) | HMM-78 (sub, le31 v1 — Core MVP) | [`specs/cook-photo-stock-list-pwa-HANDOFF.md`](specs/cook-photo-stock-list-pwa-HANDOFF.md) |
| 2026-08-14 | `offline-first-pwa-transactional-arch` | v2 owner-pains (resilience experiment, S effort, design-doc only) | [`features/66-offline-first-pwa-transactional-arch.md`](features/66-offline-first-pwa-transactional-arch.md) | HMM-79 (sub, le31 v1 — Core MVP) | [`specs/offline-first-pwa-transactional-arch-HANDOFF.md`](specs/offline-first-pwa-transactional-arch-HANDOFF.md) |