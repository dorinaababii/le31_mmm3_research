# Feature 409 — LE31's charter points at `INDEX.md` for the open questions, and `INDEX.md` has no open-questions section: 1,740 questions across 437 contracts, none answerable

> **Pick B of Daily Brainstorm 2026-10-30 (90th brainstorm pass).** **FIRST-PARTY, and the defect is in LE31's own charter and LE31's own index** — not inferred from a third-party repo.
>
> `PROJECT_CHARTER.md` §3.3, verbatim:
>
> > ### 3.3 Open scope questions (blockers for some features)
> >
> > **These are listed in `INDEX.md`. Decisions needed before code starts:**
> >
> > 1. **Menu language** — drives OCR engine (PaddleOCR for CJK, RapidOCR for EU).
> > 2. **Currency** — EUR / USD / other? Affects display formatting.
> > 3. **Tax** — flat 10%? Per-category? Per-item?
> > 4. **Waiter hardware** — tablet, phone, or laptop? Drives UI density decisions.
> > 5. **Service charge** — auto-add a percentage? (Common in EU, not US.)
> >
> > Defaults if user doesn't answer: English menus, EUR, flat 10% tax, tablet UI, no service charge.
>
> `INDEX.md` has exactly **four headings**, and **none of them is an open-questions section**:
>
> ```
> 1:# LE31 Research — Index
> 7:## Daily research log
> 95:## Specialised research log
> 109:## Active feature pipeline
> 245:## Active feature pipeline
> ```
>
> The charter names the file that is supposed to hold the decisions. **The file holds a research log and a feature pipeline. It does not hold the decisions.**
>
> **Evidence class: OBSERVED** (every count below is a reproducible command against LE31's own tree). Confidence: **high**.
>
> **Bucket: v1** — the charter calls these *"blockers for some features"* and *"Decisions needed before code starts"*. **Build verdict: `build`.**

## Goal

Give LE31 the **one place the charter already promises** — an open-questions section in `INDEX.md` — and make each question **answerable**, so a decision can be *recorded* rather than re-derived by whichever agent happens to read the feature file next.

## Scope

- **One section** in `INDEX.md` — `## Open decisions` — holding the charter's own §3.3 questions, each with its default, its status and its blocker target.
- **One row per open question** from the **feature contracts**, but only the ones that are **decisions**, not implementation choices.
- **A status vocabulary** that distinguishes *answered*, *defaulted* and *unanswered*, because **the charter's own §3.3 gives defaults** — and "defaulted" is not the same as "answered", and neither is the same as "the owner knows".
- **A pointer from each feature contract's `## Open questions` section** to the register row, so a reader of a contract can see whether their question is still open.

## Out of scope (v1)

- **Answering any of the questions.** This feature builds the register; it does **not** decide the tax rate, the service charge, or anything else. Those are **owner decisions**, and the whole point of the register is to make them visible, not to guess them.
- **A schema change.** No SQLModel table, no column, no migration. This is a **Markdown register**, because the charter promises `INDEX.md`.
- **Rewriting the 437 feature contracts.** Each gets a *pointer*, not a rewrite. Rewriting 1,740 bullets is not the job and would destroy the contracts' local context.
- **A `DECISIONS.md` file.** The charter says `INDEX.md`. Moving the register to a new file would re-create the exact defect being fixed. **If a separate file is wanted later, `INDEX.md` must still link to it** — the charter's promise is about *reachability*, not about the file's name.
- **An escalation mechanism to the owner.** §3.3's defaults already exist; the register makes them visible. Asking the owner is a **product** decision (feature 61's approval surface, feature 403's role gap), not a documentation decision.
- **A Linear issue per question.** 1,740 Linear issues would be unusable. The register is the index; Linear is the work queue.

## Description

### The defect, precisely

The charter does not merely *have* open questions. It does something stronger: it **points at a specific file** and says the decisions are *there*, and that code **must not start** before they are made.

> *"These are listed in `INDEX.md`. Decisions needed before code starts."*

And they are not there. The five §3.3 questions appear **only** in the charter itself:

```
$ grep -rl "flat 10%" --include=*.md --include=*.py . | grep -v "^./features/\|^./specs/"
./PROJECT_CHARTER.md

$ grep -rl "tablet UI" --include=*.md --include=*.py . | grep -v "^./features/\|^./specs/"
./PROJECT_CHARTER.md
```

The charter is the only place the questions exist, and the charter is a **prose document**. A prose document cannot answer *"which of these blocks feature 17?"*.

### The decision debt, counted

The register does not exist, so the debt has to be counted where it actually lives: **in the feature contracts' own `## Open questions` sections.**

```
feature contracts with an '## Open questions' section :  437
total bullet/numbered open questions across them      :  1740
sections that are present but EMPTY                   :  0
```

**1,740 open questions across 437 feature contracts**, and **not one of them has a status**. They are prose sentences in 437 separate files. Three consequences follow, and all three are observable:

1. **Nothing can be blocked.** The charter says the questions are *"blockers for some features"*. A blocker that is a sentence in another file cannot block anything — no build step reads it, no agent checks it, and no owner sees it in a list.
2. **Nothing can be answered.** To answer a question, someone must find it, decide, write the decision down, and *find every other place that assumed the old answer*. There is no register to write the decision into, so the decision goes into a chat message or a commit message, where it is lost.
3. **The defaults are invisible.** §3.3 gives five defaults — *"English menus, EUR, flat 10% tax, tablet UI, no service charge"*. Those defaults are **one line in the charter** and nothing else. Nothing in the repo reads them. Feature 408 (Pick A of this pass) is a direct consequence: **the tax default exists, and `config.py` has no tax rate** — because no mechanism ever moved the charter's default into the code.

### The finding shapes (all five)

| Shape | Here |
|---|---|
| **(a) contradiction** | §3.3 says *"These are listed in `INDEX.md`"*. `INDEX.md` has no such listing. **All 19** occurrences of *"open question / decision needed / unanswered / undecided"* in `INDEX.md` are **inside table rows** — i.e. inside feature descriptions — and **zero** are a section. |
| **(b) omission** | 437 contracts carry an `## Open questions` section; **none** carries a **status**, an **owner**, or a **decision date**. The sibling information a question needs — what it blocks — is absent from every one. |
| **(c) missing inverse edge** | The question ↔ the feature it blocks: **the question points at nothing**. A reader of feature 17 cannot learn which of its open questions blocks feature 19. |
| **(d) undefined term** | *"Decisions needed before code starts"* — **decided by whom?** The charter's §3.3 offers **defaults** for all five, and §11 says the defaults apply *"unless the user overrides"*. So a question with a default is simultaneously **answered**, **unanswered**, and **not a question**. The vocabulary has no way to say that. |
| **(e) unenforced mechanism** | §3.3's mechanism is *"listed in `INDEX.md`"*. A **Markdown table** cannot enforce anything — there is no script that reads it, no CI check, and no agent step that consults it. A written rule and a mechanism that cannot carry it. |

### The fourth firing of shape (e) in three passes

| Pass | Rule | Mechanism that cannot carry it |
|---|---|---|
| 91st (research) | §3.1 *"role-based via chat_id allowlist"* | a flat `list[int]` — no place for a role |
| 91st (research) | §3.6 *"money is `Decimal`, never `float`"* | a non-`STRICT` table that accepts and stores a float |
| **90th (brainstorm, this one)** | **§3.3 *"listed in `INDEX.md`"*** | **a Markdown index with no such section, and no reader** |

### The external instrument

`suryanshranjan/hive` (MIT, Python, ★2, created 2026-10-27, pushed 2026-10-30 = **in-window by both fields**) is a multi-agent build tool. Its README describes the exact discipline LE31 is missing:

> *"**Before building, Hive lists the business decisions the code will have to take and asks you about each one, in plain words**, in the terminal or on your phone…"*

> *"**At the end Hive writes what the code now does as plain rules (the code sheet); you mark what's off, and a fix round makes it so.**"*

> *"When you ask for something the evidence says is a mistake, such as more builders than the law recommends, **it says so once, plainly, and then it's your call.**"*

Three transferable rules:

1. **Enumerate the decisions before the work, not during it.** The decision list is produced *first*, so the work is planned against it. LE31 produces its decisions *last* — never.
2. **A decision has a written form that the human can mark as wrong.** Hive's "code sheet" is a plain-language description the owner marks off. LE31's open questions are plain-language descriptions that **nobody marks off**.
3. **Defaulted is a distinct state from answered.** Hive *says so once, plainly* when the evidence suggests a mistake, and then leaves the call to the human. That is exactly the §3.3 default mechanism — and LE31 has no way to say *"this is running on a default nobody has looked at."*

`917Dhj/dkitchen` (MIT, Python, ★9, in-window by both fields) contributes the second half from the same domain — **rules live in one named place**:

> *"**The rules every station follows live in `kitchen/`**: who owns what, how tickets are written, when to stop and ask…"*

LE31's charter promises the open questions live in `INDEX.md`. They do not live there. **The rule and the location disagree.**

### What is NOT filed here

- **Feature 46 (`havemind-decision-notes`)** and **feature 49 (`postledger-tamper-evident-hash`)** contain the words "decision notes" and "decision" in their titles, but they are about **agent decision ledgers** (append-only, tamper-evident) — a *v2-AI* vocabulary. This feature is about **the human owner deciding LE31's open questions**, in **Markdown**, in **`INDEX.md`**. Different subject, different bucket, different artefact. Verified: `grep -rliE "decision register|decision log|question index|open-question index|decision inventory" features/` returns **no feature** proposing a register of LE31's open owner decisions.
- **Feature 408 (Pick A of this pass)** is the *consequence* of this defect in one domain: the charter's tax default exists and no mechanism moved it into `config.py`. 408 **fixes the tax**; this feature **fixes the mechanism that would have told 408 which questions are answered**. **They are complementary and must not be merged** — 408's evidence is a money column, this one's evidence is an index.
- **Feature 61 (`holdfast-approval-ledger`)** owns the *approval* workflow for AI proposals. It does not own the *inventory* of open owner decisions.

## Data model

**None.** This feature adds **no** table, **no** column, **no** migration. The register is Markdown, in the file the charter already names.

```markdown
## Open decisions

> Charter §3.3. Defaults apply unless the owner overrides them (§11).
> Status vocabulary: **answered** (the owner decided) · **defaulted** (a §3.3 default is in force, the owner has not ruled) · **open** (no default; blocks) · **superseded** (answered by a later decision).

| ID | Question | Charter ref | Default in force | Status | Blocks | Decided on | Decision |
|---|---|---|---|---|---|---|---|
| D-001 | Menu language | §3.3 q1 | English menus | defaulted | features 03, 04 (OCR engine choice) | — | — |
| D-002 | Currency | §3.3 q2 | EUR | defaulted | features 05, 14 (formatting) | — | — |
| D-003 | Tax — flat / per-category / per-item | §3.3 q3 | flat 10% | defaulted | feature 05, feature 408 | — | — |
| D-004 | Waiter hardware | §3.3 q4 | tablet | defaulted | features 02, 26 (UI density) | — | — |
| D-005 | Service charge | §3.3 q5 | none | defaulted | feature 05 | — | — |
```

**The five charter rows are the seed.** The remaining 1,735 contract-level questions are **not** all promoted: many are implementation choices rather than owner decisions, and promoting all of them would produce a register nobody reads. **The promotion rule is stated and applied: a contract question becomes a register row only if (a) a different answer would change the schema or a user-visible behaviour, AND (b) it is currently blocking a named feature.** Both conditions are checked and recorded.

## Implementation steps

1. **Add the `## Open decisions` section** to `INDEX.md`, directly after the `## Daily research log` heading block's preamble, with the charter's five questions seeded as `D-001`…`D-005` in the format above.
2. **Fix the charter's sentence** in §3.3 so it points at the section that now exists — change *"These are listed in `INDEX.md`"* to *"These are listed in the **Open decisions** section of `INDEX.md`"*. **The charter's claim and the file must agree; that is the whole defect.**
3. **Add a `Decision ID` line** to the `## Open questions` section of the contracts whose questions are promoted, e.g. `→ D-003`. **Only the promoted ones.** Do not touch the other ~430 contracts beyond this.
4. **Write the promotion rule** into the section preamble, in the words used above, so a later pass can extend the register without re-deciding the rule each time.
5. **Record the count** in the preamble — the number of promoted rows, and the number of contract-level questions that were **not** promoted and why. **A register that hides its own selection rule is a register nobody can extend.**
6. **Do NOT add a script that enforces the register.** That is explicitly out of scope for v1 — a Markdown table with no reader is what the charter already asked for and what we are now at least making *true*. The enforcement step (a CI check that a contract's promoted question has a status) is a **separate** change with its own gate.

## Telegram interaction if any

None. This feature adds no bot command. The register is read by humans and by the coding agent, not by the cook or the waiter.

## Dependencies

- **`PROJECT_CHARTER.md` §3.3 and §11** — the source of the five questions and of the default semantics.
- **`INDEX.md`** — the file the charter already names; the section is added there.
- **`features/408-…-v1-tax-rate-and-rounding-in-config.md`** (Pick A of this pass) — the concrete consequence of `D-003` being `defaulted` and never moved into `config.py`. **The two features must not be merged**: 408 ships the tax mechanism, this ships the register.
- **`features/05-payment-tip-reconciliation.md`** — its *Open questions* section is the second-largest source of unpromoted questions, and it is the feature `D-003`/`D-005` block.
- **`skills/le31-conventions/SKILL.md`** — its *Feature gate* already requires *"Evidence and confidence recorded"* and *"All seven checks answered"*; the register is where an **answered** decision would be recorded.

## Open questions

1. **Should the register live in `INDEX.md` or in a dedicated file with `INDEX.md` linking to it?** The charter says `INDEX.md`; §3.3's *reachability* is the point. Recommendation: **`INDEX.md`**, because a separate file with no link re-creates the defect, and a link is one more thing to forget. Revisit only if the table becomes unwieldy.
2. **Should "defaulted" count as "answered" for the purposes of "decisions needed before code starts"?** The charter says §3.3's defaults apply if the user does not answer — so by the charter's own logic a defaulted question **does not block code**. But §3.3 also calls them *"blockers for some features"*. These two statements contradict. Recommendation: **record `defaulted` as a distinct, non-blocking state** and say so in the preamble, and **flag to the owner** that the charter's two sentences disagree. **Do not silently pick one.**
3. **Who is the decider?** The charter says *"unless the user overrides"* and `agent/USER.md` describes the owner. Recommendation: **the owner**, and the register's *Decided on* column is a date. **This feature does not build the asking mechanism.**
4. **Should the 1,740 contract-level questions be promoted in bulk over time, or only when they actually block?** Recommendation: **only when they block** — a register of 1,740 rows would be unread, and the promotion rule's second condition already says so. This is a deliberate choice, recorded.
5. **Is this a documentation fix or a product feature?** It is **documentation plus a promise**, and the honest framing is that LE31 has been running for 90 days without it. Recommendation: treat it as **`build`** on the grounds that the charter *promises* it, not on the grounds of any operator pain — there is **no observed owner complaint**. Evidence class **OBSERVED** for the defect; **INFERRED** for the priority.

## Why this matters

**The charter made a promise about where its own open questions live, and ninety passes of research have never checked whether the promise was kept.**

Three things make this worth fixing rather than noting:

1. **It is the mechanism behind the other findings.** Feature 408 (Pick A of this very pass) found that the charter's *tax default* never reached the code. That is not a tax bug — it is **this** bug, in one domain. The other 1,735 unanswered questions are the same defect waiting in a different domain. **Fixing the register once is cheaper than finding each consequence separately**, and finding them separately has already produced eight findings in seven passes.

2. **It is the cheapest high-leverage change in the repo.** One section, one charter sentence, five seed rows, a promotion rule, and a pointer line in the contracts that matter. No schema change, no migration, no new dependency, and it is **fully reversible** (delete a section).

3. **The cost asymmetry.** Today the register's absence is *inert* — nothing depends on it because nothing reads it. That is the same shape as features 374 and 385: a defect that is cheap now and expensive after. The moment an automated agent or a CI check starts consulting "the open questions", it will consult a file that has no such section, and the failure will be a **silent wrong default** rather than an error. **The plausible wrong answer is the quiet one.**

**And the honest framing, which must be stated rather than glossed:** *no operator has complained about this*. There is **no observed owner pain**. The gate's check 1 is the weakest of the seven for this pick — the JTBD is *"when the coding agent starts a feature, it wants to know which owner decisions are still open, but struggles because the charter points at a file that has no such section, so that it guesses a default that may already have been overridden."* That is a **real** JTBD, and it is **internal** (the coding agent is the actor), but it is not an operator pain.

It is filed as **`build`** anyway, for one reason: **the charter promises this file has this section, and it does not.** That is the same evidence class as the 85th pass's `Batch.qty_remaining` — a **first-party contradiction between a written rule and the repository's own state** — and it is the second-highest-leverage of the eight findings in this series, because it is the one that would have prevented the other seven from needing to be found.
