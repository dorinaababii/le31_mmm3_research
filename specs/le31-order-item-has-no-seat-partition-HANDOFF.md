# HANDOFF — 440-le31-order-item-has-no-seat-partition

> **Slice contract for the coding agent.** Produced by the 83rd LE31 daily-research pass (2026-11-05), Pick C.
>
> **Feature file**: `features/440-le31-order-item-has-no-seat-partition.md`
>
> **LE31 feature gate verdict**: **experiment** — the gap is **OBSERVED** (executed: `Visit` is one party at one table, `Bill.visit_id` is **unique**, `OrderItem` has no seat column, and the corpus probe for `order item seat` / `per-seat order` / `seat number on the line` / `split the bill across seats` / `seat-level order` returned **0 hits across all 471 feature files and all spec files** with a passing negative control). **But the PAIN is INFERRED, not observed** — there is no order-taking router and no bill router, so no order line has ever been taken and no bill has ever been closed in LE31. **The gate's rule for an assumed pain is: a small experiment, not a full feature. This contract IS the experiment.**
>
> **⛔ THIS SLICE HAS ONE STEP AND IT IS NOT CODE. See *Trigger policy* below.**

## Trigger policy

**This is an `experiment` contract, and the agent is NOT authorised to write product code.**

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, the non-goals list, and the **Privacy invariant**), §7 (the quality bar), and the **seven-check feature gate** (specifically the rule that *an assumed pain becomes a small experiment*).
3. Load **`le31-research-workflow`** — for the recorded-evidence discipline this contract depends on.
4. **Ask the owner the question**, exactly as written in the feature file:

   > *"Do you ever need to know which of the six coffees on a table was whose — or to split a bill between people at the same table?"*

   **Record the answer verbatim**, including any qualification ("only for groups of eight or more", "only at lunch, never dinner", "no, never").
5. **Branch on the answer** and do exactly what the feature file's *Implementation steps* say for that branch:

   | Answer | Next action |
   |---|---|
   | **No** | **Close the feature.** Append the answer and the date to the feature file. **No code. No column. No migration. No test.** The contract stays in the repository as a recorded decision. |
   | **Yes, sometimes** | **Re-scope.** Add the frequency evidence to the feature file, pick the shape from the candidate table, **re-run the `Cost to operational value` gate check** (it changes from "weak" to "measurable"), and write a **new** contract. |
   | **Yes, and here is what we actually need** | **Rewrite the contract to match.** The owner's actual need may not be a seat at all — it may be "the bill has to split three ways", or "one guest is paying for their own starter". **Write down what they actually said.** |

6. **Record the corpus evidence in the PR description** so the next pass does not re-derive it: the five probe phrases, their 0-hit results, the negative control, and the six adjacent features that do **not** own this ground.

**What the agent MUST NOT do** — this list is unusually important for an `experiment` contract, because the temptation to "just add the column" is exactly what the gate is designed to prevent:

- **Add a `seat` column to `OrderItem`, or any column to any table.** **No schema change is authorised in this slice.** The shapes in the feature file's *Data model* are **provisional candidates for the owner to choose between** — not a decision.
- **Add an index, a join table, a router, a service or a helper.** **There is nothing to build until the shape is decided.**
- **Write a test.** **There is nothing to test until the shape is decided.**
- **Create a guest table, a guest id, a guest name, or any per-person record.** **This is the charter's Privacy invariant and it is hard.** The seat is a **position at a table**, not a person. If the owner says a *name* is what they need, **that is a Privacy escalation, not a schema choice** — see Open question 4.
- **Touch `Visit.party_size`, `Visit.adults`, `Visit.children`, or `Table.seats`.** Features **414** and **423** own them.
- **Touch `Bill`, `Bill.total_due`, or the bill-closes-visit edge.** Features **435** and **415** own them. **A per-seat *bill* is a different feature and is not proposed.**
- **Touch `Table`, the floor map, or the seating UI.** Feature **388** owns table state; the floor map is out of scope.
- **Build a "split the bill" feature.** Not proposed — and **the answer to the question may be "only the bill split, not the seat"**, which is a different product.
- **Propose tip pooling.** Charter §3.2 non-goal.
- **Re-derive the corpus gap.** It is already proven and recorded in the feature file. **Do not spend the pass re-proving it.**
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **whether an order line can be attributed to an individual seat at a table**. It is **not** about the party count (414), the party composition (423), which lines a bill charged (435), the bill-closes-visit edge (415), table state (388), the active-visit write guard (436), order-line insertion time (430), or guest identity (charter §3.2).

## Frozen contract

**The one thing this contract exists to make true:** *whether LE31 needs per-seat attribution on an order line is a question for the owner, and the answer must be recorded rather than assumed.*

Concretely, after this slice lands:

1. **The question is asked** and the answer is **recorded verbatim** in the feature file, with the date and who answered.
2. **No schema change is made** unless the answer selects a shape — and the shape selection is **the owner's**, not the agent's.
3. **The recorded answer is one of exactly three outcomes**, each with its own recorded next step: *no → closed*; *sometimes → re-scoped*; *yes-and-here-is-what-we-need → rewritten*.
4. If the outcome is *no*, **the repository gains a documented reason not to build a thing** — which is the same class of artefact as a documented reason to build it, and is worth keeping.

**The prohibition:** *guessing at a product decision and writing a column for it.*

### Why the question comes before the column — the reasoning, recorded so it is not re-litigated

**The gap is real and uncovered. The need is unknown.** Those are two different statements, and the gate scores them separately:

- **The gap (OBSERVED, high confidence):** six coffees at one table are six `OrderItem` rows that LE31 cannot tell apart, on a `Bill` that is one aggregate for the whole visit. **Feature 430 independently records that five identical lines are "indistinguishable except by a surrogate key".**
- **The need (INFERRED, medium confidence):** the parent proved there is **no order-taking router and no bill router** in LE31, so **no order line has ever been taken and no bill has ever been closed.** Nobody has ever asked for a seat.

**And the external evidence cuts both ways.** The most complete in-window restaurant-pos implementation the parent read in full — `Jmonczewski-droid/kisnet-pos` — has a floor map with `x`/`y` coordinates and **does not model seats**; it records a party and a table. **Two readings predict the same schema:** *the problem is rare*, or *the problem is real but solved elsewhere (by the waiter, by paper, or by simply not offering it).* **The corpus of the space cannot distinguish them. Only the owner can.**

**Meanwhile the strongest external signal in the window — `rkevrellan/ComandaPOS`'s *"cuentas separadas"* and *"mover líneas entre cuentas"* — suggests the problem is real somewhere, but solves it with an account that lines move between, which is closer to candidate 2 than to a seat number.** **That is evidence that the problem exists in the space, not evidence of the shape this restaurant needs.**

### The ordering problem — named in advance, because it would change the answer

**A party of six arrives together and does not sit in seat order.** A naive `seat: int` field therefore has to answer: *which physical seat, at which moment, relative to whom?*

The three candidate shapes in the feature file — a seat integer on the line, a free-text seat label on the line, or a seat assignment on the visit plus a reference on the line — **are all defensible, and the choice is the owner's operational reality, not a designer's preference.** **Even a "yes" does not settle the shape**, which is the second reason this is an `experiment`.

**Candidate 2 (a free-text seat label) may be guest identity and must be escalated, not inherited.** A name on an order line is PII about a person, and the charter says v1 stores counts, not identity. **If the owner needs a name, that is an owner decision made explicitly — recorded as such — not a design detail.**

## Files to touch

**This contract touches exactly one file:**

| File | Action | Notes |
|---|---|---|
| `features/440-le31-order-item-has-no-seat-partition.md` | **modify** | Record the answer verbatim, with the date and who answered. If the answer is *no*, append a closing note. **No other file is touched.** |

**Nothing else is modified.** In particular, **no file under `backend/` is touched, no test file is created, and no schema is changed.**

**If the outcome is "yes"**, the follow-up work is a **new** contract with its own file list, its own gate re-run, and its own rollback path. **It is not this contract, extended.**

## Mandatory LE31 skill list

The coding agent **must** load these before acting. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The seven-check gate, and specifically the evidence-precondition rule: *"An assumed pain becomes a small experiment, not a full feature."*** Also §3.2's non-goals and the **Privacy invariant**.
- **`le31-research-workflow`** — `skills/le31-research-workflow/SKILL.md`. **The recorded-evidence discipline** — this contract's whole output is a recorded answer, so the discipline about persisting evidence before recommending anything applies directly.
- **`le31-first-party-defect-proving`** — `skills/le31-first-party-defect-proving/SKILL.md`. **The execution-proof method**, so the agent understands what the parent's proof established and what it did not.

**Also read (not skills, but mandatory context):** `features/414-…`, `features/423-…`, `features/435-…`, `features/415-…`, `features/388-…`, `features/436-…`, `features/430-…`, and `PROJECT_CHARTER.md` §3.2.

