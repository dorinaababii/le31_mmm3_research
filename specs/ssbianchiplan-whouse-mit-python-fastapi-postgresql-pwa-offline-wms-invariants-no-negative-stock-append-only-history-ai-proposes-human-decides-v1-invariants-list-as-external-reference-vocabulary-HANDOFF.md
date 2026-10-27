# HANDOFF — Feature 389: record `whouse`'s invariants list as outside prior art for LE31's stock, ledger and AI rules

**This is a `defer` pick, and it is a DOCUMENTATION-ONLY slice.** There is no code to write. The deliverable is the feature file itself. **If you are reading this and you are about to open a code editor, stop — this feature is finished the moment `features/389-…md` exists.**

**Discovery chain:** Daily Research 2026-10-27 → the parent's GitHub candidate sweep produced `SSBianchiplan/whouse` (MIT, ★1, ★1/⑂0, 2,113 KB, Python + FastAPI + PostgreSQL + PWA — the only on-stack candidate of the day) → the parent fetched its README raw → and found a section headed *"**Invariantes (regras que o sistema não deixa quebrar)**"* — *"invariants (rules the system does not let break)"* — whose five bullets map almost one-to-one onto LE31's own charter rules. The same window produced the **boundary pair** `Nomaan2288/Restaurant-Management-System` (AGPL-3.0), which documents the *opposite* choice ("never blocks a sale on a stock shortfall", `allowNegative: true`).

**Full evidence record: `features/389-ssbianchiplan-whouse-mit-python-fastapi-postgresql-pwa-offline-wms-invariants-no-negative-stock-append-only-history-ai-proposes-human-decides-v1-invariants-list-as-external-reference-vocabulary.md`**

## Active feature path

`features/389-ssbianchiplan-whouse-mit-python-fastapi-postgresql-pwa-offline-wms-invariants-no-negative-stock-append-only-history-ai-proposes-human-decides-v1-invariants-list-as-external-reference-vocabulary.md` — **defer** (Pick B of Daily Research 2026-10-27).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When an outside builder writes a stock system, they want the ledger's rules to be non-negotiable, but struggle because LE31 has never written its own rules in that form, so that the invariants can be checked against a working outside example.* Links to feature **370** (the same genre, applied to money-and-stock). **Pass as prior art, NOT as demand** — no operator is reported to want this. |
| 2 | Viability | ✓ | Reading an invariants list is free; adopting it is not. The slice changes **no file in `backend/`**. **Pass.** |
| 3 | Practicability and confidence | ✓ | §3.2-compatible (MIT) and **on-stack** (Python/FastAPI/PostgreSQL/PWA). **The useful part is documentation, not code.** **Named rabbit hole:** `whouse` is a *warehouse* WMS — NF-e XML intake, barcode collectors, ABC×XYZ MRP, picking waves, SAP/TOTVS/Senior/Sankyha/Odoo ERP connectors. **Adopting its domain would pull procurement and picking into LE31 v1, which §3.2 excludes.** The transferable item is **five sentences**. |
| 4 | Conflict | ✓ | None — nothing is being adopted. **But note two `whouse` invariants have NO LE31 counterpart** — *"Quarentena não sai"* (a blocked lot does not leave) and *"Estoque da ordem é da ordem"* (segregated stock belongs to its order). Each is a **new domain**, not a gap in an existing one. **Recorded, explicitly NOT bundled.** |
| 5 | Outcome + appetite + scope | ✓ | v1 vocabulary. **Maximum time worth spending: two sentences of documentation.** Scope: one document, a mapping table, a list of the two unmatched invariants, three operational details of the AI rule. **No schema, no code, no dependency, no new enum, no model.** |
| 6 | Cost to operational value | ✓ | Near-zero cost, near-zero immediate value. Justified as **prior art for §3.4's "AI proposes, a human decides"** and for the no-negative-stock / append-only-history pairing. **Low value is exactly why this is `defer` and not `build`.** |
| 7 | Circuit breaker + reversibility | ✓ | A Markdown document. **Delete it and nothing is lost.** No data, no migration, no rollback, no retained state. **Trivially reversible.** |

