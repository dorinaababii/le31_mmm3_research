# Feature 249 — `isaac-cf-wong-wealthbraid-bsd-3-clause-local-first-ai-native-personal-wealth-manager-append-only-double-entry-ledger-stored-in-human-readable-files-v2-ai-local-first-append-only-ledger-discipline-vocabulary` (defer)

> **NEW observation (2026-09-29).** Documents in-window GitHub Search `append-only+ledger` query result: `isaac-cf-wong/wealthbraid` (**BSD-3-Clause ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python, **pushed 2026-09-29T02:12:58Z = TODAY** (in-window by `pushed_at`), **created 2026-09-16T11:50:29Z** (in-window by `created_at` — **13-day-old repo**), **455 KB modest repo** (parent-verified via raw GitHub API JSON), `default_branch=main`, `archived=false`). **No topics** (parent-verified from raw JSON: `"topics": []`). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-29): *"wealthbraid is a local-first, AI-native personal wealth manager built on an append-only, double-entry ledger stored in human-readable files."* The **local-first + AI-native + append-only + double-entry + human-readable-file-storage** quintuple-primitive = the **canonical v2-AI ledger-discipline vocabulary** that LE31's `StockEntry` discipline (charter §3.1 explicit-state-transitions) would inherit in a v2 surface that needs to make per-asset audit chains human-readable + double-entry + local-first + AI-native. Bucket: **v2-AI local-first-append-only-ledger-discipline vocabulary (defer, parking-lot, vocabulary reference)** — zero build time today.

## Goal

