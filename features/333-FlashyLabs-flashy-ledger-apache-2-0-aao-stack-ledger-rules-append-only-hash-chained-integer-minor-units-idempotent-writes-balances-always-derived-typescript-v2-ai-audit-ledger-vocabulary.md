# Feature 333 — `FlashyLabs/flashy-ledger` Apache-2.0 v2-AI append-only-hash-chained-ledger-+-integer-minor-units-+-idempotent-writes-+-balances-always-derived-vocabulary (defer, parking-lot)

> **NEW observation (2026-10-17).** Documents in-window GitHub repo `FlashyLabs/flashy-ledger` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **★9/⑂0**, **TypeScript** (off-stack but the *open-ledger-rules* vocabulary IS portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 via a future v2-AI PR), **1596 KB modest**, `default_branch=main`, **pushed 2026-10-16T09:16:43Z = in-window by `pushed_at` (yesterday's push)**, **created 2026-08-12T00:32:28Z** = ~2-month-old repo with in-window `pushed_at` = IN-WINDOW BY `pushed_at` ONLY (`created_at` is OUT-OF-WINDOW by ~59 days before window-start), **archived=`False`**). **19 topics** (verbatim, parent-verified GitHub API direct-GET 2026-10-17 from `/tmp/le31-daily-2026-10-17/verify/ghverify_FlashyLabs_flashy-ledger.json`): `aao + agentic + agentic-ai + agentic-coding + agentic-commerce + agentic-engineering + agentic-framework + agentic-os + agentic-workflow + agentic-workflows + blockchain + blockchain-explorer + blockchain-technology + ledger + merkle + merkle-proof + merkle-root + merkle-tree + merkletree` = **most topic-rich v2-AI append-only-ledger candidate of the 78-pass series** (19 topics = highest topic count of any v2-AI append-only-ledger pick in the 78-pass series; the 4 merkle-related topics (merkle + merkle-proof + merkle-root + merkle-tree + merkletree) confirm the hash-chained-ledger discipline). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17): *⚡ The open ledger rules of the AAO Stack: append-only, hash-chained, integer minor units, idempotent writes, balances always derived. Flashy Gold is the first asset on the books. Apache-2.0 — npm install @flashylabs/ledger. The rules are open; the networks that run them live are products.*. The **open-ledger-rules-of-the-AAO-Stack + append-only + hash-chained + integer minor units + idempotent writes + balances always derived** sextuple-primitive + the **append-only + hash-chained + integer minor units + idempotent writes + balances always derived** discipline (a ledger is a strict-rules-of-the-ledger machine: every entry is append-only; every entry is hash-chained to the previous entry via a merkle tree; every amount is in integer minor units (no floats); every write is idempotent (replays are safe); every balance is always derived from the entries (no separate balance field)) = the **canonical v2-AI append-only-hash-chained-ledger-rules-vocabulary of the 78-pass series**. Bucket: **v2-AI (parking-lot, vocabulary reference)** — Pick B of Daily Research 2026-10-17. Build verdict: `defer` (parking-lot, vocabulary-only). Zero build time today.

## Goal

Retain the **open-ledger-rules-of-the-AAO-Stack + append-only + hash-chained + integer minor units + idempotent writes + balances always derived** discipline as a persistent cross-section reference for the LE31 v2-AI *append-only-hash-chained-ledger-rules* surface, and document the **integer minor units** discipline (a EUR ledger must use integer minor units = cents, NOT floats) that an independent maintainer arrived at in 2026 (2-month-old repo with yesterday-push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **open-ledger-rules-of-the-AAO-Stack + append-only + hash-chained + integer minor units + idempotent writes + balances always derived** sextuple-primitive: (1) *open-ledger-rules* (the rules of the ledger are open-source; the networks that run the ledger live are products); (2) *append-only* (every entry is append-only; no updates; no deletes); (3) *hash-chained* (every entry is hash-chained to the previous entry via a merkle tree; tamper-evident); (4) *integer minor units* (every amount is in integer minor units; no floats; cents not euros); (5) *idempotent writes* (every write is idempotent; replays are safe); (6) *balances always derived* (every balance is always derived from the entries; no separate balance field)
- A written record of the **append-only + hash-chained + integer minor units + idempotent writes + balances always derived** discipline applied to the *ledger* dimension: a *ledger* is a strict-rules-of-the-ledger machine with 5 immutable rules; the *integer minor units* rule is the only one that is *charter §3.6 EUR-accounting* directly relevant (LE31 v1 already uses `decimal.Decimal` for EUR; integer minor units = cents would be stricter = no float-rounding error even at the decimal level)
- A written record of the **AAO Stack** (Agentic Agentic Operations) posture: the ledger is the foundation of an agentic-commerce stack; the *agentic-commerce* posture IS the §3.4 *chokepoint-governed* charter invariant applied to the *AI-agent-commerce* dimension (every AI-agent commerce action is recorded in the ledger for tamper-evidence)
- A decision record: today's verdict is `defer (vocabulary-only, v2-AI append-only-hash-chained-ledger-rules with §3.4 review)` because (1) LE31 v1 charter explicitly scopes the v1 architecture to one small restaurant and excludes AI surface per charter §3.4 "no customer-facing AI"; (2) the *append-only + hash-chained + integer minor units + idempotent writes + balances always derived* primitive IS a v2-AI owner-tooling surface that requires §3.4 review; (3) the *integer minor units* discipline is directly applicable to LE31 v1's EUR-accounting (a v1 PR could adopt the *integer minor units* discipline today without §3.4 review); (4) the *AAO Stack* + *agentic-commerce* posture is a v2-AI forward-looking vocabulary

**Out of scope (defer artifact):**

- Any change to LE31 v1 (charter explicitly scopes the v1 architecture to one small restaurant; the v1 surface has no AI surface)
- Any change to LE31 v2-AI surface today (charter §3.4 not yet triggered for v2-AI; the v2-AI bucket exists in the skill file but does NOT exist as a Linear project per today's confirmed workspace-state — only 3 projects exist: `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research`)
- **Adoption of the `flashy-ledger` codebase — explicitly NOT adopted because the codebase is TypeScript (off-§3.1 stack) + requires a JavaScript runtime (not on the LE31 v1 stack) which would require §3.1 + §3.2 charter review before adoption**
- Cross-pollination with the *merkle-tree* surface (charter §3.3 §3.3 ✓ = the existing v1 `audit_logs` is append-only; the merkle-tree discipline would extend §3.3 to hash-chained-evidence; a v1 PR could add a merkle-tree column to `audit_logs` without §3.4 review)

## Evidence / JTBD

When a future LE31 v2-AI surface proposes *"the append-only-hash-chained-ledger surface that lets the owner use integer minor units + idempotent writes + balances always derived for owner-assistant AI-agent commerce"*, the owner wants *a primitive that proves this append-only + hash-chained + integer minor units + idempotent writes + balances always derived pattern is real and well-tested in 2026*, but struggles because *LE31 has no documented evidence that "append-only + hash-chained + integer minor units + idempotent writes + balances always derived" is a real reference ledger-rules pattern*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the open-ledger-rules pattern"*.

- **Evidence class**: observed (the description names the primitives explicitly: `append-only + hash-chained + integer minor units + idempotent writes + balances always derived`)
- **Confidence**: medium-high for the append-only-hash-chained-ledger-rules-vocabulary match (the verbatim description names the 6-primitive set); medium for transferability (TypeScript off-§3.1 but the *integer minor units + idempotent writes + balances always derived* rules are vocabulary-portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 via stdlib `decimal.Decimal` + `hashlib` + `tiktoken` only)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has no AI surface; the v2-AI bucket is not yet open; the existing v1 `payment-tip-reconciliation` (feature 05) + `per-recipe-cost-margin-rollup` (feature 74) already use `decimal.Decimal` for EUR-accounting = the *integer minor units* discipline would be a STRICTER primitive = no float-rounding error even at the decimal level); the value is the **append-only + hash-chained + integer minor units + idempotent writes + balances always derived** vocabulary — when the first v2-AI owner-assistant PR lands, the `flashy-ledger` pattern is a ready-made *named append-only-hash-chained-ledger-rules-primitive*

## Description

GitHub `FlashyLabs/flashy-ledger` (Apache-2.0, ★9/⑂0, TypeScript, 1596 KB modest, pushed 2026-10-16T09:16:43Z = in-window by `pushed_at`, created 2026-08-12T00:32:28Z = 2-month-old repo with in-window push). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17):

> *⚡ The open ledger rules of the AAO Stack: append-only, hash-chained, integer minor units, idempotent writes, balances always derived. Flashy Gold is the first asset on the books. Apache-2.0 — npm install @flashylabs/ledger. The rules are open; the networks that run them live are products.*

The append-only-hash-chained-ledger-rules primitive has 6 distinct sub-primitives that map 1:1 onto the LE31 v2-AI *append-only-hash-chained-ledger-rules* surface:

1. **Open-ledger-rules-of-the-AAO-Stack** — the rules of the ledger are open-source; the networks that run the ledger live are products; the *open-rules + products-on-top* posture IS the §3.2 *dependency-surface-minimization* charter invariant applied to the *ledger-rules* dimension (the rules are open = no vendor lock-in; the products are optional = the rules are the primitive)
2. **Append-only** — every entry is append-only; no updates; no deletes; the *append-only* posture IS the §3.3 *audit-log-immutability* charter invariant applied to the *ledger-entry* dimension (LE31 v1 `StockEntry` + `audit_logs` are already append-only = the *append-only* primitive is already implemented in v1)
3. **Hash-chained** — every entry is hash-chained to the previous entry via a merkle tree; tamper-evident; the *hash-chained* posture IS the §3.3 *audit-log-immutability* charter invariant applied to the *ledger-entry-tamper-evidence* dimension (LE31 v1 `audit_logs` is NOT hash-chained today; a v1 PR could add a `merkle_root` column without §3.4 review)
4. **Integer minor units** — every amount is in integer minor units; no floats; cents not euros; the *integer minor units* posture IS the §3.6 *EUR-accounting-exactness* charter invariant applied to the *ledger-amount* dimension (LE31 v1 already uses `decimal.Decimal` for EUR; integer minor units = cents would be STRICTER = no float-rounding error even at the decimal level; a v1 PR could adopt the *integer minor units* discipline today)
5. **Idempotent writes** — every write is idempotent; replays are safe; the *idempotent writes* posture IS the §3.1 *explicit-state-transition* charter invariant applied to the *ledger-write-replay-safety* dimension (LE31 v1 `StockEntry` writes are already idempotent at the database level via primary-key constraints; the *idempotent writes* primitive is already implemented in v1)
6. **Balances always derived** — every balance is always derived from the entries; no separate balance field; the *balances always derived* posture IS the §3.3 *audit-log-immutability* charter invariant applied to the *ledger-balance-derivation* dimension (LE31 v1 `StockEntry` + `SUM(qty_delta)` derives current stock; the *balances always derived* primitive is already implemented in v1)

**The 1:1 mapping onto LE31 v1 + v2-AI surface:**

| `flashy-ledger` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Open-ledger-rules-of-the-AAO-Stack | `LE31 LedgerRules` config (Python+FastAPI+Postgres+SQLModel+aiogram v3) | §3.2 | **Implemented (v1)** — exact match; the v1 `StockEntry` + `audit_logs` are the open-rules-of-the-ledger |
| Append-only | `StockEntry` + `audit_logs` tables (append-only) | §3.3 | **Implemented (v1)** — exact match; v1 §3.3 invariant |
| Hash-chained | `audit_logs.merkle_root` column (proposed) | §3.3 | **Not implemented** — v1 PR candidate (no §3.4 review needed) |
| Integer minor units | `decimal.Decimal` for EUR-accounting + (proposed) integer minor units | §3.6 | **Partial (v1)** — v1 uses `decimal.Decimal`; integer minor units = cents would be stricter; v1 PR candidate (no §3.4 review needed) |
| Idempotent writes | `StockEntry` primary-key constraint + `audit_logs` primary-key constraint | §3.1 | **Implemented (v1)** — exact match; v1 §3.1 invariant |
| Balances always derived | `SUM(qty_delta)` for current stock + `SUM(amount)` for current balance | §3.3 | **Implemented (v1)** — exact match; v1 §3.3 invariant |
| **ACTUAL implementation** | flashy-ledger codebase (TypeScript + npm + merkle-tree) | §3.1 + §3.2 | **NOT adopted** — vocabulary-only; the open-rules + integer-minor-units + idempotent-writes + balances-always-derived primitives ARE adopted; the merkle-tree + hash-chained discipline is a v1 PR candidate; the TypeScript codebase itself is OFF-§3.1 |
| **Future re-implementation** | v2-AI owner-tooling in Python + FastAPI + Postgres + SQLModel + aiogram v3 + hashlib + tiktoken | §3.1 + §3.2 + §3.4 | **Future v2-AI PR target** |

## Data model

This defer artifact does NOT modify any LE31 data model. The data model below describes the **vocabulary reference only**, not an actual v2-AI implementation:

- `AuditLogMerkleRoot` (id, root_hash: str, computed_at: datetime, entry_count: int) — vocabulary reference: a SQLModel table that records each merkle-root-computation (APPEND-ONLY; §3.3 invariant; v1 PR candidate)
- `AuditLogEntry` (id, audit_log_id, entry_hash: str, parent_hash: str, entry_data: JSON, entry_recorded_at: datetime) — vocabulary reference: a SQLModel table that records each hash-chained entry (APPEND-ONLY; §3.3 invariant; v1 PR candidate; would extend the existing `audit_logs` table with `entry_hash` + `parent_hash` columns)
- `LedgerBalance` (id, account_id, balance_minor_units: int, balance_derived_at: datetime, balance_source_entry_count: int) — vocabulary reference: a SQLModel table that records each derived balance (VIRTUAL; the balance is always derived from the entries; no separate balance field; v1 already does this via `SUM(qty_delta)` + `SUM(amount)`)

All tables would require §3.3 (append-only + hash-chained) + §3.6 (integer minor units) charter review before adoption; no §3.4 review needed for the v1 PR candidates (the v1 PR candidates are non-AI primitives).

## Implementation steps

This is a defer artifact (vocabulary-only). No implementation today. The 3 placeholder steps below document the future-v1 + v2-AI re-implementation path:

1. **Defer (vocabulary-only today)** — file the contract; no code change
2. **Re-evaluate at first v1 PR that proposes merkle-tree-extension to `audit_logs`** — when a future v1 PR proposes adding a `merkle_root` column to `audit_logs` for tamper-evidence, the `flashy-ledger` pattern is a ready-made *named append-only-hash-chained-ledger-rules-primitive*; re-run the LE31 feature gate (no §3.4 review needed for v1 PR)
3. **Re-implement in Python+FastAPI+Postgres+SQLModel+aiogram v3** — if the future v1 PR adopts the `flashy-ledger` vocabulary, re-implement from scratch in the LE31 v1 stack (Python+FastAPI+Postgres+SQLModel+aiogram v3 + stdlib `hashlib` + stdlib `tiktoken`); do NOT add `flashy-ledger` to `requirements.txt`; design the v1 surface as a fresh Python+FastAPI+Postgres+SQLModel+aiogram v3 implementation that captures the *open-ledger-rules + append-only + hash-chained + integer minor units + idempotent writes + balances always derived* primitives

## Telegram interaction

This defer artifact does NOT add any Telegram interaction today. The future v2-AI append-only-hash-chained-ledger-rules surface would add Telegram commands (operator-tooling; charter §3.4 NOT triggered for the owner-bot exposure; charter §3.4 RIPGL_REVIEW REQUIRED if any Telegram-client exposure is added to restaurant diners):

- `/ai-ledger show <audit_log_id>` — owner shows the audit-log-merkle-root
- `/ai-ledger verify <audit_log_id>` — owner verifies the merkle-root against the entries
- `/ai-ledger balance <account_id>` — owner shows the derived balance
- `/ai-ledger writes show <write_id>` — owner shows the idempotent-write record

## Dependencies

- **No new LE31 v1 dependencies** — this is a vocabulary-only defer artifact; the *integer minor units* + *idempotent writes* + *balances always derived* primitives are already implemented in v1
- **Future v1 PR dependencies** (would require §3.3 + §3.6 charter review; NO §3.4 review needed):
  - stdlib `hashlib` (already on v1 stack)
  - stdlib `decimal.Decimal` (already on v1 stack)
- **Future v2-AI re-implementation dependencies** (would require §3.1 + §3.2 + §3.4 charter review):
  - stdlib `hashlib` (already on v1 stack)
  - stdlib `tiktoken` (for token-aware-ledger discipline; OFF-§3.2 = explicit charter-decision needed)
  - stdlib `cryptography` (for hash-chained-audit-ledger discipline; OFF-§3.2 = explicit charter-decision needed)
- **Sister-shape** via the v2-AI append-only-hash-chained-ledger-rules-vocabulary cluster:
  - features 187 + 188 (`traust-security/traust-ledger` 30th-consecutive-day NEW PUSH = longest sustained-discovery signal of the 78-pass series)
  - features 232 (`lpalbou/AbstractGateway` HTTP control plane for durable AI runs + append-only ledger + Telegram surface)
  - features 287 (`noise01/endoxa` governed-beliefs + append-only-ledger + SMT-checked-consistency)
  - features 288 (`pete-builds/mcp-nixreview` MCP-server + CVE/KEV-attestation-gate + append-only-audit-ledger)
  - features 289 (`shivamk01here/LedgerLoop` Python-runtime + hash-chained-audit-ledger + 760+ tests)
  - features 298 (carry-over from 10-13 `the-vibey-project/vibey` agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger)
  - features 302 (`warrant-ai/warrant` decision-ledger)
  - features 303 (carry-over from 10-11 `Bastardki11er/tally` double-entry-ledger)
  - features 304 (carry-over from 10-11 `DSHCorrectover/agent-second-fuse` fail-closed-second-fuse)
  - features 327 (carry-over from 10-16 `musterhq/muster` agent-harness-with-audit-ledger-+-token-waste-ledger)
  - features 328 (carry-over from 10-16 `themanoj-025/Dabba` in-domain-restaurant-intelligence)
  - features 330 (carry-over from 10-16 `AXIOVEX/axiomere-python` truth-ledger + append-only + signed-hash-chained)
  - features 332 (today's `vsov/xcheck` cross-agent-audit-methodology)
  - features 334 (today's `donaldrichard19-LVD/pattern-mcp` MCP-server-with-auditable-decision-ledger)

## Open questions

- **Could the existing v1 `audit_logs` table be extended with `entry_hash` + `parent_hash` columns for hash-chained-evidence?** This is the cheapest path; a v1 PR could add the columns and reuse the existing append-only primitive; no §3.4 review needed
- **Could the existing v1 `decimal.Decimal` EUR-accounting be replaced with integer minor units (cents)?** The migration is straightforward (multiply all EUR amounts by 100, store as int); but it would require a charter §3.6 review + a data-migration plan
- **Should the `flashy-ledger` AAO Stack be adopted as a reference architecture for any v2-AI commerce surface?** The AAO Stack is a forward-looking v2-AI commerce posture; LE31 has no commerce surface today; the v2-AI commerce surface would adopt the AAO Stack as the open-ledger-rules foundation
- **What is the relationship between the `flashy-ledger` open-rules and the LE31 v1 `StockEntry` + `audit_logs` schema?** The `flashy-ledger` rules are vocabulary-portable to LE31 v1; a v1 PR could adopt the *open-rules* + *integer minor units* + *idempotent writes* + *balances always derived* disciplines without adding any new dependency

## Why this matters

This is the **canonical v2-AI append-only-hash-chained-ledger-rules-vocabulary of the 78-pass series**. The 6-rule *open-ledger-rules-of-the-AAO-Stack* discipline is a unique cross-section reference that no other v2-AI pick in the 78-pass series captures. The transferability to LE31 v1 is high (4 of 6 rules are already implemented in v1; 2 rules are v1 PR candidates); the transferability to LE31 v2-AI is high (the 6 rules are vocabulary-portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 + stdlib `hashlib` + stdlib `decimal.Decimal`); the cost is low (vocabulary-only artifact, no code today); the trigger condition is clear (first v1 PR that proposes merkle-tree-extension OR first v2-AI surface that wants open-ledger-rules). Per the 9-feature-pipeline-rule + the 77+ passes of consistency, parking-lot `defer` is the verdict. The artifact is the persistent cross-section reference for any future v1 PR that proposes merkle-tree-extension OR any future v2-AI PR that proposes open-ledger-rules. LE31 v2-AI surface is not yet open. All ripgrep-verified unique vs features 1..331. **Fully reversible** (vocabulary-only artifact).
