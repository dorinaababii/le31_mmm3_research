# 209 — Richer211/restaurant-kitchen-pass restaurant-kds-ab-expo-slots-square-pos-sync HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 kitchen-display-system + A/B-slot-routing + expo-pass + Square-POS-integration question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/209-Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync.md` (defer artifact; **no code today**).

Bucket: **v1 in-domain restaurant KDS (kitchen-pass + A/B expo slots + Square POS sync primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a kitchen-display-system surface, an expo-pass surface, an A/B-slot-routing primitive, or a Square-POS-integration surface, what is the *A/B expo slots + kitchen-pass + Square POS sync* vocabulary that preserves the existing v1 no-kitchen-display-system + no-expo-pass + no-POS-integration posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 8866 KB with 1★/0⑂ + null license + 0 topics + both `pushed_at` AND `created_at` in-window is shipping the *kitchen-pass + A/B expo slots + Square POS sync* primitive as the v1 in-domain restaurant-KDS discipline*, but struggles because *v1 has no documented kitchen-display-system primitive in the charter*, so that *v1 can introduce the kitchen-display-system + A/B expo slots + Square POS sync vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no kitchen-display-system trigger; the JTBD is primitive vocabulary extension + A/B expo slots + Square POS sync documentation, not a build-need). |
| 2 | **Viability** | Owner can read 8866 KB repo description + 0-topic vocabulary + A/B expo slots + Square POS sync + kitchen pass triple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *A/B expo slots + Square POS sync + kitchen pass* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the null-license code; LE31 v1 has no kitchen-display-system surface today). Confidence: medium for the *A/B expo slots + Square POS sync + kitchen pass* vocabulary (1★/0⑂ + null license + 0 topics + both fields in-window + description verbatim = §3.2 BLOCKER for code adoption, vocabulary-only artifact; the *A/B expo slots* discipline IS the *order-routing-to-cook* pattern applied to charter §3.1's *explicit-state-transition* discipline). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; Square POS integration = off-pattern for v1 (LE31 v1 has no POS surface); A/B-slot-routing = off-pattern for v1 (LE31 v1 has no KDS surface); null license = BLOCKER for code adoption. Practicability of adoption: vocabulary-only due to null license (§3.2 BLOCKER). **PASS** (posture validation only; adoption is v1 question). |
| 4 | **Conflict** | None. The *A/B expo slots* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the cook-availability dimension (the order-routing-to-cook pattern); the *Square POS sync* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the POS-side dimension (every POS-side event is an explicit user action). Charter §3.1 alignment (the *A/B expo slots + Square POS sync + kitchen pass* vocabulary is *explicit-state-transition* applied to the cook-availability + POS-side dimensions); §3.2 BLOCKER (null license; vocabulary-only artifact); §3.4 not triggered (no AI surface; the *A/B expo slots + Square POS sync* vocabulary is *operator-tooling*, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 in-domain restaurant KDS (kitchen-pass + A/B expo slots + Square POS sync vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 8866 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (8866 KB is substantial; only the *A/B expo slots + Square POS sync + kitchen pass* vocabulary + the both-fields-in-window signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/209-Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync-HANDOFF.md` and `features/209-Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + A/B expo slots + Square POS sync + kitchen pass documentation for the next v1 in-domain restaurant-KDS-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a kitchen-display-system surface to the LE31 v1 operator surface, an A/B-slot-routing primitive to the LE31 v1 cook-Telegram-bot, or a Square-POS-integration surface to the LE31 v1 webhook surface):

- `app/kds/` — possibly add (the kitchen-display-system module; depends on the v1 change).
- `app/kds/slots.py` — possibly add (the A/B-slot-routing primitive that routes orders to slot A or slot B; depends on the v1 change).
- `app/kds/expo_pass.py` — possibly add (the expo-pass surface that notifies waiters when orders are ready; depends on the v1 change).
- `app/integrations/square.py` — possibly add (the Square-POS-integration module; depends on the v1 change).
- `app/webhooks/square_webhook.py` — possibly add (the webhook receiver for Square POS events; depends on the v1 change).
- `tests/test_kds_slots.py` + `tests/test_expo_pass.py` + `tests/test_square_webhook.py` — possibly add (the integration tests for the kitchen-display-system + A/B-slot-routing + Square-POS-integration surfaces; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no kitchen-display-system surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/209-Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync.md` exists and is read back by the parent.
- [ ] `specs/209-Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `Richer211/restaurant-kitchen-pass` description is quoted verbatim (8866 KB repo).
- [ ] The 1★/0⑂ + null license (§3.2 BLOCKER for code adoption) + Python + both fields in-window + 0 topics + description *"Restaurant kitchen pass KDS: A/B slots and Square order sync"* is documented.
- [ ] The charter §3.1 alignment via *A/B-slot-routing = explicit-state-transition discipline applied to cook-availability* is documented.
- [ ] The charter §3.2 BLOCKER (null license; vocabulary-only) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a kitchen-display-system surface to the LE31 v1 operator surface, an A/B-slot-routing primitive to the LE31 v1 cook-Telegram-bot, or a Square-POS-integration surface to the LE31 v1 webhook surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `Richer211/restaurant-kitchen-pass` *A/B expo slots + Square POS sync + kitchen pass* vocabulary is evaluated against the PR's changes: does the change address the *A/B-slot-routing* discipline? does the change preserve the *expo-pass* primitive? does the change preserve the *Square-POS-sync* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/kds/` kitchen-display-system module; remove the `app/kds/slots.py` A/B-slot-routing primitive; remove the `app/kds/expo_pass.py` expo-pass surface; remove the `app/integrations/square.py` Square-POS-integration module; remove the `app/webhooks/square_webhook.py` webhook receiver; restore the original `app/bot/cook.py` Telegram handler.
- Migration cost: depends on the v1 change; the *A/B expo slots + Square POS sync + kitchen pass* vocabulary is *additive architecture* (the KDS is *new* files; the slots is *new* code; the expo-pass is *new* code; the Square-POS-integration is *new* code; the webhook receiver is *new* code, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the `Order` table retains all rows; the new `kds_slot` table is *new* data, not a schema change; the new `kds_assignment` table is *new* data, not a schema change; the new `square_event` table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:
1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.