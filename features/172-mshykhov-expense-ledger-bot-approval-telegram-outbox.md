# Feature 172 — `mshykhov-expense-ledger-bot-approval-telegram-outbox` (experiment)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `mshykhov/expense-ledger-bot` (**0★/0⑂**, **MIT**, Python, **pushed 2026-09-13T05:19:30Z**, in-window by create+push, 233 KB, **created 2026-09-13T05:17:59Z — 2-minute-old repo at push time**). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-13): *"Telegram expense ledger with approval-based entries, PostgreSQL transactions, an outbox, and optional Google Sheets projection."* Topics (verbatim from raw JSON, parent-verified): `postgresql, python, self-hosted, telegram-bot`. Bucket: **v1 (operator-surface reference)** — pick C of Brainstorm 2026-09-13. Build verdict: **experiment** (the *shape* is the v1-architecture-reference; the *code* may be small but the pattern is implementable in <233 KB by a single maintainer). Same author has a sister repo `mshykhov/flight-price-watcher` (also MIT, also pushed today, also Telegram + Postgres).

## Goal

Retain the **"Telegram + PostgreSQL transactions + outbox + approval gate + Sheets projection"** stack as a persistent v1-architecture-reference for the LE31 v1 backend-shape, and document the *unified reference implementation* of the four primitives that LE31 v1 already implements piecemeal (approval-based entries / PostgreSQL transactions / outbox pattern / Sheets projection). The artifact is the persistent cross-section reference + a v1-architecture-reference study for the next maintainer. No code today; an experiment is to read the codebase and evaluate the integration quality.

## Scope

**In scope (defer artifact + experiment):**
- A written record of the **"Telegram + PostgreSQL transactions + outbox + approval gate + Sheets projection"** stack as the LE31 v1 backend-shape reference. An independent maintainer arrived at this stack in 2026 without reading the LE31 charter, without the LE31 §3.1/§3.2 framework, without any of the 169 existing LE31 features. The pattern's contribution is the *architecture-confidence signal*.
- A written record of the **four 1:1 primitives**:
  1. **Approval-based entries** ↔ feature 61 `holdfast-approval-ledger` (LE31 v1 implements the approval-gate pattern via `audit_logs.actor_user_id` + role-based approval workflow)
  2. **PostgreSQL transactions** ↔ LE31 v1's `orders` + `audit_logs` SQLModel transactions (every state change is wrapped in a transaction; commit-on-approve is the LE31 v1 primitive)
  3. **Outbox pattern** ↔ feature 35 `sse-replay-buffer` (LE31 v1 implements the outbox pattern via the SSE-cook-channel; the SSE buffer is the source of truth for cook-facing events)
  4. **Sheets projection** ↔ feature 39 `owner-daily-recap-telegram` + feature 57 `owner-recap-persona-voice` (LE31 v1's owner-recap export is the Sheets-projection pattern; the operator-facing recap export)
- An **experiment** to read the `mshykhov/expense-ledger-bot` codebase (233 KB Python) and evaluate whether the *implementation quality* matches the *description*. If the code is clean, the pattern is a *reference implementation* for the next maintainer. If the code is sloppy, the pattern stays at the *description level* and the parking-lot verdict is filed.
- A decision record: today's verdict is `experiment` because (1) the repo is 0★ with single-maintainer + 2-minute-old cadence; (2) the *stack-shape* is the value, not the code; (3) the experiment is a *code-read*, not a *code-adoption*.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema or `sse_replay_buffer` (feature 35) or `outbox` (if/when introduced).
- Adoption of the expense-ledger-bot codebase (the repo is brand-new, single-maintainer, 233 KB; the pattern is portable; the codebase is not adoptable without a full read-and-eval).
- Cross-pollination with charter §3.4 AI surface (the expense-ledger-bot has zero AI; the Telegram bot is deterministic; §3.4 compatible).
- Cross-pollination with charter §3.3 (single-user, single-tenant; multi-tenant is not in scope).

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"what does the LE31 v1 backend look like in practice?"*, they want *a reference implementation* of (Telegram + PostgreSQL + outbox + approval + Sheets projection), but struggle because *LE31 v1's codebase is the only such reference, and reading the entire LE31 v1 codebase is expensive*, so that *the v1 maintainer can compare their implementation to a known-good external reference*.

- **Evidence class**: observed (the expense-ledger-bot description names the four primitives explicitly: `approval-based entries`, `PostgreSQL transactions`, `outbox`, `Google Sheets projection`).
- **Confidence**: medium-high for the architecture-shape (the description is direct; the four primitives map 1:1 onto LE31 v1 surfaces); low for the implementation-quality (the codebase is not yet read; the experiment is to read it).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is implemented; the next maintainer is the audience).
- **The value is naming + reference, not direct demand**: when the first v1 PR lands that touches the SSE-cook-channel (feature 35) or the owner-recap export (feature 39) or the approval-gate (feature 61), the expense-ledger-bot pattern is a ready-made *external reference* of the same stack-shape.

