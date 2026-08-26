# Feature 118 — textile-erp WhatsApp conversation-first audit-ERP cross-section

> **NEW observation (2026-08-26).** Documents the in-window
> `captainsaify/textile-erp` WhatsApp-native conversation-first ERP (1★
> **MIT** Python, pushed **2026-08-25T01:27:20Z yesterday**) whose README
> *verbatim mirrors* three core LE31 charter §3.1 phrases — "Nothing is
> ever deleted. Corrections are compensating entries" + "Inventory is
> reconciled nightly against the signed sum of its movements, and a
> mismatch is **reported, never repaired**" + "money is NUMERIC/Decimal,
> never a float, anywhere — including the browser" + "every mutation
> writes an `audit_logs` row, with soft deletes only". The peer
> independently invented the LE31 architectural direction (append-only
> audit + Decimal money + reconcile-don't-repair + every-mutation-writes-
> audit-row + conversation-first posture) on a *different* messaging
> surface (WhatsApp instead of Telegram) and a *different* domain (textile
> ERP instead of restaurant).
> Bucket: **v2 owner-pains (parking-lot, future-WhatsApp-cook-bot-mirror),
> defer** — the peer is a *charter-validation* signal (LE31's direction
> has peer traction in the small-business ERP niche), not a v1 build
> candidate.

## Goal

Track the in-window `captainsaify/textile-erp` WhatsApp-native
conversation-first ERP as **charter-validation peer** for the LE31 v2
WhatsApp-surface cross-section consideration. The README's verbatim
mirror of three LE31 charter §3.1 phrases is the strongest
*charter-validation* signal observed in the 27-pass brainstorm/daily-
research series. The cross-section insight: a *WhatsApp-native* mirror
of LE31's cook-Telegram-bot posture, invented independently. The
"OCR-learns-from-corrections" loop + "fuzzy-duplicate-detection" +
"weighted-average-cost-warns-before-saves" + "Decimal money, never a
float" + "every mutation writes an `audit_logs` row" formulation is
**line-for-line a mirror of LE31 charter §3.1 deterministic-gate +
features 30 (append-only-audit-redirect) + 49 (decision-rationale-mixin)
+ 81 (append-only-immutable-audit-check) + the per-batch `StockEntry`
ledger + feature 03 FIFO cost discipline**. Watch-list continue (defer
until the v2 charter review surfaces the WhatsApp-surface extension).

## Scope

**In scope:**
- Cite `textile-erp` as a charter-validation peer in the next
  daily-research pass.
- Track whether `textile-erp` reaches ≥5★ in the next 30 days
  (community-traction signal).
- Cross-reference `textile-erp` against LE31 features 30 + 49 + 81
  v2 audit-trail extension in the LE31 feature-gate trail when the v2
  charter review opens.
- Add a row to `/opt/data/INDEX.md` "Active feature pipeline" table
  with date, pick, feature path, Linear ID, status (Backlog,
  watch-list defer, v2 owner-pains).
- Re-evaluate `textile-erp` on star velocity + push activity in the
  next 30 days; if ≥5★ or new significant architectural changes, surface
  as a future-v2 charter-question prompt.

**Out of scope:**
- Any code change to the LE31 backend (peer is informational).
- Any schema change, migration, or config key change.
- Any new pip dependency (the LE31 stack already has FastAPI + Postgres
  + SQLModel + audit-log tables; the WhatsApp surface is a v2 question).
- Any charter change (charter §3.1 Telegram-first posture remains
  correct for v1; v2 WhatsApp surface is parked).
- Any code-borrow from `textile-erp` (the WhatsApp Cloud API is a v2
  integration question, not a v1 path; the architectural pattern is
  informational only).

## Description

### Peer overview

| Field | Value |
|---|---|
| Repo | `captainsaify/textile-erp` |
| Stars | 1★ |
| License | **MIT** (permissive, no contagion) |
| Last push | 2026-08-25T01:27:20Z (yesterday) |
| Topics | `accounting, celery, erp, fastapi, ocr, postgresql, python, small-business, sqlalchemy, whatsapp` |
| URL | https://github.com/captainsaify/textile-erp |
| README verification | Verified directly from `api.github.com/repos/captainsaify/textile-erp/readme` with `HERMES_GITHUB_TOKEN` at 2026-08-26 06:32 UTC |

