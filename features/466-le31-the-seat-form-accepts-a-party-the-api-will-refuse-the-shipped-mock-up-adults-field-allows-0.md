# Feature 466 — The seat form accepts a party the API will refuse: the shipped mock-up's `Adults` field allows 0

> **Pick B of Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own shipped waiter surface and in its own API, and it is proved by EXECUTION and by PARSING the shipped files**, not by reading.
>
> `index.html` is the shipped waiter UI (30,530 bytes / 720 lines), mounted at `/` by `backend/app/main.py`. Its seat-party modal contains three number inputs. Parsed out of the shipped file on 2026-11-10:
>
> ```
> Party size      id=inp-party     min=1   max=20   value=2
> Adults          id=inp-adults    min=0   max=20   value=2
> Children        id=inp-children  min=0   max=20   value=0
> Amount paid (€) id=inp-paid      min=-   max=-    value=-
> ```
>
> **`Adults` has `min="0"`.**
>
> `backend/app/routers/tables.py`, `seat_party`, verbatim:
>
> ```python
> if party_size < 1 or adults < 1:
>     raise HTTPException(400, "Need at least 1 adult")
> if adults + children < party_size:
>     raise HTTPException(400, "adults + children must cover party_size")
> ```
>
> **The API refuses `adults = 0`. The form's own lower bound says `0` is fine.**
>
> **And the second input is worse: `Children` has `min="0"` with no upper bound, while `Party size` is capped at 20 — so the form permits `party_size=1, adults=1, children=20`, which the API's second guard accepts** (`adults + children = 21 ≥ party_size = 1`).
>
> **Why the corpus does not own it.** A corpus-wide sweep over 959 feature contracts and HANDOFFs returns **zero** hits for `inp-adults` and **zero** hits for `toFixed`. Feature **423** (`le31-party-composition…`) owns the **schema-side** rule that `party_size` must equal `adults + children`; feature **414** (`le31-table-capacity…`) owns the **route-side** rule that a party must fit the table's seats. **Both are rules about the API. Neither says anything about the form the waiter actually fills in** — and the form is where the input is *chosen*, not merely validated.
>
> **Bucket: v1.** Verdict: **`build`**. Evidence class: **OBSERVED** (parsed from the shipped file; the API guard quoted verbatim from the shipped router). Confidence: **high** for the defect (both numbers are read straight out of the two shipped files); **medium** for the demand (no operator has reported it — but the mock-up is the **only** waiter surface that exists, so there is no other surface on which it could have been seen).

## Goal

Make **the form's own bounds agree with the API's bounds**, so that every party a waiter can enter is a party the API accepts, and every party the API refuses is one the form prevents.

The concrete outcome: **the seat modal's `min`/`max` attributes are derived from one shared source of truth — the same rules the API enforces — and a party that the API would refuse cannot be submitted from the UI.**

**The single sentence this feature exists to make true:** *the form cannot produce a request the API will reject.*

## Scope

**In scope (v1):**

- **One source of truth for the seating bounds**, held where both surfaces can read it. Since the mock-up is a **no-build, single-file** page (§4.1: *"vanilla HTML + JS. No build step; serves directly from FastAPI"*), the shared source must be either a **JSON file served next to `index.html`** or **a small set of constants in `index.html` that the API imports** — the implementer must pick one and say why.
- **The seat modal's `min`/`max` attributes are set from that source**, not hand-written. The literal `min="0"` on `Adults` must not be able to drift from the API's `adults < 1`.
- **The `Children` input must be bounded relative to `Party size`** — the form currently allows `children=20` with `party_size=1`, which no restaurant has and which the API's composition rule (feature **423**) is about to forbid at the schema.
- **A rule that the browser can check before submitting** — the same three rules the API has, in the same order, so the message the waiter sees matches the message the API would have returned.
- **An assertion set** that fails on today's `index.html` and passes on the fixed one.

**Explicitly NOT in scope:**