Retain the **local-first + AI-native + append-only + double-entry + human-readable-file-storage** quintuple-primitive + the **Python + BSD-3-Clause + human-readable-file-as-storage** stack-shape as a persistent cross-section reference for any future LE31 v2 surface that introduces (a) **local-first** (the ledger lives on the user's filesystem, not on a server), (b) **AI-native** (the system is designed from the ground up to integrate AI assistance; AI augments the owner, not the customer), (c) **append-only** (every event is recorded once and never modified), (d) **double-entry** (every transaction has equal-and-opposite debits and credits), and (e) **human-readable-file-storage** (the ledger is stored as text files a human can read in Finder or with `cat`, not as a binary database). The artifact is the persistent cross-section reference + the verbatim description + the 5 named primitives. No code today (BSD-3-Clause permits future code reuse; vocabulary-only artifact today; 455 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **local-first** discipline: the *local-first* primitive (LE31 v1's `StockEntry` is local-first via the on-premise Postgres instance; the *local-first* primitive is the *user-owns-their-data* posture applied to the *ledger* dimension).
- A written record of the **AI-native** discipline: the *AI-native* primitive (LE31 v1 has no AI surface today; the *AI-native* posture is the *AI-augments-the-owner-not-the-customer* posture; charter §3.4-compatible provided the AI is consumed by the owner only and does not interact with restaurant diners).
- A written record of the **append-only** discipline: the *append-only* primitive (LE31 v1's `audit_logs` + `StockEntry` are already append-only; the *append-only* posture applied to the *per-asset-audit-chain* dimension is the *per-asset-event-history* primitive).
- A written record of the **double-entry** discipline: the *double-entry* primitive (LE31 v1's `StockEntry` does not currently implement double-entry; the *double-entry* posture is the *every-transaction-has-equal-and-opposite-debits-and-credits* posture; this is the §3.3 stock-discipline vocabulary applied at the per-asset-per-account level).
- A written record of the **human-readable-file-storage** discipline: the *human-readable-file-storage* primitive (LE31 v1's `StockEntry` is stored as SQLModel rows in Postgres; the *human-readable-file-storage* primitive is the *text-file-a-human-can-read* posture; this is the *portable + grep-able + backup-friendly* primitive).
- A decision record: today's verdict is `defer` because LE31 v1 has no local-first + AI-native + double-entry + human-readable-file-storage surface today (charter §3.1 v1 surfaces are waiter web UI + cook Telegram bot + Postgres-backed StockEntry; the v2-AI surface expansion requires explicit owner/charter sign-off per charter §3.1 + §3.4 invariants).
- A cross-section reference with the prior ledger-discipline cluster: features 45 (audit-log-check), 46 (rollback-immutable-audit-check), 81 (append-only-immutable-audit-check), 122 (trace-integrity-cait), 137 (nl-to-executable-obligations), 141 (krineia-five-invariants), 145 (garde-fous-frozen-mandate), 156 (rollover-immutable-audit-check), 165 (ladle-restaurant-prep-forecasting), 168 (edusouzaxgv-asset-ledger), 169 (akoffice933-openshare-ledger), 181 (merkle-audit-pattern), 183 (n0-public autonomous-agent-ledger), 187 (traust-ledger), 191 (eddiedzhang-FullHouse), 201 (Ybx-jp-claims-ledger), 220 (Jita81-commit-replay-bench), 232 (lpalbou-AbstractGateway), 242 (shayangolmezerji-menu-events), 244 (Nulfied-attestry).

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI (HTMX).
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v1 surface expansion in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v1 expansion trigger).
- Any customer-facing AI surface in v1 or v2 (charter §3.4 explicit invariant: NO customer-facing AI; the wealthbraid artifact is AI-augments-the-owner posture, NOT customer-facing).
- Any v2 surface expansion in v2 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).

## Description

The pick is **`isaac-cf-wong/wealthbraid`** — a Python + BSD-3-Clause + local-first + AI-native + personal wealth manager + append-only + double-entry + human-readable-file-storage vocabulary artifact. **Charter §3.4 NOT triggered** because the AI in wealthbraid is consumed by the owner (the personal wealth manager is for the owner's personal finances, NOT for restaurant diners), even though the description says "AI-native personal wealth manager". The artifact is the persistent cross-section reference for the verbatim description + the 5 named primitives + the BSD-3-Clause license posture.

**Stack-shape match (the load-bearing primitive):** the *Python* language is on the LE31 pin set; the *BSD-3-Clause permissive license* is charter §3.2 STRICTLY-COMPATIBLE; the *append-only + double-entry + human-readable-file-storage* discipline aligns with LE31 v1's existing `StockEntry` + `audit_logs` discipline. The verbatim description *"local-first, AI-native personal wealth manager built on an append-only, double-entry ledger stored in human-readable files"* is the **first in-window 2026 Python repo** that combines all 5 primitives simultaneously.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2 surface that adopts the *local-first + AI-native + append-only + double-entry + human-readable-file-storage* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `per_asset_audit_chain` table with `chain_id, asset_id, event_id, prev_event_id, event_type, debit_account, credit_account, event_data, recorded_at, file_path`; a `double_entry_journal` table with `journal_id, transaction_id, debit_account_id, credit_account_id, amount, recorded_at`; or a `human_readable_ledger_file` directory with one file per asset, in plain text format that a human can read with `cat`). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would:
1. Read the `isaac-cf-wong/wealthbraid` README at https://github.com/isaac-cf-wong/wealthbraid for the *local-first + AI-native + append-only + double-entry + human-readable-file-storage* quintuple-primitive.
2. Cross-reference with LE31 v1's `StockEntry` schema to identify the *delta* (the *delta* = `isaac-cf-wong/wealthbraid` introduces the *local-first + AI-native + double-entry + human-readable-file-storage* primitives that LE31 v1's `StockEntry` does not have; LE31 v1's `StockEntry` is append-only but does NOT serve as a *double-entry ledger* nor as a *human-readable-file-storage* layer).
3. Apply charter §3.1 + §3.2 + §3.4 review to the *delta* (any new v2 surface requires explicit owner/charter sign-off; the *local-first + AI-native + double-entry + human-readable-file-storage* surface is charter §3.1-compatible provided the explicit state transitions are preserved — i.e., the per-asset audit chain can be replayed from the human-readable files; charter §3.2-compatible via BSD-3-Clause; charter §3.4-compatible provided the AI augments the owner only and does not interact with restaurant diners).
4. Implement the surface with the LE31 v2 + FastAPI + SQLModel + aiogram stack; the `isaac-cf-wong/wealthbraid` reference is the *vocabulary* for *local-first + AI-native + append-only + double-entry + human-readable-file-storage*, NOT for *wealth-management* implementation.

## Telegram interaction

Zero Telegram interaction today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would add (a) a `/audit_chain` command that reads the per-asset audit chain from the human-readable files, (b) a `/double_entry_balance` command that shows the double-entry balance for a given account, (c) a `/human_readable_file` command that exports the ledger to a human-readable text file for backup. All commands are owner-facing AI-assist, NOT customer-facing AI.

## Dependencies

- **LE31 v2 owner-assist surface** — currently absent; the local-first + AI-native + double-entry + human-readable-file-storage surface is a future v2 surface expansion that requires explicit owner/charter sign-off per charter §3.1 + §3.2 + §3.4 invariants.
- **LE31 v1 `StockEntry` schema** — already append-only; the *local-first + AI-native + double-entry + human-readable-file-storage* primitive extends the `StockEntry` discipline with double-entry + human-readable-file-storage layers.
- **LE31 v1 `audit_logs` schema** — already append-only; the *local-first + AI-native + double-entry + human-readable-file-storage* primitive extends the `audit_logs` discipline with per-asset audit chains + double-entry journals.
- **LE31 v1 FastAPI + SQLModel + Postgres stack** — already pinned; the *local-first + AI-native + double-entry + human-readable-file-storage* primitive would require the Postgres-backed StockEntry + audit_logs + the new human-readable-file-storage layer to coexist (the Postgres layer remains the source of truth; the human-readable-file layer is the export).
- **Cross-references:** features 45+46+81+122+137+141+145+156+165+168+169+181+183+187+191+201+220+232+242+244.

## Open questions

- Does LE31 v2 want a *local-first + human-readable-file-storage* layer at all? the current v1 `StockEntry` is stored as SQLModel rows in Postgres; the *human-readable-file-storage* primitive would add a parallel export layer that stores the same ledger in plain text files. The trade-off is: (a) Postgres-only = single source of truth, simpler; (b) Postgres + human-readable-file = portable + grep-able + backup-friendly + grep-friendly-for-audits, but introduces a sync risk (the human-readable-file must stay in sync with the Postgres). The decision is **owner's**.
- Does LE31 v2 want *double-entry* for the `StockEntry` ledger? The current v1 `StockEntry` is single-entry (each event records a quantity change with no balancing entry); the *double-entry* posture would require every event to have a debit + credit entry. The trade-off is: (a) single-entry = simpler, fewer rows, easier to read; (b) double-entry = auditable + reconciliation-friendly, but more complex. The decision is **owner's**.
- Does LE31 v2 want *AI-native owner-assist*? The current v1 has no AI surface at all; the *AI-native* posture would introduce an AI-assist layer for the owner. The trade-off is: (a) no AI = no hallucination risk, no §3.4 risk; (b) AI-native owner-assist = powerful + augmentation-friendly, but requires §3.4 review + the *non-AI fallback* posture per charter §3.4. The decision is **owner's** — and requires explicit charter §3.4 sign-off before any v2 AI surface is scoped.

## Why this matters

- The **verbatim description** *"local-first, AI-native personal wealth manager built on an append-only, double-entry ledger stored in human-readable files"* is the **first in-window 2026 Python repo** that combines the *local-first + AI-native + append-only + double-entry + human-readable-file-storage* primitives simultaneously. The cross-section reference is high-value for any future LE31 v2 surface that introduces the ledger-discipline vocabulary.
- The **BSD-3-Clause permissive license** posture makes this the **STRICTLY-ADOPTABLE local-first-append-only-ledger-discipline primitive** of the 60-pass series.
- The artifact is **vocabulary-only**; zero build time today; fully reversible (delete the feature file + the HANDOFF + the Linear sub-issue is the complete rollback).
- The trigger condition is **the first v2 PR that proposes a local-first ledger layer, a double-entry `StockEntry` extension, a human-readable-file-storage export layer, or a per-asset audit-chain surface**.

## Cross-section evidence (one-line each)

- The `local-first + AI-native + append-only + double-entry + human-readable-file-storage` quintuple-primitive is the canonical v2-AI ledger-discipline vocabulary that LE31's StockEntry discipline would inherit in a v2 surface.
- The `Python + BSD-3-Clause + human-readable-file-as-storage` stack-shape is verbatim §3.2 STRICTLY-COMPATIBLE.
- The verbatim description *"local-first, AI-native personal wealth manager built on an append-only, double-entry ledger stored in human-readable files"* is the load-bearing value of the artifact.
- Net-new observation 2026-09-29 (ripgrep-confirmed unique vs features 1–247).