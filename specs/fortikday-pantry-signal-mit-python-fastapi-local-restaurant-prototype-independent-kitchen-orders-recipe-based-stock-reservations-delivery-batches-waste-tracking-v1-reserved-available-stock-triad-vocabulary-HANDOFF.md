# HANDOFF — Feature 395: stock is three quantities, not one — on hand, reserved, and available

**This is a `defer` slice. There is no code to write today, and there is no Linear issue to hang it under (Linear MCP write endpoint blocked — 41st consecutive day).**

**The one-line reason it is `defer` and not `build`:** `Pantry Signal`'s three quantities are denominated in **grams of ingredients**, and **LE31 has no recipe or ingredient concept at all** (`grep -rn -i "recipe|ingredient|bom" backend/app/` → **no output**; `MenuItem` has no recipe link). **The concept transfers; the denominators do not.** So the implementation depends on feature 359 (recipe-linked depletion), and this slice is filed so the question is not lost.

**Discovery chain:** Daily Research 2026-10-28 → the parent read the README of the in-window repo `fortikday/pantry-signal` (MIT, ★0, 1,255 KB, Python, created **and** pushed 2026-10-22) whose "Stock and dates" section names three distinct quantities — *"**On hand:** received grams minus recorded recipe usage and logged waste … **Reserved:** ingredients required by queued orders not yet prepared or cancelled … **Available:** a conservative estimate using dated batches, on-hand balance, and reservations"* → the parent then went and read **LE31's own `backend/`** and found, by grep: `grep -rn -i "reserved\|available\|on_hand\|on hand" backend/app/` → **exactly one hit, and it is the word "reserved" inside a SQL comment** about the word `table` being a reserved SQL keyword. **LE31's `Batch` has `qty_start` and `qty_remaining` — one number — and it cannot express the difference between what is physically present and what is already promised.**

**Full evidence record: `features/395-fortikday-pantry-signal-mit-python-fastapi-local-restaurant-prototype-independent-kitchen-orders-recipe-based-stock-reservations-delivery-batches-waste-tracking-v1-reserved-available-stock-triad-vocabulary.md`**

## Active feature path

`features/395-fortikday-pantry-signal-mit-python-fastapi-local-restaurant-prototype-independent-kitchen-orders-recipe-based-stock-reservations-delivery-batches-waste-tracking-v1-reserved-available-stock-triad-vocabulary.md` — **`defer`** (Pick B of Daily Research 2026-10-28).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When several orders are queued against the same prepared batch, the owner wants to know how much is genuinely still sellable, but struggles because LE31 keeps a single number, so that stock promised to an order is not also promised to another.* Links to features **374**, **03**, **385**. **Pass on REPORTED evidence** — the shape is documented by the artifact; the *demand* is not (see check 6). |
| 2 | Viability | ✓ | Reading a README is free; adopting it is not. **No new role, no new surface, no admin.** **Pass.** |
| 3 | Practicability and confidence | ⚠ **CONDITIONAL** | MIT ✓, Python ✓, on-stack. **The named rabbit hole is the denominator**: the artifact's quantities are over **ingredients**; LE31's are over **prepared-item units**, and LE31 has no recipe model. Confidence: **medium** for the shape, **low** for LE31's need. |
| 4 | Conflict | ✓ | Nothing is adopted. The triad is a **refinement** of §3.3 (*"current stock is derived from entries"*), not a contradiction — it makes the *derivation inputs* richer. **The negative-balance question is explicitly NOT answered here** — that belongs to feature 394 (Pick A of the same pass). |
| 5 | Outcome + appetite + scope | ✓ | v1 vocabulary, one paragraph. **Explicitly NOT in scope:** any `Batch` column or model (**feature 374**), any recipe/ingredient/BOM/waste model, any change to `backend/app/`, **the artifact's two-service architecture (explicitly rejected — see below)**, any delivery or waste feature, any pin bump. |
| 6 | Cost to operational value | ✓ | Near-zero cost, low immediate value — the owner has not asked for it. Justified because it is the **first external artifact in this series to name three distinct stock quantities**, which feature 374's single-number argument cannot express. **The asymmetry that decides the ordering: cheap now (one vocabulary decision); expensive after — if the first selling path ships against a single `qty_remaining`, every historical sale is permanently ambiguous about whether it consumed reserved or unreserved stock, and the ledger is append-only, so the ambiguity cannot be recovered later.** ICE/RICE as vocabulary only. |
| 7 | Circuit breaker + reversibility | ✓ | A vocabulary note. **Fully reversible by deleting one file; no data, schema, dependency, or configuration is touched.** **Stop evidence:** the pre-flight below. **Review point:** when feature 359 lands, re-read the feature contract and decide whether the triad becomes implementable. **Pre-mortem:** someone reads *"reserved"* and assumes a reservation mechanism is being adopted — **it is not; feature 269 already owns the reservation vocabulary and this pick is the read-side triad.** |