## Description

GitHub `mshykhov/expense-ledger-bot` (MIT, 0★/0⑂, Python, pushed 2026-09-13T05:19:30Z, created 2026-09-13T05:17:59Z, 233 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-13): *"Telegram expense ledger with approval-based entries, PostgreSQL transactions, an outbox, and optional Google Sheets projection."*

The architectural pattern has one core observation and four sub-primitives:

1. **"Telegram expense ledger"** — the operator-facing surface is a Telegram bot. Every entry is initiated by a Telegram message. The Telegram surface is the *operator-side* channel; the *customer-side* channel is not in scope.
2. **"Approval-based entries"** — every entry must be approved before it becomes a state change. The approval gate is the *human-in-the-loop* discipline. This maps to LE31 v1's `audit_logs.actor_user_id` + role-based approval workflow (cook approves the order before it transitions to "in-prep"; owner approves the variance before it transitions to "variance-recorded").
3. **"PostgreSQL transactions"** — every state change is wrapped in a PostgreSQL transaction. The transaction is the *atomicity* discipline. This maps to LE31 v1's `orders` + `audit_logs` SQLModel transactions (every state change is wrapped in `with session.begin(): ...`).
4. **"An outbox"** — every state change is appended to an outbox table; a separate worker reads the outbox and dispatches to downstream surfaces (Sheets, in this case). The outbox is the *event-sourcing* discipline. This maps to LE31 v1's `sse_replay_buffer` (feature 35) — the SSE buffer is the cook-facing outbox.
5. **"Optional Google Sheets projection"** — the operator can opt-in to a Google Sheets projection of the ledger. The Sheets projection is the *secondary export* surface. This maps to LE31 v1's owner-recap export (feature 39 `owner-daily-recap-telegram`) — the owner-recap is the operator-facing recap, which could be exported to Sheets as a secondary surface.

**The 1:1 mapping onto LE31 v1 backend:**

| expense-ledger-bot primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Telegram bot | cook Telegram bot (feature 33 `telegram-walkin-pin`) | §3.1 ✓ | **Implemented (v1)** |
| Approval-based entries | `audit_logs.actor_user_id` + role-based approval workflow (cook approves; owner approves variance) | §3.1 + §3.2 ✓ | **Implemented (v1)** — equivalent to feature 61 `holdfast-approval-ledger` |
| PostgreSQL transactions | `orders` + `audit_logs` SQLModel transactions (every state change is wrapped) | §3.1 + §3.2 ✓ | **Implemented (v1)** |
| Outbox | `sse_replay_buffer` (feature 35) — the SSE buffer is the cook-facing outbox | §3.1 + §3.2 ✓ | **Implemented (v1)** — equivalent to outbox pattern |
| Google Sheets projection | owner-recap export (feature 39 `owner-daily-recap-telegram`) + voice-persona recap (feature 57 `owner-recap-persona-voice`) | §3.1 + §3.2 ✓ | **Implemented (v1)** — but not yet exported to Sheets |

The mapping table makes the case: **LE31 v1 already implements the four primitives of the expense-ledger-bot pattern**. The expense-ledger-bot is the *external reference implementation* of the same stack-shape, in a different domain (expense vs restaurant). The pattern's contribution is the *architecture-confidence signal*: an independent maintainer arrived at the same stack-shape in 2026 for a different use case.

## Data model

**No schema change today.** The defer artifact is documentation only.

The pattern itself does not require a schema change — the LE31 v1 schema already implements the *Telegram + PostgreSQL + outbox + approval + Sheets-projection* surface.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v1 implementation would include:
1. None — the v1 surface is already implemented. The expense-ledger-bot pattern is the *external reference* for the LE31 v1 backend-shape.

**No existing code change today.**

The *experiment* is to read the codebase in a separate session:
1. `git clone https://github.com/mshykhov/expense-ledger-bot`
2. Read the README + the entry-point script + the outbox worker
3. Evaluate the implementation quality: is the approval gate deterministic? Is the outbox pattern correct? Is the Sheets projection transactional?
4. If the implementation is clean, file a cross-section evidence note in the feature contract. If the implementation is sloppy, downgrade to parking-lot.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

