# Feature 119 — BalanceDesk local-first reconciliation terminal cross-section

> **NEW observation (2026-08-26).** Documents the in-window
> `Ritchalison/BalanceDesk` local-first offline Windows-desktop daily-
> reconciliation terminal (1★ **NOASSERTION**, pushed **2026-08-22**) —
> the direct mirror of LE31's daily-reconciliation + business-day-
> closure flow on a different surface (Windows desktop / SQLite vs
> Linux server / Postgres / Telegram bot). **NOASSERTION license is
> pending clarification** — if the repo author clarifies to MIT /
> Apache-2.0 in a future push, this becomes Tier 0 (highest priority)
> for the next pass.
> Bucket: **v2 owner-pains (parking-lot, future-local-first-desktop-
> mirror), defer, license-pending** — the peer is a pattern-validation
> signal (local-first reconciliation terminal pattern has emerging
> peer traction outside restaurant-tech), not a v1 build candidate.
> **License status is a blocking concern** for any future code-borrow
> question; reported plainly.

## Goal

Track the in-window `Ritchalison/BalanceDesk` local-first offline
Windows-desktop daily-reconciliation terminal as **pattern-validation
peer** for the LE31 v2 cross-platform-deployment cross-section
consideration. The README's verbatim phrasing (local-first, offline,
daily sales + credit activity + expenses + physical closing counts +
reconciliation + final Business Day closure + audit history + SQLite
in folder) is the direct mirror of LE31's daily-reconciliation +
business-day-closure flow on a different surface. Watch-list continue
(defer until the v2 charter review surfaces the cross-platform-
deployment extension). **Re-evaluate license status on next pass**;
if clarified to MIT/Apache-2.0, the pick becomes Tier 0.

## Scope

**In scope:**
- Read `BalanceDesk` README + commit log in the next daily-research
  pass (2026-08-27) and check for license-file addition.
- Track whether `BalanceDesk` reaches ≥5★ in the next 30 days
  (community-traction signal).
- If the repo author adds a LICENSE file (MIT/Apache-2.0) in a future
  push, re-evaluate the pick as Tier 0 (highest priority) for the
  next brainstorm pass.
- Cross-reference `BalanceDesk` against LE31 features 03 + 05 v2
  cross-platform-deployment extension in the LE31 feature-gate trail
  when the v2 charter review opens.
- Add a row to `/opt/data/INDEX.md` "Active feature pipeline" table
  with date, pick, feature path, Linear ID, status (Backlog,
  watch-list defer, v2 owner-pains, license-pending).

**Out of scope:**
- Any code change to the LE31 backend (peer is informational).
- Any schema change, migration, or config key change.
- Any new pip dependency (the LE31 stack already has FastAPI + Postgres
  + SQLModel; the Windows-desktop surface is a v2 question).
- Any charter change (charter §3.2 single-Linux-platform posture
  remains correct for v1; v2 cross-platform is parked).
- Any code-borrow from `BalanceDesk` (NOASSERTION license = no
  code-borrow without license clarification; pattern is informational
  only).

## Description

### Peer overview