### Description (verbatim from GitHub API)

> "WhatsApp-native trading ERP for a textile business: OCR purchase
> intake, weighted-average inventory, double-entry accounting, and a
> read-only dashboard."

### README key claims (verbatim, verified 2026-08-26 06:32 UTC)

- "Inventory is reconciled nightly against the signed sum of its
  movements, and a mismatch is *reported, never repaired* — repairing
  it would destroy the evidence that something upstream is broken"
- "Nothing is ever deleted. Corrections are compensating entries, so a
  reversed payment and the entry that reversed it both stay on the
  page"
- "Every document says what changed about it — a corrected bill
  carries a MODIFIED banner, per-row markers, and who changed what
  and when, read straight from the audit log"
- "Two rules the whole codebase is built on: **money is `NUMERIC`/
  `Decimal`, never a float**, anywhere — including the browser; and
  **every mutation writes an `audit_logs` row**, with soft deletes only"
- "OCR pipeline → conversational intake → PostgreSQL → read-only web"
- "Selling below weighted-average cost warns before it saves"

### LE31 adjacency analysis

The `textile-erp` README's pattern maps directly to LE31's existing
feature contracts:

| `textile-erp` pattern | LE31 feature | Status |
|---|---|---|
| "Inventory is reconciled nightly... reported, never repaired" | Feature 03 (kitchen-stock-tracker) + per-batch `StockEntry` ledger | Active in v1 |
| "Nothing is ever deleted. Corrections are compensating entries" | Feature 30 (append-only-audit-redirect) + Feature 81 (append-only-immutable-audit-check) | Active in v1 |
| "every mutation writes an `audit_logs` row, with soft deletes only" | Feature 30 + Feature 81 + Feature 49 (decision-rationale-mixin) | Active in v1 |
| "money is NUMERIC/Decimal, never a float" | Feature 03 FIFO cost discipline + charter §3.2 (Decimal invariant) | Active in v1 |
| "Selling below weighted-average cost warns before it saves" | Feature 19 (menu-engineering) + per-batch `StockEntry` ledger | v1 active / v2 reference |
| "OCR-learns-from-corrections" loop | Feature 04 (menu-photo-bot, OCR wiring) | Active in v1 |
| "Duplicate invoices caught fuzzily" | Feature 49 (decision-rationale-mixin) | Active in v1 |
| "conversation-first posture (WhatsApp-native)" | Feature 04 (cook Telegram bot surface) | v1 Telegram surface, v2 WhatsApp = parked |
| "read-only dashboard" | Feature 06 (guest-demographics reports) + Feature 07 (demand-estimation) | Active in v1 |

