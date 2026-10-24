# Feature 372 — `hitaishi2222/kinv` terminal-inventory-TUI-+-tells-you-what-is-about-to-expire-+-without-stock-valuation-busywork (defer)

> **NEW observation (2026-10-24).** Documents in-window GitHub repo `hitaishi2222/kinv` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, **36 KB tiny — the smallest pick of the 86-pass series**, **Python ✓ ON-STACK**, created **2026-02-27 AND pushed 2026-10-20T15:09:40Z = IN-WINDOW BY BOTH FIELDS**, `archived=false`, `fork=false`, 0 open issues, default_branch=`dev`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-24, not from search-result numbers. Description (verbatim from GitHub API): *"A terminal inventory TUI that tells you what is about to expire, without stock-valuation busywork."* Topics (verbatim): `expiry, inventory, kitchen, python, terminal, tui`. Bucket: **v1 (expiry-first inventory without valuation vocabulary)** — Pick C of Daily Research 2026-10-24. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Retain the **expiry-first, valuation-free** inventory posture as a persistent reference, and record the one observation this pass surfaced that is directly actionable as a **named non-goal**: LE31's charter already derives stock and never values it (§4.3), and this project states the *refusal* — "without stock-valuation busywork" — as its pitch.

The deliverable is a **rule LE31 should write down before someone builds it**: no stock valuation, no stock-value field, no costing report on the v1 floor.

## Scope

**In scope (defer artifact):**

- A written record of the **expiry-first ordering**: the question the tool answers is *"what is about to expire?"*, not *"what is worth?"* — and expiry is the question that actually destroys value in a kitchen, while value is the question that never gets asked.
- A written record of the **valuation refusal as a feature of the design**, and the argument for making it a named LE31 non-goal.
- A written record of the **terminal-as-a-surface** observation: a 36 KB terminal program is a complete, usable inventory interface for one operator with one screen.

**Out of scope (defer artifact):**

- Any LE31 code, schema, or migration.
- Adopting the kinv codebase (36 KB, `dev` default branch, 0 stars — the code is not the point and its maturity is unproven).
- Any expiry tracking in LE31. §4.3's `StockEntry` reasons are `initial`, `sale`, `sold_out`, `waste`, `restock` — **there is no expiry reason**, and adding one is a data-model decision, not a vocabulary adoption.
- Any third UI surface. §3.1 says two surfaces (waiter web UI + cook Telegram bot). A terminal TUI would be a **third**.
- Any stock valuation, costing, or margin report — see "Why this matters".

## Description

`hitaishi2222/kinv` is a terminal inventory TUI that tells you what is about to expire, without stock-valuation busywork. Three things are worth separating out:

1. **Expiry-first, not value-first.** The tool's entire premise is that the useful question about perishable stock is *time-to-expiry*, and the useless question is *monetary value*. **This maps onto LE31's §3.3/§4.3 distinction but on a different axis.** LE31 derives *quantity* from entries and never stores it; it says nothing about *time*. A kitchen's real waste is spoilage, and spoilage is a clock, not a number. **The vocabulary is genuinely new for LE31 even though the surrounding domain is not.**
2. **"without stock-valuation busywork" is the sentence worth keeping.** It is a **refusal stated as a selling point**. Most inventory tools lead with what they compute. This one leads with what it deliberately declines to compute. LE31's charter reaches the same place by omission — §4.3 derives `qty_remaining` and never mentions cost — but **omission is not a decision**. A charter that says "we do not value stock" is a charter that can be defended against the well-meant PR that adds a `cost_per_unit` column.
3. **36 KB, one operator, one screen.** The smallest pick of the 86-pass series. It is a complete answer to "how do I see what needs using up" without a web server, without a database migration, without a second client install. Recorded because **LE31's §3.1 two-surface discipline means any new surface is expensive**, and this repo shows the size of the thing that could tempt a third.

**What is *not* adoptable:** the code is on the `dev` branch, has ★0/⑂0, 0 open issues, and a 2026-02 creation date. There is no evidence it works well. **The shape is the artifact; the implementation is not.** Recorded plainly.