**Note:** `development` / `speckit-*` / `pre-merge-review` are **not** required for this slice, **because no product code is written.** **They become required the moment the outcome is "yes" and a new contract is written.**

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.2 — the non-goals list and *"Capture of guest gender, age, or any PII beyond counts"* | repo root | **The hard filter.** It is also why a free-text seat label holding a name is an owner decision, not a schema choice. |
| `features/414-…` (party size vs table seats) | `features/` | **The party is not a seat.** |
| `features/423-…` (party composition) | `features/` | **The composition is not a seat.** |
| `features/435-…` (bill line membership) | `features/` | **The adjacent pair, and the feature most likely to interact with a seat reference.** |
| `features/415-…` (bill-closes-visit edge) | `features/` | The bill is one aggregate. |
| `features/388-…` (table state) | `features/` | Table state is not seat state. |
| `features/430-…` (order-line insertion time) | `features/` | **The disambiguation connection** — five identical lines are already indistinguishable. |
| `features/436-…` (active visit) | `features/` | The visit is the unit; a seat would live under it. |
| The proof script | `/opt/data/le31_proof_picks_2026_11_05.py` | **The parent's execution transcript** for the schema facts. Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic`; **the system Python does not have `sqlmodel`.** |
| The trigger READMEs | `/tmp/le31-daily-2026-11-05/readme/readme_Jmonczewski-droid__kisnet-pos.md`, `.../readme_rkevrellan__ComandaPOS.md` | The party-not-seat observation, and the *cuentas separadas* counter-signal. |
| The research report | `/opt/data/le31-daily-research-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (recorded evidence, no fabrication) and `skills/le31-first-party-defect-proving/SKILL.md`.

**The verification for this slice is a record, not a test run:**

1. **The question is asked** and the answer is **recorded verbatim** in the feature file — the exact words, plus the date and who answered. **A paraphrase is not a record.**
2. **The corpus gap is not re-derived.** It is already proven and recorded in the feature file, with the probe phrases, the 0-hit results and the negative control. **If the agent re-probes, the result must match; a different result means the corpus changed, and that must be recorded, not smoothed over.**
3. **The commit contains no product code.** `git diff --stat` must show **only** the feature file changed. **If any file under `backend/` appears, the slice has been over-implemented** — that is a defect, and the agent must revert it.
4. **The outcome is one of exactly three**, and the recorded next step matches the branch table above.

**Anti-fabrication:** the recorded answer must be the owner's actual answer. **Do not paraphrase it into a yes or a no that was not given**, and **do not record an answer that was not obtained.** If the question cannot be asked in this session, **record that fact** — *"the question was not asked; the slice remains open"* — and stop. **An unanswered question is a legitimate recorded outcome; an invented answer is not.**

## Rollback path

**Trivially reversible, because nothing is built.**

- **The code rollback:** there is no code. **The only change is the recorded answer in one file**, and a recorded answer is never rolled back — **it is corrected in place with a new dated note.**
- **The data rollback:** no schema change, so no data is affected.
- **The migration rollback:** none required — **and a migration file would be a scope violation of this contract.**
- **The one irreversible thing:** **the passage of time.** Every month that passes without the answer, the historical gap widens — no order line carries a seat, and no future migration can reconstruct which coffee was whose. **That is the cost of the *no answer* branch, and it is the strongest argument for asking the question soon.**

**Rollback cost:** seconds. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That the owner will answer.** The agent may be in a context where the question cannot be asked. **The recorded outcome in that case is "the question was not asked; the slice remains open"** — and that is a legitimate, honest result. **Do not substitute a guess.**
- **That the shape in the feature file is right.** All three candidates are **hypotheses**. The owner's actual need may be a **bill split** rather than a seat, in which case this whole contract is aimed at the wrong question and must be rewritten.
- **That the restaurant has numbered seats.** If it does not, `seat: int` is meaningless and candidate 1 is dead on arrival. **This is part of the question to the owner.**
- **That per-seat attribution is the only gap.** Feature **430** already records that five identical lines are indistinguishable — and if the owner's answer is *no*, the correct conclusion may be *"one line with a quantity is the right shape"*, which is feature 430's ground and not this one. **The "no" branch is a real outcome with a real alternative, not a dead end.**
- **Any owner decision about a guest's *name* on a line.** That is a Privacy escalation, recorded as Open question 4, and it must be made explicitly.

## Handoff summary

**One question. One recorded answer. No code.**

The gap is **real and uncovered** — six coffees at one table are six rows LE31 cannot tell apart, on a bill that is one aggregate — and it was proven by execution, with a passing negative control on the corpus probe.

**But the need is inferred, not observed**: there is no order-taking router and no bill router, so **no order line has ever been taken in LE31 and nobody has ever asked for a seat.** The most complete in-window implementation the parent read in full models parties and tables and **not seats** — and two different readings of that absence predict the same schema.

**The gate's rule for an assumed pain is: a small experiment, not a full feature.** **This contract IS the experiment.**

**So the agent's job is to ask and to record — not to build.** The three candidate shapes in the feature file are **hypotheses for the owner to choose between**, and the *seat ordering* problem (parties do not arrive in seat order) is named in advance so that a future implementer meets it before writing a column rather than after.

**And if the answer is "no", that is a legitimate, valuable recorded outcome** — a documented reason not to build a thing, in a corpus that is 471 features deep.
