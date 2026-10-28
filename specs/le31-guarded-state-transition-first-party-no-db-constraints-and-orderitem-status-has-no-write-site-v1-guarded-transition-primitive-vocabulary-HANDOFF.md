# HANDOFF — Feature 394: the guarded-transition primitive and the unmade negative-balance question

**This is a `defer` slice. There is no code to write today, and there is no Linear issue to hang it under (Linear MCP write endpoint blocked — 41st consecutive day).**

**Why it is `defer` and not `build` — read this before anything else:** the constraint's **sign** is undetermined, and two in-window artifacts disagree. `hemeshwar09/StockGuard` makes the database **refuse** to commit a negative balance (*"`CHECK (stock >= 0)` constraints: the DB refuses to commit an oversold state"*); `fortikday/pantry-signal` **allows** it and flags it (*"This is an estimate and can become negative when records are incomplete"*). **LE31 has never chosen.** Writing a `CHECK` constraint today would make the policy by accident, which `le31-conventions` forbids: *"When sources conflict, stop and expose the exact conflict. Do not silently pick the newest-looking or easiest rule."*

**Discovery chain:** Daily Research 2026-10-28 → the parent read the README of the in-window repo `hemeshwar09/StockGuard` (licence `null`, ★0, 55 KB, Python/FastAPI/PostgreSQL, created **and** pushed 2026-10-21) whose guarantees table says *"Every state change is `UPDATE ... WHERE status = 'ACTIVE'`, so exactly one transition wins"* and *"`CHECK (reserved <= stock)`, `CHECK (stock >= 0)` constraints: the DB refuses to commit an oversold state"* → the parent then went and read **LE31's own `backend/`** and found, by grep: `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **no output**; `grep -n "status" backend/app/models.py` → **exactly one hit** (`OrderItem.status`, line 151), and feature 379 had already established there is **no write site for it at all**; `grep -rn -i "reserved\|available\|on_hand" backend/app/` → **no output**. The same day's second pick (`fortikday/pantry-signal`) supplied the **conflicting** position on the negative-balance sign, which is what made this a charter question rather than a code change.

**Full evidence record: `features/394-le31-guarded-state-transition-first-party-no-db-constraints-and-orderitem-status-has-no-write-site-v1-guarded-transition-primitive-vocabulary.md`**

## Active feature path

`features/394-le31-guarded-state-transition-first-party-no-db-constraints-and-orderitem-status-has-no-write-site-v1-guarded-transition-primitive-vocabulary.md` — **`defer`** (Pick A of Daily Research 2026-10-28).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When the first LE31 feature writes an `OrderItem.status` or a `Table.status` — and the request is retried, or two surfaces write concurrently — the owner wants one state, not two, but struggles because no write is guarded and no constraint exists, so that the ledger never holds a contradiction.* Links to feature **388** (table state machine) and feature **379** (transition attribution). **Pass on OBSERVED evidence** — the code state was established by grep against `backend/`, not inferred. |
| 2 | Viability | ✓ | A guarded write and a `CHECK` constraint are ordinary engineering; the owner recovers by seeing the refusal. **No new role, no new surface, no admin.** **Pass.** |
| 3 | Practicability and confidence | ⚠ **CONDITIONAL** | Fits the fixed stack exactly (SQLModel + Postgres; SQLite in dev). **The named rabbit hole is the reason this is `defer`:** the constraint's **sign** is undetermined, and two in-window artifacts take opposite positions (StockGuard *refuses*; pantry-signal *allows and flags*). Confidence: **high** for the gap, **low** for the sign. **Evidence strength:** the gap is grep-verified; the sign has no LE31 decision behind it. |
| 4 | Conflict | ✓ | Nothing is being implemented, so no invariant is violated. But §3.3 (*"stock is derived from entries"*) and feature 382's shortfall rule are **already decisions about the business half** of this question, and the **storage half** (is a negative derived balance representable?) is **not**. **Recorded as a charter-level question, not resolved here.** |
| 5 | Outcome + appetite + scope | ✓ | v1 vocabulary + one question. **Maximum time worth spending: one slice** (one helper, one constraint, one test) — *once the sign is decided*. **Explicitly NOT in scope:** any `CHECK` constraint today, any change to `backend/`, any `Table.status` column (**feature 388**), any change to `ItemStatus` semantics, any idempotency-key mechanism (**feature 382**), any reservation/hold mechanism (**feature 269**), any pin bump. |
| 6 | Cost to operational value | ✓ | The gap is currently **inert** — feature 379 established there is **no write site** for `OrderItem.status`, so nothing is lost today. But it is **frozen in** by the first feature that writes a status (03, 09, 15, 17, 30, 45 all plan to move items through `ItemStatus`). **Cheap now, expensive after** — a wrongly-recorded sale is permanent, because `StockEntry` is append-only and a well-formed-but-wrong ledger row cannot be distinguished from a correct one. ICE/RICE as vocabulary only. |
| 7 | Circuit breaker + reversibility | ✓ | A vocabulary document and one question — **fully reversible, no data at risk**. **Stop evidence:** the pre-flight below. **Review point:** after the sign is decided, re-run the gate. **Pre-mortem (the most likely failure):** a future contributor adds a `CHECK` constraint in whichever direction they happened to read first, and the policy is thereby decided by accident — **this is exactly what this `defer` prevents.** |