**This is the strongest charter-validation signal in the 27-pass
series.** Three exact phrases ("Nothing is ever deleted" + "reported,
never repaired" + "every mutation writes an audit_logs row" + "money is
NUMERIC/Decimal, never a float") that LE31 has been carrying since the
2026-07-24 charter are now *verbatim* in an independently-developed
peer (textile ERP, not restaurant ERP; WhatsApp, not Telegram). The
architectural direction is community-validated in the small-business
ERP niche.

### Why this peer matters (but is still a watch-list defer)

1. **Strongest charter-validation signal in the 27-pass series.**
   The verbatim README mirror of LE31 charter §3.1 phrases is
   independent confirmation that the LE31 architectural direction
   (append-only audit + Decimal money + reconcile-don't-repair +
   every-mutation-writes-audit-row + conversation-first posture)
   has peer traction in the small-business ERP niche.
2. **Direct adjacency to LE31 features 30+49+81+03+04+19+49**. The
   README mirrors 8+ LE31 v1 features (above table). The pattern is
   already validated by the LE31 stack itself; the peer is the
   *external validation* of the pattern.
3. **WhatsApp cross-section v2 candidate**. The peer's WhatsApp
   surface is the v2 cross-section candidate for LE31 (charter §3.1
   keeps v1 Telegram-only; v2 WhatsApp = parked). The peer's
   WhatsApp Cloud API integration is informational reference for
   any future LE31 v2 WhatsApp surface.
4. **Permissive-licensed**. MIT license = no contagion for code or
   pattern-borrow.
5. **Watch-list defer**. The peer is a charter-validation signal, not
   a v1 build candidate. Watch-list continue until the v2 charter
   review surfaces the WhatsApp-surface extension.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 30 `append-only-audit-redirect` | Append-only audit-redirect (LE31 v1) | LE31 feature, not external peer |
| 49 `decision-rationale-mixin` | Decision-rationale mixin (LE31 v1) | LE31 feature, not external peer |
| 81 `append-only-immutable-audit-check` | Audit-trail primitive (LE31 v1) | LE31 feature, not external peer |
| 102 `nightmux-stdlib-telegram-bridge` | Stdlib-only Telegram-agent bridge peer | Different peer, Telegram surface (not WhatsApp); LE31-direct |
| 104 `aldia-ai-agent-business-engine-cross-section` | ALdia peer (Apache-2.0 MCP business engine) | Different peer, MCP framing |
| 108 `telegram-chat-history-fuzzy-search-stockentry-audit` | Telegram fuzzy-search for `StockEntry`-audit (LE31 v2 cross-section) | LE31 feature, not external peer |
| 111 `arXiv-scroll-append-only-event-log-context-arch` | Scroll paper academic-backing for v2 audit-search | Academic, not external peer |
| 112 `twff-deterministic-process-logging-human-ai-collab` | Twff open-standard peer (Apache-2.0) | Different peer, open-standard framing |
| **118 `textile-erp-whatsapp-conversation-first-audit-erp` (this)** | `textile-erp` WhatsApp-native conversation-first ERP peer (MIT) | **Charter-validation** — verbatim mirror of LE31 charter §3.1 phrases; WhatsApp surface (v2 cross-section candidate) |

This pick is **charter-validation**, not a duplicate of features
30/49/81/102/104/108/111/112. It is the **strongest charter-validation
signal** in the 27-pass brainstorm/daily-research series.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a watch-list artifact; no schema change.

## Implementation

1. Read `textile-erp` README in full in the next daily-research pass
   (2026-08-27) and cite in the report.
2. Track `textile-erp` star velocity + push activity in the next 30
   days. If ≥5★ or new significant architectural changes, surface as
   a future-v2 charter-question prompt.
3. Cross-reference `textile-erp` against features 30 + 49 + 81 v2
   extension in the LE31 feature-gate trail when the v2 charter
   review opens.
4. **No build today.** The pick is a watch-list defer. The "should LE31
   v2 adopt a WhatsApp-surface mirror of `textile-erp`'s
   conversation-first posture?" question is parked pending the v2
   charter review.

## Telegram interaction

None. This is a passive watch-list observation; no LE31 cook/manager
action. The peer's WhatsApp surface is a v2 question; v1 Telegram
cook-bot surface remains unchanged.

## Dependencies

- None. The `textile-erp` peer is a charter-validation signal; no new
  dependencies. The WhatsApp Cloud API integration is a v2 question,
  not a v1 path.

## Open questions

- Does `textile-erp` reach ≥5★ in the next 30 days? (If yes,
  indicates community traction in the conversation-first small-
  business ERP niche.)
- Does the `textile-erp` maintainer push a v2 of the architecture
  with multi-tenant posture? (If yes, surfaces as a v2 charter-
  question prompt.)
- Does the v2 charter review surface the WhatsApp-surface extension
  in the next 90 days? (If yes, `textile-erp` becomes a
  charter-question reference.)
- Does `textile-erp` ship a public release of the reference
  implementation with a stable `requirements.txt`? (If yes, evaluate
  for code-borrow per charter §3.2 — MIT permissive.)

## Why this matters

The `captainsaify/textile-erp` peer is the **strongest charter-
validation signal in the 27-pass brainstorm/daily-research series**.
The README's verbatim mirror of three LE31 charter §3.1 phrases
(append-only audit + Decimal money + reconcile-don't-repair + every-
mutation-writes-audit-row + conversation-first posture) is
independent confirmation that the LE31 architectural direction has
peer traction in the small-business ERP niche. The peer's WhatsApp
surface is a v2 cross-section candidate for LE31 (charter §3.1 keeps
v1 Telegram-only; v2 WhatsApp = parked). **The peer is the strongest
*external validation* of the LE31 charter direction observed in the
27-pass series.**