# HANDOFF — Feature 390: record `Pantry`'s recipe-consumption snapshot — the order line remembers what was deducted, not what the recipe says today

**This is a `defer` pick, it is DOCUMENTATION-ONLY, and it is BLOCKED behind feature 359.** There is no code to write. The deliverable is the feature file itself. **If you are about to open a code editor, stop — this feature is finished the moment `features/390-…md` exists, and it must not be implemented until feature 359 lands.**

**Discovery chain:** Daily Research 2026-10-27 → the parent's GitHub candidate sweep produced `bhargavkalita47/Pantry` (licence `null`, ★0/⑂0, 53 KB, JavaScript/Node 24, created AND pushed 2026-10-26 — a same-day repo) → the parent fetched its README raw → and found, under "Engineering decisions", *"**Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities.**"* plus *"Operation IDs prevent duplicate deductions when retrying a request."* → the parent then checked the two things that decide whether this is a real gap or a duplicate: `grep -n -i "snapshot\|cancel\|reverse\|restore\|revert" features/359-*.md` (**no output**) and `grep -rn -i "recipe\|ingredient\|bom" backend/app/` (**no output**).

**Full evidence record: `features/390-bhargavkalita47-pantry-mit-null-licence-recipe-based-inventory-idempotent-deduction-order-recipe-consumption-snapshot-v1-recipe-consumption-snapshot-vocabulary.md`**

## Active feature path

`features/390-bhargavkalita47-pantry-mit-null-licence-recipe-based-inventory-idempotent-deduction-order-recipe-consumption-snapshot-v1-recipe-consumption-snapshot-vocabulary.md` — **defer** (Pick C of Daily Research 2026-10-27).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When a recipe changes after a sale, the owner wants the earlier sale's quantities to stay as they were, but struggles because the model has no snapshot concept, so that a cancellation reverses exactly what was deducted.* Links to feature **359** — **but not the same gap**: 359 specifies the depletion; 359 says nothing about what an already-deducted order line remembers after the recipe changes. **Pass on reported evidence, not observed pain.** |
| 2 | Viability | ✓ | A snapshot field on the order line is a normal modelling move, with no operator-facing configuration. **Pass.** |
| 3 | Practicability and confidence | ✓ | Licence `null` → the **shape** is transferable, the **code** is not (§3.2). The specific claim is a **data-shape** claim, so §3.2 does not block it as vocabulary. **Named rabbit hole:** LE31 has **no recipe or ingredient concept at all** (`grep -rn -i "recipe\|ingredient\|bom" backend/app/` → no output; `MenuItem` has no recipe link; `Batch` is a *prepared output*, not a *recipe*). So the sentence has **no subject in LE31 yet** — it depends on 359 landing first. **Pass, conditional on 359.** |
| 4 | Conflict | ✓ | None. It would **strengthen** §3.3 (stock is derived from entries) by making the *derivation inputs* immutable. **Adjacent, not bundled:** the ledger-write idempotency rule is feature 382's; the order-state rule is feature 388's; the batch-provenance question is feature 385's. |
| 5 | Outcome + appetite + scope | ✓ | v1 vocabulary, **one sentence**: *"the order line records what was deducted, not a live reference to the current recipe."* **Explicitly NOT in scope:** any `Recipe`/`RecipeComponent`/`Ingredient`/`Depletion` model (359's subject), any change to `MenuItem`, any cancellation/void/comp flow, any schema or code change. |
| 6 | Cost to operational value | ✓ | Near-zero cost; the value is real but small, and it is **blocked behind 359** — stacking a vocabulary note on an experiment is how dependency chains form with nobody owning the root. **Pass, low value → `defer`.** |
| 7 | Circuit breaker + reversibility | ✓ | A vocabulary note. **Delete it and nothing is lost.** No data, no migration, no retained state. **Trivially reversible.** |

**Gate verdict: `defer`** — check 1 passes on **reported** evidence (the repo states the design), confidence **low** (a same-day, ★0, unlicensed repo with no traction evidence). **The premise is also unproven: if the depletion already writes one ledger row per deduction, the snapshot may be *implicit* and this pick may be recommending a concept that is not needed.**

## Bucket

**v1 (consumption-provenance vocabulary — a documentation reference)** — Pick C of Daily Research 2026-10-27. The subject is LE31's v1 stock-derivation rules, so the matching project would be **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on 2026-10-27 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **40th consecutive day**), the sub-issue has no parent to hang under — it is routed to **`le31 Research` (P-HMM-1)** in the fallback payload (the parent research issue's own project), and **no project attachment actually occurred**.

## Files to touch

**Exactly one file — and it already exists:**

- `features/390-bhargavkalita47-pantry-mit-null-licence-recipe-based-inventory-idempotent-deduction-order-recipe-consumption-snapshot-v1-recipe-consumption-snapshot-vocabulary.md` — **this is the deliverable. It is complete.**

**Do NOT touch (out of scope, explicitly):**

- `backend/` — **any file, for any reason.** `git diff --stat backend/` must be **empty** after this slice. This is the load-bearing check for a documentation-only pick.
- **`features/359-dollyzn-react-menu-…`** — **this feature points at 359; it does NOT edit 359.** If 359's author wants to adopt the snapshot sentence, that is a change to 359, made by 359's owner, with its own review.
- `PROJECT_CHARTER.md` — **no change required.** If you touch it, the only permitted edit is a pointer to this feature.
- Any other feature contract — **no cross-edits.**
- `docs/`, `research/` — **do not create a second copy of this mapping in another folder.** One copy, in the feature tree.
- `backend/requirements.txt` — **no dependency change.** `Pantry` is **not** added as a dependency, a submodule, or a vendored directory. **It is read as a text.**
- **No `Recipe`, `RecipeComponent`, `Ingredient` or `Depletion` model. No `MenuItem` change. No cancellation/void/refund flow.** These are the exact things this slice must not create.

