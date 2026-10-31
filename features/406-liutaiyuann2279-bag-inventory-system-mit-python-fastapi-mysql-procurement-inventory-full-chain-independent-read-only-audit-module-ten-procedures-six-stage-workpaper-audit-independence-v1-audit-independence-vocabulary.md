# Feature 406 — The auditor must be structurally unable to write: audit-independence vocabulary

> **Pick B of Daily Research 2026-10-30 (92nd pass).** **Reference artifact, vocabulary-only.** **Verdict: `defer`** (v1 parking lot). **No code is adopted.**
>
> **Source artifact**: `LiutaiyuaN2279/bag-inventory-system` — **MIT ✓ §3.2 strictly-compatible**, **★1/⑂0 recorded explicitly as NO traction evidence in EITHER direction**, **9,801 KB**, **Python ✓ ON-STACK** (FastAPI + MySQL/MariaDB + Knex), **created 2026-10-26T… AND pushed 2026-10-26T… = IN-WINDOW BY BOTH FIELDS**, 1 topic, `archived=false`, `fork=false`, default_branch `main`. **All fields parent-verified via direct `GET /repos/`** (`/tmp/le31-daily-2026-10-30/gh/repo_LiutaiyuaN2279__bag-inventory-system.json`, HTTP 200), **never from search-result numbers**. Description (verbatim from the GitHub API): *"面向箱包制造企业的一体化业务演示系统：物料 → BOM → 请购 → 采购订单 → 到货检验 → 退货 → 出入库 → 盘点 → 报表全链路…"*.
>
> **Bucket: v1** (vocabulary reference for a v1-owned question). **Evidence class: INFERRED, confidence LOW** — no LE31 owner has asked for an auditor; the *gap* is observed, the *demand* is not.
>
> **⭐ The transferable idea is a structural one, not a feature: the audit module opens the business database READ-ONLY and the audited roles are denied the audit permissions entirely.** From the artifact's own README:
>
> > *"以**只读**方式打开本系统自己的业务库"* — *it opens its own business database in **read-only** mode.*
>
> > *"**只读约束**：连接串固定为 `file:<db>?mode=ro`（SQLite URI 只读模式），程序内部只发 `SELECT` — **审计规则写错也改不到被审计数据**。"* — *"the connection string is fixed to `file:<db>?mode=ro`; the program issues only `SELECT` — **a wrong audit rule cannot modify the audited data**."*
>
> > *"**被审计对象不应同时持有审计端权限，这是审计独立性要求在权限设计上的落点**。"* — *"**the audited party must not simultaneously hold the audit-side permissions; this is where the audit-independence requirement lands in the permission design.**"*
>
> The artifact implements this at **two** layers: the audit permissions (`audit:view`, `audit:run`) are granted to `admin` and `manager` and **withheld** from the business roles (`buyer` / `keeper` / `qc`), enforced at both the route (`meta.permission`) and the API (`require_permissions`) — *"直接敲 URL 也进不去"* (*"even typing the URL directly gets you nowhere"*).

## Goal

Retain the **audit-independence** discipline as a persistent cross-section reference for LE31, and record the **two concrete mechanisms** by which the artifact makes it true:

1. **Read-only at the connection, not at the application.** The auditor cannot write because the *database session* cannot write — not because the auditor's code is careful. A bug in a rule cannot become data corruption.
2. **Permission separation, enforced twice.** The audited roles do not hold the audit permission; and the check happens at the route *and* at the API, so bypassing one does not bypass the other.

**No LE31 code changes today.** The recorded question is: *when LE31 writes its first audit row, who may read the audit log — and may that reader write to the database?*

## Scope

**In scope (defer artifact, v1 vocabulary reference):**