**Gate verdict: `defer`** — check 3 is conditional on an unmade owner/charter decision.

## Bucket

**v1** — Pick A of Daily Research 2026-10-28. Per `le31-feature-pipeline/SKILL.md` step 4 the matching project is **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on **2026-10-28** that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **41st consecutive day**), there is no parent issue to hang the sub-issue under; the sub-issue is routed to **`le31 Research` (P-HMM-1)** in the fallback payload as the parent research issue's home, and **no project attachment actually occurred**. The `Feature` label id (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`) **was re-verified this pass** via `list_issue_labels` (not carried forward unverified).

## Files to touch

**Today: none. This slice touches zero files outside `features/` and `specs/`.**

When the sign is decided, the files a future implementer would touch (recorded so the shape is not lost — **not** this slice's scope):

- `backend/app/models.py` — **ADD** the `CHECK` constraint, **with the sign the owner chose**. **DO NOT** change any existing class, field, or timestamp. Note `Batch.qty_remaining` is feature 374's and `OrderItem.batch_id` is feature 385's.
- `backend/app/services/` — **CREATE** (it does not exist) the single guarded-write helper, if that is where the team puts it. Feature 379 already requires *"one single write path"*; **if you find yourself creating a service layer for a different purpose, STOP.**
- `backend/app/routers/` — the guarded transition's **refusal** must be visible on whichever surface attempted it (feature 388's HTTP-409-with-`visit_id` is the precedent). **Do not add a new router.**
- `backend/app/bot/cook_bot.py` — **no new command, no new output.**
- `backend/requirements.txt` — **no dependency change.**
- `PROJECT_CHARTER.md` — **the sign decision belongs here** if it is a charter-level decision, or in the feature file if it is a feature-level one. **Do not encode both interpretations.**
- `features/01-table-management.md` — **do not touch.** Feature 388 owns it.

**Do NOT touch (out of scope, explicitly):**

- Any `CHECK` constraint **before the sign is decided.**
- `backend/app/models.py` — **any class other than the one the owner names.** Not `Visit`, `OrderItem`, `StockEntry`, `Bill`, `DerivedTip`, `Shift`, `Batch`, `MenuItem`.
- The `ItemStatus` enum values or their order.
- The `Table.status` column — **feature 388**.
- The `OrderItem` actor field — **feature 379**.
- Idempotency-key semantics — **feature 382**.
- Atomic stock reservation — **feature 269**.
- `Batch.qty_remaining` stored-vs-derived — **feature 374**.
- The FastAPI / SQLAlchemy / SQLModel / Postgres pins.
- Any `Option`/`Modifier`/`Variant` model — features 386/387.

## The load-bearing checks (for the future implementer — none of these run today)

