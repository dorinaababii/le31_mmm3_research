# Feature 131 — puntovivo fiscal-native local-first POS cross-section

> **NEW observation (2026-08-28).** Documents the in-window
> `johnny4young/puntovivo` repo — **2★ / 1 fork, MIT, TypeScript**,
> created **2026-01-30** (off-window), pushed **2026-08-27**
> (in-window by push only) — from the 2026-08-28 brainstorm pass.
> Bucket: **v2 owner-pains (parking-lot)** — defer.
> Zero build time today.
>
> **Weakest of the three picks in this pass, and recorded as such.**
> 2★, off-window creation date, stack entirely disjoint from LE31,
> and — most importantly — **no LE31 owner has ever raised a
> fiscal-compliance requirement in any of the 29 passes.** The value
> here is contingent and the trend line matters more than the repo.

## Goal

Record the **third independent local-first-POS data point** in the
series, and the **first with statutory fiscal compliance as a
first-class architectural concern** rather than a bolt-on. Track it
as a parking-lot observation against the possibility that a
receipt-retention or statutory-record requirement ever surfaces for
LE31 — and note, for that eventuality, that LE31's existing
append-only posture is already most of the answer.

## Scope

**In scope:**
- This contract file as the durable record of the repo, its verbatim
  description, and its position in the local-first-POS trend line.
- One INDEX.md row in the active-feature-pipeline table.
- Adding `johnny4young/puntovivo` to the daily-research watch list
  for star/fork/push tracking.
- Re-evaluation trigger: if the repo crosses **≥10★**, or if any
  owner conversation touches receipts, tax, or record retention.

**Out of scope (v1 and today):**
- Any code. No fiscal module, no receipt model, no e-invoicing, no
  schema change, no migration.
- Any code import from `puntovivo`. MIT licence permits it; the
  stack forbids it in practice — Electron + React + Fastify + tRPC +
  SQLite has no overlap with FastAPI + SQLModel + htmx. **No
  dependency is proposed.**
- Any assumption about Swiss fiscal or receipt-retention law.
  **This agent has not verified what Switzerland requires and must
  not pretend otherwise.** The question is flagged, not answered.
- Any desktop/Electron surface for LE31. That question belongs to
  feature 119's cross-platform-deployment consideration, not here.
- Any claim that 2★ constitutes evidence of demand. It does not.
- Any new dependency.

## Description

### Source