**Gate verdict: `defer`** — check 1 passes on **reported** evidence (the repo states the rules), not on observed operator pain. **Confidence medium** for the shape, **low** for LE31's need.

## Bucket

**v1 (external-invariants vocabulary — a documentation reference)** — Pick B of Daily Research 2026-10-27. The subject is LE31's v1 stock/ledger/AI rules, so the matching project would be **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on 2026-10-27 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **40th consecutive day**), the sub-issue has no parent to hang under — it is routed to **`le31 Research` (P-HMM-1)** in the fallback payload (the parent research issue's own project, so the sub-issue sits with the research pass it came from), and **no project attachment actually occurred**.

## Files to touch

**Exactly one file — and it already exists:**

- `features/389-ssbianchiplan-whouse-mit-python-fastapi-postgresql-pwa-offline-wms-invariants-no-negative-stock-append-only-history-ai-proposes-human-decides-v1-invariants-list-as-external-reference-vocabulary.md` — **this is the deliverable. It is complete.**

**Do NOT touch (out of scope, explicitly):**

- `backend/` — **any file, for any reason.** `git diff --stat backend/` must be **empty** after this slice. This is the load-bearing check for a documentation-only pick.
- `PROJECT_CHARTER.md` — **no change required.** If you touch it, the only permitted edit is a pointer to this feature; **do not** add a new section, a citation block, or a "prior art" appendix.
- `features/01-table-management.md` and every other feature contract — **no cross-edits.**
- `features/370-…` — **read it, do not edit it.** It is the precedent for this genre.
- `features/382-…`, `features/385-…` — **read them, do not edit them.** They own the idempotency rule and the batch-provenance question respectively; `whouse`'s `Idempotency-Key` and its FEFO/FIFO allocation are recorded here as prior art **for those features**, and belong to them.
- `docs/`, `research/` — **do not create a second copy of this mapping in another folder.** One copy, in the feature tree. A duplicate is a defect.
- `backend/requirements.txt` — **no dependency change.** `whouse` is **not** added as a dependency, a submodule, a vendored directory, or a reference implementation to copy from. **It is read as a text.**
- No new enum, field, model, table, config value or env var.

## The load-bearing tests

**There are no runtime tests for this slice — and that is the point.** The checks are:

1. **`git diff --stat backend/` is empty.** This is the load-bearing check. A documentation pick that touches code has smuggled scope.
2. **The feature file exists and contains the mapping.** Read it back. It must contain: the five verbatim invariants with source URL, the mapping to LE31's rules, the explicit "NO COUNTERPART" marking for invariants 2 and 3, and the three operational details of invariant 5 (server-only key, per-person monthly USD quota default US$ 20, 30-calls-per-minute + 3-concurrent limit).
3. **The source attribution is exact.** The verbatim Portuguese text is quoted from `https://github.com/SSBianchiplan/whouse` (README section *"Invariantes (regras que o sistema não deixa quebrar)"*), read on 2026-10-27. The repository's licence is `mit` (verified by direct `/repos/` GET, not by search-result text).
4. **No claim of traction.** The feature must state ★1/⑂0 and that no traction evidence exists in either direction. **A vocabulary pick that implies demand is a defect.**
5. **The two unmatched invariants are marked as unmatched** and are **not** proposed as features.

If the parent wants an automated check for (1), the one-liner is:

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

# 1. the invariants section exists, verbatim
grep -n "Invariantes\|Sem saldo negativo\|Histórico não se apaga\|A IA propõe" SSBianchiplan__whouse.md
# expect: hits for all four — the five bullets are at lines 46, 47, 49, 50 and one more

# 2. the two LE31-absent invariants are real and really absent from LE31
grep -n "Quarentena não sai\|Estoque da ordem é da ordem" SSBianchiplan__whouse.md
# expect: hits
cd /opt/data/le31_mmm3_research_work
grep -rni "quarantine\|quarentena\|segregated" backend/app/ features/ | grep -v "^features/389"
# expect: NO output — LE31 has neither concept

