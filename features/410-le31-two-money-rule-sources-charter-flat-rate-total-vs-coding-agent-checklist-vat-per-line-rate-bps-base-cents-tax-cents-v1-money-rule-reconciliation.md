# Feature 410 — LE31's coding-agent checklist demands per-line VAT (`rate_bps`, `base_cents`, `tax_cents`) and the schema has one stored tax total: two rule sources, one violated money model

> **Pick C of Daily Brainstorm 2026-10-30 (90th brainstorm pass).** **FIRST-PARTY, and the defect is in LE31's own schema against LE31's own two rule sources** — the external artifact is the *instrument*, not the subject.
>
> LE31 ships **two** co-equal rule sources that both say the same thing about tax, and **neither is implemented**.
>
> **Source 1 — `PROJECT_CHARTER.md` §7 Quality bar:**
> > - **No magic numbers.** Tax rate, tip rounding rules, buffer factors — all in `config.py` or `services/`.
>
> **Source 2 — `coding-agent/checklist.md`,** the one-page checklist the coding agent is told to enforce before and during every feature:
> > - [ ] **VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line.**
>
> **LE31's schema has neither.** `backend/app/models.py`:
> ```python
> class Bill(SQLModel, table=True):
>     subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
>     subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)   # ONE stored total
>     total_due: Decimal = Field(max_digits=10, decimal_places=2)
> ```
> There is **no `rate_bps`**, **no `base_cents`**, **no `tax_cents`**, and **no per-line tax at all**. `grep -rn "rate_bps\|base_cents\|tax_cents" backend/` returns **no hits**. `grep -rliE "rate_bps|base_cents|tax_cents" features/ specs/` returns **no hits across all 437 feature contracts and 409 HANDOFFs.**
>
> **Evidence class: OBSERVED** (four greps and a schema parse, all reproducible). Confidence: **high**.
>
> **Bucket: v1.** **Build verdict: `build`** — as a **corroborating constraint on feature 408**, not as a competing design.
>
> **⚠️ This feature does NOT propose the checklist's per-line design as the answer.** The checklist's shape is **not adopted**; see *Why the checklist's shape is explicitly not adopted* below. What is filed is the **contradiction between two rule sources and the schema**, and the decision that has to be made about which of them governs.

## Goal

Resolve — **explicitly and in one place** — the fact that LE31 has **two** money rule sources that disagree with each other and that **neither** the schema nor the feature contracts implement, so that a coding agent following the checklist is not simultaneously told to build something the charter forbids.

## Scope

- **One decision record** naming which tax model governs v1: **the charter's flat-rate-total** (feature 408) or **the checklist's per-line basis**.
- **One reconciliation** of the two rule sources — the charter §7 line and the checklist line — so that the checklist does not ask for a shape the charter's design does not have.
- **An explicit reconciliation of the checklist's other money/time lines** with the schema, because they fail in the same way.
- **A pointer from the checklist to the governing feature**, so a coding agent reading the checklist is not left to guess.

## Out of scope (v1)

- **Adopting the per-line VAT design.** `rate_bps`/`base_cents`/`tax_cents` is a **different money model** from the charter's flat-rate-total. Adopting it would be a **schema redesign** of `Bill` and would need its own gate. **Not adopted here — explicitly.**
- **Changing the schema.** This feature records the contradiction and the decision; it does **not** add columns. **Feature 408** owns the schema change for the chosen model.
- **Changing `Decimal` to integer cents.** The checklist already permits *"integer cents **or** `Decimal`"*, so LE31's `Decimal` choice is **compliant** with that line. **No action.**
- **Changing the timestamp columns to `TIMESTAMPTZ`.** That is **feature 405**'s territory (the business-date / timezone question, filed by the concurrent research cron today). This feature only records that the checklist line disagrees with the schema and points at 405. **Do not merge.**
- **Rewriting the whole checklist.** One section, reconciled.
- **The `allowlist` and `InlineKeyboardButton` checklist lines.** They relate to feature 403 (the role/allowlist gap, filed 2026-10-29) and are **not** re-litigated here.