- **A written record** of the **read-only-auditor + permission-separation** discipline, quoted from the artifact.
- **A written record of LE31's current audit posture**, so the reference is anchored to reality:
  - `grep -n 'audit_log\|class Audit' backend/app/models.py` → **no output.** **LE31 has no `audit_logs` table at all.** Feature 30 (`append-only-audit-redirect`) and feature 49 (tamper-evident hash chain) are **specifications for a table that does not exist**.
  - `grep -rn 'UserRole\.' backend/` → **zero qualified read sites.** The role enum is declared and never consulted. Feature 403 files the role-carrying gap.
  - Therefore **there is no audit surface today that could be made read-only**, and **no role whose audit permission could be withheld.**
- **A named trigger** (below) at which this reference must be read.

**Out of scope (defer artifact):**

- **Any audit module, audit table, audit route or audit procedure.** Nothing is built.
- **Any permission system, RBAC layer or role split.** Feature 403 owns the role-carrying gap; this artifact does not touch it.
- **The artifact's ten audit procedures (R01–R10)** — 请购超量, 到货入库差异, 订单账龄, 价格偏离, 退货来源, 验收及时性, 供应商集中度, 采购与库存匹配, 三单匹配, 订单空转. **They are procurement-specific, depend on a purchase-order domain LE31 v1 does not have (charter §3.2 excludes supplier purchasing from v1), and are not portable.** The *shape* — a named procedure with a threshold, a materiality level, and a finding list — is recorded; the *procedures* are not proposed.
- **The artifact's procurement chain** (请购 → 采购订单 → 到货检验 → 出入库 → 盘点). LE31 v1 has **no purchase-order domain**.
- **Adopting SQLite's `mode=ro` URI.** LE31's production database is **Postgres** (§3.2) and development is SQLite. The *mechanism* is "a session that cannot write"; the concrete syntax is Postgres's `SET TRANSACTION READ ONLY` / a read-only role. **The SQLite URI is the artifact's syntax, not LE31's.**
- **The six-stage audit workflow, the risk scoring formula, the materiality level and the workpaper UI.** Recorded as an artifact's shape; **not proposed**.
- **The artifact's own honest "known boundaries" section** — which says the audit results are a one-off read-only snapshot with no findings lifecycle, no rectification tracking and no cross-period comparison. **That boundary is why this is a reference and not a template.**

## Description

### What the artifact does, and the two mechanisms worth keeping

The artifact is a procurement-and-inventory system for a bag-manufacturing firm. Its interest to LE31 is **not** the domain. It is that the author built an **audit module that audits the system's own database**, and made two specific structural choices:

**Mechanism 1 — the auditor cannot write, at the connection level.**

```
只读约束：连接串固定为 file:<db>?mode=ro（SQLite URI 只读模式），
程序内部只发 SELECT — 审计规则写错也改不到被审计数据。
```

The audit code and the business code share **the same data** but **not the same capabilities**. The audit program cannot corrupt the thing it audits **even by mistake**. This is a stronger property than *"the auditor is careful"* and it is **strictly stronger than LE31's current posture**, where feature 49's hash chain is the *detection* layer and the prevention layer is *"no UPDATE or DELETE statements in the codebase"* — **enforced by convention**.

**Mechanism 2 — permission separation, enforced at two layers.**

```
为什么不给业务岗位：被审计对象不应同时持有审计端权限，
这是审计独立性要求在权限设计上的落点。buyer / keeper / qc 登录后
侧边菜单里没有「智能审计」，直接敲 URL 也进不去
（路由 meta.permission + 接口 require_permissions 双重拦截）。
```

Two enforcement points, **not one**. The menu hides the entry (cosmetic), the route guard blocks the page (the real check), and the API guard blocks the data (the check that matters). **Bypassing the UI reaches neither.** This maps directly onto LE31's own §3.3 append-only posture: the guard is below the interface.

### Why this fails the LE31 v1 gate today — stated plainly

**LE31 v1 has one restaurant and two roles** (charter §3.1: a waiter and a cook). Audit independence is a **two-party control**: it requires an auditor who is *not* the audited party. **LE31's owner is a single person** who both operates the restaurant and would be the one reading the audit output. **A control against yourself is not a control.** Building it now would create a permission split for a party that does not exist, and the split would be **ceremonial** — the same human behind both roles.

