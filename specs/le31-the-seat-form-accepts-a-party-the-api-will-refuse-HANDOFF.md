# HANDOFF — Feature 466: the seat form accepts a party the API will refuse

> **Slice contract for the coding agent.** Feature: `features/466-le31-the-seat-form-accepts-a-party-the-api-will-refuse-the-shipped-mock-up-adults-field-allows-0.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (parsed from the shipped files on 2026-11-10).
> Filed by: Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass), Pick B.

---

## 1. The active feature path

```
features/466-le31-the-seat-form-accepts-a-party-the-api-will-refuse-the-shipped-mock-up-adults-field-allows-0.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 414 / 423 / 388 / 08 / 24 / 465 / 467, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | Parsed out of the shipped `index.html` on 2026-11-10: `Adults id=inp-adults min=0 max=20`, `Party size id=inp-party min=1 max=20`, `Children id=inp-children min=0 max=20`. The API's guard, verbatim from `backend/app/routers/tables.py`: `if party_size < 1 or adults < 1: raise HTTPException(400, "Need at least 1 adult")`. **The form permits a value the API refuses.** |
| 2 | The defect is in LE31's own code | **PASS** | `index.html` — 30,530 bytes, 720 lines, **the shipped waiter surface**, mounted at `/` by `backend/app/main.py`. The `min="0"` literal is on the `Adults` input. `PROJECT_CHARTER.md` P0 row 42: *"Waiter can seat a party at any free table and capture `party_size`, `adults`, `children`."* |
| 3 | No filed feature owns it | **PASS** | Sweep over **959** feature contracts + HANDOFFs: `inp-adults` → **0 hits**; `toFixed` → **0 hits**. Feature **423** owns the **schema-side** composition rule; feature **414** owns the **route-side** capacity rule. **Neither says anything about the form's own bounds.** |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **414** = party vs table seats, enforced in the router. **423** = `party_size == adults + children`, enforced in the schema. **This slice = the form's bounds agree with the API's.** Three different enforcement points, three different artefacts. |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported it — **the mock-up has zero `fetch()` calls**, so the form never reaches the API. **Yet.** |
| 6 | It is cheap now and expensive later | **PASS** | One attribute, one validation block, one shared constants object. **No schema change.** Expensive later: the moment the surface is wired, every `adults=0` submission is a **`400` round trip** and every `children=20, party_size=1` is a **constraint violation** — on the two busiest flows in a restaurant. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it DOES fire** | Feature **423** is about to add the schema-side equality rule, and feature **414** is about to add the capacity check **to the same validation block in `tables.py`** that this slice reads. **This slice must land with or after 423, and must cite both.** |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as the other two picks of this pass: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `index.html` | **The seat modal's `min`/`max` attributes + the client-side validation** | **Derive the bounds; do not hand-write them again.** The literal `min="0"` on `Adults` must not survive. |
| `backend/app/config.py` | **The seating bounds, in one place** | The charter §7 names this home: *"No magic numbers … all in `config.py` or `services/`"*. **Read the feature's Open questions 1 — the implementer must record where the shared source lives and why.** |
| `backend/app/routers/tables.py` | **Nothing — the guards are correct as written** | **This slice must NOT relax or tighten the API's guards.** The API is the authority; the form catches up. **Check 7 asserts this file is untouched.** |
| `features/08-index-mockup.md` | **One line** — record that the form's bounds must match the API's | So the informal spec and the contract agree. |
| `features/423-…` and `features/414-…` | **One line each** — name this feature | Both own rules this slice mirrors client-side. |

**Do NOT touch:** `backend/app/models.py` (423 owns the schema rule; 414 owns the capacity rule), `backend/app/routers/tables.py` (feature 388 owns the status guard; 414 owns the capacity check), the bill modal's arithmetic (**feature 465**), the floor grid (feature 24), the fixture's status values (**feature 467**).

## 4. The implementation, in order