## Description

### The defect, precisely

LE31 has a **two-source money model** and **no reconciliation**. Both sources are real, both are committed, both date from the same repo-layout commit (`6215445`, 2026-07-29), and both are addressed to the implementer:

| Source | Says |
|---|---|
| `PROJECT_CHARTER.md` §7 | *"**No magic numbers.** Tax rate, tip rounding rules, buffer factors — all in `config.py` or `services/`."* — a **flat rate in config**, with **no per-line basis** mentioned anywhere. |
| `coding-agent/checklist.md` | *"**VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line.**"* — a **per-line basis**, with **no config** mentioned, and using **basis points** rather than a decimal rate. |
| `backend/app/models.py` | **neither.** One stored `subtotal_tax: Decimal` total on `Bill`. |

**The two sources are not merely both unimplemented — they are mutually exclusive.** A flat-rate total and a per-line basis are different schemas. A coding agent that follows the checklist will build something the charter does not describe; an agent that follows the charter will fail the checklist's line. **There is no rule anywhere in LE31 that says which one wins.**

### Why this is the same defect as Pick A, seen from a second direction

Feature 408 (Pick A of this pass) found that **the charter's** rule has no home: `config.py` has no tax rate, `services/` does not exist, and `Bill.subtotal_tax` is a free-floating number. **Proven by execution**: for a realistic `subtotal_items = 12.45` at 10%, the rounding mode alone changes the stored tip (6.30 vs 6.31), and the DB accepted `total_due = 999.99` against `items = 12.45, tax = 0.00`, deriving a tip of **−979.99**.

**This feature is the corroboration.** Pick A found the gap from the charter side. This one finds it from the **implementation-checklist** side — a *different file, a different audience, written for the agent that actually writes the code*, stating the rule **more specifically** than the charter does (`rate_bps`, `base_cents`, `tax_cents`, **per line**). Two independent rule sources, one schema, zero reconciliation.

That is the strongest available form of this evidence, because it removes the obvious objection — *"maybe the charter was just loose"* — by showing **a second, more precise, differently-worded rule** that says the same thing in a different shape.

### The finding shapes

| Shape | Here |
|---|---|
| **(a) contradiction** | The checklist requires a per-line VAT basis; the charter requires a config rate and describes a flat total; the schema has a flat total with neither. **Two rule sources, one schema, no reconciliation.** |
| **(b) omission** | `Bill` has no `tax_cents`-per-line structure; `OrderItem` — the *line* — has **no tax column of any kind** (`id, visit_id, menu_item_id, qty, unit_price, course, status, notes, fired_at, ready_at, served_at`). If the checklist's model is the governing one, **the per-line tax does not exist and never will** without a schema change. |
| **(c) missing inverse edge** | The line ↔ its tax: **`OrderItem` has no tax column**, so the checklist's *"per line"* has nothing to attach to. |
| **(d) undefined term** | *"VAT"* vs *"tax"*. The charter says **tax**; the checklist says **VAT**; the schema column says `subtotal_tax`. **Three names, one concept, no definition** of whether VAT *is* LE31's tax line or a separate thing. |
| **(e) unenforced mechanism** | The checklist is the **mechanism** the coding agent is told to enforce. It is a Markdown file with **no reader**: `grep -rn "coding-agent/checklist" PROJECT_CHARTER.md HANDOFF.md README.md` returns **no hits** — the charter, the HANDOFF and the README **never point at it**, so an agent following the charter never learns the checklist exists. |

### The checklist's other lines fail in exactly the same way

The reconciliation is not a one-line fix, and the honest thing is to record the **other** lines that disagree with the schema rather than to pretend this is the only one:

| Checklist line | Schema reality | Status |
|---|---|---|
| *"VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line."* | `Bill.subtotal_tax` = one stored total; no per-line tax | **contradiction — this feature** |
| *"Every timestamp is `TIMESTAMPTZ`."* | every column is `Column(DateTime(timezone=True))` — **SQLite has no `TIMESTAMPTZ`**; the type only becomes `TIMESTAMPTZ` on Postgres, and the charter's dev DB is **SQLite** | **off-stack-conditional — feature 405's territory** |
| *"Money columns are integer cents **or** `Decimal` only. Never `float`."* | every money column is `Decimal` | **✅ compliant** |
| *"Plain French."* | `agent/USER.md` says the owner *"Speaks fluent English"*; the charter's §3.3 default is *"English menus"* | **contradiction — recorded, not owned here** |
| *"Allowlist `TELEGRAM_ALLOWED_USERS` checked first."* | `config.py` has `telegram_allowed_user_ids`, **never read**; the bot carries `# TODO: filter incoming messages to allowed user IDs.` | **feature 403 (filed 2026-10-29)** |
| *"Idempotency key on every state-changing endpoint."* | no idempotency key on any column | **feature 382** (recorded) |
| *"Reconciliation: ledger total = derivation view total (zero delta)."* | `Batch.qty_remaining` is **stored**, not derived | **feature 374** (recorded) |

**Seven checklist lines, one compliant, four already owned by other features, and two that are contradictions this feature records.** That is the honest picture — **the checklist is not a small document that happens to be mostly right; it is a second, partly-divergent specification of the same product.**

### Why the checklist's shape is explicitly not adopted

The tempting move is to "fix the schema to match the checklist" — add `rate_bps` to `MenuItem`, `base_cents`/`tax_cents` to `OrderItem`. **That is rejected here**, for three stated reasons:

1. **It contradicts the charter.** §3.1 says *"**Flat tax** (single rate, e.g. 10%)"* and §3.3's default is *"flat 10% tax"*. A per-line basis supports **per-category and per-item** rates — which §3.3 lists as an **open question**, not a decision. **Adopting the checklist's shape would silently answer an open owner question.**
2. **It is a larger change than the defect warrants.** Feature 408's cost is *one config entry, one small service module, one column, one constraint*. The per-line model is *a new column on `MenuItem`, a new pair of columns on every `OrderItem`, a new derivation, a new constraint set, and a rewrite of every bill-close path*. The cost asymmetry the 87th-pass rule names applies: **the cheaper correct answer should win unless there is a reason it cannot.**
3. **The checklist is not the charter.** It is an *aide* to the coding agent. The charter is the source of truth (`le31-conventions`: *"Truth: GitHub is source of truth for files and code"*). When they disagree, the **charter governs and the checklist is corrected** — that is the whole point of this feature.

**So the decision this feature records is: the charter's flat-rate total governs; the checklist's VAT line is corrected to match; and the checklist gains a pointer to feature 408.** The per-line model stays on file as **parking-lot** — if the owner ever answers §3.3's *"Per-category?"* with **yes**, this feature's Open questions point at exactly the right place to revive it.

### The external instrument

`suryanshranjan/hive` (MIT, Python, ★2, created 2026-10-27, pushed 2026-10-30 = **in-window by both fields**) is a multi-agent build tool whose README describes the discipline LE31's two rule sources are missing:

> *"**Before building, Hive lists the business decisions the code will have to take and asks you about each one, in plain words**…"*

> *"**The guard refuses a landing that breaks a passing test, duplicates a definition, or commits a secret.**"*

> *"Every experiment (a gate) **pushes its predictions and kill conditions to GitHub before it runs** (`lab/run_gate.py` refuses to start otherwise), then scores them in its `RESULTS.md`, **failures included**."*

> *"**Lab flaws found later are written up, not hidden** (`gates/LAB_NOTE_guard_python.md`)."*

Three transferable rules, all of them about **agreement between what is written down and what is built**:

1. **A guard that is not wired to anything is not a guard.** Hive's guard *refuses* a landing. LE31's checklist is a Markdown file that **nothing reads** and **nothing points at** — the charter, the HANDOFF and the README never mention it.
2. **Predictions and kill conditions are pushed before the run, not written after.** This is the *pre-registration* primitive, and it is exactly what a checklist line is: a prediction ("VAT will be stored per line") that should be **checkable before** the code lands, not noticed after.
3. **Failures are included, and flaws are written up rather than hidden.** This is the part LE31 has **no mechanism for at all**: `grep -rniE "failed attempt|failure record|negative result|post-mortem|retrospective" backend/ PROJECT_CHARTER.md` returns **no hits**. A checklist line that is *known* to disagree with the schema is currently just... a line.

