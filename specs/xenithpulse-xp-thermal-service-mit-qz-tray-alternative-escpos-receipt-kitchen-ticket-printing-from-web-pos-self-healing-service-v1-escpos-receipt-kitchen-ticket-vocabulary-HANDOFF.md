# HANDOFF — 362-xenithpulse-xp-thermal-service-escpos-receipt-kitchen-ticket-print-boundary

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-23
**Active feature path**: `/opt/data/le31_mmm3_research/features/362-xenithpulse-xp-thermal-service-mit-qz-tray-alternative-escpos-receipt-kitchen-ticket-printing-from-web-pos-self-healing-service-v1-escpos-receipt-kitchen-ticket-vocabulary.md`
**LE31 feature gate verdict**: **defer** — LE31 v1 has no printer surface and no hardware posture. The peer value is the **print-chokepoint boundary** vocabulary, not adoption.

## Gate verdict (seven checks)

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | **FAIL** — no JTBD exists. LE31's owner has never asked for printing; no observed or reported pain. Evidence class: **assumed**. |
| 2 | Viability | **FAIL** — requires physical thermal-printer procurement and a driver path the non-technical owner cannot maintain alone. |
| 3 | Practicability | **PARTIAL** — ESC/POS is platform-independent and non-copyrightable (protocol primitive is reusable regardless of licence); the pick's *implementation* is TypeScript/Node.js/Windows-service = OFF-STACK. |
| 4 | Conflict | **OPEN CONFLICT** — server-side (this pick) vs client-side (feature 355, phone + Bluetooth). Both on file, unresolved. Also brushes §State: a dropped print must be an explicit operational state, never silent. |
| 5 | Outcome / scope | **NOT REACHED** — v1 surface, but only after gate 1 passes. |
| 6 | Cost to value | **FAVOURS DEFERRAL** — high pain frequency in principle, zero current demand; procurement cost is real and immediate. |
| 7 | Circuit breaker | **N/A for a defer.** Fully reversible: delete one file, nothing else depends on it. |

**Decision: defer.** Fails checks 1 and 2 outright; check 4 is a real unresolved conflict.

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build.

If the trigger condition is met — **any v1 PR proposing printer output of any kind, OR an offline-sync decision being opened** — the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-23.md`).
2. **Load feature 355 (`Haroon-World/RestaurantPOS_Android`) TOGETHER WITH this one.** Their HANDOFFs share the `backend/services/print_service.py` boundary. **Implementing either alone will fork the business logic per surface — the exact failure mode the pair exists to prevent.**
3. Resolve the server-side vs client-side conflict explicitly and in writing **before** any code. Do not pick a side implicitly by starting whichever is easier.
4. Read `xp-thermal-service`'s **service/supervisor** code, not its ESC/POS byte layer (already covered by features 348 and 355).
5. Re-run the seven-check gate with a real printer in hand and the owner's answer to the server-vs-client question.
6. If built: the print job must be an **append-only** `PrintJob` row (§3.3). **Retries must not be a mutable counter on that row** — §3.3 forbids it. Put retries in a separate table or do not implement retries.
7. Any print failure at service time must surface as an **explicit operational state**, never a silent Telegram drop (§State invariant, §3.4 observable evidence).

If the trigger condition is **not** met, do nothing.

## Files to touch

**None today.** If promoted to build (not recommended until trigger fires):
- `backend/services/print_service.py` — the single print chokepoint, shared with feature 355's design.
- A new `PrintJob` SQLModel table — append-only (§3.3).
- **Shared with feature 355** — read both HANDOFFs before touching either.

## Verification protocol reference

- **Parent-verified direct GET**: `https://api.github.com/repos/xenithpulse/xp-thermal-service` → HTTP 200, 2026-10-23. Confirms `stargazers_count=5`, `forks_count=3`, `size=1026`, `language=TypeScript`, `license.spdx_id=MIT`, `created_at=2026-03-19T16:57:44Z`, `pushed_at=2026-10-22T15:20:56Z`, `archived=false`, `fork=false`, 17 topics. **Read from `/repos/`, NOT from search-result numbers.**
- **Raw fetch**: `/tmp/le31-daily-2026-10-23/pv/xenithpulse_xp-thermal-service.json`
- **Anti-fabrication canary**: `grep -rcF 'LE31' /tmp/le31-daily-2026-10-23/` → 0 files with non-zero matches (parent-run). None of the upstream sources mention LE31.
- **Distinct-from-features**: verified 0 matches against all 349 pre-existing files in `features/`.

## Rollback path

Fully reversible. This is a vocabulary-only artifact — delete `features/362-*.md` and `specs/*359*-HANDOFF.md`, revert the commit. No runtime dependency, no schema, no migration, no retained data. Nothing else in the repo imports it.

## Mandatory LE31 skill list

- `le31-conventions` — seven-check gate, hard invariants (§3.1 stack, §3.3 append-only, §3.4 chokepoint + observable evidence, §State explicit transitions).
- `le31-research` — GitHub-as-source-of-truth discipline; verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON, never from search results.
- `le31-v1-feature-pattern` — canonical contract shape (informative: this is a v1-bucket pick).
- Do NOT load `le31-feature-pipeline` until this defer is promoted to build by the owner.