| Field | Value |
|---|---|
| Repo | `Ritchalison/BalanceDesk` |
| Stars | 1★ |
| License | **NOASSERTION** (GitHub's "no LICENSE file" default; **pending clarification**) |
| Last push | 2026-08-22T05:10:42Z |
| Topics | `local-first, offline-first, sqlite, daily-reconciliation, sales-tracking, windows-app, small-business` |
| URL | https://github.com/Ritchalison/BalanceDesk |
| README verification | Verified directly from `api.github.com/repos/Ritchalison/BalanceDesk/readme` with `HERMES_GITHUB_TOKEN` at 2026-08-26 06:32 UTC |

### Description (verbatim from GitHub API)

> "Local-first, offline daily transaction and reconciliation terminal."

### README key claims (verbatim, verified 2026-08-26 06:32 UTC)

- "local-first, offline Windows application for recording daily sales,
  credit activity, expenses, physical closing counts, reconciliation,
  and final Business Day closure"
- "designed for a small business that wants a clear operational record
  without placing business data in a cloud database"
- "The application, user accounts, audit history, backups, and SQLite
  database remain inside the extracted BalanceDesk folder on the
  user's computer"
- "Opens, reviews, reconciles, and closes one Business Day at a time"
- "Records MoMo Sales, Credit Sales, Credit Payments, and Cash or MoMo
  Expenses"
- "Tracks credit customers, invoices, payment allocations, balances"

### LE31 adjacency analysis

The `BalanceDesk` README's pattern maps directly to LE31's existing
feature contracts:

| `BalanceDesk` pattern | LE31 feature | Status |
|---|---|---|
| "recording daily sales" | Feature 06 (guest-demographics + reports) | Active in v1 |
| "credit activity" + "Tracks credit customers, invoices, payment allocations, balances" | Feature 05 (payment-tip reconciliation) + credit-accounts pattern | Active in v1 + v2 parking-lot |
| "expenses" | Feature 03 (kitchen-stock-tracker) + per-batch `StockEntry` ledger | Active in v1 |
| "physical closing counts" | Feature 03 + daily closing count pattern | Active in v1 (StockEntry per-batch reconciliation) |
| "reconciliation" + "final Business Day closure" | Feature 03 + Feature 05 + daily-reconciliation pattern | Active in v1 |
| "audit history" | Feature 30 (append-only-audit-redirect) + Feature 81 (append-only-immutable-audit-check) | Active in v1 |
| "local-first, offline" | Charter §3.2 single-Linux-platform posture | v1 single-platform; v2 cross-platform = parked |
| "SQLite in folder" | Charter §3.2 Postgres-only | v1 Postgres; v2 SQLite = parked |
| "Windows application" | Charter §3.2 Linux-server only | v1 Linux; v2 Windows = parked |

The peer's local-first + offline + reconciliation + credit-accounts +
business-day-closure triad is the direct mirror of LE31's daily-
reconciliation flow on a different deployment surface (Windows desktop
/ SQLite vs Linux server / Postgres). The peer is the *external
validation* of the pattern in the small-business Windows-desktop
niche.

### Why this peer matters (but is still a watch-list defer, license-pending)

1. **Pattern-validation in the small-business Windows-desktop niche.**
   The peer's local-first + offline + reconciliation + credit-accounts
   + business-day-closure triad mirrors LE31's daily-reconciliation
   flow on a different deployment surface. The pattern has emerging
   peer traction outside restaurant-tech.
2. **Direct adjacency to LE31 features 03 + 05 + 30 + 81**. The
   README mirrors 8+ LE31 v1 features (above table). The pattern is
   already validated by the LE31 stack itself; the peer is the
   *external validation* of the pattern.
3. **Cross-platform-deployment v2 candidate**. The peer's Windows
   desktop + SQLite surface is the v2 cross-section candidate for
   LE31 (charter §3.2 keeps v1 Linux/FastAPI/Postgres only; v2 cross-
   platform = parked).
4. **NOASSERTION license = blocking concern**. NOASSERTION = GitHub's
   default "no LICENSE file" classification. **License is pending
   clarification**. If the repo author clarifies to MIT/Apache-2.0 in
   a future push, the pick becomes Tier 0 (highest priority) for the
   next pass. **Reported plainly.**
5. **Watch-list defer**. The peer is a pattern-validation signal, not
   a v1 build candidate. Watch-list continue until the v2 charter
   review surfaces the cross-platform-deployment extension.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 03 `kitchen-stock-tracker` | Per-batch `StockEntry` ledger (LE31 v1) | LE31 feature, not external peer |
| 05 `payment-tip-reconciliation` | Payment + tip reconciliation (LE31 v1) | LE31 feature, not external peer |
| 06 `guest-demographics` | Guest demographics + reports (LE31 v1) | LE31 feature, not external peer |
| 30 `append-only-audit-redirect` | Append-only audit-redirect (LE31 v1) | LE31 feature, not external peer |
| 81 `append-only-immutable-audit-check` | Audit-trail primitive (LE31 v1) | LE31 feature, not external peer |
| 108 `telegram-chat-history-fuzzy-search-stockentry-audit` | Telegram fuzzy-search for `StockEntry`-audit (LE31 v2 cross-section) | Different peer, Telegram surface (not Windows desktop); LE31-direct |
| **119 `balancedesk-local-first-reconciliation-terminal-cross-section` (this)** | `BalanceDesk` local-first offline Windows-desktop reconciliation terminal peer (**NOASSERTION license pending**) | **Pattern-validation** — direct mirror of LE31 daily-reconciliation flow on Windows desktop / SQLite; v2 cross-platform-deployment candidate; NOASSERTION license = blocking concern |

This pick is **pattern-validation**, not a duplicate of features
03/05/06/30/81/108. It is a v2 cross-platform-deployment cross-
section candidate with a **NOASSERTION license-pending blocker**.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a watch-list artifact; no schema change.

## Implementation

1. Read `BalanceDesk` README + commit log in the next daily-research
   pass (2026-08-27) and check for license-file addition. **License
   clarification is the primary watch-list item.**
2. Track `BalanceDesk` star velocity + push activity in the next 30
   days. If ≥5★ or new significant architectural changes, surface as
   a future-v2 charter-question prompt.
3. If the repo author adds a LICENSE file (MIT/Apache-2.0) in a future
   push, **re-evaluate as Tier 0** (highest priority) for the next
   brainstorm pass.
4. Cross-reference `BalanceDesk` against features 03 + 05 v2 cross-
   platform-deployment extension in the LE31 feature-gate trail when
   the v2 charter review opens.
5. **No build today.** The pick is a watch-list defer, license-
   pending. The "should LE31 v2 adopt a Windows-desktop / SQLite
   mirror of `BalanceDesk`'s local-first reconciliation terminal?"
   question is parked pending the v2 charter review AND license
   clarification.

## Telegram interaction

None. This is a passive watch-list observation; no LE31 cook/manager
action. The peer's Windows-desktop posture is a v2 question; v1
Telegram/Linux/Postgres posture remains unchanged.

## Dependencies

- None. The `BalanceDesk` peer is a pattern-validation signal; no new
  dependencies. The Windows-desktop surface is a v2 question, not a
  v1 path.
- **License clarification is the primary dependency for any future
  code-borrow question.** Without a LICENSE file, NOASSERTION
  classification persists = no code-borrow possible.

## Open questions

- Does `BalanceDesk` add a LICENSE file (MIT/Apache-2.0) in the next
  30 days? (If yes, the pick becomes Tier 0 — highest priority — for
  the next pass.)
- Does `BalanceDesk` reach ≥5★ in the next 30 days? (If yes,
  indicates community traction in the local-first Windows-desktop
  reconciliation niche.)
- Does the v2 charter review surface the cross-platform-deployment
  extension in the next 90 days? (If yes, `BalanceDesk` becomes a
  charter-question reference IF clarified to MIT/Apache-2.0.)
- Does `BalanceDesk` ship a public release of the reference
  implementation with a stable `requirements.txt` + LICENSE file?
  (If yes, evaluate for code-borrow per charter §3.2 — pending
  license.)

## Why this matters

The `Ritchalison/BalanceDesk` peer is a **pattern-validation signal**
for the LE31 v2 cross-platform-deployment cross-section consideration.
The README's verbatim phrasing (local-first + offline + daily sales +
credit activity + expenses + physical closing counts + reconciliation
+ final Business Day closure + audit history + SQLite in folder) is
the **direct mirror** of LE31's daily-reconciliation + business-day-
closure flow on a different deployment surface (Windows desktop /
SQLite vs Linux server / Postgres / Telegram bot). The local-first
reconciliation terminal pattern has emerging peer traction in the
small-business Windows-desktop niche. **License status is the primary
blocker** for any future code-borrow question; if clarified to
MIT/Apache-2.0, the pick becomes Tier 0. **Reported plainly.**