- **The API's own guards.** `backend/app/routers/tables.py` is correct as written — `adults < 1` is refused there. **This slice changes no Python file.** The API is the authority; the form must catch up.
- **The schema-side composition rule.** That is feature **423** — filed.
- **The capacity rule (party vs table seats).** That is feature **414** — filed. **This slice must not add a capacity input to the form**; it must only make the form's *existing* bounds agree with the API. If 414 adds a capacity check, this slice's bounds must be extended to include it — see *Dependencies*.
- **The table's status check** (seat a table that is already occupied). That is feature **388** — filed.
- **Any change to the form's *visual* design**, its layout, its three views, or the rest of the modal.
- **Any change to `features/08-index-mockup.md`'s visual spec.**

## Description

### The two shipped files, side by side

**`index.html` (the form the waiter fills in), parsed 2026-11-10:**

```
Party size      id=inp-party     min=1   max=20   value=2
Adults          id=inp-adults    min=0   max=20   value=2
Children        id=inp-children  min=0   max=20   value=0
```

**`backend/app/routers/tables.py` (the API that receives the form), verbatim:**

```python
if party_size < 1 or adults < 1:
    raise HTTPException(400, "Need at least 1 adult")
if adults + children < party_size:
    raise HTTPException(400, "adults + children must cover party_size")
```

### ⭐ The first divergence: `adults = 0`

`min="0"` on `Adults` means the browser's own number-input widget permits `0`. A waiter who clears the field and types `0` gets a **client-side-valid** form that the API then rejects with **`400 "Need at least 1 adult"`**.

**This is the worst kind of form error**: the input is marked valid by the widget, the submit button is enabled, and the rejection arrives **after** the waiter has filled in the party size and moved on. The API's message is correct and unhelpful at the same time — from the waiter's point of view the form let them do something and then refused it.

**The asymmetry is the tell.** `Party size` has `min="1"` — the author *did* carry the API's `party_size < 1` rule into the widget. `Adults` has `min="0"` — the author did **not** carry the `adults < 1` rule across. **Two guards in the API, one of them mirrored into the form.** The one that was missed is the one that bites.

### ⭐ The second divergence: `children` is unbounded against `party_size`

`Party size` is capped at `max="20"`. `Children` is capped at `max="20"` **independently**. So the form permits:

```
Party size = 1, Adults = 1, Children = 20
```

**Twenty children at a table for one.** The API's second guard (`adults + children < party_size`) checks a **lower** bound only — `1 + 20 = 21 ≥ 1` — **so the API accepts it too.**

**Both surfaces agree on this one, and both are wrong.** Feature **423** (`le31-party-composition…`) owns the schema-side rule that `party_size` must equal `adults + children`, which will refuse this row — **but that is a schema rule, and it produces a database error, not a form error.** The waiter still gets a form that offers a nonsensical party and a rejection that arrives as a constraint violation rather than as an explanation.

### ⭐ Why the form is the right place to fix the second one

The API cannot reject `children=20` with `party_size=1` under its current two guards without also rejecting legitimate cases — the guards are **lower bounds**, and the composition rule is an **equality**. Feature 423's equality rule is the right rule, but it is enforced at the database. **The form can enforce it at the point of entry, where the waiter can still be told what to change.**

**This is the same "write-side vs read-side" distinction the corpus has already filed** (features 431, 455, 460 — canonicalisation and uniqueness at the write site, not at read time), applied to a form instead of a row.

### The cost of leaving it

**Today the cost is near zero, and that is exactly why it must be fixed now.** The mock-up has **zero `fetch()` calls** — it never reaches the API. So the divergence between the form and the API is currently invisible.

**The moment the surface is wired** — which `features/08-index-mockup.md` states is the intent (*"When the real backend exists, the same HTML can be served by FastAPI"*) and `main.py` has already done the mounting for — every `adults=0` submission becomes a **`400` round trip** and every `children=20, party_size=1` becomes a **constraint violation**. Both are **user-visible errors on the two most common flows in a restaurant**: seating a party and billing it.

**And the fix is one attribute on one input today.** It becomes a multi-surface reconciliation the day the API and the form are both live and both evolve.

