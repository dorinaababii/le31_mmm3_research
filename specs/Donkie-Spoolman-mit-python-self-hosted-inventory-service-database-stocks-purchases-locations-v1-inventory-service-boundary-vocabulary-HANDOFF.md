# HANDOFF — Feature 371: `Donkie/Spoolman` — inventory-service-as-a-separate-boundary vocabulary

**Upstream source repo: [`Donkie/Spoolman`](https://github.com/Donkie/Spoolman)** — see `features/371-Donkie-Spoolman-mit-python-self-hosted-inventory-service-database-stocks-spools-purchases-locations-v1-inventory-service-as-a-separate-boundary-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/371-Donkie-Spoolman-mit-python-self-hosted-inventory-service-database-stocks-spools-purchases-locations-v1-inventory-service-as-a-separate-boundary-vocabulary.md` — defer/parking-lot (Pick B of Daily Research 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | When the owner wants the stock ledger to be consumable outside the LE31 process, they want *a separate service*, but LE31 has **no reported need** for a second consumer and no reported pain with a monolith — evidence class **inferred**. **A failing check 1 is what makes this a defer.** |
| 2 | Viability | ✓ | MIT ✓ §3.2 STRICTLY-COMPATIBLE, **★2932/⑂308**, 8,827 KB, Python on-stack. **Traction caveat recorded plainly: this is traction for 3D-printer filament inventory — NOT for restaurant software and NOT for LE31's problem.** A star count is not a demand signal. The *cost* side (171 open issues) is the more useful number. |
| 3 | Practicability and confidence | ✓ | On-stack (Python service + database). **But the domain shift is severe**: filament has no expiry, no FEFO, no prep-batch, no kitchen; §4.3's `StockEntry` reasons (`initial`, `sale`, `sold_out`, `waste`, `restock`) have **no counterpart** in a filament store. **Do not read this repo as a model of LE31's stock semantics** — it models the *deployment* shape and the *derivation* discipline only. Evidence strength: high for the derivation discipline (§4.3), low for domain applicability. |
| 4 | Conflict | ✓ | No invariant is violated by the *documentation*. **But adopting the shape WOULD conflict**: a second long-running process is a §3.5 deployment decision, and §3.2 explicitly prefers "single VPS + systemd unit" with no Docker. §3.2 also excludes multi-location — the reference's `Location` concept must not leak into v1. |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Maximum time worth spending: **45 min documentation**. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is **the negative result**: the shape works and does not pay at LE31's scale (one restaurant vs a ★2932 project with 171 issues). Roughly 45 min of documentation; no build. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. If ever built, the feature-removal path is: stop the service, drop its schema, restore the monolith's direct read of the same ledger. |

**Gate verdict: `defer` (parking-lot)** — check 1 fails on evidence class. The reference's value is its **cost**, which makes the defer decision explicit rather than implicit.

## Bucket

**v1 (inventory-service-as-a-separate-boundary vocabulary)** — Pick B of Daily Research 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — today's confirmed workspace state is exactly 3 projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1); `le31 v2 owner-pains` and `le31 v2-AI` **do not exist**. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload.

## Files to touch

**None today.** Documentation-only.

If the owner ever needs a second consumer of the stock ledger, the expected files are:

- `backend/services/stock_service.py` — the derivation itself: `batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)`, computed on read, never stored. **This function already exists conceptually; the change would be its *transport*, not its logic.**
- `backend/app/models.py` — `stock_entry` / `batch` — **read-only audit**: confirm no `qty_remaining` column is persisted. **This is the load-bearing check of any future build.** A stored `qty_remaining` would break §4.3 and must be derived, not cached.
- `backend/main.py` — mount the service boundary **only if** a real second consumer exists. A service boundary with one consumer is an operational cost with no benefit.
- `bot/handlers/stock_handlers.py` — the **cook bot's stock calls must degrade gracefully** if the service is unreachable: a degraded bot that cannot reach the stock service **must still accept orders** (see feature 370's "no required outbound calls" rule).
- `deploy/` or the systemd unit — a second long-running process. **⚠️ §3.2 prefers a single unit; this needs an explicit owner decision.**
- `tests/test_stock_derivation.py` — **the load-bearing test**: assert that `qty_remaining` is never written, only derived, and that the derivation equals the sum of entries after a duplicate entry is rejected.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. The observable behaviour is **the bot still taking orders when the stock path is degraded**: stop the stock service, take an order through the Telegram cook surface, and confirm the order is accepted and the kitchen sees it. That degraded-mode exercise — not the happy path — is the thing a service boundary actually changes.

## Rollback path

`git rm features/371-*.md specs/Donkie-Spoolman-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Stock* and *State* rules first)
- `le31-data` — append-only ledger rules (`StockEntry`: never update or delete; current stock derived)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.1, §3.2, §3.5, §4.3)

## Open questions carried into any future build

1. **Would LE31 ever split the stock ledger into its own service?** Unmade. Nothing has asked for it. Recorded because this reference shows both the shape *and* its price (171 open issues).
2. **Does the cook bot degrade gracefully if a stock service is unreachable?** Unanswerable today (no such service). If feature 370's "no required outbound calls" rule is adopted, this becomes a design constraint to write down.
3. **What is the real cost of the derived-projection discipline at LE31's scale?** Unknown. LE31 has one restaurant, one kitchen, and perhaps a few hundred entries a day — far below the scale at which a separate service pays for itself. **Recorded as an explicit reason this is a defer, not a build.**
4. **Does the `Location` concept leak into v1?** §3.2 excludes multi-location. If a location concept is ever needed, it must be scoped as "which batch is on the pass" and not as "which site".