1. **Decide and record where the shared source of truth lives.** Recorded default: **`backend/app/config.py`**, with the page receiving the values at render time and keeping a checked-in fallback so the file still opens standalone (feature 08 values the single-file property). **Do not start implementing before the decision is recorded.**
2. **Add the seating bounds to `config.py`** — `party_size {min:1,max:20}`, `adults {min:1,max:20}`, `children {min:0,max:20}`, plus the two rules. **Cite features 423 and 414 in the comment.**
3. **Make the seat modal's `min`/`max` attributes derive from those bounds** — set them in JS at load, or render them server-side. **The literal `min="0"` on `Adults` must not survive.**
4. **Add the client-side validation, in the same order as the API's, with the same messages:**
   - `adults < 1` → *"Need at least 1 adult"*
   - `adults + children < party_size` → *"adults + children must cover party_size"*
   - `adults + children > party_size` → *"adults + children must equal party_size"* (feature **423**'s equality rule, mirrored)
5. **Add the `children ≤ party_size` constraint**, which the API's current two guards do **not** express. **The form permits `party_size=1, adults=1, children=20` today and the API accepts it too — this is the shared blind spot.**
6. **Disable the confirm button** while the party is invalid, and show the reason.
7. **Write the regression test first** — it must fail on today's file.
8. **Add one line to features 08, 423 and 414.**

## 5. The four things that will go wrong if nobody tells you

1. **Hard-coding the bounds into the HTML again.** That is how `min="0"` got there in the first place: `Party size` carries `min="1"` (the API's rule mirrored) and `Adults` carries `min="0"` (the API's rule **not** mirrored). **Hard-coding them a second time guarantees the same divergence returns.** **Derive them.**
2. **Leaving `children` bounded absolutely (`max=20`) rather than relatively.** `Party size` is capped at 20 and `Children` is capped at 20 **independently**, which is exactly what permits `party_size=1, children=20`. **The cap must be `children ≤ party_size`.**
3. **Tightening the API's guards.** It is tempting, since the form now knows more. **Do not.** The API's guards are **lower bounds** and are correct as written; the composition **equality** is feature **423**'s decision, not this slice's. **Recorded default: the API is untouched; check 7 asserts it.**
4. **Editing `index.html` without knowing features 465, 467 and 24 are in it.** **Four features touch this file.** The regions are disjoint — **the seat modal's inputs** (this), **the bill modal's arithmetic** (465), **the fixture's statuses** (467), **the floor grid** (24) — but **a rebase is required.** Say which landed first in your report.

## 6. Verification protocol

Four offline commands, plus the executed test:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The literal 'min="0"' on Adults must be GONE.
grep -c 'id="inp-adults"[^>]*min="0"' index.html    # must be 0

# 2. No number input may carry a hand-written min/max that duplicates a rule.
grep -nE 'id="inp-(party|adults|children)"' index.html
#    -> every one must have its bounds derived, not written as a literal

# 3. The composition rule is mirrored (feature 423's equality).
grep -c "must equal party_size" index.html           # must be >= 1

# 4. The API's guards are UNCHANGED — this slice must not have relaxed them.
git diff backend/app/routers/tables.py | wc -l        # must be 0

# 5. The corpus agrees: the form's bounds rule is now owned.
grep -rl "inp-adults" features/ specs/ | wc -l        # must be >= 1 (this feature)
```

**The executed test** — enumerate every `(party_size, adults, children)` triple **the form accepts** and assert the API's own guards accept it too:

```python
for party_size in range(1, 21):
    for adults in range(0, 21):
        for children in range(0, 21):
            if form_accepts(party_size, adults, children):
                assert party_size >= 1
                assert adults >= 1              # <-- FAILS on today's min="0"
                assert adults + children >= party_size
```

**It must fail on today's file** (the `adults = 0` case) and pass after.

**The negative control** — re-introduce `min="0"` on `Adults` and confirm the test's **exit code flips 0 → 1**. A check that has only ever passed proves nothing.

**Record in the HANDOFF:** where you put the shared bounds and why; whether the form now mirrors feature 423's equality rule; and **that `backend/app/routers/tables.py` is untouched** (check 4).

## 7. Rollback path

**Fully reversible in one step.** `git revert <the commit>`.

**No data is at risk** — the mock-up writes nothing. **No schema change, no migration, no backfill. No API change** — check 4 asserts `backend/app/routers/tables.py` is untouched, so the server's behaviour is identical before and after.

**The rollback is visible and harmless**: the form's `min` attribute returns to `0`. Because nothing is wired, **no operator ever sees the difference.**

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (strings, enums, money, timestamps).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-frontend` — the front-end conventions.
5. `le31-backend` — the FastAPI/SQLModel conventions.
6. `le31-handoff-spec` — the handoff format itself.
7. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these four feature contracts in full before you start:**

- `features/423-le31-party-composition-first-party-party-size-is-never-checked-against-adults-plus-children-so-party-size-2-is-accepted-for-four-adults-v1-party-composition-rule.md` — **owns the equality rule you mirror.** It must land first, or in the same PR.
- `features/414-le31-table-capacity-first-party-party-size-is-never-compared-to-table-seats-so-a-party-of-12-is-seated-at-a-4-seat-table-v1-table-capacity-rule.md` — **owns the capacity check, in the same validation block you read.**
- `features/388-le31-table-state-machine-first-party-table-has-no-status-column-…md` — **owns the table-status guard on the same route.** Its *Out of scope* says the UI is *"feature 01's scope"* — this feature supplies the missing contract for that surface.
- `features/24-visual-table-layout-v2.md` — **the other `index.html` editor.**

## 9. The one thing that matters

**The form is where the waiter makes the decision; the API is where the decision is refused.** LE31 built the refusal carefully — two guards with human-readable messages — and then built a form that can produce inputs both guards reject.

**The error is not "the number is slightly off". It is "the waiter enters a party, presses Seat, and is told no"** — with a customer waiting at the table, after the waiter has already filled in the party size. And the second case is worse: `party_size=1, adults=1, children=20` is accepted by **both** surfaces today. That is not a divergence — it is a **shared blind spot**, and feature 423 will fix only the *storage* of that row, not the fact that the waiter was **offered** it.