**The domain shift, stated plainly:** a household kitchen's expiry clock runs in days; LE31's prepared batches are made *for service today* (§4.3: `batch` is "a concrete prepared quantity of a menu_item **for a day**"). A batch that expires tomorrow is a *planning* problem (prep forecasting), not a *stock-integrity* problem. LE31's "expiry" equivalent — and it already has one — is **waste** (`reason = 'waste'`, i.e. `/leftover N`) and **sold-out**. **LE31 already has the concept; it calls it waste and sells out.** That mapping is the genuinely useful thing in this pick.

## Data model

None shipped. The vocabulary implies: an **expiry timestamp or date** on a stock item, and a **derived "expiring soon" projection** — the same derive-never-store discipline as `batch.qty_remaining`, applied to a different dimension. LE31's `batch` table would need a date dimension if this were ever adopted, and `StockEntry` would need an expiry-related reason. **Neither is proposed.** The mapping to LE31's existing vocabulary is: *expiry ≈ waste + sold-out*, i.e. a **projection over existing `StockEntry` reasons**, not a new ledger.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):** (1) the owner reports food waste as a problem (currently an **assumed** pain, not an observed one); (2) a prep-forecasting feature is proposed, at which point batch date becomes a first-class field and this reference must be read first; (3) a costing/valuation PR is proposed, at which point this feature's "Why this matters" section is the pre-agreed answer.

## Telegram interaction if any

None today. Long-horizon note: if waste ever becomes a tracked pain, the **cook Telegram bot is the natural surface** — "what's expiring" is a question the cook asks at the start of a shift, and it is the one question a bot can answer without adding a client. **This is worth recording because it is the one new surface in this pass that does not require a third interface:** the expiry projection would ride the existing cook bot, not create one.

## Dependencies

None. No new packages, no schema migration, no infrastructure.

## Open questions

1. **Does LE31 want a "waste is a first-class outcome" view?** LE31 records `reason = 'waste'` but has no waste *report*. That is a plausible v2 owner-facing view. Unmade.
2. **Should "no stock valuation" be added to the charter as an explicit non-goal?** §3.2's non-goal list does not currently include it, and §3.2 also does not exclude cost accounting by name. **Unmade, and this feature's main recommendation.**
3. **Is batch-date a field LE31 wants?** §4.2's schema sketch has `batch` without a date column, yet §4.3 describes batch as "for a day". **This is a small internal inconsistency in the charter** — noted, not resolved here.

## Why this matters

Because a **refusal** is worth more than a feature, and this one is cheap to adopt.

LE31's §4.3 is unambiguous that current stock is *derived* and never stored. What LE31 has **never** said is that it will not *value* stock. The gap is small but real: a well-meaning contributor could add `menu_item.cost_per_unit`, then a "food cost %" report, then a margin view on the bill — and each step would look like a natural extension of the existing `Decimal` price field. The charter's silence is the only thing preventing it, and charter silence is not a defence.

`kinv` states the opposite position in seven words and makes it a selling point: **"without stock-valuation busywork."** A 36 KB project whose pitch is that it refuses to compute the thing LE31 has not yet decided to refuse is a cheap, memorable way to write the rule down. **Recommendation: add "no stock valuation / no costing" to §3.2's explicit non-goals, citing this reference.**

The second thing worth keeping is the mapping: **expiry in a restaurant kitchen is waste + sold-out.** LE31 already records both as `StockEntry` reasons. The vocabulary was not missing; the *label* was. A future waste-reporting feature should be read as a **projection over the existing ledger**, not as a new expiry-tracking subsystem — which is exactly what §4.3's derive-never-store rule would demand, and exactly what a naive expiry feature would get wrong.

## Cross-section

Features 03 (`kitchen-stock-tracker`), 15 (`inventory-variance`), 28 (`shelf-threshold-receiving-bot`), 38 (`cook-voice-note-to-stockentry`), 41 (`telegram-msg-stock-update`), 153 (`sausageos-production-erp-append-only-stock-fefo-versioned-recipes`), 176 (`Sholu021/KitchenIQ` — FEFO), 307 (waste/leftover-adjacent). Features 153 and 176 already carry **FEFO** (first-expiry-first-out) vocabulary, so the *ordering* primitive is not new; what is new here is the **valuation refusal** and the explicit **expiry ≈ waste + sold-out** mapping to LE31's existing `StockEntry` reasons. GitHub `hitaishi2222/kinv` is unique vs features 1–369 (verified by ripgrep against `features/`, `specs/` and `INDEX.md`). Fully reversible — documentation-only artifact.
