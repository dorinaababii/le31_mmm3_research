# Slice Contract — `isaac-cf-wong-wealthbraid-bsd-3-clause-local-first-ai-native-personal-wealth-manager-append-only-double-entry-ledger-stored-in-human-readable-files-v2-ai-local-first-append-only-ledger-discipline-vocabulary` (defer, parking-lot, vocabulary reference)

> **Active feature path:** `features/249-isaac-cf-wong-wealthbraid-bsd-3-clause-local-first-ai-native-personal-wealth-manager-append-only-double-entry-ledger-stored-in-human-readable-files-v2-ai-local-first-append-only-ledger-discipline-vocabulary.md`
> **Linear sub-issue:** [linear: blocked] (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — 10th consecutive day; intended project `le31 Research` P-HMM-1 [parent of v2-AI sub-issue because `le31 v2-AI` does NOT exist per le31-feature-pipeline/SKILL.md line 33]; intended label `Feature`; parent fallback at `/opt/data/le31-daily-research-2026-09-29.linear-fallback.json`)
> **Status:** defer (parking-lot, vocabulary reference; zero build time today)
> **Bucket:** v2-AI (ledger-discipline vocabulary)
> **Trigger condition:** the first v2 PR that proposes a local-first ledger layer, a double-entry `StockEntry` extension, a human-readable-file-storage export layer, or a per-asset audit-chain surface.

## Seven-check gate verdict

| Gate item | Verdict | Evidence |
|---|---|---|
| 1. License (charter §3.2) | **PASS** — BSD-3-Clause ✓ STRICTLY-COMPATIBLE | parent-verified GitHub API direct-GET 2026-09-29: `license.spdx_id = "BSD-3-Clause"` |
| 2. Stack fit (charter §3.1 + Python) | **PASS** — Python + local-first + append-only | description verbatim: *"local-first, AI-native personal wealth manager built on an append-only, double-entry ledger stored in human-readable files"* |
| 3. Customer-facing AI (charter §3.4) | **NOT TRIGGERED** — AI augments the owner, NOT the customer | description says "personal wealth manager" = owner-facing; wealth management is for the owner's personal finances, NOT for restaurant diners |
| 4. Stars (signal) | **WEAK** — 0★ | parent-verified GitHub API direct-GET: `stargazers_count = 0`; 0★ is a weak signal but the language is clear and + the repo is fresh (13-day-old); §3.2 STRICTLY-COMPATIBLE mitigates |
| 5. In-window (≤7 days) | **PASS** — by BOTH `created_at` (2026-09-16) AND `pushed_at` (2026-09-29 = TODAY) | parent-verified: 13-day-old repo with TODAY's NEW PUSH = strongest fresh-discovery signal of today's 3 picks |
| 6. LE31-shape-fit | **PASS** — append-only + double-entry + human-readable-file-storage vocabulary | the only in-window 2026 Python repo combining local-first + AI-native + append-only + double-entry + human-readable-file-storage primitives |
| 7. No observed pain | **DEFER** — no LE31 owner pain (v1 has no local-first + double-entry + human-readable-file-storage layer) | the artifact is vocabulary-only; trigger condition requires explicit owner/charter sign-off |
| **Final verdict** | **defer (parking-lot)** — vocabulary reference only | per le31-daily-research/SKILL.md hard rule "do not fabricate" + charter §3.1 + §3.4 invariants (v2 surface expansion + AI surface requires explicit owner/charter sign-off) |

## Files to touch (when triggered)