**Three further reasons the v1 build is not ready:**

1. **There is nothing to make read-only.** No `audit_logs` table exists. The audit surface is a **specification**, not an implementation (features 30 and 49).
2. **There are no roles to withhold permissions from.** `UserRole` has **zero read sites**; feature 403 files that gap. Withholding a permission from a role nobody reads is a no-op.
3. **The `audit:run` check is itself loose in the source artifact** — the README's own "known boundaries" section admits: *"`audit:run` 未单独校验：`POST /audit/run` 当前校验的仍是 `audit:view`，即"能看就能重跑"* — *"`audit:run` is not separately validated: `POST /audit/run` currently still checks `audit:view`, i.e. **'if you can view it, you can re-run it'**."* **The artifact teaches its own failure mode.** That honesty is worth recording: **a permission named `audit:run` that is not separately enforced is a permission that does not exist.**

### The one genuinely portable piece — and it is about LE31's own future code

**A named procedure with a threshold, and a materiality level.** The artifact's ten procedures are each *"an independent method encapsulating that procedure's audit objective, decision rule and threshold"*, with all thresholds collected in one config table. And the audit runs a **six-stage pipeline** — scope → collect → clean → check → judge → workpaper — where **every stage records its own elapsed time and a summary of what it produced**.

That shape maps onto something LE31 will need **when the stock board and the daily recap exist**: *"is the ledger plausible?"* — e.g. *are there `StockEntry` rows whose `qty_delta` sum contradicts the batch's `qty_start`?* LE31 already has the ingredients (an append-only ledger, a derived-stock rule) but **no procedure, no threshold and no materiality concept.**

**Recorded, not proposed** — because a stock-integrity procedure is a **first-party feature with its own gate**, not a by-product of a reference artifact.

## Data model

**None. No table, no column, no route.** This is a vocabulary record.

The artifact's own model, recorded for reference only: `code_sequences (scope, business_date) → last_seq` for day-scoped codes; a `staff` table; `inventory_items`; plus the procurement chain LE31 v1 does not have (`请购单`, `采购订单`, `到货单`, `检验`, `退货`, `出入库流水`, `库存调整`, `盘点`).

**Not adopted**: none of it. The two mechanisms are **patterns**, not schemas.

## Implementation steps

**None. This artifact builds nothing.** The implementation steps are the steps a future implementer takes **at the trigger**, recorded here so the reference is complete:

1. **When the first audit row is written** (the trigger), read this artifact alongside feature 30 (audit redirect), feature 49 (hash chain) and feature 403 (role carrying).
2. **Decide, in writing:** (a) **is the audit surface a separate read-only session or the same session with a permission check?** (b) **who may read the audit log, and may that reader write to the database?** (c) **is the read-only guarantee enforced at the connection, or at the application?** — the artifact's answer is *the connection*.
3. **If (c) is "the connection",** the Postgres implementation is a **read-only role** or `SET TRANSACTION READ ONLY`, **not** the artifact's SQLite `mode=ro` URI. **That is a separate, freshly-gated architecture feature** — do not implement it under this contract.
4. **Enforce at two layers** if a permission layer exists at all: the route **and** the API. **One layer is a UI convention.**
5. **Name the procedures** with their thresholds in one config table, so a threshold change is a config change and not a code change.
6. **If no decision can be made,** close this artifact and leave the current posture (no audit surface at all) as-is. **That is a valid outcome** — the artifact is a reference, not a commitment.

## Telegram interaction if any

**None.** No command is added, changed, or removed. The cook sees nothing different.

**One thing to state plainly if this reference is ever promoted**: an audit surface in LE31 would be an **owner-facing** artifact, not a cook-facing one, so it would live in the waiter/owner web surface — **not** in the Telegram bot. **No Telegram command is proposed here, and none should be inferred from this reference.**

## Dependencies