**Gate verdict: `defer`** — check 3 is conditional on feature 359 (the recipe model).

## Bucket

**v1** — Pick B of Daily Research 2026-10-28. Per `le31-feature-pipeline/SKILL.md` step 4 the matching project is **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on **2026-10-28** that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **41st consecutive day**), there is no parent issue to hang the sub-issue under; the sub-issue is routed to **`le31 Research` (P-HMM-1)** in the fallback payload as the parent research issue's home, and **no project attachment actually occurred**. The `Feature` label id (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`) **was re-verified this pass** via `list_issue_labels`.

## Files to touch

**Today: none. This slice touches zero files outside `features/` and `specs/`.**

When feature 359 (recipe-linked depletion) lands, the files a future implementer would touch (recorded so the shape is not lost — **not** this slice's scope):

- `backend/app/models.py` — **no new stored column.** The triad is a **derivation** over `StockEntry`, consistent with feature 374's direction. **The open question this slice does not answer:** how `reserved` is represented in an **append-only** ledger where §3.3 forbids updating or deleting entries — a reservation is a **claim on a future movement**, not a movement. Candidates: a distinct `StockReason` with a sign convention; a separate table; a derived join over `OrderItem`. **Do not pick one silently.**
- `backend/app/services/` (or a query module) — the **derivation** of `on_hand` / `reserved` / `available`. **If you find yourself adding a stored column, STOP — that is feature 374's subject and it contradicts 374's direction.**
- `backend/app/routers/` — **no new router** unless a separate proposal creates a surface.
- `backend/app/bot/cook_bot.py` — **no new command.**
- `backend/requirements.txt` — **no dependency change.**
- `PROJECT_CHARTER.md` — **no change.** The triad is a clarification of §3.3, not a new charter rule. **If you think it needs one, stop.**

**Do NOT touch (out of scope, explicitly):**

- `backend/app/models.py` — **any class other than the one feature 359 names.** Not `Batch.qty_remaining` (**feature 374**), not `OrderItem.batch_id` (**feature 385**).
- **Any recipe / ingredient / BOM / waste model** — feature 359's subject.
- **The negative-balance question** — feature 394 (Pick A of the same pass).
- The **reservation write-side** vocabulary — feature 269.
- Any two-service / event-over-HTTP architecture — **explicitly rejected**; see the "Architecture rejection" note below.
- Any delivery / delivery-batch / waste-tracking feature — out of v1 scope.
- The FastAPI / SQLAlchemy / SQLModel / Postgres pins.
- Any `Option`/`Modifier`/`Variant` model — features 386/387.

### ⭐ Architecture rejection (recorded so this is not mistaken for an architecture recommendation)

`Pantry Signal` is a **two-service, event-over-HTTP, locally-hosted prototype**: *"The order service commits each kitchen change and its event together in `local/orders.sqlite3`. The inventory service reads those events over HTTP and updates `local/inventory.sqlite3`."*

**LE31 is one service with one Postgres** (§3.5's fixed stack). Copying this would mean introducing a service boundary, a cursor, and an HTTP hop between the order and the inventory — **for no v1 benefit**, at real operational cost for a one-restaurant product whose premise is that the owner can run and understand it.

**The transferable part is the vocabulary — three quantities — not the architecture.** The replay-safety property (*"Replaying an event cannot deduct stock again"*) is recorded as a **forward-looking** item for the day LE31 grows a second reader of the ledger; it is **not** a present gap, because LE31 is single-service today.

## The load-bearing checks (for the future implementer — none of these run today)

1. **The three quantities are distinct** — construct a state where `on_hand ≠ reserved ≠ available` and assert all three read back correctly. **A test that only exercises the case where they coincide proves nothing.**
2. **The derivation, not a stored number** — assert no column holds `available` or `reserved`; changing a `StockEntry` must change all three derived values with no other write.
3. **A reservation is not a movement** — assert that creating a reservation **does not** alter the `on_hand` derivation (it is a claim, not a consumption) while it **does** alter `available`.
4. **The recipe dependency is respected** — assert the derivation denominates in the same unit as the stock it reads (prepared-item units for LE31, **not** grams), and that no unit conversion is smuggled in.
5. **The append-only rule holds** — assert no `StockEntry` row is updated or deleted to represent a reservation change.
6. **The negative-balance behaviour matches the decided sign** — **if feature 394's sign is "allow and flag"**, assert a negative derived balance is *representable* and *flagged*; **if it is "refuse"**, assert it cannot occur. **Do not implement this until feature 394's question is answered.**

## Verification protocol reference

- **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — the general protocol for exercising behaviour, not asserting it.
- **`coding-agent/skills/le31-data-correctness/SKILL.md`** — **mandatory** for any slice that touches stock derivation; this slice is a derivation slice.
- **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the quality gates this slice must pass **when it is built**.
- **`skills/le31-conventions/SKILL.md`** — the seven-check gate and the *"research novelty is not user demand"* pitfall.
- **`coding-agent/skills/le31-conventions-coder/SKILL.md`** — coding conventions.

**The definition of done for this slice, as it stands: the document exists, the dependency is stated, and nothing else was done.** That is the correct outcome for a `defer` pick.

## Rollback path

**Nothing to roll back.** This slice adds:

- One Markdown file under `features/` (the contract).
- One Markdown file under `specs/` (this handoff).
- One row in `/opt/data/INDEX.md`.

**All three are reversible by deletion, and none of them is referenced by running code.** No database change, no schema change, no dependency, no configuration. **No data is destroyed by removing them.**

**If the slice is later built**, the rollback is: drop the derivation, drop the reservation representation, and return the call sites to their prior form. **The one irreversible thing is any historical sale recorded against a single-number model** — which is why the derivation, if it ever lands, should land **before** the first selling path rather than after.

## Trigger condition

This slice activates when **any** of the following becomes true:

1. **Feature 359 (recipe-linked depletion) lands** — the denominator question resolves and the triad becomes implementable. **This is the primary trigger.**
2. **A PR adds a selling path that decrements stock** (features 03, 15, 26, 34 all plan to). **This is the time-sensitive trigger** — after the first sale is recorded against a single number, every historical sale is permanently ambiguous about whether it consumed reserved or unreserved stock.
3. **The owner asks how much is really sellable**, or reports promising the same portion twice.
4. **Feature 374 (`qty_remaining` stored-vs-derived) is decided** — the two questions are orthogonal but adjacent, and both point toward deriving.
5. **A PR proposes a reservation or hold mechanism** — **note that feature 269 already owns the reservation vocabulary**; the trigger here is the *read-side triad*, not the write-side reservation.

## Mandatory LE31 skill list

The external agent **must** load these before acting:

1. **`skills/le31-conventions/SKILL.md`** — the seven-check gate, the hard invariants (§3.3's derivation rule especially), and the *"research novelty is not user demand"* pitfall. **Read first.**
2. **`skills/le31-v1-feature-pattern/SKILL.md`** — the v1 contract shape and slicing rules.
3. **`skills/le31-handoff-spec/SKILL.md`** — the handoff package discipline.
4. **`coding-agent/skills/le31-data-correctness/SKILL.md`** — **mandatory**; this is a derivation slice.
5. **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — how to *exercise* the behaviour rather than assert it.
6. **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the gates this slice must pass when built.
7. **`coding-agent/skills/le31-conventions-coder/SKILL.md`** — coding conventions.
8. **`skills/le31-research/SKILL.md`** — to understand what was and was not established by the research pass.

## Read-first ordering (a stranger must be able to act from this package alone)

1. `features/395-...-v1-reserved-available-stock-triad-vocabulary.md` — **the contract**, including Open question 1 (how a reservation is represented in an append-only ledger).
2. `features/374-le31-qty-remaining-derived-not-stored-...md` — **the orthogonal sibling question.** 374 asks *"should the number be stored?"*; this one asks *"how many numbers are there?"*. **Both must be answered.**
3. `features/359-...` (recipe-linked depletion) — **the hard dependency.**
4. `features/394-...` (Pick A of the same pass) — owns the negative-balance question this slice must not re-answer.
5. `/opt/data/le31-daily-research-2026-10-28.md` — the full report.

## Linear reference

- **Parent research issue:** **not created** — Linear MCP write endpoint blocked (**41st consecutive day**, HTTP 400 `invalid_request` *"You've exceeded the free issue limit for this workspace"*; two write probes, requestIds `a51808a5284dd349` and `a51808cf1e574e32`, **both failed before any write**).
- **Sub-issue:** **not created** — same blocker. **Intended:** project `le31 Research` (P-HMM-1), state `Backlog`, label `Feature` (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`, re-verified this pass).
- **Fallback payload:** `/opt/data/le31-daily-research-2026-10-28.linear-fallback.json`.
- **Read endpoints were verified reachable** on 2026-10-28: `list_projects` (3 projects), `list_issue_statuses` (`Done` = `449bbe45-5f5b-40f6-9d6c-ec69ba432ffc`), `list_issue_labels` (`Feature`), `list_issues` (confirms no 2026-10-28 issue exists).
