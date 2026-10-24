# HANDOFF — Feature 372: `hitaishi2222/kinv` — expiry-first inventory without valuation vocabulary

**Upstream source repo: [`hitaishi2222/kinv`](https://github.com/hitaishi2222/kinv)** — see `features/372-hitaishi2222-kinv-mit-terminal-inventory-tui-tells-you-what-is-about-to-expire-without-stock-valuation-busywork-expiry-kitchen-inventory-python-v1-expiry-first-inventory-without-valuation-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/372-hitaishi2222-kinv-mit-terminal-inventory-tui-tells-you-what-is-about-to-expire-without-stock-valuation-busywork-expiry-kitchen-inventory-python-v1-expiry-first-inventory-without-valuation-vocabulary.md` — defer/parking-lot (Pick C of Daily Research 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | When the owner sees food spoil, they want *to know what is about to expire*, but LE31's owner has **never reported waste or spoilage as a problem** — evidence class **assumed** (the weakest class on the scale). **A failing check 1 is what makes this a defer.** |
| 2 | Viability | ✓ | MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★0⑂0, **36 KB tiny — the smallest pick of the 86-pass series**, Python on-stack. **Traction caveat recorded plainly: ★0⑂0, 0 open issues, created 2026-02, default branch `dev` — the implementation is unproven. The shape is the artifact, not the code.** |
| 3 | Practicability and confidence | ✓ | On-stack. **Domain shift recorded plainly:** a household kitchen's expiry clock runs in days; LE31's prepared batches are made *for service today* (§4.3: `batch` is "a concrete prepared quantity of a menu_item **for a day**"), so LE31's expiry equivalent is already `reason = 'waste'` and `sold_out` — **the concept exists, the label does not.** Evidence strength: high for the *valuation refusal*, medium for the expiry mapping. |
| 4 | Conflict | ✓ | The *vocabulary* conflicts with nothing. **But adopting the surface WOULD conflict**: a terminal TUI is a **third interface** and §3.1 says two surfaces (waiter web UI + cook Telegram bot). **The valuation refusal, by contrast, conflicts with nothing and is the recommendation.** |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Maximum time worth spending: **45 min documentation**. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is **a named non-goal**: "no stock valuation / no costing" written into §3.2. Roughly 45 min of documentation; the saving is one future PR that would otherwise have to be argued against. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. If the non-goal is ever adopted it is a *charter* change, reversible by editing §3.2. |

**Gate verdict: `defer` (parking-lot)** — check 1 fails on evidence class (**assumed**, the weakest class). Note the asymmetry: the *vocabulary* and the *recommendation* are both sound; only the pain is missing.

## Bucket

**v1 (expiry-first inventory without valuation vocabulary)** — Pick C of Daily Research 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — today's confirmed workspace state is exactly 3 projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1); `le31 v2 owner-pains` and `le31 v2-AI` **do not exist**. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload.

## Files to touch

**None today.** Documentation-only.

If the owner ever reports waste as a problem, the expected files are:

- `PROJECT_CHARTER.md` §3.2 — **the recommended change**: add *"Stock valuation, costing and margin reporting"* to the explicit non-goals list. **This is the whole point of the pick and it costs one line.** Cite feature 372 and `hitaishi2222/kinv` as the external prior art for the refusal.
- `backend/app/models.py` — **read-only audit**: confirm **no** `cost_per_unit`, `unit_cost`, `price` or `value` field exists on `menu_item`, `batch` or `stock_entry`. **This is the load-bearing check of any future build** — the non-goal is only real if the schema enforces it.
- `backend/app/models.py` — `batch` — if batch date is ever added, it must be a **date column on `batch`**, not a derived expiry timestamp, and `StockEntry` needs an expiry-adjacent reason alongside `waste`/`sold_out`.
- `backend/services/stock_service.py` — the expiry projection, if ever built, is a **projection over existing `StockEntry` reasons** (waste + sold_out), **not a new expiry-tracking subsystem**. §4.3's derive-never-store rule applies.
- `bot/handlers/stock_handlers.py` — the **cook bot is the natural surface** if waste ever becomes tracked (a question the cook asks at the start of a shift). **This is the one new idea in this pass that rides an existing surface rather than creating a third.**
- `tests/test_no_stock_valuation.py` — **the load-bearing test**: assert that no model on the stock path carries a monetary valuation field, and that a `float`-typed price is rejected. A charter rule with no test is a comment.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For the non-goal, the observable behaviour is **the absence**: no screen anywhere in the running system shows a stock value or a cost figure, and the derived quantities still work. To verify the expiry projection, if it is ever built, it must be exercised as **a real waste event in the running system** — record a `waste` entry through the cook bot, then observe the projection change.

## Rollback path

`git rm features/372-*.md specs/hitaishi2222-kinv-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible. (If the §3.2 non-goal was adopted, it is reversible by editing the charter — but it should not be removed just to unblock a feature; that is a §3.2 scope decision, not a technical one.)

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Stock*, *Money* and *Truth* rules first)
- `le31-data` — append-only ledger rules (`StockEntry`: never update or delete; current stock derived)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.1, §3.2, §3.6, §4.3)

## Open questions carried into any future build

1. **Should "no stock valuation" be added to the charter as an explicit non-goal?** §3.2's non-goal list does not currently include it, and §3.2 also does not exclude cost accounting by name. **Unmade, and this feature's main recommendation.**
2. **Does LE31 want a "waste is a first-class outcome" view?** LE31 records `reason = 'waste'` but has no waste *report*. That is a plausible v2 owner-facing view. Unmade.
3. **Is batch-date a field LE31 wants?** §4.2's schema sketch has `batch` without a date column, yet §4.3 describes batch as "for a day". **This is a small internal inconsistency in the charter** — noted, not resolved here.
4. **Would an expiry projection require a new `StockEntry` reason, or is `waste` sufficient?** Unmade. The pick's position is that `waste` + `sold_out` already cover it as a projection.
