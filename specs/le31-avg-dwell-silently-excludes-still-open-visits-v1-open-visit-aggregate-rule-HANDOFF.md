# HANDOFF — 428-le31-avg-dwell-silently-excludes-still-open-visits

**Status**: **build** (v1, first-party — **the defect is in LE31's own schema and is proven by execution**)
**Date**: 2026-11-02
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/428-le31-avg-dwell-silently-excludes-still-open-visits-first-party-a-null-closed-at-row-is-dropped-by-avg-with-no-signal-v1-open-visit-aggregate-rule.md`
**LE31 feature gate verdict**: **build** — gate check 1 (**demand**) is **OBSERVED**: the charter's P1 row asks for *"covers today, sales, tips, avg dwell, top items"* and **two of those five numbers have an unstated population**. Gate check 2 (**evidence**) is **OBSERVED by EXECUTION**: against LE31's real schema, the naive `AVG((closed_at − opened_at))` and the explicit `WHERE closed_at IS NOT NULL` returned **the identical value** `59.99999977648258`, while `COUNT(closed_at)=3` against `COUNT(*)=4` — one row invisible to the KPI, with **no signal at all**. Gate check 3 (**practicability**) is **PASS**: one written rule, one helper module, four assertions — and the directory `backend/app/services/` is already in the charter's §4.4 layout. Gate check 4 (**scope**) is **PASS**: no schema change, no route, no bot command. Gate check 5 (**consistency**) is **PASS** with one stated dependency: the missing **writer** for `closed_at` is feature **415**.

## Trigger policy

This is a **`build`** contract. The external coding agent **SHOULD** write the population rule down, implement the helper, and write the regression tests.

**⏱️ ORDERING — READ FIRST.** This slice is **inert** unless feature **415** (`le31-bill-closes-visit-edge`) has landed. Feature 415 owns the **writer**: today `closed_at` is **never written**, so *every* visit is open, `dwell_population` is `0`, and there is no value for the aggregate to be wrong about. **Feature 415 must land first, or in the same PR.** If 415 is not yet landed, **stop and say so** rather than landing a rule with no data behind it.

**The two edges are different and must not be merged:**

- **Feature 415** — *"the value is never written"*.
- **This feature (428)** — *"when the value IS written, the aggregate silently changes its population."*

**What the agent MAY do:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the out-of-scope list); §3.5 (the explicit-state invariant — a KPI whose population is implicit is exactly the kind of unwritten state this project distrusts); the truth invariant.
3. Load **features 415, 06, 405, 388, 414, 423** — the contracts that surround the visit domain — **and read what each reserves.**
4. **Write the population rule down, in text, before the code.**
5. **Create `backend/app/services/visit_analytics.py`** with the helper and the paired SQL form.
6. **Write the four regression tests**, including the **Python-vs-SQL population agreement** test.
7. **Amend feature 06** with a one-line pointer to this feature (optional, see *Open questions* in the feature file).

**What the agent MUST NOT do:**

- **Do not write `Visit.closed_at`.** That is **feature 415**.
- **Do not decide the dwell endpoint.** Whether dwell is `closed_at − opened_at` or `paid_at − opened_at` is **feature 415's open question**, recorded there verbatim as *"**Not decided.**"* This feature does not change `Visit.closed_at`'s semantics.
- **Do not change `backend/app/models.py`.** No column changes. `closed_at` is nullable **correctly** — a visit in progress genuinely has no end time. **The defect is the unwritten rule, not the schema.**
- **Do not build the manager dashboard.** This feature supplies the KPI helper; the UI is separate work.
- **Do not create `/api/reports/today`.** The route does not exist; this feature supplies the helper it will call.
- **Do not use one shared filter for `avg_dwell` and `covers_today`.** **They are different populations and the asymmetry is the whole point of the rule.**
- **Do not change `avg dwell` to a median.** The charter says *"avg"*. A median is a product decision about the KPI's definition, not a defect fix, and it is **not decided here**.
- **Do not add an "abandoned visit" flag.** Recorded as open; **not decided**.
- **Do not implement Alembic.** §3.2's v1 policy is `init_db()`.
- **Do not touch the money KPIs** on the same dashboard (sales, tips) — features 408, 411 and 420 own those.

**Disambiguation**: this slice is about **the population an average is computed over**. It is **not** about the missing writer (feature 415), **not** about the service-day boundary (feature 405), **not** about the table's occupied state (feature 388), **not** about `party_size` (features 414, 423), and **not** about the forecast average `avg_14d × 1.1` (feature 07 — a different average over a different population, whose rule *is* explicit).

## Frozen contract

**The one thing this contract exists to make true:** *a KPI that excludes rows must say so.*

**The rule, as it would be recorded:**

> **Rule — the manager dashboard's visit population.**
>
> 1. **`avg dwell`** is `AVG(closed_at − opened_at)` over visits with `closed_at IS NOT NULL`. Visits still open are **excluded by definition**, not by accident.
> 2. **`covers today`** counts visits whose `opened_at` falls on the service day — **regardless of `closed_at`**. A visit that is still open is still a cover.
> 3. **`currently seated`** counts visits with `closed_at IS NULL` and reports their elapsed occupancy (`now − opened_at`). This is the number that replaces the silent exclusion.
> 4. **The population is stated in the response.** The KPI payload carries the counts it was computed over, so a reader can check `dwell_population + currently_seated == total_visits`.
>
> Rules 1 and 2 are **different populations** and must not share a filter. Rule 1 excludes open visits; rule 2 includes them.

**Why the rule must exist at all, and not merely as a query habit:** the charter's P1 row names *"avg dwell"* and *"covers today"* and **never says what they cover.** A `NULL` in a nullable column is not an error, a warning, or a row — it is a row the aggregate skips. **The proof is in the numbers:** the naive query and the careful query returned **the same value**. There is no discrepancy to notice. **The defect is not wrong-arithmetic; it is wrong-SET, and it is invisible about itself.**

**Why the Python and SQL forms must both be tested against each other:** the *rule* has to be expressible in Python, but LE31's derivations run in SQL — and the two disagree in the worst direction:

| Form | `closed_at IS NULL` row | Result |
|---|---|---|
| Python: `None > x` | **raises** `TypeError` | loud |
| SQL: `AVG(a − b)` where `b IS NULL` | **excluded silently** | quiet |

**A developer testing the rule in Python gets an error and adds a `WHERE`. A developer writing only SQL gets a number that is wrong by exactly the open visits, and never finds out.** That asymmetry is the reason the paired test is mandatory, not optional.

**And the sibling KPI is the more dangerous half.** *"covers today"* means **covers seated today**. If it is implemented as *"closed today"*, the dashboard would show **fewer covers at 21:00 than at 20:00** on the same evening — a number that falls while the restaurant gets busier. **The owner would not debug that; they would stop reading the dashboard.** This is the sentence that makes the rule worth writing.

**Anti-goals, stated so they are not drifted into:**

- **Not a schema slice.** No column changes. `closed_at` stays nullable.
- **Not a route slice.** No `/api/reports/today`.
- **Not a UI slice.** No dashboard.
- **Not a writer slice.** That is feature 415.
- **Not a KPI-definition slice.** The charter says *"avg"*; it stays *"avg"*.
- **Not a service-day slice.** That is feature 405; this feature's rule 2 depends on it but does not decide it.

## Files to touch

| File | Change |
|---|---|
| `backend/app/services/__init__.py` | **CREATE** (empty). **The directory does not exist today** — it is listed in the charter's §4.4 folder layout. |
| `backend/app/services/visit_analytics.py` | **CREATE.** The `dwell_summary` helper (Python form) and the paired SQL constant `SQL_AVG_DWELL` (**with** the `WHERE closed_at IS NOT NULL` clause). |
| `backend/tests/` (or the repo's existing test location) | **ADD** four tests: the population excludes open visits; `covers_today` **includes** them; the Python and SQL forms select the **same rows**; the counts reconcile. |
| `PROJECT_CHARTER.md` (or the helper's docstring) | **AMEND** with the "Rule — the manager dashboard's visit population" block, **or** record the rule in the helper's docstring. **One of the two — not both.** |
| `features/06-guest-demographics.md` | **AMEND** (optional, one line): point at feature 428 as the owner of the population rule. **Feature 06 is a brief, not a contract — amend it, do not rewrite it.** |
| `features/428-…md` | **VERIFY** the rule text and the *Dependencies* section name features 415, 06, 405, 388, 414 and 423 correctly. **Amend only if a name is wrong.** |
| `INDEX.md` | **ADD** one row to the "Active feature pipeline" table. |

**Any other file is out of scope.** If the agent believes another file must change, that is a **new finding** — surface it, do not silently widen the slice.

**Explicitly NOT to be touched:** `backend/app/models.py` (**no column changes**), `backend/app/routers/` (no route), `backend/app/bot/` (no command), `features/415-…` (the writer), `features/405-…` (the service day), `features/388-…` (the table state), `features/07-demand-estimation.md` (it owns its own average over its own population), `features/408-…` / `features/411-…` / `features/420-…` (the money KPIs).

## Mandatory LE31 skill list

The external coding agent must load:

- **`le31-conventions`** — the seven-check feature gate and the hard invariants (§3.2 the out-of-scope list; §3.5 the explicit-state invariant — a KPI with an implicit population is an unwritten state; the truth invariant).
- **`le31-v1-feature-pattern`** — the canonical contract shape and the slicing rules.
- **`le31-research`** — the source-of-truth discipline behind the artifact quote.
- **`le31-handoff-spec`** — the frozen-contract discipline.
- **`le31-data`** — the derivation discipline; §4.3's *"computed on read, not stored"* principle and the **Python-vs-SQL asymmetry** are the substance of this slice.

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

## Mandatory inputs

- **Active feature**: `features/428-le31-avg-dwell-silently-excludes-still-open-visits-first-party-a-null-closed-at-row-is-dropped-by-avg-with-no-signal-v1-open-visit-aggregate-rule.md`
- **Execution proof** (re-runnable): `/opt/data/le31_mmm3_research_work/_exec_proof2_2026_11_02.py` — run with `/opt/data/le31-verify-2026-10-27/.venv/bin/python`. The naive and explicit `AVG` returned the **same** number; `COUNT(closed_at)=3` vs `COUNT(*)=4`; `MIN(elapsed) WHERE closed_at IS NULL = 10.000167042016983` minutes.
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-11-02.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-11-02/`

## Verification protocol reference

**Reference**: `coding-agent/skills/le31-verification-protocol` and `PROJECT_CHARTER.md` §8.

1. **Re-run the execution proof** and confirm that the naive and explicit `AVG` **now differ in their populations** — i.e. the helper reports `dwell_population=3` and `currently_seated=1` for the same seed, where the raw naive SQL still silently drops the row. **The proof must show the gap between the raw SQL and the rule; if the raw SQL and the helper still agree, the rule is not being applied.**
2. **Run the four regression tests.** The population test must fail **before** the change and pass after. **A test that only ever passed proves nothing.**
3. **Confirm the counts reconcile** — `dwell_population + currently_seated == total_visits`. This is the assertion that catches a rule that quietly loses a row.
4. **Confirm `covers_today` includes open visits** — with 3 closed + 1 open, `covers_today` must be **4**, not 3. **This is the test that fails first if someone shares one filter between the two KPIs**, and it is the more important of the two population tests.
5. **Confirm the Python and SQL forms agree** — the same seed through `dwell_summary` and through `SQL_AVG_DWELL` must select the same rows and produce the same number.
6. **Confirm the rule is written down in text**, not only in code. Re-read it and check it states (a) the `avg dwell` population, (b) the `covers today` population, (c) the "currently seated" number, and (d) that the population is carried in the response.
7. **Confirm `backend/app/models.py` is untouched** — `git diff --stat` must show no change to it. **The nullable `closed_at` is correct; the defect is the unwritten rule.**
8. **Confirm nothing else changed** — `git diff --stat` must show only the files in *Files to touch*.

## Rollback path

**Trivially reversible. The slice writes no rows, reads no rows, and changes no schema.**

1. **Revert the commit.** `git revert` removes the helper module and the tests.
2. **No data loss.** The helper **writes no rows and reads no rows**.
3. **What remains safe if removed:** every existing behaviour. **The slice is inert by construction** — there is no dashboard and no report route today, so nothing reads the KPI.
4. **Retained data:** none.
5. **⚠️ Rollback interaction:** if this is rolled back **after** feature 415 has landed, then `closed_at` **will** be written — and the dashboard (once it exists) would compute `avg dwell` and `covers today` over an **unstated population**, which is precisely the defect this feature exists to remove. **That must be recorded if it happens**, because the defect becomes *live* at that point rather than latent.

## Sign-off gap

**Five owner decisions are open. None blocks the rule; each is recorded so the next pass does not re-open it.**

1. **Should the KPI payload carry the population counts, or should the dashboard render them separately?** **Recorded default: carry them in the payload.** The point is that the population is *visible without asking*; a rendering step can be forgotten, a payload field cannot.
2. **Should `avg dwell` be `AVG` or a median?** **Recorded default: `AVG`, as the charter names it.** A median is arguably the better dwell statistic (one long party skews the mean), but that is a **product decision about the KPI's definition**, not a defect fix, and it is **not decided here**.
3. **Should a visit still open after N hours be flagged as abandoned?** **Recorded default: no.** That is a product rule with an operational consequence (a table appears occupied forever). **Not decided here** — recorded so the next pass does not mistake it for an oversight.
4. **Should `covers_today` use `opened_at` or `closed_at` for the service-day boundary?** **Recorded default: `opened_at`** (a cover is seated, not closed). Feature 405 owns the *day* boundary itself. **Not decided here** — rule 2 is stated with the day boundary delegated to 405.
5. **Should feature 06 be amended to point at this feature?** **Recorded default: yes — a one-line amendment**, exactly as feature 404's deferral note is amended by feature 426. **An amendment, not a rewrite.**

**The agent must not widen any of these decisions.** If the KPI set seems to require a different answer, that is a **finding to surface**, not a choice to make.

## Handoff summary

The charter's P1 row asks the manager dashboard for *"covers today, sales, tips, avg dwell, top items"* — and **two of those five numbers have never been given a population.** The parent proved it by **executing against LE31's real schema**: three closed visits at 60 minutes and one still-open visit produce **the identical result** from `AVG((closed_at − opened_at))` and from `AVG(...) WHERE closed_at IS NOT NULL` — `59.99999977648258` minutes either way — while `COUNT(closed_at)=3` against `COUNT(*)=4`. **One row is invisible to the KPI and nothing says so.** The naive query gives no signal that it dropped anything.

The mechanism is SQL's three-valued logic meeting a nullable column: `NULL` is not a value, so the subtraction is `NULL`, and `AVG` skips it. **And the two forms do not merely differ in loudness — they differ in result.** Python's `None > x` **raises**; SQL's `AVG` is **quiet**. A developer testing the rule in Python gets an error and adds a `WHERE`; a developer writing only SQL gets a wrong number and never finds out. **That asymmetry is why the paired Python-vs-SQL test is mandatory here and not merely good practice.**

The sibling KPI is the more dangerous half. *"covers today"* means covers **seated** today; implemented as *"closed today"*, it would report **fewer covers at 21:00 than at 20:00** on the same evening — a number that falls while the restaurant gets busier. **The owner would not debug that; they would stop reading the dashboard.**

And the finding's origin is worth recording, because it changes how the next pass should work. The concept sweep over **456** feature contracts returned **zero** uncovered concepts — the audit is **saturating** — and this defect was still there. The words it is written in (*"avg dwell"*) appear in only **two** contracts, and the one that owns the KPI, **feature 06**, is a **brief**: it has `## Goal`, `## Scope`, `## Description`, `## Data model`, `## Manager dashboard`, `## Privacy stance`, `## Dependencies`, `## Open questions` — and **neither `## Out of scope` nor `## Why this matters`**. It states *"Capture `opened_at` and `closed_at` → dwell time"* and moves on. **Nobody had asked what the average is over.** This defect was found by auditing the charter's P1 row against the schema **one row at a time**, not by grepping the corpus — and it is the **sixth** first-party finding in the series, all of them execution-proven.

**A zero-hit sweep is a candidate, not a licence** — and a zero-hit sweep on the *concepts* is not a licence to stop either.