## Data model

**No schema change. No Python change. No new table, no new column.**

The change is in `index.html`'s seat modal, plus **one shared constants object** that both the form and the API read.

**The shape:**

```
seat-rules.json  (or a constants block in index.html)
  {
    "party_size":  { "min": 1, "max": 20 },
    "adults":      { "min": 1, "max": 20 },
    "children":    { "min": 0, "max": 20 },
    "max_party":  20,
    "require_adults_at_least_one": true,
    "require_adults_plus_children_equals_party_size": true
  }
```

**Three decisions the implementer must make and record:**

1. **Where does the source of truth live?** If it is a **JSON file served next to `index.html`**, the API must read it from disk at import time — a **new runtime dependency of the backend on a static asset**, which is a real coupling and may be the wrong trade. If it is **a Python module that generates the JS**, the page is no longer a single self-contained file, which `features/08` values (*"Single file vs. multi-file (separated CSS/JS)? Single is easier to share."*). **Recorded default: the constants live in `backend/app/config.py`** (which the charter §7 names as the home for exactly this — *"No magic numbers. Tax rate, tip rounding rules, buffer factors — all in `config.py` or `services/`"*), **`index.html` receives them at render time**, and the single-file property is preserved for the *static* case by keeping a checked-in fallback. **The implementer must state which they chose and why.**
2. **Does the browser re-check, or does the server only check?** Recorded default: **both** — the browser checks so the waiter is told immediately, and the server still checks because the browser's check is not a guarantee. **The server's guards stay exactly as they are.**
3. **Is the `children` bound relative or absolute?** Recorded default: **relative** — `children ≤ party_size` and `adults + children == party_size` (feature 423's equality rule, mirrored client-side). **An absolute `max=20` on children is not enough**, as the `party_size=1, children=20` case shows.

## Implementation steps

1. **Add the seating bounds to `backend/app/config.py`** (or the chosen single home) with a comment citing **feature 423** (composition) and **feature 414** (capacity).
2. **Make the seat modal's `min`/`max` attributes derive from those bounds** — set them in JS at load, or render them server-side. **The literal `min="0"` on `Adults` must not survive.**
3. **Add the client-side validation**, in the same order as the API's, with the same messages:
   - `adults < 1` → *"Need at least 1 adult"*
   - `adults + children < party_size` → *"adults + children must cover party_size"*
   - `adults + children > party_size` → the **equality** rule (feature 423), stated as *"adults + children must equal party_size"*
4. **Add the `children ≤ party_size` constraint**, which the current API guards do not express.
5. **Disable the confirm button** while the party is invalid, and show the reason — the waiter should not be able to submit a party the API will refuse.
6. **Add the assertion set** below.

## Telegram interaction if any

**None.** This slice touches the waiter surface only. The cook bot has no seat flow — feature **414** states this explicitly: *"The cook bot has no seat flow, and the charter's two-role split puts table seating on the waiter surface exclusively."*

## Dependencies

- **Feature 08** (`08-index-mockup.md`) — the informal spec for `index.html`. This slice adds one constraint to it (the form's bounds must match the API's) and does not rewrite it.
- **Feature 423** (`le31-party-composition…`) — owns the **schema-side** equality rule `party_size == adults + children`. **This slice mirrors that rule client-side.** 423 must land first, or in the same PR, or the two rules will disagree.
- **Feature 414** (`le31-table-capacity…`) — owns the **route-side** capacity rule (party vs table seats). **414 puts its check "at the seating write site (backend/app/routers/tables.py, seat_party), next to the two validations already there"** — i.e. in the same block this slice is reading. **⚠️ 414 and this slice touch the same two lines' neighbourhood.** They are complementary (414 adds a check; this slice makes the *form* match), and they must not be developed in parallel without a rebase.
- **Feature 388** — owns the table-status guard on the same route. **Explicitly puts `index.html` out of scope.**
- **Feature 460** — owns `Table.section` (the floor map's grouping). Independent.
- **Feature 465** (this pass's Pick A) — owns the **money** arithmetic in the same file. **⚠️ FILE-LEVEL COLLISION**: 465 edits the bill modal's arithmetic; this slice edits the seat modal's inputs. **Different regions of `index.html`; the implementer must say which lands first.**
- **Feature 24** (`visual-table-layout-v2`) — an `index.html` rewrite of the floor grid. **⚠️ FILE-LEVEL COLLISION with this slice too.**

## Open questions

1. **Where does the shared source of truth live?** Recorded default: **`backend/app/config.py`**, with the page receiving the values at render time and keeping a checked-in fallback so the file still opens standalone. **The implementer must record the choice and its cost.**
2. **Should the form enforce the equality rule (`adults + children == party_size`) even though the API only enforces the lower bound?** Recorded default: **yes** — feature 423's schema rule makes the equality the truth, and the form should tell the waiter *before* the database does. **But this is a behaviour change at the form, and the implementer must say whether the API's weaker guard is left as-is or tightened.** **Left as-is** is the recorded default, because tightening the API is feature 423's decision, not this slice's.
3. **What is the maximum party?** The form says `20`; the charter says *"≤40 seats"* for the restaurant, so `20` is a *per-table* cap and not the room's. **Recorded default: keep `20`**; the cap is a table question and feature 414 owns it.
4. **Should `max=20` on `Children` remain?** Recorded default: **no** — it should be derived (`≤ party_size`), because an absolute cap is what produced the `children=20, party_size=1` case.
5. **Does this slice touch the bill modal's `Amount paid` input?** **No** — that is feature 465's money territory, except that 465's `money.parse` must not change the *bounds*. **Say so in the PR.**
6. **What about `party_size` vs `adults` when `children` is the whole party (a children's party)?** Recorded default: **out of scope** — the API's rule (`adults >= 1`) is the current truth and this slice does not change it.

## Why this matters

**The form is where the waiter makes the decision; the API is where the decision is refused.** LE31 has built the refusal carefully — two explicit guards with human-readable messages — and then built a form that can produce inputs both guards reject.

**That is not a cosmetic mismatch.** It is the difference between *"the waiter cannot enter this"* and *"the waiter enters it, presses Seat, and gets told no."* The second one costs a customer waiting at the table.

**And there is a second, quieter cost.** `party_size=1, adults=1, children=20` is accepted by **both** surfaces today. That is not a divergence — it is a **shared blind spot**: a form that offers a party of twenty-one for a table of one, and an API that agrees. Feature 423 will fix the *storage* of that row; **this slice fixes the fact that a waiter was offered it.**

**It is free today because the mock-up is not wired.** Zero `fetch()` calls. The moment it is wired, these are **production errors on the two busiest flows in a restaurant** — seating a party and billing it — and they will be found by the owner on the first busy Saturday, not by a test.

**The fix is one attribute and one validation block.** It is a **one-file, one-region change** to a file that nothing depends on. That is the cheapest defect in this whole corpus, and the cheapest defects are the ones that must be taken before the surface goes live.

## Adjacent evidence

**Third-party instruments — read in the raw fetch, no code adopted:**

- **`nikolaosmanhss-png/pantrytrack`** (MIT ✓, ★3 / ⑂3, created 2026-11-09, Python/SQLite — *"Open-source stock and food-waste tracker for small restaurants and cafes"*) — the closest domain match in the fresh 2026-11-10 pool. **Recorded, not adopted**: ★3 is **no traction evidence**, and its food-waste model is feature **432**'s sign-matrix territory, not a form-validation territory.
- **`salhiworks/sorrel-restaurant-starter`** (MIT ✓, ★1, created 2026-11-09) — a Next.js restaurant starter with a Supabase backend. **Not adopted: LE31's stack is FastAPI/SQLModel/vanilla HTML (§4.1).**
- **`farulivan/roomflow`** (MIT ✓, ★1, created 2026-10-20 — *"Guest-service dashboard for hotel staff"*) — a **staff-facing** dashboard with request forms. **Adjacent in shape (a form that must not accept impossible input) but for a different domain; recorded, not adopted.**

**⭐ THE GENUINE DUPLICATES, MARKED AND SKIPPED (not re-picked):**

- **`AlgoVyn/bikri`** (MIT ✓, ★1 / ⑂0) — 11 corpus files cite it. **Skipped.**
- **`baba-dev/menuminute`** (MIT ✓, ★1 / ⑂0) — 3 corpus files cite it. **Skipped.**
- **`manoranjan2050/RestoPro-ERP-Web`** (MIT ✓, ★1 / ⑂0) — 7 corpus files cite it. **Skipped.**
- **`ahmerahdev/karobar-erp`** (MIT ✓, ★3) — multi-tenancy is **§3.2's explicit non-goal**. **Skipped on scope.**
- **`famalthtechnologies/famalth-lynx-pos`** (Apache-2.0 ✓, ★3) — 2 corpus files cite it. **Skipped.**
- **`ferret-project/ferret`** (MIT ✓, ★18) — a home-inventory app. **Not adopted.**
- **`kavineksith/INSOPHINIA-POS-v7-Java-MySQL-Multi-Platform-Edition`** (Apache-2.0 ✓, ★1, created 2026-11-09) — a Java Spring Boot POS with React/JavaFX. **Not adopted: wrong stack (§4.1) and ★1 is no traction evidence.**
- **`opensourcepos`, `NexoPOS`, `n8n`, `medusajs`, `saleor`, `strapi`, `nocodb`** — created **before the window** and/or licence-incompatible. **§3.2 blockers. No code adopted.**

**The HN family produced no signal for this pick** — 20 in-window hits, 0 promoted, titles such as *"Show HN: Tablet menu that works without internet"* and *"Show HN: A no-code POS for pop-up shops"*. **Soft for the eighth consecutive pass.**

## Verification protocol

**All checks run against the FILE, offline. No network, no database.**

```bash
# 1. The form's bounds are derived, not hand-written.
#    No number input may carry a hand-written min/max that duplicates a rule.
grep -nE 'id="inp-(party|adults|children)"' index.html
#    -> every one must have its min/max set by JS (or server-rendered
#       from the shared source), not by a literal attribute.

# 2. The literal 'min="0"' on Adults must be GONE.
grep -c 'id="inp-adults"[^>]*min="0"' index.html   # must be 0

# 3. The form cannot produce an API-rejected party.
#    For every (party_size, adults, children) the form accepts, the API's
#    own guards must accept it too.
node -e '<enumerate the form-accepted range; check both guards>'
#    -> for each accepted triple:
#         assert party_size >= 1
#         assert adults >= 1
#         assert adults + children >= party_size

# 4. The composition rule is mirrored (feature 423's equality).
grep -c "must equal party_size" index.html        # must be >= 1

# 5. The corpus agrees: the form's bounds rule is now owned.
grep -rl "inp-adults" features/ specs/ | wc -l     # must be >= 1 (this feature)

# 6. Nothing outside index.html (and the chosen rules home) changed.
git diff --name-only | grep -vE "^(index.html|backend/app/config.py)$" | wc -l

# 7. The API's guards are UNCHANGED — this slice must not have relaxed them.
git diff backend/app/routers/tables.py | wc -l     # must be 0
```

**The negative control** must be run on check 3: re-introduce `min="0"` on `Adults` and require the check's exit code to flip **0 → 1**. A check that has only ever passed is not evidence it works.

## Rollback path

**Revert one file** (plus the shared rules home if one was added). `git revert <the commit>`.

- **No data is at risk** — the mock-up writes nothing.
- **No schema change, no migration, no backfill.**
- **No API change** — check 7 asserts `backend/app/routers/tables.py` is untouched. The server's behaviour is identical before and after.
- **Fully reversible in one step.**
- **The rollback is visible and harmless**: the form's `min` attribute returns to `0`. Because nothing is wired, **no operator ever sees the difference.**