1. **The defect is impossible to reintroduce** — issue the same transition twice concurrently; assert **exactly one** succeeded and **zero** extra rows exist. **This is the test that makes the defect impossible to reintroduce silently.**
2. **The refusal is not decorative** — the losing attempt receives a **visible** refusal carrying the current state (feature 388's HTTP-409-with-`visit_id` is the precedent), and **no row was written**.
3. **The transition is atomic** — the state change and its precondition are **one statement**; there is no window between check and write.
4. **The database is the backstop** — assert the constraint **refuses** the state the application should never produce. If the constraint's sign is "allow", this check becomes *"the derived balance may be negative and the surface flags it as an estimate"* — **and it must be tested in that form, not silently omitted.**
5. **The threshold-freezing discipline (from Pick C's artifact)** — if thresholds exist, they are frozen before the results are seen.
6. **No write site bypasses the helper** — assert that no code path sets a status column except the guarded helper. (Feature 379's *"no other code path may set `status` directly"*.)

## Verification protocol reference

- **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — the general protocol for exercising behaviour, not asserting it.
- **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the quality gates this slice must pass **when it is built**.
- **`coding-agent/skills/le31-data-correctness/SKILL.md`** — mandatory for any slice that touches stock derivation or money.
- **`coding-agent/skills/le31-cook-bot-ux/SKILL.md`** — mandatory if the refusal surfaces on the cook bot (it does not today).
- **`skills/le31-conventions/SKILL.md`** — the seven-check gate and the source-of-truth order.

**The definition of done for this slice, as it stands: the document exists, the question is stated, and nothing else was done.** That is the correct outcome for a `defer` pick, and reporting it as a partial build would be wrong.

## Rollback path

**Nothing to roll back.** This slice adds:

- One Markdown file under `features/` (the contract).
- One Markdown file under `specs/` (this handoff).
- One row in `/opt/data/INDEX.md`.

**All three are reversible by deletion, and none of them is referenced by running code.** No database change, no schema change, no dependency, no configuration. **No data is destroyed by removing them.**

**If the slice is later built**, the rollback is: drop the constraint, drop the helper, and return the call sites to their prior form. **The one irreversible thing is the data written while the guard was absent** — which is precisely why the guard should land before the first write site, not after.

## Trigger condition

This slice activates when **any** of the following becomes true:

1. **The owner decides the sign** of the negative-balance question (refuse vs allow-and-flag). **This is the primary trigger** — the question is cheap to answer and expensive to leave open.
2. **A PR adds a write site for `OrderItem.status`** (features 03, 09, 15, 17, 30, 45 all plan to). **This is the time-sensitive trigger** — after the first unguarded write, the cost of the guard is a historical audit rather than a helper.
3. **A PR adds a write site for `Table.status`** — feature 388.
4. **A PR proposes any `CHECK` constraint or any guarded conditional write** anywhere in `backend/`. **If you are reading this because you are about to write one, STOP and read Open question 1 in the feature contract first.**
5. **A PR adds a second reader of the `StockEntry` ledger** (a report, an export, a bot-side projection) — at which point the *"each event is applied once"* property becomes a real requirement, not a hypothetical one.

## Mandatory LE31 skill list

The external agent **must** load these before acting:

1. **`skills/le31-conventions/SKILL.md`** — the seven-check gate, the hard invariants, and the *"when sources conflict, stop and expose the exact conflict"* rule that produced this `defer`. **Read first.**
2. **`skills/le31-v1-feature-pattern/SKILL.md`** — the v1 contract shape and slicing rules.
3. **`skills/le31-handoff-spec/SKILL.md`** — the handoff package discipline.
4. **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — how to *exercise* the behaviour rather than assert it.
5. **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the gates this slice must pass when built.
6. **`coding-agent/skills/le31-data-correctness/SKILL.md`** — mandatory for any stock-derivation or money work.
7. **`coding-agent/skills/le31-conventions-coder/SKILL.md`** — coding conventions.
8. **`skills/le31-research/SKILL.md`** — to understand what was and was not established by the research pass.

## Read-first ordering (a stranger must be able to act from this package alone)

1. `features/394-...-v1-guarded-transition-primitive-vocabulary.md` — **the contract**, including Open question 1 (the unmade sign question).
2. `features/388-le31-table-state-machine-first-party-...md` — **the adjacent first-party finding, filed the day before**. It shows the same class of defect in the same codebase and the house style for fixing it.
3. `features/379-le31-order-item-transition-actor-attribution-first-party-...md` — establishes that there is **no write site** today, which is the basis of the *"cheap now"* argument.
4. `/opt/data/le31-daily-research-2026-10-28.md` — the full report, including the parent's re-derivation and the two subagent corrections.

## Linear reference

- **Parent research issue:** **not created** — Linear MCP write endpoint blocked (**41st consecutive day**, HTTP 400 `invalid_request` *"You've exceeded the free issue limit for this workspace"*; two write probes, requestIds `a51808a5284dd349` and `a51808cf1e574e32`, **both failed before any write**).
- **Sub-issue:** **not created** — same blocker. **Intended:** project `le31 Research` (P-HMM-1), state `Backlog`, label `Feature` (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`, re-verified this pass).
- **Fallback payload:** `/opt/data/le31-daily-research-2026-10-28.linear-fallback.json`.
- **Read endpoints were verified reachable** on 2026-10-28: `list_projects` (3 projects), `list_issue_statuses` (`Done` = `449bbe45-5f5b-40f6-9d6c-ec69ba432ffc`), `list_issue_labels` (`Feature`), `list_issues` (confirms no 2026-10-28 issue exists).