The expense-ledger-bot's Telegram surface maps to LE31 v1's cook Telegram bot (feature 33). The Telegram-bot pattern is *operator-facing* (the cook or owner, not the customer), so §3.4 does not trigger.

Future v1: if the owner approves a feature that adds a *Sheets-export* surface for the owner-recap (e.g. an "Export to Google Sheets" button), the Sheets-projection pattern becomes a *named companion surface*. The owner-recap export (feature 39) is the LE31-native operator-surface-shape; the Sheets export would be a *secondary* surface for owners who prefer Sheets over Telegram.

## Dependencies

- **LE31 v1 status**: cook Telegram bot implemented (feature 33), approval gate implemented (feature 61), PostgreSQL transactions implemented (`orders` + `audit_logs`), outbox pattern implemented (feature 35 `sse-replay-buffer`), owner-recap implemented (feature 39), Sheets projection NOT YET implemented (v2 surface).
- **External**: aiogram (cook Telegram bot uses the same library), PostgreSQL (LE31 v1 uses the same DB), Sheets API (not yet integrated; v2 surface).
- **Charter**: §3.1 + §3.2 + §3.4 all compatible (zero AI, single-restaurant scope, no customer-facing AI).

## Open questions

1. **Is the expense-ledger-bot implementation quality worth a code-read experiment?** — the codebase is 233 KB Python, single maintainer, 2-minute-old. The risk is that the code is sloppy and the pattern is *description-only*. The experiment is to read the code and decide.
2. **Should LE31 v1 add a Sheets-export surface?** — the owner-recap could be exported to Google Sheets for the owner who wants to analyze the data in a spreadsheet. This is a v2 surface. Decision deferred to first v2 PR that touches the owner-facing surface.
3. **Should LE31 v1 add a Sheets-import surface?** — an operator who is currently using a Google Sheets template could migrate to LE31 v1 by importing the spreadsheet. This is a v2 surface. Decision deferred.
4. **Is the outbox pattern in LE31 v1's `sse_replay_buffer` correct?** — the outbox pattern requires that every state change is appended to the outbox *in the same transaction* as the state change. If the SSE buffer is updated in a separate transaction, the outbox pattern is broken (the SSE buffer can lose entries). The experiment is to verify that LE31 v1's `sse_replay_buffer` is updated in the same transaction as the state change. If not, this is a *vulnerability* in the LE31 v1 architecture.

## Why this matters

The expense-ledger-bot pattern is the **architecture-confidence signal** for the LE31 v1 backend-shape. An independent maintainer in 2026 independently arrived at (Telegram + PostgreSQL + outbox + approval + Sheets projection) as the *minimum-viable Telegram-ledger backend* — without reading the LE31 charter, without the LE31 §3.1/§3.2/§3.4 framework, without any of the 169 existing LE31 features. The pattern's contribution is the *architecture-confidence signal*: there is at least one independent maintainer in 2026 who arrived at the same stack-shape. The 0★ is a popularity signal (§3.2 note: stars are not need-validation), not a negation. The stakeholder reasoning: if LE31 v1 ever proposes a v1 backend refactor (e.g. consolidating the SSE-cook-channel into a true outbox pattern), the expense-ledger-bot pattern is a *named architectural reference* + a *cross-section with the four existing v1 primitives*.

## Distinct from existing features

Ripgrep-verified unique vs features/ 1–169 (2026-09-13). Sister-shape references (each covers one slice of the four primitives):
- `30-append-only-audit-redirect` — ledger pattern
- `33-telegram-walkin-pin` — Telegram operator surface
- `35-sse-replay-buffer` — outbox pattern (cook-facing)
- `39-owner-daily-recap-telegram` — owner-recap export (Sheets-projection pattern)
- `41-telegram-msg-stock-update` — Telegram stock-update surface
- `43-telegram-prep-checkoff-adherence` — Telegram prep-check surface
- `57-owner-recap-persona-voice` — operator recap export (voice-persona)
- `60-restaurant-telegram-front-desk-mirror` — Telegram mirror surface
- `61-holdfast-approval-ledger` — approval gate
- `78-postledger-tamper-evident-hash` — ledger-tamper-evidence
- `108-telegram-chat-history-fuzzy-search-stockentry-audit` — Telegram-history + stockentry

The expense-ledger-bot pattern is the **unified external reference** for the four primitives. The existing features cover each primitive individually; the expense-ledger-bot is the *integration* of all four primitives in a 233 KB Python codebase.

---

**End of feature contract.**