# 3. LE31's own rules are as the mapping claims
grep -n "never UPDATE or DELETE" backend/app/models.py
# expect: a hit (the StockEntry docstring)
grep -n "AI may assist\|non-AI fallback" PROJECT_CHARTER.md
# expect: a hit (§3.4)

# 4. the precedent exists and is the same genre
ls features/370-jdmacleod-kitchen-erp-*.md
# expect: the file — read it before rewriting the framing

# 5. the boundary pair says the opposite thing (context, not scope)
grep -n "allowNegative" /tmp/le31-daily-2026-10-27/gh/readmes/Nomaan2288__Restaurant-Management-System.md
# expect: hits
```

**Note on the source-of-truth for the quoted text:** the **README is authoritative** where it contradicts the GitHub `description` field. This series has recorded two occasions where a repo's topics or description described a *different project* from what its README says (feature 386's `ChainWarden` case). **The README is what was quoted; the description was not used for any claim.**

## Rollback path

- **Delete the feature file and its HANDOFF.** Nothing else changed. No data, no migration, no retained state, no configuration, no dependency.
- **If the mapping turns out to be wrong**, correct the feature file in place — there is nothing to unwind.
- **No consumer of this document exists yet.** No code reads it, no test asserts on it, no runtime path depends on it. It is safe to amend or remove at any time without consequence.

## Mandatory LE31 skill list for the coding agent

**This slice needs no coding agent.** It is documentation. The relevant skills are for whoever later reads it:

- `le31-conventions` — **read first** if you act on any of the open questions. The hard invariants and the seven-check gate are what the mapping is measured against.
- `le31-research` — for the evidence discipline the document follows (source URL, date, direct quote, confidence, limitations).
- `development` — **only if** the open questions are ever escalated into real work. They are not in scope here.
- `test-driven-development` / `pre-merge-review` — **not applicable** to this slice. There is no product code to review. **Do not fabricate a test suite to make a documentation pick look like an engineering task.**

## Open questions carried into any future build

1. **Should LE31's §3.3 state a correction mechanism?** `whouse` says *"correção é por estorno ou ajuste, com autor e data"* — correction is **by reversal or adjustment, with author and date**. LE31 says only *"never UPDATE or DELETE rows"* and **does not say what to do when a row is wrong**. This is a genuine one-sentence gap found from outside. **Not decided here — a charter question.**
2. **Should LE31's §3.4 grow the three operational details** (server-only AI key, per-person monthly quota, rate limit)? They are what makes *"observable evidence and a non-AI fallback"* enforceable rather than aspirational. **Not decided here — a charter decision.**
3. **Do the two unmatched invariants deserve features?** *"Quarentena não sai"* and *"Estoque da ordem é da ordem"* are plausible v2 features, but LE31 has **no batch-blocking concept and no order-segregated stock concept** — each is a **new domain**, not a gap. **Deliberately not proposed.** A pick that bundles two new domains into a "vocabulary" note smuggles scope across the §3.2 line.
4. **Is `whouse` a better reference than `research/01-pos-systems.md`?** It is on-stack, permissively licensed, and states the rules explicitly — where `01-pos-systems.md` is a summary of a different project. **Not decided here.** That comparison belongs to a maintenance pass over `research/`, not to this slice.
5. **Should the FEFO/FIFO allocation rule be adopted?** `whouse` allocates with FEFO/FIFO and a *"quarantine doesn't leave"* rule. LE31's "active batch" rule is still an **open question in feature 03** (and feature 385 records it). **Not decided here — feature 385 owns it.**

---

**Bottom line for the coding agent:** **there is no code in this slice.** The feature file exists and is the deliverable. The single load-bearing check is `git diff --stat backend/` being empty. If you find yourself designing a `Quarantine` model or an `Order`-segregated stock table, **stop — that is Open question 3, deliberately not proposed here.**
