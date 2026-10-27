# Feature 389 — `whouse`'s invariants list: the outside builder who wrote down the same rules LE31 has, in the same order

> **Pick B of Daily Research 2026-10-27 (89th pass).** Documents in-window GitHub repo `SSBianchiplan/whouse` (**licence `mit` ✓ §3.2 STRICTLY-COMPATIBLE — the *vocabulary-shape* is the transferable item; the *code-shape* is NOT adopted**), **★1/⑂0 — no traction evidence in either direction**, **2,113 KB**, Python 3.12+ **✓ ON-STACK** (FastAPI + PostgreSQL + PWA/offline — **the only on-stack candidate of today's three**), created **2026-10-22T14:19:53Z AND pushed 2026-10-22T17:42:43Z = IN-WINDOW BY BOTH FIELDS**, 14 topics `['almoxarifado','barcode','erp-integration','estoque','fastapi','fefo','gplansis','inventory','nfe','offline-first','postgresql','pwa','warehouse-management','wms']`, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-27, not from search-result numbers. Description (verbatim from GitHub API): *"GPlanSiS|WHOUSE — almoxarifado e WMS multiusuário: recebimento com CQ e NF-e, endereços, lotes e validade (FEFO), stock by order, picking, inventário cíclico, reposição ABC×XYZ com IA que só propõe e integração com ERPs. PWA offline, coletor com câmera. FastAPI + PostgreSQL."*
>
> **The README was read** (parent, 2026-10-27, `/tmp/le31-daily-2026-10-27/gh/readmes/SSBianchiplan__whouse.md`). The repo ships an explicit section headed *"Invariantes (regras que o sistema não deixa quebrar)"* — *"invariants (rules the system does not let break)"* — whose five bullets map almost one-to-one onto LE31's own charter rules. **This is a vocabulary pick: two sentences of documentation. No schema change, no code change, no dependency.**
>
> Bucket: **v1**. Verdict: **`defer`** — vocabulary only.

## Goal

Record, in LE31's own vocabulary, that **an outside builder independently wrote down the same stock, ledger and AI rules LE31 has** — and in a form that is *checkable* (a named list, not a prose paragraph).

The concrete outcome: **a short note in the feature tree stating which of LE31's rules have outside prior art, and which of `whouse`'s rules have no LE31 counterpart at all.**

## Scope

**In scope (v1):**

- **One document** recording the mapping between `whouse`'s five invariants and LE31's charter rules, with the **verbatim source text** and the **source URL** for each.
- **An explicit list of the two `whouse` invariants that have NO LE31 counterpart** — *"Quarentena não sai"* (quarantine does not leave) and *"Estoque da ordem é da ordem"* (the order's stock belongs to the order) — recorded as **adjacent evidence, not as scope**.
- **A pointer to the §3.4 "AI proposes, human decides" rule** and the three operational details that make it real in `whouse`: the server-only AI key, a per-person monthly USD quota (default US$ 20), and a 30-calls-per-minute / 3-concurrent limit.

**Explicitly NOT in scope:**

- **Any adoption of `whouse`'s domain.** It is a *warehouse* WMS: NF-e XML intake, barcode collectors, ABC×XYZ MRP, picking waves, SAP/TOTVS/Senior/Sankyha/Odoo ERP connectors. **Procurement and picking are §3.2 out-of-scope territory for LE31 v1.** This feature adopts **sentences**, not a system.
- **Any code, schema, dependency or configuration change.** This feature changes **no file in `backend/`.**
- **Any new enum, field or model.** The two unmatched invariants are recorded, **not** proposed as features.
- **A FEFO/FIFO batch-selection rule** — feature 385 already owns the unresolved "active batch" question, and `whouse` is prior art *for that question*, not a resolution of it.
- **Idempotency-Key / HMAC-SHA256 webhook semantics** — feature 382 already owns the ledger-write idempotency rule; `whouse` is a fourth external naming, recorded only.

## Description

### What `whouse` actually is

A **multi-user warehouse management system** (Portuguese: *almoxarifado*) — materials, addresses, lots and expiry, picking, cyclic inventory and replenishment. It runs two ways: multi-user served by a server (login, profiles, shared and versioned state in PostgreSQL, offline operation with merge-on-reconnect), and local (open `web/app.html` from disk, no server, no login, data in the browser). It is **Python 3.12+, FastAPI, PostgreSQL, PWA** — **the same stack LE31's charter names**, which is why it is filed at all.

Its README states the core design in one sentence: *"o saldo é a soma dos movimentos, por lote, endereço e tipo de estoque"* — *"the balance is the sum of the movements, per lot, address and stock type."* **That is LE31's §3.3 derivation rule, stated by a stranger.**

### The five invariants, verbatim, and what each one is in LE31

The README section is headed *"**Invariantes (regras que o sistema não deixa quebrar)**"* — *"invariants (rules the system does not let break)"*. Verbatim:

| # | `whouse` (verbatim) | LE31's counterpart | Verdict |
|---|---|---|---|
| 1 | *"**Sem saldo negativo** — a saída é checada por posição, lote e tipo de estoque."* | §3.1 *"Prepared-item stock with per-batch quantities and an append-only ledger"*; feature 382's shortfall rule | **MATCH** — LE31 is the *stricter* side: LE31 refuses/records a shortfall, `whouse` blocks the issue |
| 2 | *"**Quarentena não sai** — lote em inspeção ou bloqueado fica fora da alocação e das requisições."* | **none** | **NO COUNTERPART** — LE31 has no quarantine concept |
| 3 | *"**Estoque da ordem é da ordem** — saldo segregado só é consumido pela ordem dona até ser liberado."* | **none** | **NO COUNTERPART** — LE31 has no segregated-stock concept |
| 4 | *"**Histórico não se apaga** — movimentos só são acrescentados; correção é por estorno ou ajuste, com autor e data."* | §3.3 append-only `StockEntry` ledger; *"Never UPDATE or DELETE rows"* | **MATCH** — and note `whouse`'s addition: correction is **by reversal or adjustment, with author and date** — LE31 has the append-only rule but **no stated correction mechanism** |
| 5 | *"**A IA propõe, você decide** — o assistente cria apenas propostas; a aprovação é sempre de uma pessoa."* | §3.4 *"AI may assist owner/staff, with observable evidence and a non-AI fallback"* | **MATCH** — and `whouse` states it more operationally than LE31 does |

### The two matches that are worth more than the match itself

**Invariant 5, operationally.** LE31's §3.4 says AI *"may assist owner/staff, with observable evidence and a non-AI fallback"*. `whouse` says the same thing and then **says how**: the AI key lives **only on the server** (`server/ia_cota.py`); the prompt and the tool list are assembled server-side; there is a **monthly quota in USD per person** (default US$ 20, adjustable by the admin at `/api/admin/ia`); there is a **30-calls-per-minute limit and 3 concurrent calls**; and the assistant *"cria apenas propostas"* — creates only proposals, with a human approving. **LE31 has none of these.** §3.4 is a *principle* in LE31 and a *mechanism* in `whouse`. The transferable item is the mechanism vocabulary: **budget, rate limit, server-only key, proposal-not-action.**

**Invariant 4, the correction mechanism.** LE31's append-only rule is currently *"never UPDATE or DELETE rows"* with **no stated way to correct a mistake**. `whouse` names one: *"correção é por estorno ou ajuste, com autor e data"* — correction is **by reversal or adjustment, with author and date**. LE31's `StockReason` enum exists; whether it has a reversal reason is a separate question (see Open questions). **This is a one-sentence gap in LE31's own vocabulary, discovered from outside.**

### The boundary pair in the same window

`Nomaan2288/Restaurant-Management-System` (AGPL-3.0 → §3.2 blocked) documents the **opposite** choice on invariant 1: *"automatic ingredient deduction on checkout (combo-aware, **never blocks a sale on a stock shortfall**)"* and *"StockService.consumeStock(..., **allowNegative: true**) lets stock go negative rather than fail a paid order over a recipe-modeling gap."*

**Two in-window repos make opposite choices on the same question, and LE31's choice is the stricter one.** That is worth knowing out loud: LE31 is not unusual for refusing to go negative, it is unusual in *how much* it is willing to refuse — and `whouse`'s framing ("the issue is checked by position, lot and stock type") shows a middle path between the two: **the check is specific, so the failure is precise** rather than a blanket refusal.

## Data model

**No data-model change. None.**

This feature adds **no column, no table, no enum, no model**. It is a documentation-only pick.

The *content* of the documentation is a mapping table (the one above), a list of the two unmatched invariants, and the three operational details of invariant 5 (server-only key, per-person monthly USD quota, 30/min + 3-concurrent limits).

## Implementation steps

1. **`features/389-…md`** — this file. It is the deliverable.
2. **Do not** add a `docs/` folder, a `research/` entry, or a `PROJECT_CHARTER.md` edit for this feature. The mapping lives here, in the feature tree, where the pipeline will find it. **A second copy in a second place is a defect.**
3. **Do not** create a `Backend` or `backend/` change of any kind. `git diff --stat backend/` must be **empty** after this feature.
4. **Do not** add `whouse` as a dependency, a submodule, a vendored directory, or a reference implementation to copy from. The repository is **read as a text**, not as a codebase.
5. **Optionally** — and only if a natural place already exists — add one line to `PROJECT_CHARTER.md` §3.4 pointing at this feature as outside prior art. **Do not** add a new section, a new subsection, or a citation block.

## Telegram interaction if any

**None.** No command, no message, no change to the cook bot.

## Dependencies

- `PROJECT_CHARTER.md` §3.1 — prepared-item stock, per-batch quantities, append-only ledger.
- `PROJECT_CHARTER.md` §3.3 — the ledger derivation rule; **the appendix's own stock-consumption paths** are the LE31-side counterpart to `whouse`'s "the issue is checked by position, lot and stock type".
- `PROJECT_CHARTER.md` §3.4 — the AI-assistance rule this pick documents outside prior art for.
- `PROJECT_CHARTER.md` §3.2 — the non-goals that keep this pick small (no procurement, no picking, no multi-branch).
- `features/370-jdmacleod-kitchen-erp-…` — **the precedent for this genre.** That feature recorded *"Decimal money, append-only facts, no required outbound calls"* as outside prior art for LE31's money-and-stock rules. **This pick is the same move, applied to a different repository and a different rule set.** Read it before writing — do not reinvent the framing.
- `features/382-dc-tech-inc-dotnet-pos-integration-…` — the ledger-write idempotency rule; the reason `whouse`'s `Idempotency-Key` + HMAC-SHA256 webhook is recorded and **not** filed.
- `features/385-le31-order-item-batch-provenance-…` — the unresolved "active batch" question; the reason `whouse`'s FEFO/FIFO allocation is prior art **for that question** and not filed here.
- `research/01-pos-systems.md` — LE31's peer-model reference; `whouse` is a second independent statement of the same derivation rule.

## Open questions

1. **Should LE31's §3.3 state a correction mechanism?** `whouse` says *"correção é por estorno ou ajuste, com autor e data"*. LE31's `StockReason` enum exists but **no reversal reason is specified**, and the charter says only *"never UPDATE or DELETE rows"*. **This is a genuine one-sentence gap discovered from outside.** It is **not** decided here — it is a charter question, and feature 385 already shows how expensive a charter ambiguity becomes downstream. **Recorded, not filed.**
2. **Should LE31's §3.4 grow the three operational details** (server-only key, per-person quota, rate limit)? They are what makes *"observable evidence and a non-AI fallback"* enforceable rather than aspirational. **Not decided here.** A §3.4 amendment is a charter decision and out of this pick's scope.
3. **Do the two unmatched invariants deserve features?** *"Quarentena não sai"* (a blocked lot does not leave) and *"Estoque da ordem é da ordem"* (segregated stock belongs to its order) are both plausible v2 features — but LE31 has **no batch-blocking concept** and **no order-segregated stock concept**, so each is a *new domain*, not a gap in an existing one. **Deliberately not proposed.** A pick that bundles two new domains into a "vocabulary" note is how scope gets smuggled across the §3.2 line.
4. **Is `whouse` a better reference than `research/01-pos-systems.md`?** It is on-stack, licensed permissively, and states the rules explicitly — where `01-pos-systems.md` is a *summary* of a different project. **Not decided here.** That comparison belongs to a maintenance pass over the research folder, not to this pick.

## Why this matters

**Because the strongest defence of LE31's rules is that an outside builder chose the same ones — and today LE31's own documentation does not say so.**

LE31's charter states its stock, ledger and AI rules. Every prior confirmation of those rules has been **internal**: LE31 decided, LE31 wrote it down, LE31 obeyed it. Feature 370 broke that pattern for money-and-stock. `whouse` breaks it again, for the **AI boundary** — and it breaks it in the one direction that matters most, because §3.4 is the rule most likely to be quietly eroded by a well-meaning feature request (*"let the assistant just adjust the stock"*).

`whouse` answers that request structurally, not rhetorically: the assistant *"cria apenas propostas"*, the approval is *"sempre de uma pessoa"*, the key is on the server, and there is a **budget and a rate limit**. **That is what "AI proposes, you decide" looks like when someone has actually built it.** LE31's §3.4 is one sentence; this is a mechanism. The difference between a sentence and a mechanism is the difference between a rule and a wish.

**And invariant 4's correction clause is a genuine finding.** LE31 says *"never UPDATE or DELETE rows"* and does not say what to do when a row is wrong. `whouse` says: **by reversal or adjustment, with author and date** — i.e. an error is itself an event. That is one sentence of vocabulary that closes a real hole, and it was found by reading an outside project's README rather than by ninety citations (feature 385's finding, repeated).

**Why it is `defer` and not `build`.** Because nothing about it *needs* to change today. The rule LE31 actually has is correct; this pick adds *corroboration* and *two open questions*, not a fix. The value is that the next time someone proposes letting an AI adjust stock, the answer is not "the charter says no" but "here is how a system that ships this does it, and here is the sentence LE31 is missing." That is worth having before the request arrives — and it is not worth a sprint.