**Note the connection to Pick B.** Pick B (feature 409) is about the charter's **open questions** having no register. This feature is about the **charter's rules** having no reconciliation. Both are the same underlying shape — **LE31 writes down things and never checks whether they agree.** `hive` is the instrument for both, from the same in-window artifact.

## Data model

**None.** This feature adds **no** table, **no** column, **no** migration. It is a **decision record + a checklist reconciliation**.

```markdown
<!-- coding-agent/checklist.md — the VAT line, reconciled -->

## Money

- [ ] Tax rate comes from `settings.tax_rate`; the rounding mode from
      `settings.money_rounding`. See feature 408.
- [ ] `Bill.subtotal_tax` is DERIVED from `subtotal_items` and the configured
      rate, never supplied by the caller.
- [ ] `Bill.total_due == Bill.subtotal_items + Bill.subtotal_tax` (the
      cross-column CHECK from feature 408).
- [ ] `Bill.tax_rate_applied` records the rate actually used, so a historic
      bill stays explainable after the owner changes the rate.
- [ ] ~~VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line.~~
      **SUPERSEDED 2026-10-30 — the charter's flat-rate-total model governs
      (PROJECT_CHARTER.md §3.1, §3.3). The per-line basis is retained as the
      shape to adopt *if* §3.3's "Per-category?" is answered yes. See
      feature 410.**
```

**And a decision record**, in the format feature 409's register uses, so the two features compose:

```markdown
| D-006 | Tax storage model — flat rate in config (charter) or per-line
           basis (checklist)? | §3.3 q3 + coding-agent/checklist.md |
           flat rate, charter governs | **answered** | feature 05, feature 408,
           feature 410 | 2026-10-30 | Charter §3.1/§3.3 govern; the checklist's
           VAT line is corrected to the flat-rate model. The per-line basis is
           parking-lot, to be revived only if §3.3's "Per-category?" is
           answered yes. |
```

## Implementation steps