## The load-bearing tests

**There are no runtime tests for this slice — and that is the point.** The checks are:

1. **`git diff --stat backend/` is empty.** The load-bearing check. A documentation pick that touches code has smuggled scope.
2. **The dependency is stated and the subject is absent.** The feature must state that LE31 has no recipe concept, and the greps proving it must be reproducible.
3. **The non-duplication claim is backed by a grep.** `grep -n -i "snapshot\|cancel\|reverse\|restore\|revert" features/359-*.md` → **no output.** Without that, "this is not a duplicate" is an assertion.
4. **No claim of traction.** ★0/⑂0, same-day repo, licence `null`, and the feature must say so plainly. **A vocabulary pick that implies demand is a defect.**
5. **The operation-id claim is recorded as evidence, not filed as a feature.** It must appear as the third arrival at the idempotency convergence, alongside features 382 and 388 — **not** as new scope.

If the parent wants an automated check for (1):

```bash
cd /opt/data/le31_mmm3_research_work
git diff --stat backend/
# expect: EMPTY
```

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. **For a documentation-only pick, the observable behaviour is that the document exists, says what it claims, and that nothing else moved.**

**The pre-flight (parent-run on 2026-10-27; re-run it to confirm the source is as recorded):**

```bash
cd /tmp/le31-daily-2026-10-27/gh/readmes

# 1. the snapshot claim, verbatim
grep -n "recipe-consumption snapshots\|later recipe edits do not change" bhargavkalita47__Pantry.md
# expect: a hit — the sentence quoted in the feature

# 2. the operation-id claim, verbatim
grep -n "Operation IDs prevent duplicate deductions" bhargavkalita47__Pantry.md
# expect: a hit

cd /opt/data/le31_mmm3_research_work

# 3. LE31 has NO recipe concept — the reason this is blocked
grep -rn -i "recipe\|ingredient\|bom" backend/app/
# expect: NO output
grep -n "class MenuItem" -A 10 backend/app/models.py
# expect: id, name, category, unit_price, unit, is_prepared, photo_url — NO recipe link

# 4. NOT a duplicate of feature 359
grep -n -i "snapshot\|cancel\|reverse\|restore\|revert" features/359-*.md
# expect: NO output

# 5. the "Pantry" match in the feature tree is INCIDENTAL, not a prior Pantry pick
grep -rn -i "pantry" features/ specs/
# expect: only feature 370 — and there it is about a DIFFERENT project:
#   "its domain is a household pantry, not a restaurant floor"
grep -n "household pantry" features/370-*.md
# expect: a hit — confirming the match is incidental

# 6. the sibling first-party finding this mirrors
ls features/385-le31-order-item-batch-provenance-*.md
# expect: the file — read it; the framing transfers, the domain does not
```

**Note on the source-of-truth for the quoted text:** the **README is authoritative** where it contradicts the GitHub `description` field. **The README was what was quoted**; the description was used only for identity.

## Rollback path

- **Delete the feature file and its HANDOFF.** Nothing else changed. No data, no migration, no retained state, no configuration, no dependency.
- **If the mapping turns out to be wrong**, correct the feature file in place — there is nothing to unwind.
- **No consumer of this document exists yet.** No code reads it, no test asserts on it. It is safe to amend or remove at any time without consequence.
- **If feature 359 is rejected or abandoned**, this pick's dependency fails and it should be **re-evaluated, not deleted** — the snapshot question would still be open, just unmoored.

## Mandatory LE31 skill list for the coding agent

**This slice needs no coding agent.** It is documentation. The relevant skills are for whoever later reads it:

- `le31-conventions` — **read first** if you act on any of the open questions. The hard invariants and the seven-check gate are what the vocabulary is measured against.
- `le31-research` — for the evidence discipline the document follows (source URL, date, direct quote, confidence, limitations).
- `development` — **only if** the open questions are ever escalated into real work. They are not in scope here.
- `test-driven-development` / `pre-merge-review` — **not applicable** to this slice. There is no product code to review. **Do not fabricate a test suite to make a documentation pick look like an engineering task.**

## Open questions carried into any future build

1. **Where does the snapshot live — on the order line, or on the depletion record?** `Pantry` says *"orders retain recipe-consumption snapshots"* — on the order. But LE31's §3.3 model derives everything from `StockEntry` rows, so a snapshot could equally be *implied* by ledger entries that already exist. **Not decided here — it is feature 359's decision, and it must be made there, not retrofitted here.**
2. **Is a snapshot needed at all if the depletion is already a ledger row?** **This is why the pick is `defer` and not `build:** it is not yet known that a new concept is needed rather than an existing one being read correctly.*
3. **Should LE31 record a revision number on recipes?** `Pantry` mentions *"revision-guarded writes"* — a mechanism for concurrent recipe edits, not just a snapshot. **Out of scope**; §3.2 keeps single-location single-chef operations simple. Recorded only.
4. **Does a cancellation flow exist in LE31 v1 at all?** Features 05/14 (the bill) and a void/comp path are separate features. If there is no cancellation, there is no consumer for the snapshot. **Not verified this pass** — noted as an open question rather than asserted.

---

**Bottom line for the coding agent:** **there is no code in this slice, and it must not be implemented yet.** The feature file exists and is the deliverable. The single load-bearing check is `git diff --stat backend/` being empty. If you find yourself designing a `Recipe` model, an `Ingredient` table, or a cancellation flow, **stop — those are feature 359's subject and the bill feature's, and this slice explicitly proposes neither.**