- **Repo**: [`johnny4young/puntovivo`](https://github.com/johnny4young/puntovivo)
- **Stars / forks**: **2★ / 1 fork**
- **Licence**: **MIT** (charter §3.2 satisfied for reference
  purposes; no import intended)
- **Language**: TypeScript
- **Created**: 2026-01-30 — **off-window by ~7 months**
- **Pushed**: 2026-08-27 — **in-window by push only**
- **Discovered by**: creative query
  `restaurant+language:python+stars:%3E1` (note: surfaced under a
  `language:python` query despite being TypeScript — GitHub's
  search matched repository text, not the language filter's intent)
- **Topics**: `colombia, dian, drizzle, electron, electronic-invoicing,
  fastify, inventory-management, invoicing, latam, local-first,
  offline-first, point-of-sale, pos, pos-system, react, retail,
  small-business, sqlite, trpc, typescript`
- **Raw fetch**: `/tmp/le31-brainstorm-2026-08-28/gh_search_restaurant_language_python_stars_3E1.json`
- **Metadata provenance**: every field above re-extracted by the
  parent agent from the raw GitHub search JSON. The subagent's
  curated table omitted licences and creation dates entirely.

### Verbatim description

> "Local-first, fiscal-native POS for Latin American retail —
> Electron + React + Fastify + tRPC + SQLite"

### What the topics reveal

The `dian` topic is Colombia's national tax authority (Dirección de
Impuestos y Aduanas Nacionales). Paired with `electronic-invoicing`
and the phrase **"fiscal-native"** in the description, the repo is
asserting that statutory invoicing obligations are satisfied by the
core data model rather than by an export step bolted on afterwards.

That is the only genuinely new dimension this repo adds over the two
prior local-first-POS data points. Everything else about it
(local-first, offline-first, SQLite-in-a-folder, small-business
retail) is already recorded.

### The trend line — the actual signal

| # | Repo | Surface | Licence | First seen | Feature |
|---|---|---|---|---|---|
| 1 | `Ritchalison/BalanceDesk` | Windows desktop reconciliation terminal | **NOASSERTION** | 2026-08-26 | 119 |
| 2 | `MehfoozurRehman/restopilot-command` | Electron + React 19 + Vite + Convex desktop restaurant POS | — | 2026-08-27 | logged under 119 |
| 3 | **`johnny4young/puntovivo`** | **Electron + React + Fastify + tRPC + SQLite, fiscal-native** | **MIT** | **2026-08-28** | **this one** |

Three independent local-first POS/back-office projects surfacing in
three consecutive days is a pattern worth tracking regardless of any
individual repo's star count. **The trend is the signal; the repo is
the data point.** All three are Electron-or-desktop-shaped, which is
the opposite of LE31's server + Telegram + htmx posture — so the
trend is interesting as a divergent-approach observation, not as
something to copy.

### Why this could matter to LE31 — and why it probably will not

**The transferable question**, stated as a question because it has
not been answered: *if a statutory receipt-retention or
record-immutability obligation ever applies to LE31, does the
existing data model satisfy it, or would compliance be a bolt-on
that drifts from operational reality?*

**The reassuring answer**, and the reason this is cheap to file:
LE31's charter §3.1 already mandates append-only `StockEntry` rows,
no updates, no deletes, and an `audit_logs` row per mutation. That
is architecturally *already* what a fiscal-immutability requirement
would ask for. If such a requirement ever lands, LE31 is well
positioned rather than exposed. Recording that observation is worth
one file.

**The honest deflation**: no owner has raised fiscal compliance in
29 passes. Switzerland's actual requirements are unverified by this
agent. The repo is 2★, created off-window, and stack-disjoint. If
the question never arrives, this artifact is worth nothing and
should expire.

### Honest assessment of strength

- **Weakest pick of the pass, explicitly.** Picks 129 and 130 rest
  on published papers with specified mechanisms. This rests on a
  repo description and a topic list.
- **2★ is not evidence.** Two stars says nothing about whether any
  restaurant needs this. The stars are reported for completeness and
  are **not** offered as demand signal.
- **In-window by push only.** Created 2026-01-30, roughly seven
  months before the window opens. Stated plainly rather than
  presented as a fresh discovery.
- **Value is contingent, not latent.** Unlike an architectural
  primitive that becomes useful when the system grows, this becomes
  useful only if an external legal requirement appears. It is
  binary, external, and outside LE31's control.
- **Nothing was read beyond the description.** The README has not
  been fetched. The claim "fiscal-native" is the author's, not a
  verified property.
- Confidence: **medium** that the repo is what its description says;
  **low** for any LE31 relevance; **low** for present urgency.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 05 `payment-tip-reconciliation` | Payment and tip reconciliation | Operational reconciliation; this is statutory record obligation |
| 49 `postledger-tamper-evident-hash` | Per-row tamper evidence | Cryptographic immutability; this is *legally-mandated* immutability (overlapping mechanism, different driver) |
| 53 `zentra-offline-first-fb-pattern` | Offline-first F&B pattern | Offline-first pattern; this adds the fiscal-compliance dimension |
| 54 `corner-mart-pos-double-entry` | Double-entry POS accounting | Accounting correctness; this is statutory filing/retention |
| 64 `retail-localization-reference-pattern` | Retail localisation | **Closest neighbour** — localisation of retail software; this is specifically tax-authority integration |
| 66 `offline-first-pwa-transactional-arch` | Offline-first transactional arch | Architecture; this is compliance-as-data-model |
| 107 `smb-erp-pos-schema-separation-lsfusion` | SMB ERP/POS schema separation | Schema separation; this is fiscal-native modelling |
| 119 `balancedesk-local-first-reconciliation-terminal-cross-section` | **Same trend line, data point 1** | BalanceDesk is reconciliation, NOASSERTION-licensed, no fiscal layer; puntovivo is POS, MIT, fiscal-native |

Ripgrep-clean against features 1–130 by slug and by repo name.
Checked explicitly against feature 119 (`fiscal|invoicing|DIAN|
local-first`) — 119 is a reconciliation terminal with an unresolved
licence and **no fiscal-compliance dimension**, so this is a
distinct data point in the same trend, not a duplicate.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero
migrations.

If a statutory receipt requirement ever surfaced, the mechanism would
imply (not decided, not designed, and **not** to be designed from
this repo):

- a statutory-receipt record whose immutability guarantee is
  documented as legally-driven, not merely architectural;
- a canonical serialised form fixed at write time, since a statutory
  record must be reproducible byte-for-byte later;
- an explicit retention period as data, not as a code constant;
- **no change** to `StockEntry` / `audit_logs`, which already satisfy
  the append-only property such a requirement would demand.

Sketches only. The actual requirements would come from Swiss law,
which **this agent has not read**, not from a Colombian POS repo.

## Implementation

1. **No implementation today.** The deliverable is this contract
   file.
2. **Watch-list additions**: daily `GET
   https://api.github.com/repos/johnny4young/puntovivo` via
   `$HERMES_GITHUB_TOKEN`; track stars, forks, `pushed_at`.
3. **Re-evaluation triggers** (either one):
   - the repo crosses **≥10★** (community-traction threshold), or
   - **any** owner conversation touches receipts, tax filing, or
     statutory record retention.
4. **When triggered by an owner conversation** (the only trigger
   that actually matters):
   - Establish what Swiss law requires. **Start there, not here.**
     This repo is a Colombian implementation of Colombian rules and
     is not authority on anything.
   - Then check whether LE31's existing append-only model already
     satisfies it. It plausibly does.
   - Only then consider whether any new modelling is needed.
   - Run `le31-conventions` on the concrete v2 feature. This
     artifact pre-authorises nothing.
5. **If neither trigger fires within 90 days (by 2026-11-26)**,
   retire this artifact. Contingent-value parking-lot entries should
   not accumulate indefinitely.

## Telegram interaction

None today, and none plausibly. A statutory receipt obligation is an
owner/back-office concern, not a cook-surface one. No cook-bot
interaction is implied.

## Dependencies

- None today.
- Same trend line as feature 119 (and the `restopilot-command`
  observation logged under it). Neither is a prerequisite.
- Conceptually adjacent to features 49 (tamper-evident hash) and 54
  (double-entry) — a fiscal requirement would likely reuse 49's
  mechanism with a different justification.

## Open questions

- **Does Switzerland impose a receipt-retention or record-
  immutability obligation on a restaurant of LE31's size?**
  Unverified. This is the question the whole artifact hinges on and
  it has not been asked, let alone answered.
- Has any LE31 owner ever raised fiscal compliance? **No — not in
  29 passes.** This is the strongest argument that the pick is
  premature.
- Is "fiscal-native" a real architectural property of puntovivo or
  marketing in a repo description? **Unknown; the README was not
  fetched.**
- Why does a TypeScript repo surface under a `language:python`
  query? GitHub matched repository text rather than honouring the
  filter's intent. Worth noting as a **search-hygiene caveat for
  future passes** — the `language:` qualifier does not guarantee the
  language of returned repos.
- Is the three-repo local-first-desktop trend meaningful, or is it
  three unrelated hobby projects in a popular template stack? **Three
  points is not a trend with confidence.** Worth watching, not worth
  concluding.

## Why this matters

The durable content of this artifact is two sentences, and they
should be read as the whole point:

1. **Three independent local-first POS/back-office projects appeared
   in three consecutive days**, all desktop-shaped — the opposite of
   LE31's server + Telegram posture. Worth watching as a divergent
   approach, not worth copying.
2. **If a statutory record-immutability requirement ever reaches
   LE31, the append-only discipline in charter §3.1 is already most
   of the answer.** That is a reassuring fact about a decision
   already made, and it is cheap to have written down.

Everything else here is contingent on an external legal requirement
nobody has asked about. The repo itself contributes a description and
a topic list.

The recommendation is **defer (parking-lot)** with a hard 90-day
retirement date. This is the weakest pick of the pass and is filed at
its true weight rather than inflated to match the other two.