If a future v2 PR is triggered by the trigger condition above, the implementation would touch:
1. `backend/app/models/per_asset_audit_chain.py` (new file) — SQLModel schema for the `per_asset_audit_chain` table
2. `backend/app/models/double_entry_journal.py` (new file) — SQLModel schema for the `double_entry_journal` table
3. `backend/app/services/human_readable_ledger.py` (new file) — export service that writes the ledger to plain text files
4. `backend/app/services/ai_native_owner_assist.py` (new file) — AI-assist layer for the owner (charter §3.4 owner-facing-only)
5. `backend/app/routers/reconciliation.py` (modify) — add `/audit_chain` + `/double_entry_balance` + `/human_readable_file` endpoints
6. `backend/app/services/stock_entry.py` (modify) — add `double_entry_record()` method
7. `backend/app/services/audit_logs.py` (modify) — record every ledger export as an `audit_logs` entry
8. `tests/test_double_entry.py` (new file) — pytest tests for the double-entry discipline
9. `tests/test_human_readable_ledger.py` (new file) — pytest tests for the human-readable file export
10. `docs/ledger-discipline.md` (new file) — owner documentation for the ledger-discipline vocabulary

## Verification protocol reference

Per `verification-protocol/SKILL.md` (LE31 charter §3.5): every PR must pass:
1. `make test` — pytest full suite
2. `make lint` — ruff + mypy strict
3. `make type-check` — mypy --strict on all backend/app/**/*.py
4. `make smoke` — docker-compose up + curl health check
5. Manual: create a `StockEntry` decrement → verify the human-readable file is updated → verify the double-entry journal is balanced → verify the per-asset audit chain is replayable

## Rollback path

1. `git revert <commit-sha>` — single-commit revert
2. Drop the new tables (`per_asset_audit_chain`, `double_entry_journal`) — these are additive-only, no data loss
3. Delete the human-readable file directory — `rm -rf data/ledger_human_readable/`
4. Disable the AI-assist layer — `docker-compose stop ai-assist`

## Mandatory LE31 skill list

When the coding agent starts work on this feature, the load MUST consult these skills in order:
1. `le31-conventions` — project conventions + git workflow
2. `le31-v1-feature-pattern` — v1 feature contract template (v2 surface expansion must read v1 conventions too)
3. `le31-coding-agent-brief` — paste-in prompt template
4. `development` — full development pipeline (specify → plan → tasks → implement)
5. `speckit-implement` — task execution protocol
7. `pre-merge-review` — independent review before merge
8. `charter-3-4-review` — explicit §3.4 owner-facing-AI-only review before any AI surface is scoped

## Notes on the trigger

LE31 v1 today does NOT have a local-first + double-entry + human-readable-file-storage layer. The Postgres-backed `StockEntry` + `audit_logs` schemas are the source of truth. The local-first + double-entry + human-readable-file-storage primitive would add a parallel export layer that:
- Stores the same ledger in plain text files (one file per asset) that a human can read with `cat`
- Implements double-entry for every transaction (debit + credit)
- Provides an AI-assist layer for the owner (charter §3.4 owner-facing-only)

This is a substantial v2 surface expansion that requires explicit owner/charter sign-off per charter §3.1 + §3.4 invariants. The defer artifact documents the *vocabulary* so the next owner review can scope it properly.

## Out of scope reminder

The artifact is vocabulary-only. Do NOT:
- Implement the local-first + double-entry + human-readable-file-storage surface today
- Add new dependencies (the LE31 v1 stack is sufficient; no new deps required for vocabulary-only)
- Modify any v1 SQLModel schema
- Modify any v1 FastAPI router
- Modify any v1 aiogram bot handler
- Modify the audit_logs table
- Modify the StockEntry table
- Introduce any customer-facing AI surface (charter §3.4 explicit invariant)
- Introduce any v2 horizontal-expansion surface (charter §3.1 + §3.2 invariant)

If any of the above is requested, escalate to the owner for explicit charter §3.1 + §3.4 sign-off before any code change.

## v2-AI attachment note

Per `le31-feature-pipeline/SKILL.md` line 33 (verified 2026-08-28): the workspace contains only three projects — `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1 — and `le31 v2 owner-pains` and `le31 v2-AI` DO NOT EXIST. For this v2-AI-bucket pick, the sub-issue should be attached to `le31 Research` P-HMM-1 (where the parent research issue lives) and the report should say so. Do NOT silently invent a project, and do NOT report a project attachment that did not happen.