1. **Correct the VAT line** in `coding-agent/checklist.md` to the reconciled form above, keeping the original line as a struck-through `SUPERSEDED` entry **with the reason and the pointer** — do not silently delete it. **A silently deleted rule is the defect this feature is about.**
2. **Record decision `D-006`** in the open-decisions register (feature 409's `## Open decisions` section). If feature 409 has not landed yet, **land 409 first** — the register is where a decision goes. **Do not create a second place to record decisions.**
3. **Add the pointer** from the checklist's `## Money` section to feature 408, so the agent reading the checklist knows where the tax mechanism lives.
4. **Record the other checklist/schema disagreements** in a short `## Known disagreements with the schema` section of the checklist, each with the owning feature number — the seven-row table above, minus the compliant line. **This is the reconciliation artifact; without it, the next agent rediscovers the same seven gaps.**
5. **Make the checklist reachable.** Add a line to `HANDOFF.md` and/or `README.md` pointing at `coding-agent/checklist.md`, and a line in `PROJECT_CHARTER.md` §8's verification protocol. **Today the checklist is orphaned: `grep -rn "coding-agent/checklist" PROJECT_CHARTER.md HANDOFF.md README.md` returns nothing.**
6. **Do not change the schema in this feature.** Feature 408 owns the `Bill` change.

## Telegram interaction if any

None. This feature adds no bot command.

## Dependencies

- **`coding-agent/checklist.md`** — the file being reconciled.
- **`features/408-…-v1-tax-rate-and-rounding-in-config.md`** (Pick A of this pass) — the governing feature. **408 owns the schema; this feature owns the decision and the checklist.**
- **`features/409-…-v1-open-decisions-register.md`** (Pick B of this pass) — the register where `D-006` is recorded. **409 must land first.**
- **`PROJECT_CHARTER.md` §3.1, §3.3, §7, §8** — the charter's rate decision, the open question, the magic-numbers rule and the verification protocol.
- **`features/05-payment-tip-reconciliation.md`** — the bill-close flow whose tax line is in question.
- **`HANDOFF.md`, `README.md`** — where the checklist pointer is added.
- **`features/405-…` (business date), `403` (role allowlist), `382` (idempotency), `374` (derived qty_remaining)** — the already-owned checklist lines. **Referenced, not re-litigated.**

## Open questions

1. **Is the checklist normative or advisory?** If the checklist is *advisory* — a set of suggestions for the coding agent — then it cannot contradict the charter, and the fix is a preamble saying so. If it is *normative*, then a contradiction between it and the charter is a **blocking** condition and belongs in the gate. Recommendation: **normative for the lines it covers, subordinate to the charter on conflict** — and say that in a preamble. **This decision is the point of the feature.**
2. **Should `Plain French` be corrected to English?** `agent/USER.md` says the owner *"Speaks fluent English"*; §3.3's default is *"English menus"*. The checklist says *"Plain French"*. Recommendation: **correct the checklist to English** and record the French variant as a **localization** question owned by feature 64 (the localization-profile shape). **Recorded here, not decided here.**
3. **Should the per-line VAT model be revived as a v2 option if §3.3 is answered "per-category"?** Recommendation: **keep it on file, not decided.** This feature's Open questions point at exactly the revival point.
4. **Is `TIMESTAMPTZ` a checklist error or a Postgres-only note?** The checklist is unconditional; the charter's dev DB is SQLite, where `TIMESTAMPTZ` does not exist. Recommendation: **qualify the checklist line** to *"Postgres deployments: `TIMESTAMPTZ`. SQLite dev: timezone-aware `DATETIME`."* **Coordinate with feature 405** — the two must not contradict.
5. **Should the checklist get an executable form?** A script that reads the checklist and checks the schema would turn shape (e) into a mechanism. Recommendation: **out of scope for v1** — it is a separate change with its own gate, and the 91st-pass note about "a mechanism that cannot carry it" applies to *any* Markdown checklist. **Recorded as a future option.**

## Why this matters

**LE31 has two rule sources for money, they are mutually exclusive, and both are unimplemented — and the coding agent's checklist is orphaned, so nothing checks either.**

Three reasons this matters more than a documentation tidy-up:

1. **It removes the strongest objection to Pick A.** Feature 408's evidence was *"the charter says X and the schema does not-X"*. The obvious reply is *"the charter is loose prose; a checklist is more specific"*. This feature answers that reply with evidence: **the checklist is specific in a *different direction*.** It does not merely fail to require a config rate — it requires a **per-line basis**, which the charter's flat-rate design cannot express. Two specific, mutually exclusive, unimplemented specifications of the same money model.

2. **The checklist is aimed at exactly the actor who will get it wrong.** Its own preamble says *"This is the field checklist. Each line is enforced by a SKILL.md in this folder."* The agent that will write the bill-close code is told *"VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line"* and will build a per-line tax the charter never described and no feature contract specifies. **The failure mode is a schema change made on the strength of a checklist line, by an agent that has no way to know the line disagrees with the charter.**

3. **Seven lines, one compliant.** The honest reading of the table above is not *"the checklist is wrong about VAT"* but *"the checklist and the schema are two specifications of the same product that have never been reconciled"*. That is a **systemic** finding, and it is the same systemic finding as Pick B (the open-questions register): **LE31 writes things down and never checks whether they agree.** Two of this pass's three picks are that one finding, seen in two places — the charter's questions and the checklist's rules.

**The cost asymmetry again:** reconciling a checklist is **free** — it is a Markdown edit. The cost of *not* reconciling it is a schema change made for the wrong reason, at the moment a coding agent implements feature 05, with a money model that the charter does not describe and that **no feature contract covers** (`grep -rliE "rate_bps|base_cents|tax_cents" features/ specs/` → **no hits across 437 contracts and 409 HANDOFFs**).