- **No new package. No code.**
- **Feature 30** (`append-only-audit-redirect`) — owns the *redirect primitive*: route writes through one function so they cannot bypass the ledger. **Complementary**: 30 is *"writes go through one door"*; this artifact is *"the reader cannot write at all"*.
- **Feature 49** (tamper-evident hash chain) — owns *detection* of out-of-band edits. **This artifact is the prevention layer**: 49 proves a row was not edited; this says the auditor could not have edited it in the first place. **Different questions — do not merge.**
- **Feature 379** (`OrderItem` transition attribution) — its own cross-section note already says: *"LE31's StockEntry ledger is append-only but not tamper-evident. **That is a separate, larger question** … do not bundle it here."* **This artifact is that separate question's neighbour, not its owner.**
- **Feature 403** (role carrying / chat-id allowlist) — owns the fact that `UserRole` has **zero read sites**. **Permission separation is meaningless until roles are carried, so 403 is a prerequisite for any promotion of this artifact.**
- **Not** features 181 / 196 / 273 (tamper-evident and append-only-ledger variants) — they are **hash-chain** concerns, and **a hash chain is not audit independence.**

## Open questions

1. **Does LE31 ever have a second party?** Audit independence requires an auditor who is not the audited party. LE31 v1 is **one owner**. **If that is permanent, this control is permanently ceremonial** — and the honest answer may be *"not needed"*, which is a **valid, cheap outcome**.
2. **Is prevention or detection the right layer?** LE31 has detection (feature 49). Prevention costs a second connection and a second identity. **Which is worth it is an owner decision**, not a research finding.
3. **Would a read-only audit session be a separate process or a connection mode?** The artifact uses a connection mode inside the same application. A separate process is a stronger boundary and a bigger change. **Undecided.**
4. **Should an audit surface ever be exposed to the cook bot?** **Presumed no** — the artifact's audit output is a management surface, and LE31's §3.1 fixes two surfaces. **Recorded as a presumption, not a decision.**
5. **What would the first audit procedure be for LE31?** A stock-integrity check (ledger sum vs. batch) is the obvious candidate and is **deliberately not proposed here** — it would be a **first-party feature with its own gate**.

## Why this matters

**Because it names the difference between a control and a convention, and LE31's audit posture is currently a convention.** LE31's append-only rule — *"every change to batch stock is a new `StockEntry` row, never UPDATE or DELETE"* (charter §3.3) — is enforced, in the shipped code, by **nobody**: no database constraint, no trigger, no restricted role. Feature 404 (the other 404) is about `CHECK` constraints on exactly this kind of column; feature 49 adds **detection**. **Nothing in LE31 today makes a wrong write impossible** — only unlikely.

This artifact supplies the *shape* of the missing third thing: **make the forbidden operation impossible to perform, not merely forbidden by documentation.** Two concrete mechanisms, both quoted, both implementable in LE31's stack — a read-only session, and a permission split enforced at two layers.

**And it supplies the artifact's own correction, which is worth as much as the rule.** The README's *known boundaries* section admits that `audit:run` is not separately enforced — *"能看就能重跑"* — **"if you can view it, you can re-run it."** That is a **named permission that does not exist**, in a system whose entire point is permission separation. **An artifact that publishes its own control failure is more useful to LE31 than one that does not**, because the failure mode is exactly the one LE31 would have copied: *a permission on the menu, a check on the route, and the data still reachable*.

**Why the artifact mattered, precisely.** It did not tell LE31 anything about inventory. It told LE31 that **an auditor can be given capabilities the operator does not have** — and the mechanism is boring, which is the point: *a connection string that cannot write*.

**The honest counterweight.** Every reason to file this is a reason LE31 v1 **should not build it**: one owner, no audit surface, no role reads, no second party. That is why the verdict is `defer` and not `build` — and it is why the artifact is filed **with a trigger attached**, so that the next implementer inherits the rule *and* the precondition, instead of inheriting an idea and reinventing the prerequisites.
